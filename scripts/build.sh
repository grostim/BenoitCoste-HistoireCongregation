#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
export RELEASE_VERSION="${1:-Version de développement}"
mkdir -p dist
python3 - <<'PYCODE'
import os
import re
from pathlib import Path
version = os.environ['RELEASE_VERSION']
if version != 'Version de développement' and not re.fullmatch(r'v[0-9]+\.[0-9]+\.[0-9]+', version):
    raise SystemExit('Version attendue : vX.Y.Z')
source = Path('main.tex').read_text(encoding='utf-8')
default = r'\providecommand{\releaseversion}{Version de développement}'
if source.count(default) != 1:
    raise SystemExit('Définition de version introuvable ou ambiguë.')
Path('dist/main.release.tex').write_text(source.replace(default, rf'\providecommand{{\releaseversion}}{{{version}}}'), encoding='utf-8')
PYCODE
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=dist dist/main.release.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=dist dist/main.release.tex
cp dist/main.release.pdf dist/Histoire_de_la_Congregation.pdf
pandoc dist/main.release.tex -f latex -t gfm --lua-filter=scripts/markdown.lua --wrap=none -o dist/Histoire_de_la_Congregation.md
pandoc dist/main.release.tex -f latex -t epub3 --toc --toc-depth=2 \
  --metadata title="Histoire de la Congrégation des jeunes gens — transcription en cours" \
  --metadata author="Benoît Coste (attribution précisée par Timothée Gros ; manuscrit copié)" \
  --metadata language=fr -o dist/Histoire_de_la_Congregation.epub
