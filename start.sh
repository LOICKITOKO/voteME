#!/bin/bash

# Démarrer le backend (ex: Django)
echo "Lancement du serveur backend..."
cd backend || exit  # On s'assure que le dossier backend existe
source env/bin/activate  # Active l'environnement virtuel si nécessaire
python manage.py runserver &  # Démarre Django en arrière-plan

# Démarrer le frontend (ex: React)
echo "Lancement du serveur frontend..."
cd ../frontend || exit  # On s'assure que le dossier frontend existe
npm start
