# 🚀 Deploy Connect Link via Git Bash

## 📋 Deployment Using Git Bash + SSH/FTP

---

## Method 1: Using SCP (Secure Copy) - RECOMMENDED

### Step 1: Upload Backend Files

Open Git Bash and run:

```bash
# Navigate to your project
cd "/c/Users/HP/Desktop/connect link"

# Upload entire backend folder to server
scp -r backend/* conlkaccountftp@conlk.zen-apps.com:/conlk.zen-apps.com/

# Or upload specific files/folders:
scp -r backend/app conlkaccountftp@conlk.zen-apps.com:/conlk.zen-apps.com/
scp backend/wsgi.py conlkaccountftp@conlk.zen-apps.com:/conlk.zen-apps.com/
scp backend/.htaccess conlkaccountftp@conlk.zen-apps.com:/conlk.zen-apps.com/
scp backend/.env.production conlkaccountftp@conlk.zen-apps.com:/conlk.zen-apps.com/.env
scp backend/requirements.production.txt conlkaccountftp@conlk.zen-apps.com:/conlk.zen-apps.com/requirements.txt
scp backend/init_database.py conlkaccountftp@conlk.zen-apps.com:/conlk.zen-apps.com/
```

**Password when prompted:** `1xbz22B0?`

---

### Step 2: Upload Frontend Files

```bash
# Upload frontend build
scp -r frontend/dist/* conlkaccountftp@conlk.zen-apps.com:/conlk.zen-apps.com/
```

---

### Step 3: SSH into Server and Configure

```bash
# Connect to server
ssh conlkaccountftp@conlk.zen-apps.com

# Once connected, run these commands:
cd /conlk.zen-apps.com

# Install Python dependencies
python3 -m pip install -r requirements.txt --user

# Initialize database
python3 init_database.py

# Set correct permissions
chmod 755 wsgi.py
chmod 644 .htaccess
chmod 600 .env

# Exit SSH
exit
```

---

## Method 2: Using SFTP via Git Bash

```bash
# Connect via SFTP
sftp conlkaccountftp@conlk.zen-apps.com

# Once connected, navigate to directory
cd /conlk.zen-apps.com

# Upload backend
put -r backend/app
put backend/wsgi.py
put backend/.htaccess
put backend/.env.production .env
put backend/requirements.production.txt requirements.txt
put backend/init_database.py

# Upload frontend
put -r frontend/dist/*

# Exit SFTP
exit
```

---

## Method 3: Using rsync (Most Efficient)

```bash
# Upload backend (excludes unnecessary files)
rsync -avz --exclude='venv' --exclude='__pycache__' --exclude='*.pyc' \
  backend/ conlkaccountftp@conlk.zen-apps.com:/conlk.zen-apps.com/

# Upload frontend
rsync -avz frontend/dist/ conlkaccountftp@conlk.zen-apps.com:/conlk.zen-apps.com/
```

---

## 🔧 Complete Deployment Script

Save this as `deploy.sh` in your project root:

```bash
#!/bin/bash

echo "🚀 Deploying Connect Link to conlk.zen-apps.com..."

SERVER="conlkaccountftp@conlk.zen-apps.com"
REMOTE_PATH="/conlk.zen-apps.com"

# Upload backend
echo "📤 Uploading backend files..."
scp -r backend/app "$SERVER:$REMOTE_PATH/"
scp backend/wsgi.py "$SERVER:$REMOTE_PATH/"
scp backend/.htaccess "$SERVER:$REMOTE_PATH/"
scp backend/.env.production "$SERVER:$REMOTE_PATH/.env"
scp backend/requirements.production.txt "$SERVER:$REMOTE_PATH/requirements.txt"
scp backend/init_database.py "$SERVER:$REMOTE_PATH/"

# Upload frontend
echo "📤 Uploading frontend files..."
scp -r frontend/dist/* "$SERVER:$REMOTE_PATH/"

# Configure server
echo "⚙️  Configuring server..."
ssh "$SERVER" << 'EOF'
cd /conlk.zen-apps.com
python3 -m pip install -r requirements.txt --user
python3 init_database.py
chmod 755 wsgi.py
chmod 644 .htaccess
chmod 600 .env
EOF

echo "✅ Deployment complete!"
echo "🌐 Visit: https://conlk.zen-apps.com"
```

Then run:
```bash
chmod +x deploy.sh
./deploy.sh
```

---

## 🎯 Quick One-Liner Deployment

```bash
cd "/c/Users/HP/Desktop/connect link" && \
scp -r backend/app backend/wsgi.py backend/.htaccess backend/init_database.py conlkaccountftp@conlk.zen-apps.com:/conlk.zen-apps.com/ && \
scp backend/.env.production conlkaccountftp@conlk.zen-apps.com:/conlk.zen-apps.com/.env && \
scp backend/requirements.production.txt conlkaccountftp@conlk.zen-apps.com:/conlk.zen-apps.com/requirements.txt && \
scp -r frontend/dist/* conlkaccountftp@conlk.zen-apps.com:/conlk.zen-apps.com/ && \
ssh conlkaccountftp@conlk.zen-apps.com "cd /conlk.zen-apps.com && python3 -m pip install -r requirements.txt --user && python3 init_database.py"
```

---

## 📝 Important Notes

### Files to Upload:

**Backend:**
- ✅ `app/` folder
- ✅ `wsgi.py`
- ✅ `.htaccess`
- ✅ `.env.production` → rename to `.env`
- ✅ `requirements.production.txt` → rename to `requirements.txt`
- ✅ `init_database.py`

**Frontend:**
- ✅ Everything from `frontend/dist/` folder

### Files to EXCLUDE:
- ❌ `venv/`
- ❌ `__pycache__/`
- ❌ `*.pyc`
- ❌ `node_modules/`
- ❌ `.git/`

---

## 🔍 Verify Upload

After uploading, check files are on server:

```bash
ssh conlkaccountftp@conlk.zen-apps.com "ls -la /conlk.zen-apps.com"
```

Should see:
```
app/
assets/
wsgi.py
.htaccess
.env
requirements.txt
init_database.py
index.html
```

---

## 🆘 Troubleshooting

### "Permission denied" error
```bash
# Add your SSH key (if you have one)
ssh-copy-id conlkaccountftp@conlk.zen-apps.com
```

### "Connection refused"
```bash
# Try with explicit port
scp -P 22 -r backend/app conlkaccountftp@conlk.zen-apps.com:/conlk.zen-apps.com/
```

### "No such file or directory"
```bash
# Create directory first
ssh conlkaccountftp@conlk.zen-apps.com "mkdir -p /conlk.zen-apps.com"
```

---

## ✅ After Deployment

Visit: **https://conlk.zen-apps.com**

You should see your Connect Link application running!

---

**Password:** `1xbz22B0?` (when prompted)
