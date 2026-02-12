import os
import sys

# Ajouter le dossier du projet au chemin Python
sys.path.insert(0, os.path.dirname(__file__))

# Importer l'application WSGI de Django
from katauparfum.wsgi import application

# Ce fichier est le point d'entrée pour LWS / cPanel (Phusion Passenger)