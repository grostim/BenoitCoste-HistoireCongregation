#!/usr/bin/env python3
"""Contrôle hors ligne du corpus et du suivi, sans valider la lecture."""
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / 'Originaux/manifest.json').read_text(encoding='utf-8'))
with (ROOT / 'SUIVI_TRANSCRIPTION.csv').open(encoding='utf-8', newline='') as stream:
    rows = list(csv.DictReader(stream))
expected = manifest['original']['pages']
if [int(row['vue_pdf']) for row in rows] != list(range(1, expected + 1)):
    raise SystemExit('Les vues du suivi doivent couvrir le PDF une fois et dans l’ordre.')
covered = []
for volume in manifest['volumes']:
    path = ROOT / 'Originaux' / volume['fichier']
    with path.open('rb') as stream:
        digest = hashlib.file_digest(stream, 'sha256').hexdigest()
    if digest != volume['sha256'] or path.stat().st_size != volume['octets']:
        raise SystemExit(f'Volume altéré : {path.name}')
    indices = list(range(volume['premiere_vue'], volume['derniere_vue'] + 1))
    if len(indices) != volume['pages']:
        raise SystemExit(f'Nombre de vues incohérent : {path.name}')
    covered.extend(indices)
    for index in indices:
        row = rows[index-1]
        if row['volume'] != path.name or int(row['page_dans_volume']) != index-indices[0]+1:
            raise SystemExit(f'Correspondance de source incorrecte pour la vue {index}')
if covered != list(range(1, expected+1)):
    raise SystemExit('Les volumes ne couvrent pas exactement le document original.')
allowed = {'à transcrire', 'en cours', 'transcrit', 'relu', 'sans texte'}
for row in rows:
    if row['statut'] not in allowed:
        raise SystemExit(f"Statut inconnu : {row['statut']}")
    if row['statut'] in {'transcrit', 'relu'}:
        target = (ROOT / row['fichier_transcription']).resolve()
        if not row['fichier_transcription'] or not target.is_relative_to(ROOT) or not target.is_file():
            raise SystemExit(f"Fichier de transcription manquant pour la vue {row['vue_pdf']}")
print(f'Corpus intègre : {expected} vues, {len(manifest["volumes"])} volumes.')
print('Suivi : ' + ', '.join(f'{count} {status}' for status, count in Counter(row['statut'] for row in rows).items()))
