# 📤 FTP Upload Guide - Git Bash

## Problem: SCP Connection Closed

Your hosting server uses **FTP only** (not SSH/SCP). Here are your options:

---

## ✅ SOLUTION 1: Use FileZilla (EASIEST)

Since Git Bash SCP doesn't work, **FileZilla is the best option**:

### Download FileZilla
https://filezilla-project.org/download.php?type=client

### Connect
```
Host:     conlk.zen-apps.com
Username: conlkaccountftp
Password: 1xbz22B0?
Port:     21
```

### Upload Files

**Left side:** `C:\Users\HP\Desktop\connect link\backend\`  
**Right side:** `/conlk.zen-apps.com/`

Drag and drop:
- `app/` folder
- `wsgi.py`
- `.htaccess`
- `.env.production` (rename to `.env`)
- `requirements.production.txt` (rename to `requirements.txt`)
- `init_database.py`

**Left side:** `C:\Users\HP\Desktop\connect link\frontend\dist\`  
**Right side:** `/conlk.zen-apps.com/`

Drag and drop:
- `index.html`
- `assets/` folder

---

## ✅ SOLUTION 2: Use WinSCP (Windows FTP Client)

Download: https://winscp.net/

Same credentials as FileZilla.

---

## ✅ SOLUTION 3: Use Git Bash with `lftp`

### Install lftp (if not installed)
```bash
# Check if lftp is available
which lftp
```

If not available, download from: https://lftp.yar.ru/

### Use lftp to upload

```bash
cd "/c/Users/HP/Desktop/connect link"

lftp -u conlkaccountftp,1xbz22B0? conlk.zen-apps.com << EOF
cd /conlk.zen-apps.com
mirror -R backend/app app
put backend/wsgi.py
put backend/.htaccess
put backend/.env.production -o .env
put backend/requirements.production.txt -o requirements.txt
put backend/init_database.py
mirror -R frontend/dist .
bye
EOF
```

---

## ✅ SOLUTION 4: Use cPanel File Manager

1. Login to your hosting cPanel
2. Open "File Manager"
3. Navigate to `/conlk.zen-apps.com/`
4. Upload files using the web interface

---

## ✅ SOLUTION 5: Use Windows Built-in FTP

```bash
# Open Git Bash
cd "/c/Users/HP/Desktop/connect link"

# Connect to FTP
ftp conlk.zen-apps.com

# When prompted:
# Name: conlkaccountftp
# Password: 1xbz22B0?

# Then run these commands:
cd /conlk.zen-apps.com
binary
lcd backend
put wsgi.py
put .htaccess
put init_database.py
put .env.production .env
put requirements.production.txt requirements.txt

# For folders, you'll need to upload files individually
# or use FileZilla which is much easier
```

---

## 🎯 RECOMMENDED APPROACH

**Use FileZilla** - It's the easiest and most reliable for FTP uploads.

1. Download and install FileZilla
2. Connect with your credentials
3. Drag and drop files
4. Done in 5 minutes!

---

## 📋 Files to Upload Checklist

### Backend (to `/conlk.zen-apps.com/`)
- [ ] `app/` folder (entire folder with all subfolders)
- [ ] `wsgi.py`
- [ ] `.htaccess`
- [ ] `.env` (from `.env.production`)
- [ ] `requirements.txt` (from `requirements.production.txt`)
- [ ] `init_database.py`

### Frontend (to `/conlk.zen-apps.com/`)
- [ ] `index.html`
- [ ] `assets/` folder

---

## 🔧 After Upload

You'll need to access your hosting control panel to:

1. **Install Python packages** (via cPanel Terminal or SSH if available)
2. **Initialize database** (run `python3 init_database.py`)
3. **Set permissions** (if needed)

Or contact your hosting support to help with Python setup.

---

## ❓ Why SCP Doesn't Work

Your hosting plan likely:
- Only supports FTP (not SSH/SFTP)
- Doesn't have SSH access enabled
- Requires a different port for SSH

**FTP is perfectly fine for deployment!** Just use FileZilla.

---

**Next Step:** Download FileZilla and upload the files! 🚀
