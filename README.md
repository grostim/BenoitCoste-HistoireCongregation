# BenoitCoste-HistoireCongrégation

[![Validation et publication](https://github.com/grostim/BenoitCoste-HistoireCongregation/actions/workflows/ci-release.yml/badge.svg)](https://github.com/grostim/BenoitCoste-HistoireCongregation/actions/workflows/ci-release.yml)

Projet de transcription de l’**Histoire de la Congrégation des jeunes gens**, à partir du manuscrit numérisé fourni sous le nom « Histoire Congrégation (1).pdf ».

Projet jumeau de [grostim/BenoitCoste](https://github.com/grostim/BenoitCoste) : même classe LaTeX `report`, typographie française, notes séparant auteur et transcripteur, signalement des corrections et publication PDF, EPUB et Markdown.

Le nom éditorial du projet conserve l’accent. L’adresse GitHub utilise `BenoitCoste-HistoireCongregation` pour disposer d’une URL simple et stable.

## État d’avancement

**92 vues entièrement transcrites sur 182, plus le début de la vue 93.** Le texte couvre les pages manuscrites 1 à 27 puis 30 à 186 (début) : épître dédicatoire, adresse du 8 mai 1841, plan et quatre chapitres du Précis historique complet, puis les six premiers chapitres complets de l’histoire : fondation, préfecture de M. Ripoud et celle de M. Chaulet, jusqu’au passage du pape et à l’ouverture de Fourvières (p. 77–186, début). Les pages 28–29 manquent entre les vues 14 et 15 du PDF fourni ; la lacune est signalée sans reconstitution. Lecture directe avec la vision du modèle, sans OCR ; relecture indépendante à effectuer. Les lectures incertaines et toutes les questions restent dans le [registre dédié](LECTURES_A_VERIFIER.md). La reprise se fera à la vue 93, côté gauche, p. 186 : début du chapitre septième, préfecture de M. Philpin et suspension de la célébration des fêtes dans une chapelle particulière. La numérotation des chapitres recommence au début de cette partie, conformément au manuscrit. Les vues PDF sont généralement des doubles pages du manuscrit ; leur nombre ne correspond pas au nombre de pages manuscrites.

Le titre est lisible au début du document. Le rattachement à Benoît Coste reprend le cadrage du projet ; l’attribution des parties, le découpage en chapitres et les changements de main restent à vérifier directement dans le manuscrit. Aucun contenu des Mémoires ni aucune annexe généalogique n’a été repris comme texte de cet ouvrage.

## Consulter les sources

- [Original intégral, inchangé](https://github.com/grostim/BenoitCoste-HistoireCongregation/releases/download/sources-v1.0.0/Histoire_Congregation_original.pdf) : 182 vues, environ 155 Mo.
- [Originaux/README.md](Originaux/README.md) : trois volumes de consultation et provenance.
- [SUIVI_TRANSCRIPTION.csv](SUIVI_TRANSCRIPTION.csv) : une ligne par vue, repères du manuscrit et état de lecture.

Le PDF ne comporte pas de couche de texte exploitable. La transcription se fait exclusivement avec la vision du modèle, par lecture directe des scans, sans OCR.

## Éditions de travail

Chaque mise à jour de `main` compile et publie les trois formats. Une demande de modification les compile sans créer de release.

- [PDF](https://github.com/grostim/BenoitCoste-HistoireCongregation/releases/latest/download/Histoire_de_la_Congregation.pdf)
- [EPUB](https://github.com/grostim/BenoitCoste-HistoireCongregation/releases/latest/download/Histoire_de_la_Congregation.epub)
- [Markdown](https://github.com/grostim/BenoitCoste-HistoireCongregation/releases/latest/download/Histoire_de_la_Congregation.md)

Ces fichiers restent explicitement marqués comme travaux en cours jusqu’à la fin de la transcription et de la relecture.

## Travailler sur la transcription

1. Lire les [conventions](CONVENTIONS_TRANSCRIPTION.md).
2. Relever les numéros réellement visibles, sans les déduire du rang de la vue.
3. Créer les sections transcrites dans `transcription/`, puis les inclure depuis `transcription/texte.tex`.
4. Ajouter les repères de source dans les commentaires LaTeX et compléter le suivi CSV.
5. Compiler et contrôler les trois sorties avant de valider un lot.

Dépendances : Python 3.11 ou ultérieur, TeX Live avec français, `lmodern`, `fancyhdr`, et Pandoc.

```sh
python3 scripts/check_project.py
make build
```

Les sorties sont placées dans `dist/`. `make clean` les supprime. Pour injecter un numéro de version : `make build VERSION=v0.1.0`.

## Organisation

```text
main.tex                       Mise en page et note éditoriale
transcription/texte.tex         Point d’entrée du texte à transcrire
Originaux/                     Volumes, manifeste et provenance
SUIVI_TRANSCRIPTION.csv         Suivi des 182 vues
CONVENTIONS_TRANSCRIPTION.md    Règles adaptées à ce manuscrit
scripts/check_project.py       Intégrité et cohérence du corpus
scripts/build.sh               PDF, EPUB et Markdown
.github/                       Publication et formulaire de correction
PROVENANCE.md                  Origine des éléments réutilisés
```

Les commits suivent les conventions françaises du projet modèle : `feat:` pour un nouveau lot transcrit, `fix:` pour une correction, `docs:`, `style:`, `refactor:` ou `chore:` selon le changement. La numérotation repart de zéro pour ce nouveau corpus ; elle n’est pas reprise des Mémoires.
