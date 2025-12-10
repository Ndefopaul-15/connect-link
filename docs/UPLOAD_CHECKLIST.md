# 📋 Checklist de Déploiement - conlk.zen-apps.com

## ✅ Étapes Complétées

- [x] Clés secrètes générées
- [x] Frontend build créé (`frontend/dist/`)
- [x] Configuration production prête
- [x] PyMySQL installé

---

## 📦 Fichiers à Uploader via FTP

### Connexion FTP
- **Hôte:** conlk.zen-apps.com
- **Utilisateur:** conlkaccountftp
- **Mot de passe:** 1xbz22B0?
- **Port:** 21
- **Répertoire:** /conlk.zen-apps.com

---

## 📂 Structure à Créer sur le Serveur

```
/conlk.zen-apps.com/
├── api/                          # Backend Flask
│   ├── app/                      # Copier tout le dossier app/
│   ├── migrations/               # Copier migrations/
│   ├── .env                      # CRÉER sur le serveur (voir ci-dessous)
│   ├── wsgi.py                   # CRÉER sur le serveur
│   └── requirements.txt          # Copier requirements.production.txt
│
├── public_html/                  # Frontend (ou www/)
│   └── [Contenu de frontend/dist/]
│       ├── index.html
│       ├── assets/
│       └── ...
│
└── .htaccess                     # Configuration Apache
```

---

## 🔧 Fichiers à CRÉER sur le Serveur

### 1. `/conlk.zen-apps.com/api/.env`

```env
FLASK_ENV=production
FLASK_DEBUG=False

# ⚠️ REMPLACER par les clés générées
SECRET_KEY=0cc77ae1bbdda1c1a89d087550cd5bedc6abe27bf022051ae2d9095a17c8b3ee
JWT_SECRET_KEY=3e37307a56af10b69cd3a26a396b1bae4e62151a94480002c1aea3e82b21bbfb

# Base de données MariaDB
DATABASE_URL=mysql+pymysql://conlkdbuser:l0X&Vo$6pok0Wqii@localhost:3306/conlkdb

# Domaine
DEFAULT_DOMAIN=https://conlk.zen-apps.com
FRONTEND_URL=https://conlk.zen-apps.com
```

### 2. `/conlk.zen-apps.com/api/wsgi.py`

```python
import sys
import os

# Ajouter le chemin du projet
sys.path.insert(0, os.path.dirname(__file__))

from app import create_app

application = create_app('production')

if __name__ == "__main__":
    application.run()
```

### 3. `/conlk.zen-apps.com/.htaccess` (Racine)

```apache
# Redirection HTTPS
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

# API Backend (Flask)
RewriteCond %{REQUEST_URI} ^/api/
RewriteRule ^api/(.*)$ /api/wsgi.py/$1 [QSA,L]

# Frontend (React)
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ /public_html/index.html [L]
```

---

## 🚀 Commandes à Exécuter sur le Serveur

### Via SSH (si disponible)

```bash
# 1. Aller dans le dossier API
cd /conlk.zen-apps.com/api

# 2. Installer les dépendances Python
python3 -m pip install -r requirements.txt --user

# 3. Initialiser la base de données
export FLASK_APP=wsgi.py
export FLASK_ENV=production
flask db upgrade

# 4. Tester l'application
python3 wsgi.py
```

### Via cPanel / Panneau d'administration

1. **Python App Manager:**
   - Créer une application Python
   - Pointer vers `/conlk.zen-apps.com/api/wsgi.py`
   - Installer les requirements

2. **phpMyAdmin:**
   - Vérifier que la base `conlkdb` existe
   - Importer le schéma si nécessaire

---

## ✅ Tests Post-Déploiement

### 1. Tester le Frontend
```
https://conlk.zen-apps.com
```
✓ La page de login/register doit s'afficher

### 2. Tester l'API
```
https://conlk.zen-apps.com/api
```
✓ Doit retourner un JSON avec les infos de l'API

### 3. Tester l'inscription
```
1. Aller sur https://conlk.zen-apps.com
2. Créer un compte
3. Se connecter
4. Créer un lien court
```

### 4. Tester la redirection
```
https://conlk.zen-apps.com/{slug}
```
✓ Doit rediriger vers l'URL longue

---

## 🐛 Dépannage

### Erreur 500
- Vérifier les logs Apache/Python
- Vérifier que `.env` existe et est correct
- Vérifier les permissions des fichiers

### Base de données non accessible
- Vérifier les credentials dans `.env`
- Tester la connexion avec `test_db_connection.py` sur le serveur
- Vérifier que MariaDB est démarré

### Frontend ne charge pas
- Vérifier que les fichiers sont dans `public_html/`
- Vérifier le `.htaccess`
- Vérifier les permissions (755 pour dossiers, 644 pour fichiers)

### CORS Errors
- Vérifier `FRONTEND_URL` dans `.env`
- Vérifier la configuration CORS dans Flask

---

## 📞 Support

Si problème persistant:
1. Consulter les logs du serveur
2. Contacter le support de l'hébergeur
3. Vérifier la documentation Flask/MariaDB

---

## 🔒 Sécurité

- [ ] Clés secrètes changées
- [ ] HTTPS activé
- [ ] `.env` non accessible publiquement
- [ ] Permissions fichiers correctes
- [ ] Base de données sécurisée

---

**Date de déploiement:** _____________
**Version:** 1.0.0
**Déployé par:** _____________
