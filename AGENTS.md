# Instructions pour poursuivre le projet

- Transcrire exclusivement par lecture directe des images avec la vision du modèle, sans OCR, même comme brouillon. Les originaux ne sont jamais modifiés.
- Lire `CONVENTIONS_TRANSCRIPTION.md`, `SUIVI_TRANSCRIPTION.csv` et `LECTURES_A_VERIFIER.md` avant chaque reprise.
- Centraliser toutes les questions et tous les doutes dans `LECTURES_A_VERIFIER.md`, avec ID stable, repère de vue/côté/page manuscrite, question précise et statut. Garder aussi les réponses et preuves pour les questions résolues. Ne jamais combler silencieusement une lecture douteuse.
- Avancer par lots cohérents. Après chaque étape vérifiée, faire un commit conventionnel en français puis un push, comme demandé par l’utilisateur. Inclure dans le même lot le texte, le suivi et les questions nouvelles.
- Une transcription n’est pas une relecture indépendante : utiliser le statut `transcrit`, et ne pas annoncer le manuscrit complet tant qu’il ne l’est pas.
- Avant publication d’un lot : `python3 scripts/check_project.py`, `make build`, puis inspection visuelle du PDF et vérification des exports. Les repères de source restent dans les commentaires LaTeX.
