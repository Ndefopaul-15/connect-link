# Déploiement sur conlk.zen-apps.com

## Informations de Production

**Domaine:** conlk.zen-apps.com  
**Type d'hébergement:** Hébergement web avec FTP  
**Base de données:** MariaDB

---

## Étape 1: Préparation Locale

### 1.1 Installer les dépendances de production
```bash
pip install -r requirements.production.txt
```

### 1.2 Créer les tables de base de données
```bash
# Configurer la connexion à la base de données de production
export FLASK_ENV=production
export DATABASE_URL="mysql+pymysql://conlkdbuser:l0X&Vo$6pok0Wqii@localhost:3306/conlkdb"

# Initialiser les migrations
flask db init  # Si pas déjà fait
flask db migrate -m "Initial production migration"
flask db upgrade
```

---

## Étape 2: Build du Frontend

### 2.1 Mettre à jour l'URL de l'API
Éditer `frontend/src/services/api.ts`:
```typescript
const API_BASE_URL = 'https://conlk.zen-apps.com/api';
```

### 2.2 Build de production
```bash
cd frontend
npm install
npm run build
```

Le dossier `dist/` contiendra les fichiers optimisés.

---

## Étape 3: Préparation des Fichiers Backend

### 3.1 Créer le fichier .env sur le serveur
Créer `.env` avec le contenu de `.env.production` (sans le mot de passe en clair)

### 3.2 Créer le fichier WSGI
Créer `wsgi.py` à la racine:
```python
from app import create_app

app = create_app('production')

if __name__ == "__main__":
    app.run()
```

---

## Étape 4: Upload via FTP

### Informations FTP
- **Hôte:** conlk.zen-apps.com
- **Utilisateur:** conlkaccountftp
- **Mot de passe:** 1xbz22B0?
- **Répertoire:** /conlk.zen-apps.com
- **Port:** 21

### Structure à uploader
```
/conlk.zen-apps.com/
├── app/                    # Dossier Flask backend
├── frontend/dist/          # Build React (renommer en 'public' ou 'static')
├── instance/               # Dossier pour la base de données SQLite (si utilisé)
├── migrations/             # Migrations de base de données
├── .env                    # Variables d'environnement (CRÉER SUR LE SERVEUR)
├── wsgi.py                 # Point d'entrée WSGI
├── requirements.production.txt
└── .htaccess              # Configuration Apache (à créer)
```

---

## Étape 5: Configuration du Serveur

### 5.1 Créer .htaccess pour Apache
```apache
# Redirection vers HTTPS
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

# Configuration Python/Flask
Options +ExecCGI
AddHandler wsgi-script .py
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^(.*)$ /wsgi.py/$1 [QSA,L]
```

### 5.2 Vérifier Python sur le serveur
Le serveur doit avoir:
- Python 3.9+
- pip
- Support WSGI (mod_wsgi pour Apache)

---

## Étape 6: Configuration de la Base de Données

### 6.1 Créer les tables
Connectez-vous au serveur via SSH (si disponible) ou utilisez phpMyAdmin:

```sql
-- Les tables seront créées automatiquement par Flask-Migrate
-- Ou manuellement via le script de migration
```

### 6.2 Tester la connexion
```python
# Test de connexion MariaDB
import pymysql

connection = pymysql.connect(
    host='localhost',
    user='conlkdbuser',
    password='l0X&Vo$6pok0Wqii',
    database='conlkdb',
    port=3306
)
print("Connexion réussie!")
connection.close()
```

---

## Étape 7: Sécurité

### 7.1 Générer des clés secrètes
```python
import secrets
print("SECRET_KEY:", secrets.token_hex(32))
print("JWT_SECRET_KEY:", secrets.token_hex(32))
```

### 7.2 Mettre à jour .env sur le serveur
Remplacer les clés par défaut par les nouvelles clés générées.

### 7.3 Permissions des fichiers
```bash
chmod 644 .env
chmod 755 app/
chmod 755 wsgi.py
```

---

## Étape 8: Test et Vérification

### 8.1 URLs à tester
- https://conlk.zen-apps.com (Frontend)
- https://conlk.zen-apps.com/api (API)
- https://conlk.zen-apps.com/api/auth/register (Test endpoint)

### 8.2 Vérifier les logs
Consulter les logs du serveur pour détecter les erreurs.

---

## Dépannage

### Erreur 500
- Vérifier les logs Apache/Python
- Vérifier les permissions des fichiers
- Vérifier la connexion à la base de données

### CORS Errors
- Vérifier que FRONTEND_URL est correctement configuré
- Vérifier la configuration CORS dans Flask

### Database Connection Failed
- Vérifier les credentials dans .env
- Vérifier que MariaDB est accessible
- Tester la connexion manuellement

---

## Notes Importantes

1. **Ne jamais commiter .env dans Git**
2. **Sauvegarder régulièrement la base de données**
3. **Utiliser HTTPS en production**
4. **Monitorer les logs d'erreur**
5. **Mettre à jour régulièrement les dépendances**

---

## Contact Support

Si vous rencontrez des problèmes:
1. Vérifier les logs du serveur
2. Contacter le support de l'hébergeur
3. Consulter la documentation Flask/MariaDB
