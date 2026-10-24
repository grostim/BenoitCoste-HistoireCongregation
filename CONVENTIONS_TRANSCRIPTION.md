# Conventions de transcription

Adaptation des principes du projet jumeau [BenoitCoste](https://github.com/grostim/BenoitCoste), pour un corpus manuscrit distinct.

## Corpus et repérage

- Source de référence : PDF intégral archivé, décrit dans `Originaux/manifest.json`.
- Distinguer systématiquement la vue PDF, son côté gauche/droit et la pagination manuscrite.
- Ne pas inventer de chapitre, de date ou de numéro de page à partir des Mémoires.
- Conserver l’ordre du manuscrit. Établir les titres et les changements de main sur lecture directe ; toute attribution incertaine reste signalée.
- Ne pas copier de texte des Mémoires, de leurs préfaces ou de leurs annexes dans cet ouvrage.

## Lecture et fidélité

- Transcrire exclusivement par lecture visuelle directe des scans avec la vision du modèle, sans OCR. Cette règle s’applique aussi aux reprises, aux marges et à la relecture. Ne pas utiliser de moteur OCR ni de transcription OCR comme base du texte.
- Développer les abréviations de mois en toutes lettres (notamment « 7bre » en « septembre »), suivant la décision de Timothée Gros en Q006 ; conserver les dates divergentes du manuscrit.
- Respecter le sens et le vocabulaire. À la demande de Timothée Gros du 24 octobre 2026, moderniser les anciennes terminaisons verbales `-ois`, `-oit`, `-oient` en `-ais`, `-ait`, `-aient`, ainsi que les familles de « connoître » / « reconnoître » et « paroître » (« connaître », « reconnaissance », « paraître », etc.). Les formes modernes comme « doit », « croit », « reçoit », les noms propres et les mots non verbaux restent inchangés. Les autres particularités d’orthographe historique sont conservées. Les réponses et citations de travail du registre gardent leur forme d’origine.
- Intégrer les ajouts et corrections lisibles qui constituent le texte final. Signaler une lecture concurrente importante en note du transcripteur.
- Indiquer explicitement `[illisible]`, `[mot incertain : …]` ou `[lacune]` ; ne pas compléter par conjecture silencieuse.
- Conserver toutes les notes de l’auteur. Marquer séparément toute explication ajoutée par `(Note du transcripteur)`.
- Pour le latin, conserver le texte, ajouter une traduction en note du transcripteur et vérifier sa source avant de donner une référence précise. Ne pas inventer d’identification.

## Structure LaTeX

Le point d’entrée est `main.tex`, qui inclut `transcription/texte.tex`. Les lots peuvent être répartis dans des fichiers à noms stables, par exemple `transcription/001-epitre.tex`, lorsqu’un découpage aura été vérifié.

Utiliser `\chapter{...}` pour un chapitre confirmé, `\chapter*{...}` avec `\addcontentsline` pour une pièce liminaire, `\section*{...}` pour une mention marginale et `\footnote{...}` pour les notes.

Avant chaque passage, conserver un commentaire de provenance :

```latex
% Source : PDF original, vue 002, côté droit, page manuscrite 3.
% Statut : transcrit ; relecture à effectuer.
```

Typographie française : accents et ligatures (`œ`, `æ`), espaces gérées par `babel`, exposants avec `\up{e}`, intervalles de dates avec `--`, latin en `\textit{...}`. Échapper les caractères spéciaux LaTeX (`%`, `&`, `_`, `#`, etc.). Les titres conservent les noms propres et emploient une casse ordinaire.

## Avancement et validation

`SUIVI_TRANSCRIPTION.csv` contient une ligne par vue PDF. Ne jamais calculer l’avancement en pages manuscrites à partir du nombre de vues.

Statuts autorisés : `à transcrire`, `en cours`, `transcrit`, `relu`, `sans texte`. Une vue partiellement transcrite reste `en cours`. Une vue ne passe à `relu` qu’après comparaison de toute sa surface avec la source, notes et marges comprises. `sans texte` exige également une inspection visuelle.

Toutes les questions et tous les doutes à lever sont centralisés dans `LECTURES_A_VERIFIER.md`, avec un identifiant stable, les repères de source, la question précise et son statut. Conserver les questions résolues avec la solution et la preuve de lecture ; ne pas les effacer.

Le fichier de transcription et les observations doivent permettre de retrouver chaque passage. Relever les blancs, anomalies de pagination et changements de main au fil de la lecture. Un scan vierge ne doit pas être classé automatiquement.

Avant validation : lancer `python3 scripts/check_project.py`, puis `make build`, vérifier le PDF, l’EPUB et le Markdown, et mettre à jour le suivi et la présentation du projet. Les contrôles automatiques vérifient la structure et les empreintes ; ils ne prouvent pas la justesse de la lecture.

## Versionnement et publication

À la demande de Timothée Gros, chaque étape terminée et vérifiée fait l’objet d’un commit puis d’un push. Une étape de transcription inclut le texte, les repères, le suivi et les nouvelles questions. Ne pas attendre la fin du manuscrit pour publier les étapes.

Commits conventionnels en français : `feat:`, `fix:`, `docs:`, `style:`, `refactor:`, `chore:`. Un nouveau lot transcrit correspond à un commit cohérent avec les repères sources et le suivi à jour.

La CI compile les demandes de modification. Une mise à jour de `main` publie une nouvelle édition de travail PDF, EPUB et Markdown, après succès des contrôles. Version initiale `v0.0.1`, puis version majeure pour `feat:`, mineure pour `fix:`, `docs:`, `style:` et `refactor:`, corrective pour la maintenance.

La release `sources-v1.0.0` conserve l’original ; elle est distincte de la numérotation de l’édition. Les versions de travail ne doivent jamais être présentées comme une transcription complète tant que le corpus n’a pas été transcrit et relu.
