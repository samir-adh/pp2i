# PPII «Projet Pluridisciplinaire d'Informatique Intégrative» (2022-2023)

Olivier Festor <<olivier.festor@telecomnancy.eu>>  
Anne-Claure Heurtel <<anne-claire.heurtel@telecomnancy.eu>>
Gérald Oster <<gerald.oster@telecomnancy.eu>>  


## PlantPlacer

**Membres du groupe** :
- ABDALLAH Samir
- BOUALIT Yamine
- DIDON Adrien
- SAMBA Romain

## Description du projet

Créer une application web capable de créer au mieux un plan de potager optimisé par rapport à la surface disponible et aux plantes à disposition.

## Comment lancer l'application

ATTENTION : il faut faire tourner l'app dans le dossier 'pp2i', SURTOUT PAS dans 'app' ni 'app/flask/'

Pour la faire tourner en "mode presentation" il suffit juste d'entrer dans le terminal "source ./setup.sh" dans LE BON DOSSIER (cf. la ligne du dessus) AVERTISSEMENT : "setup.sh" VIDE TOTALEMENT LA BASE DE DONNÉES. (cf. Nota bene)

Au cas où on souhaiterai relancer l'application sans supprimer les données présentes il faut entrer dans le terminal "source ./run.sh" dans LE BON DOSSIER

## Nota bene :
Le fichier "setup_presentation.py" executé lors de l'éxecution de "run.sh" vide la base de donnée (utilisateurs et plans).
Puis la remplit en ajoutant comme unique utilisateur "Romain Samba" avec comme mot de passe "columbia".
Ensuite il ajoute automatiquement 3 potagers à son profil.
