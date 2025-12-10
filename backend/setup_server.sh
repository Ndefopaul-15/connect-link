#!/bin/bash
# Script d'installation automatique pour Connect Link
# À exécuter sur le serveur conlk.zen-apps.com

echo "=========================================="
echo "INSTALLATION CONNECT LINK - PRODUCTION"
echo "=========================================="

# Aller dans le répertoire racine
cd /

echo ""
echo "1️⃣  Installation des dépendances Python..."
python3 -m pip install -r requirements.production.txt --user

echo ""
echo "2️⃣  Initialisation de la base de données..."
python3 init_database.py

echo ""
echo "3️⃣  Vérification des permissions..."
chmod 755 wsgi.py
chmod 644 .env
chmod 755 app/
chmod 755 public_html/

echo ""
echo "=========================================="
echo "✅ INSTALLATION TERMINÉE!"
echo "=========================================="
echo ""
echo "Testez votre application:"
echo "- Frontend: https://conlk.zen-apps.com"
echo "- API: https://conlk.zen-apps.com/api"
echo ""
