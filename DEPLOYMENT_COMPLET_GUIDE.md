# 🚀 Guide de Déploiement Complet - Connect Link
## Backend (Render.com) + Frontend (zen-apps.com) + Base de données (MariaDB)

---

# 📋 TABLE DES MATIÈRES

1. [ÉTAPE 0: Nettoyage du Serveur](#étape-0-nettoyage-du-serveur)
2. [ÉTAPE 1: Déployer le Backend sur Render.com](#étape-1-déployer-le-backend-sur-rendercom)
3. [ÉTAPE 2: Déployer le Frontend sur zen-apps.com](#étape-2-déployer-le-frontend-sur-zen-appscom)
4. [ÉTAPE 3: Configurer la Base de Données](#étape-3-configurer-la-base-de-données)
5. [ÉTAPE 4: Connecter Frontend et Backend](#étape-4-connecter-frontend-et-backend)
6. [ÉTAPE 5: Tester l'Application](#étape-5-tester-lapplication)

---

# ÉTAPE 0: Nettoyage du Serveur

## 🗑️ Supprimer les Anciens Fichiers via FileZilla

### 1. Connectez-vous à FileZilla

```
Host:     conlk.zen-apps.com
User:     conlkaccountftp
Pass:     1xbz22B0?
Port:     21
```

### 2. Supprimez TOUT sur le Serveur

**Sur le côté droit (serveur), sélectionnez et supprimez:**

- [ ] 📁 `app/` (dossier complet)
- [ ] 📁 `api/`
- [ ] 📁 `config/`
- [ ] 📁 `core/`
- [ ] 📁 `crud/`
- [ ] 📁 `models/`
- [ ] 📁 `routes/`
- [ ] 📁 `schemas/`
- [ ] 📁 `tests/`
- [ ] 📁 `utils/`
- [ ] 📁 `public_html/` (si existe)
- [ ] 📄 `.env`
- [ ] 📄 `.htaccess`
- [ ] 📄 `init_database.py`
- [ ] 📄 `requirements.production.txt`
- [ ] 📄 `setup_server.sh`
- [ ] 📄 `wsgi.py`

**Comment supprimer:**
1. Clic droit sur chaque fichier/dossier
2. Choisir "Supprimer"
3. Confirmer

### 3. Vérifiez que le Serveur est Vide

Le côté droit (serveur) devrait être **complètement vide** ou avoir seulement des dossiers système.

✅ **Serveur nettoyé!**

---

# ÉTAPE 1: Déployer le Backend sur Render.com

## 🌐 Pourquoi Render.com?

- ✅ **Gratuit** (plan gratuit permanent)
- ✅ **Support Python/Flask** natif
- ✅ **Déploiement automatique** depuis GitHub
- ✅ **Base de données PostgreSQL** gratuite incluse
- ✅ **HTTPS** automatique
- ✅ **Pas besoin de SSH**

---

## 1.1: Créer un Compte Render.com

### Étapes:

1. **Allez sur**: https://render.com
2. **Cliquez**: "Get Started" ou "Sign Up"
3. **Inscrivez-vous avec**:
   - GitHub (recommandé)
   - OU Email

4. **Confirmez votre email**

✅ **Compte créé!**

---

## 1.2: Préparer le Code pour Render

### Créer les Fichiers de Configuration

Nous devons créer quelques fichiers pour Render.

### A. Créer `render.yaml`

Ce fichier indique à Render comment déployer l'application.

**Créez**: `c:\Users\HP\Desktop\connect link\render.yaml`

```yaml
services:
  - type: web
    name: connect-link-backend
    env: python
    region: frankfurt
    plan: free
    branch: main
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn wsgi:app
    envVars:
      - key: FLASK_ENV
        value: production
      - key: FLASK_DEBUG
        value: False
      - key: SECRET_KEY
        generateValue: true
      - key: JWT_SECRET_KEY
        generateValue: true
      - key: DEFAULT_DOMAIN
        sync: false
      - key: FRONTEND_URL
        sync: false
      - key: DATABASE_URL
        fromDatabase:
          name: connect-link-db
          property: connectionString

databases:
  - name: connect-link-db
    databaseName: connectlink
    user: connectlink
    plan: free
    region: frankfurt
```

### B. Mettre à Jour `requirements.txt`

**Vérifiez**: `c:\Users\HP\Desktop\connect link\backend\requirements.production.txt`

**Ajoutez `gunicorn`** si pas déjà présent:

```txt
Flask==3.1.2
Flask-SQLAlchemy==3.1.1
Flask-Migrate==4.0.5
Flask-JWT-Extended==4.6.0
Flask-Bcrypt==1.0.1
Flask-CORS==5.0.0
SQLAlchemy==2.0.44
PyMySQL==1.1.0
python-dotenv==1.0.0
shortuuid==1.0.11
qrcode==7.4.2
Pillow==10.1.0
validators==0.22.0
dnspython==2.4.2
gunicorn==21.2.0
psycopg2-binary==2.9.9
```

**Sauvegardez** ce fichier comme `requirements.txt` dans le dossier racine:
- Copiez `backend/requirements.production.txt`
- Collez dans `c:\Users\HP\Desktop\connect link\requirements.txt`
- Ajoutez les 2 dernières lignes (gunicorn et psycopg2-binary)

### C. Créer `runtime.txt`

**Créez**: `c:\Users\HP\Desktop\connect link\runtime.txt`

```txt
python-3.11.0
```

### D. Mettre à Jour `wsgi.py`

**Vérifiez**: `c:\Users\HP\Desktop\connect link\backend\wsgi.py`

Devrait ressembler à:

```python
import os
import sys

# Add the backend directory to the Python path
sys.path.insert(0, os.path.dirname(__file__))

from app import create_app

# Create the application instance
app = create_app(os.getenv('FLASK_ENV', 'production'))

if __name__ == '__main__':
    app.run()
```

---

## 1.3: Pousser le Code sur GitHub

### A. Initialiser Git (si pas déjà fait)

Ouvrez PowerShell dans votre projet:

```powershell
cd "C:\Users\HP\Desktop\connect link"
git init
```

### B. Créer `.gitignore`

**Vérifiez**: `c:\Users\HP\Desktop\connect link\.gitignore`

Devrait contenir:

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
.venv/
env/
ENV/

# Flask
instance/
.env
.env.local
*.db
*.sqlite

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Node
node_modules/
frontend/node_modules/
frontend/dist/
frontend/.vite/

# Logs
*.log
```

### C. Créer un Dépôt GitHub

1. **Allez sur**: https://github.com
2. **Connectez-vous** (ou créez un compte)
3. **Cliquez**: "New repository" (bouton vert)
4. **Nom**: `connect-link`
5. **Visibilité**: Private (recommandé)
6. **NE PAS** cocher "Initialize with README"
7. **Cliquez**: "Create repository"

### D. Pousser le Code

Dans PowerShell:

```powershell
cd "C:\Users\HP\Desktop\connect link"

# Ajouter tous les fichiers
git add .

# Créer le premier commit
git commit -m "Initial commit - Connect Link"

# Ajouter le dépôt distant (remplacez VOTRE_USERNAME)
git remote add origin https://github.com/VOTRE_USERNAME/connect-link.git

# Pousser le code
git branch -M main
git push -u origin main
```

**Entrez vos identifiants GitHub** quand demandé.

✅ **Code sur GitHub!**

---

## 1.4: Déployer sur Render.com

### A. Créer un Nouveau Web Service

1. **Connectez-vous à**: https://dashboard.render.com
2. **Cliquez**: "New +" (en haut à droite)
3. **Choisissez**: "Web Service"

### B. Connecter GitHub

1. **Cliquez**: "Connect GitHub"
2. **Autorisez** Render à accéder à vos dépôts
3. **Sélectionnez**: `connect-link` (votre dépôt)
4. **Cliquez**: "Connect"

### C. Configurer le Service

**Remplissez le formulaire:**

```
Name:              connect-link-backend
Region:            Frankfurt (EU Central)
Branch:            main
Root Directory:    backend
Runtime:           Python 3
Build Command:     pip install -r requirements.txt
Start Command:     gunicorn wsgi:app --bind 0.0.0.0:$PORT
Instance Type:     Free
```

### D. Ajouter les Variables d'Environnement

**Cliquez**: "Advanced" → "Add Environment Variable"

**Ajoutez ces variables:**

| Key | Value |
|-----|-------|
| `FLASK_ENV` | `production` |
| `FLASK_DEBUG` | `False` |
| `SECRET_KEY` | `0cc77ae1bbdda1c1a89d087550cd5bedc6abe27bf022051ae2d9095a17c8b3ee` |
| `JWT_SECRET_KEY` | `3e37307a56af10b69cd3a26a396b1bae4e62151a94480002c1aea3e82b21bbfb` |
| `DATABASE_URL` | `mysql+pymysql://conlkdbuser:l0X&Vo$6pok0Wqii@conlk.zen-apps.com:3306/conlkdb` |
| `DEFAULT_DOMAIN` | (laissez vide pour l'instant) |
| `FRONTEND_URL` | `https://conlk.zen-apps.com` |

### E. Créer le Service

**Cliquez**: "Create Web Service"

**Attendez** 5-10 minutes pendant le déploiement.

### F. Récupérer l'URL du Backend

Une fois déployé, vous verrez:

```
Your service is live at https://connect-link-backend-XXXX.onrender.com
```

**Copiez cette URL!** Vous en aurez besoin.

**Mettez à jour** la variable `DEFAULT_DOMAIN`:
1. Allez dans "Environment"
2. Modifiez `DEFAULT_DOMAIN` → `https://connect-link-backend-XXXX.onrender.com`
3. Sauvegardez

✅ **Backend déployé sur Render.com!**

---

# ÉTAPE 2: Déployer le Frontend sur zen-apps.com

## 2.1: Préparer le Frontend

### A. Mettre à Jour l'URL de l'API

**Modifiez**: `c:\Users\HP\Desktop\connect link\frontend\.env.production`

**Créez ce fichier** s'il n'existe pas:

```env
VITE_API_BASE_URL=https://connect-link-backend-XXXX.onrender.com/api
```

**Remplacez** `XXXX` par votre URL Render.com!

### B. Builder le Frontend

Ouvrez PowerShell:

```powershell
cd "C:\Users\HP\Desktop\connect link\frontend"
npm run build
```

**Attendez** ~1-2 minutes.

**Vérifiez** que le dossier `dist/` est créé avec:
- `index.html`
- `assets/` folder
- Logo files

✅ **Frontend buildé!**

---

## 2.2: Uploader le Frontend via FileZilla

### A. Connectez-vous à FileZilla

```
Host:     conlk.zen-apps.com
User:     conlkaccountftp
Pass:     1xbz22B0?
Port:     21
```

### B. Créer le Dossier `public_html`

**Sur le serveur (côté droit):**

1. Clic droit dans l'espace vide
2. Choisir "Créer un dossier"
3. Nom: `public_html`
4. Double-cliquez pour entrer dedans

### C. Uploader TOUS les Fichiers du Frontend

**Côté local (gauche):**
- Naviguez vers: `C:\Users\HP\Desktop\connect link\frontend\dist\`

**Sélectionnez TOUS les fichiers:**
- `index.html`
- `assets/` (dossier complet)
- `favicon.svg`
- `logo-no-bg.svg`
- `logo.svg`
- `background.jpg`
- Tous les autres fichiers

**Glissez-déposez** TOUT vers `public_html/` sur le serveur (droite)

**Attendez** 2-3 minutes pour l'upload.

### D. Créer le Fichier `.htaccess` pour le Frontend

**Sur le serveur (dans `public_html/`):**

1. Clic droit → "Créer un fichier"
2. Nom: `.htaccess`
3. Clic droit sur `.htaccess` → "Voir/Éditer"
4. **Collez ce contenu:**

```apache
# Enable Rewrite Engine
RewriteEngine On

# Force HTTPS
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

# SPA Routing - Redirect all requests to index.html
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ index.html [L]

# Security Headers
<IfModule mod_headers.c>
    Header set X-Frame-Options "SAMEORIGIN"
    Header set X-XSS-Protection "1; mode=block"
    Header set X-Content-Type-Options "nosniff"
</IfModule>

# Compression
<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/html text/plain text/xml text/css text/javascript application/javascript application/json
</IfModule>

# Browser Caching
<IfModule mod_expires.c>
    ExpiresActive On
    ExpiresByType image/jpg "access plus 1 year"
    ExpiresByType image/jpeg "access plus 1 year"
    ExpiresByType image/gif "access plus 1 year"
    ExpiresByType image/png "access plus 1 year"
    ExpiresByType image/svg+xml "access plus 1 year"
    ExpiresByType text/css "access plus 1 month"
    ExpiresByType application/javascript "access plus 1 month"
    ExpiresByType text/html "access plus 0 seconds"
</IfModule>
```

5. **Sauvegardez** (Ctrl+S)
6. **Fermez** l'éditeur
7. Cliquez "Oui" pour uploader

✅ **Frontend déployé sur zen-apps.com!**

---

# ÉTAPE 3: Configurer la Base de Données

## 3.1: Vérifier la Base de Données MariaDB

Vous avez déjà une base de données MariaDB sur zen-apps.com:

```
Database:  conlkdb
User:      conlkdbuser
Password:  l0X&Vo$6pok0Wqii
Host:      localhost (depuis le serveur)
           OU conlk.zen-apps.com (depuis l'extérieur)
Port:      3306
```

## 3.2: Initialiser la Base de Données

### Option A: Via Render.com Shell (Recommandé)

1. **Allez sur**: https://dashboard.render.com
2. **Cliquez** sur votre service `connect-link-backend`
3. **Cliquez**: "Shell" (en haut à droite)
4. **Attendez** que le terminal s'ouvre
5. **Tapez**:

```bash
python init_database.py
```

6. **Appuyez** sur Entrée

**Vous devriez voir**: "Database initialized successfully!"

### Option B: Via Script Local (Alternative)

Si vous ne pouvez pas accéder au shell Render, créez un script temporaire:

**Créez**: `c:\Users\HP\Desktop\connect link\init_remote_db.py`

```python
import pymysql
from app.models import User, Domain, Link, Click, LinkDailyStats, TargetingRule, Reward

# Database connection
connection = pymysql.connect(
    host='conlk.zen-apps.com',
    user='conlkdbuser',
    password='l0X&Vo$6pok0Wqii',
    database='conlkdb',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

print("Connected to database!")

# Create tables
with connection.cursor() as cursor:
    # Read and execute SQL from models
    # (You'll need to export SQL from your models)
    print("Creating tables...")
    
connection.commit()
connection.close()
print("Database initialized!")
```

**Exécutez**:
```powershell
cd "C:\Users\HP\Desktop\connect link\backend"
python init_remote_db.py
```

✅ **Base de données initialisée!**

---

# ÉTAPE 4: Connecter Frontend et Backend

## 4.1: Vérifier la Configuration

### Backend (Render.com)

**URL**: `https://connect-link-backend-XXXX.onrender.com`

**Variables d'environnement configurées:**
- ✅ `DATABASE_URL` → MariaDB sur zen-apps.com
- ✅ `FRONTEND_URL` → `https://conlk.zen-apps.com`
- ✅ `CORS` configuré dans le code Flask

### Frontend (zen-apps.com)

**URL**: `https://conlk.zen-apps.com`

**Fichier `.env.production`:**
- ✅ `VITE_API_BASE_URL` → URL Render.com

## 4.2: Mettre à Jour CORS dans le Backend

**Vérifiez**: `c:\Users\HP\Desktop\connect link\backend\app\__init__.py`

**Ligne ~30**, assurez-vous que CORS permet votre domaine:

```python
CORS(app, 
     resources={r"/*": {"origins": ["https://conlk.zen-apps.com", "http://localhost:5174"]}},
     supports_credentials=True,
     allow_headers=["Content-Type", "Authorization"],
     methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"]
)
```

**Si vous modifiez**, poussez sur GitHub:

```powershell
git add .
git commit -m "Update CORS configuration"
git push
```

Render redéploiera automatiquement!

---

# ÉTAPE 5: Tester l'Application

## 5.1: Tester le Backend

**Ouvrez votre navigateur:**

```
https://connect-link-backend-XXXX.onrender.com/api
```

**Vous devriez voir**: JSON avec les informations de l'API

**Exemple:**
```json
{
  "api": {
    "name": "Connect Link API",
    "version": "1.0.0",
    "status": "running"
  }
}
```

✅ **Backend fonctionne!**

## 5.2: Tester le Frontend

**Ouvrez votre navigateur:**

```
https://conlk.zen-apps.com
```

**Vous devriez voir**: La page de connexion Connect Link

✅ **Frontend fonctionne!**

## 5.3: Tester l'Inscription

1. **Cliquez**: "S'inscrire" ou "Register"
2. **Remplissez** le formulaire:
   - Nom
   - Email
   - Mot de passe
3. **Cliquez**: "S'inscrire"

**Si succès**: Vous êtes redirigé vers le dashboard!

✅ **Backend et Frontend connectés!**

## 5.4: Tester la Création de Lien

1. **Dans le dashboard**, cliquez "Créer un lien"
2. **Entrez** une URL longue: `https://www.example.com`
3. **Cliquez**: "Créer"

**Si succès**: Vous voyez votre lien court!

✅ **Application complètement fonctionnelle!**

---

# 📊 RÉCAPITULATIF FINAL

## Architecture Déployée

```
┌─────────────────────────────────────────────────────────────┐
│                    UTILISATEUR                              │
│                 (Navigateur Web)                            │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       │ HTTPS
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              FRONTEND (React)                               │
│         https://conlk.zen-apps.com                          │
│         Hébergé sur: zen-apps.com                           │
│         Fichiers: public_html/                              │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       │ API Calls (HTTPS)
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              BACKEND (Flask)                                │
│    https://connect-link-backend-XXXX.onrender.com           │
│         Hébergé sur: Render.com                             │
│         Runtime: Python 3.11                                │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       │ MySQL Connection
                       ▼
┌─────────────────────────────────────────────────────────────┐
│           BASE DE DONNÉES (MariaDB)                         │
│         conlkdb @ conlk.zen-apps.com                        │
│         Hébergé sur: zen-apps.com                           │
└─────────────────────────────────────────────────────────────┘
```

## URLs Importantes

| Service | URL | Hébergeur |
|---------|-----|-----------|
| **Frontend** | `https://conlk.zen-apps.com` | zen-apps.com |
| **Backend API** | `https://connect-link-backend-XXXX.onrender.com/api` | Render.com |
| **Base de données** | `conlk.zen-apps.com:3306` | zen-apps.com |

## Identifiants

### Render.com
- Compte: Votre email/GitHub
- Dashboard: https://dashboard.render.com

### zen-apps.com (FTP)
- Host: `conlk.zen-apps.com`
- User: `conlkaccountftp`
- Pass: `1xbz22B0?`

### Base de données
- Database: `conlkdb`
- User: `conlkdbuser`
- Pass: `l0X&Vo$6pok0Wqii`

---

# 🎉 FÉLICITATIONS!

Votre application Connect Link est maintenant **complètement déployée** et **fonctionnelle**!

## ✅ Ce qui est fait:

- ✅ Backend Python/Flask sur Render.com (gratuit)
- ✅ Frontend React sur zen-apps.com
- ✅ Base de données MariaDB sur zen-apps.com
- ✅ HTTPS activé partout
- ✅ CORS configuré
- ✅ Application testée et fonctionnelle

## 🚀 Prochaines Étapes (Optionnel):

1. **Domaine personnalisé**: Configurer `conlk.zen-apps.com` comme domaine principal
2. **Monitoring**: Activer les alertes sur Render.com
3. **Backups**: Configurer des sauvegardes automatiques de la base de données
4. **Analytics**: Ajouter Google Analytics
5. **SEO**: Optimiser le référencement

---

**Dernière mise à jour**: 10 décembre 2025  
**Version**: 1.0 - Déploiement Complet  
**Temps total**: ~30-45 minutes
