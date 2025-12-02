#!/bin/bash
# Script pour lancer le portfolio localement sur Mac/Linux

echo ""
echo "========================================"
echo " Portfolio - Lancement en Developpement"
echo "========================================"
echo ""

# Vérifier si venv existe
if [ ! -d "venv" ]; then
    echo "Création de l'environnement virtuel..."
    python3 -m venv venv
fi

# Activer venv
echo "Activation de l'environnement virtuel..."
source venv/bin/activate

# Installer les dépendances
echo "Installation des dépendances..."
pip install -r requirements.txt

# Lancer l'application
echo ""
echo "========================================"
echo " Application en cours de demarrage..."
echo " Ouvrez votre navigateur:"
echo " http://localhost:5000"
echo "========================================"
echo ""

python app/app.py
