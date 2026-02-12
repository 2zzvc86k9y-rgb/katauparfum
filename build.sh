#!/usr/bin/env bash
# exit on error
set -o errexit

# Installer les dépendances
pip install -r requirements.txt

# Collecter les fichiers statiques (CSS, Images)
python manage.py collectstatic --no-input

# Mettre à jour la base de données
python manage.py migrate

# Créer le superutilisateur (si inexistant)
python create_superuser.py