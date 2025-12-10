# 📁 Guide FileZilla - Upload FTP Facile

## Étape 1: Téléchargement et Installation 💾

### 1.1 Télécharger FileZilla
1. Ouvrir votre navigateur
2. Aller sur: **https://filezilla-project.org/download.php?type=client**
3. Cliquer sur **"Download FileZilla Client"**
4. Choisir la version pour Windows (64-bit)

### 1.2 Installer FileZilla
1. Ouvrir le fichier téléchargé (`FileZilla_3.x.x_win64-setup.exe`)
2. Cliquer sur **"I Agree"** (accepter la licence)
3. Choisir **"Anyone who uses this computer"**
4. Laisser les options par défaut
5. Cliquer sur **"Install"**
6. Cliquer sur **"Finish"**

---

## Étape 2: Configuration de la Connexion FTP 🔧

### 2.1 Ouvrir FileZilla
- Lancer FileZilla depuis le menu Démarrer

### 2.2 Créer une Nouvelle Connexion

1. **Cliquer sur l'icône "Gestionnaire de Sites"** (en haut à gauche)
   - Ou: Fichier → Gestionnaire de sites

2. **Cliquer sur "Nouveau site"**

3. **Remplir les informations:**

```
┌─────────────────────────────────────────────────┐
│ Nom du site: Connect Link Production           │
├─────────────────────────────────────────────────┤
│ Protocole:   FTP - File Transfer Protocol       │
│ Hôte:        conlk.zen-apps.com                 │
│ Port:        21                                 │
│ Chiffrement: Utiliser FTP simple (non sécurisé) │
│ Type:        Normal                             │
│ Utilisateur: conlkaccountftp                    │
│ Mot de passe: 1xbz22B0?                         │
└─────────────────────────────────────────────────┘
```

4. **Cliquer sur "Connexion"**

### 2.3 Première Connexion

Si un message de certificat apparaît:
- ✅ Cocher "Toujours faire confiance à ce certificat"
- Cliquer sur **"OK"**

---

## Étape 3: Interface FileZilla 📊

Une fois connecté, vous verrez 4 zones:

```
┌──────────────────────────────────────────────────────────┐
│  [Messages de connexion]                                 │
├────────────────────────┬─────────────────────────────────┤
│  ORDINATEUR LOCAL      │  SERVEUR DISTANT                │
│  (Votre PC)            │  (conlk.zen-apps.com)           │
├────────────────────────┼─────────────────────────────────┤
│  C:\Users\HP\Desktop\  │  /conlk.zen-apps.com/           │
│  connect link\         │                                 │
│                        │                                 │
│  📁 app/               │  📁 (vide pour l'instant)       │
│  📁 frontend/          │                                 │
│  📄 wsgi.py            │                                 │
│  📄 .htaccess          │                                 │
└────────────────────────┴─────────────────────────────────┘
```

---

## Étape 4: Upload des Fichiers 📤

### 4.1 Naviguer vers le Bon Dossier

**Sur votre PC (gauche):**
1. Naviguer vers: `C:\Users\HP\Desktop\connect link`

**Sur le serveur (droite):**
1. Vous devriez voir: `/conlk.zen-apps.com/`
2. Si vous voyez un autre dossier, double-cliquer pour entrer dans `/conlk.zen-apps.com/`

### 4.2 Upload du Backend (Flask)

**Fichiers à uploader:**

1. **Dossier `app/`**
   - Glisser-déposer le dossier `app/` de gauche vers droite
   - ⏱️ Temps estimé: 1-2 minutes

2. **Dossier `migrations/`** (si existe)
   - Glisser-déposer `migrations/` de gauche vers droite

3. **Fichier `wsgi.py`**
   - Glisser-déposer `wsgi.py` de gauche vers droite

4. **Fichier `.htaccess`**
   - Glisser-déposer `.htaccess` de gauche vers droite

5. **Fichier `requirements.production.txt`**
   - Glisser-déposer vers droite
   - ⚠️ Sur le serveur, le renommer en `requirements.txt`

6. **Fichier `init_database.py`**
   - Glisser-déposer vers droite

### 4.3 Upload du Frontend (React)

**Important:** Le frontend doit aller dans `public_html/` ou `www/`

1. **Créer le dossier sur le serveur:**
   - Clic droit dans la zone serveur (droite)
   - Choisir "Créer un répertoire"
   - Nommer: `public_html` (ou `www` selon votre hébergeur)

2. **Entrer dans le dossier:**
   - Double-cliquer sur `public_html/`

3. **Sur votre PC (gauche):**
   - Naviguer vers: `frontend/dist/`

4. **Uploader TOUT le contenu:**
   - Sélectionner TOUS les fichiers dans `dist/`
   - Glisser-déposer vers `public_html/`
   - ⏱️ Temps estimé: 2-3 minutes

**Vérification:**
Le serveur doit avoir cette structure:
```
/conlk.zen-apps.com/
├── app/
├── migrations/
├── public_html/
│   ├── index.html
│   └── assets/
├── wsgi.py
├── .htaccess
├── requirements.txt
└── init_database.py
```

---

## Étape 5: Créer le Fichier .env 📝

**Le fichier .env ne peut PAS être uploadé, il doit être créé sur le serveur.**

### Option A: Via FileZilla (Recommandé)

1. **Clic droit dans la zone serveur**
2. Choisir **"Créer un nouveau fichier"**
3. Nommer: `.env`
4. Clic droit sur `.env` → **"Voir/Éditer"**
5. Copier-coller le contenu ci-dessous:

```env
FLASK_ENV=production
FLASK_DEBUG=False

SECRET_KEY=0cc77ae1bbdda1c1a89d087550cd5bedc6abe27bf022051ae2d9095a17c8b3ee
JWT_SECRET_KEY=3e37307a56af10b69cd3a26a396b1bae4e62151a94480002c1aea3e82b21bbfb

DATABASE_URL=mysql+pymysql://conlkdbuser:l0X&Vo$6pok0Wqii@localhost:3306/conlkdb

DEFAULT_DOMAIN=https://conlk.zen-apps.com
FRONTEND_URL=https://conlk.zen-apps.com
```

6. **Sauvegarder** (Ctrl+S)
7. **Fermer** l'éditeur
8. FileZilla va demander si vous voulez uploader les changements → **Oui**

### Option B: Via cPanel

1. Se connecter au cPanel de votre hébergeur
2. Aller dans **"Gestionnaire de fichiers"**
3. Naviguer vers `/conlk.zen-apps.com/`
4. Cliquer sur **"+ Fichier"**
5. Nommer: `.env`
6. Éditer et coller le contenu ci-dessus

---

## Étape 6: Vérification 🔍

### Checklist Upload Complet

Sur le serveur, vous devez avoir:

```
✅ /conlk.zen-apps.com/app/
✅ /conlk.zen-apps.com/migrations/
✅ /conlk.zen-apps.com/public_html/index.html
✅ /conlk.zen-apps.com/public_html/assets/
✅ /conlk.zen-apps.com/wsgi.py
✅ /conlk.zen-apps.com/.htaccess
✅ /conlk.zen-apps.com/.env
✅ /conlk.zen-apps.com/requirements.txt
✅ /conlk.zen-apps.com/init_database.py
```

### Vérifier les Tailles

- `app/` → Plusieurs fichiers Python
- `public_html/assets/` → ~900 KB
- `wsgi.py` → ~1 KB
- `.env` → ~300 bytes

---

## Étape 7: Permissions des Fichiers 🔐

### Via FileZilla

1. **Clic droit sur un fichier/dossier**
2. Choisir **"Permissions du fichier..."**
3. Définir les permissions:

```
Dossiers (app/, migrations/, public_html/):
  ✅ Lecture, Écriture, Exécution pour le propriétaire
  ✅ Lecture, Exécution pour le groupe
  ✅ Lecture, Exécution pour les autres
  → Valeur numérique: 755

Fichiers Python (.py):
  ✅ Lecture, Écriture, Exécution pour le propriétaire
  ✅ Lecture, Exécution pour le groupe
  ✅ Lecture, Exécution pour les autres
  → Valeur numérique: 755

Fichiers de config (.env, .htaccess):
  ✅ Lecture, Écriture pour le propriétaire
  ✅ Lecture pour le groupe
  ✅ Lecture pour les autres
  → Valeur numérique: 644
```

---

## 🎉 Upload Terminé!

### Prochaines Étapes

1. **Installer les dépendances Python** (via SSH ou cPanel)
2. **Initialiser la base de données**
3. **Tester l'application**

Voir le fichier **`READY_TO_DEPLOY.md`** pour les étapes suivantes!

---

## 🐛 Problèmes Courants

### Connexion FTP échoue
```
Problème: "Connexion refusée" ou "Timeout"
Solution: 
  - Vérifier le nom d'hôte (conlk.zen-apps.com)
  - Vérifier le port (21)
  - Vérifier le nom d'utilisateur et mot de passe
  - Désactiver temporairement le pare-feu
```

### Upload très lent
```
Problème: Transfer très lent
Solution:
  - Vérifier votre connexion Internet
  - Essayer en mode passif: 
    Édition → Paramètres → Connexion → FTP → Mode passif
```

### Fichier .env invisible
```
Problème: Le fichier .env n'apparaît pas
Solution:
  - Afficher les fichiers cachés dans FileZilla:
    Serveur → Forcer l'affichage des fichiers cachés
```

### Permission refusée
```
Problème: "Permission denied" lors de l'upload
Solution:
  - Vérifier que vous êtes dans le bon dossier
  - Contacter le support de l'hébergeur
```

---

## 💡 Astuces FileZilla

### Sauvegarder la Session
- Les paramètres de connexion sont sauvegardés automatiquement
- Pour reconnecter: Gestionnaire de sites → Connect Link Production → Connexion

### Transfer Rapide
- Glisser-déposer multiple fichiers en même temps
- FileZilla gère automatiquement la file d'attente

### Synchronisation
- Pour mettre à jour uniquement les fichiers modifiés:
  Navigation → Parcourir de manière synchronisée

---

**✅ Vous êtes maintenant prêt à uploader votre application!**
