# 🚀 Complete FileZilla Upload Guide - Connect Link
## Upload Backend + Frontend - Step by Step

---

## 🔐 STEP 1: Connect to FileZilla

### Connection Details:
```
Host:        conlk.zen-apps.com
Username:    conlkaccountftp
Password:    1xbz22B0?
Port:        21
Protocol:    FTP - File Transfer Protocol
```

### How to Connect:
1. Open **FileZilla**
2. Click **"Site Manager"** (top left icon) OR press `Ctrl+S`
3. Click **"New Site"**
4. Enter the connection details above
5. Click **"Connect"**
6. If certificate warning appears → Check "Always trust" → Click **OK**

✅ **You're connected when you see files on the right side!**

---

## 📂 STEP 2: Understand the FileZilla Interface

```
┌─────────────────────────────────────────────────────────────┐
│  [Connection Messages - Top]                                │
├──────────────────────────┬──────────────────────────────────┤
│  LOCAL (Your Computer)   │  REMOTE (Server)                 │
│  LEFT SIDE               │  RIGHT SIDE                      │
├──────────────────────────┼──────────────────────────────────┤
│  C:\Users\HP\Desktop\    │  /conlk.zen-apps.com/            │
│  connect link\           │  (Your server root)              │
│                          │                                  │
│  📁 backend/             │  📁 (empty - we'll fill it)      │
│  📁 frontend/            │                                  │
│  📁 docs/                │                                  │
└──────────────────────────┴──────────────────────────────────┘
```

---

## 🎯 STEP 3: Upload Backend Files

### 3.1 Navigate to Backend Folder (Local - Left Side)

1. On **LEFT side**, navigate to:
   ```
   C:\Users\HP\Desktop\connect link\backend\
   ```

2. On **RIGHT side**, make sure you're in:
   ```
   /conlk.zen-apps.com/
   ```
   (This is your server root directory)

### 3.2 Upload Backend Folders

**Drag these folders from LEFT to RIGHT:**

#### ✅ Upload `app/` folder
- **What**: Main Flask application
- **How**: Drag `app/` folder from left to right
- **Time**: ~2-3 minutes
- **Contains**: All your Python code (models, routes, etc.)

#### ✅ Upload `instance/` folder (Optional)
- **What**: Local database (SQLite)
- **Note**: Skip this if using MariaDB on server
- **How**: Drag `instance/` folder from left to right

### 3.3 Upload Backend Files

**Drag these individual files from LEFT to RIGHT:**

#### ✅ `wsgi.py`
- **What**: Production entry point for Flask
- **How**: Drag `wsgi.py` from left to right
- **Important**: This file starts your backend

#### ✅ `.htaccess`
- **What**: Apache web server configuration
- **How**: Drag `.htaccess` from left to right
- **Critical**: Routes API requests properly

#### ✅ `requirements.production.txt`
- **What**: Python dependencies list
- **How**: Drag `requirements.production.txt` from left to right
- **IMPORTANT**: After upload, rename it to `requirements.txt`
  - Right-click on server → Rename → `requirements.txt`

#### ✅ `init_database.py`
- **What**: Database initialization script
- **How**: Drag `init_database.py` from left to right

#### ✅ `setup_server.sh` (Optional)
- **What**: Server setup helper script
- **How**: Drag `setup_server.sh` from left to right

### 3.4 Create `.env` File on Server

**IMPORTANT: You CANNOT upload .env file - must create on server!**

1. **Right-click** in the server panel (RIGHT side)
2. Choose **"Create new file"**
3. Name it: `.env` (with the dot!)
4. **Right-click** on `.env` → **"View/Edit"**
5. **Paste this content:**

```env
FLASK_ENV=production
FLASK_DEBUG=False

SECRET_KEY=0cc77ae1bbdda1c1a89d087550cd5bedc6abe27bf022051ae2d9095a17c8b3ee
JWT_SECRET_KEY=3e37307a56af10b69cd3a26a396b1bae4e62151a94480002c1aea3e82b21bbfb

DATABASE_URL=mysql+pymysql://conlkdbuser:l0X&Vo$6pok0Wqii@localhost:3306/conlkdb

DEFAULT_DOMAIN=https://conlk.zen-apps.com
FRONTEND_URL=https://conlk.zen-apps.com
```

6. **Save** (Ctrl+S)
7. **Close** the editor
8. Click **"Yes"** when FileZilla asks to upload changes

---

## 🎨 STEP 4: Upload Frontend Files

### 4.1 Create `public_html` Folder on Server

1. On **RIGHT side** (server), **right-click** in empty space
2. Choose **"Create directory"**
3. Name it: `public_html`
4. **Double-click** to enter the `public_html/` folder

### 4.2 Navigate to Frontend Build (Local - Left Side)

1. On **LEFT side**, navigate to:
   ```
   C:\Users\HP\Desktop\connect link\frontend\dist\
   ```

2. You should see:
   - `index.html`
   - `assets/` folder
   - `favicon.svg`
   - `logo-no-bg.svg`
   - `logo.svg`
   - `background.jpg`

### 4.3 Upload ALL Frontend Files

**Select ALL files in `dist/` folder:**

1. Click on first file
2. Press `Ctrl+A` to select all
3. **Drag ALL files** from LEFT to RIGHT into `public_html/`
4. **Time**: ~2-3 minutes
5. **Important**: Upload EVERYTHING from `dist/` folder

**Files being uploaded:**
- ✅ `index.html` (main HTML file)
- ✅ `assets/` folder (JavaScript & CSS)
- ✅ All logo files (.svg)
- ✅ Background images

---

## 🔍 STEP 5: Verify Upload - Check Server Structure

### 5.1 Navigate Back to Root

On **RIGHT side** (server), click the up arrow `↑` to go back to `/conlk.zen-apps.com/`

### 5.2 Your Server Should Look Like This:

```
/conlk.zen-apps.com/
│
├── 📁 app/                      ✅ Backend application
│   ├── __init__.py
│   ├── models/
│   ├── routes/
│   ├── core/
│   └── ...
│
├── 📁 public_html/              ✅ Frontend application
│   ├── index.html
│   ├── assets/
│   │   ├── index-[hash].js
│   │   └── index-[hash].css
│   ├── favicon.svg
│   └── logo files...
│
├── 📄 wsgi.py                   ✅ Backend entry point
├── 📄 .htaccess                 ✅ Apache config
├── 📄 .env                      ✅ Environment variables
├── 📄 requirements.txt          ✅ Python dependencies
└── 📄 init_database.py          ✅ Database script
```

### 5.3 Verification Checklist

- [ ] `app/` folder exists with Python files
- [ ] `public_html/` folder exists with `index.html`
- [ ] `public_html/assets/` folder exists
- [ ] `wsgi.py` file exists
- [ ] `.htaccess` file exists
- [ ] `.env` file exists
- [ ] `requirements.txt` file exists (renamed from requirements.production.txt)

---

## 🔐 STEP 6: Set File Permissions

### 6.1 Set Folder Permissions (755)

**Right-click on each folder → "File permissions":**

- `app/` → Set to **755**
- `public_html/` → Set to **755**

**What 755 means:**
- Owner: Read, Write, Execute
- Group: Read, Execute
- Others: Read, Execute

### 6.2 Set File Permissions

**Python files (755):**
- Right-click `wsgi.py` → Permissions → **755**
- Right-click `init_database.py` → Permissions → **755**

**Config files (644):**
- Right-click `.env` → Permissions → **644**
- Right-click `.htaccess` → Permissions → **644**

**What 644 means:**
- Owner: Read, Write
- Group: Read
- Others: Read

---

## 🚀 STEP 7: Server Setup (SSH or cPanel Terminal)

### 7.1 Connect to Server Terminal

**Option A: SSH**
```bash
ssh conlkaccountftp@conlk.zen-apps.com
```

**Option B: cPanel**
- Login to cPanel
- Find "Terminal" or "SSH Access"
- Open terminal

### 7.2 Navigate to Project Directory

```bash
cd /home/conlkaccountftp/conlk.zen-apps.com
# OR
cd /conlk.zen-apps.com
```

### 7.3 Install Python Dependencies

```bash
pip install -r requirements.txt
```

**Expected output:**
```
Collecting Flask==3.1.2
Collecting SQLAlchemy==2.0.44
...
Successfully installed Flask-3.1.2 ...
```

**Time**: ~3-5 minutes

### 7.4 Initialize Database

```bash
python init_database.py
```

**Expected output:**
```
Database initialized successfully!
Tables created.
```

### 7.5 Test Backend

```bash
python wsgi.py
```

**Expected output:**
```
* Running on http://0.0.0.0:5000
```

Press `Ctrl+C` to stop (we'll use Apache/Passenger to run it properly)

---

## 🌐 STEP 8: Configure Web Server

### 8.1 Restart Web Server

**Via cPanel:**
1. Go to cPanel
2. Find "Restart Services" or "Passenger"
3. Click "Restart"

**Via SSH:**
```bash
touch tmp/restart.txt
```

### 8.2 Configure Python Application (cPanel)

If your host uses **Passenger** (common for Python apps):

1. Go to cPanel → **"Setup Python App"**
2. Click **"Create Application"**
3. Fill in:
   - **Python version**: 3.9 or higher
   - **Application root**: `/home/conlkaccountftp/conlk.zen-apps.com`
   - **Application URL**: Leave empty (for root domain)
   - **Application startup file**: `wsgi.py`
   - **Application Entry point**: `app`
4. Click **"Create"**

---

## ✅ STEP 9: Test Your Application

### 9.1 Test Backend API

Open browser and visit:
```
https://conlk.zen-apps.com/api
```

**Expected**: JSON response with API information

### 9.2 Test Frontend

Open browser and visit:
```
https://conlk.zen-apps.com
```

**Expected**: Your Connect Link login page appears

### 9.3 Test Registration

1. Click "Register"
2. Create a test account
3. Try logging in

---

## 📊 Upload Summary

### Total Upload Time: ~15-20 minutes

- **Backend upload**: 5-10 minutes
- **Frontend upload**: 2-3 minutes
- **Configuration**: 5 minutes
- **Server setup**: 5-10 minutes

### Total Files Uploaded:

- **Backend**: ~60-70 files (app folder + config files)
- **Frontend**: ~10-15 files (HTML, JS, CSS, images)
- **Total size**: ~2-3 MB

---

## 🐛 Troubleshooting

### Problem: Cannot see .htaccess or .env files

**Solution:**
- In FileZilla: Server → Force showing hidden files
- Check "Show hidden files" in settings

### Problem: Upload very slow

**Solution:**
- Check internet connection
- Try passive mode: Edit → Settings → Connection → FTP → Passive mode

### Problem: Permission denied

**Solution:**
- Verify you're in correct directory
- Contact hosting support

### Problem: 500 Internal Server Error

**Solution:**
1. Check `.env` file exists and has correct content
2. Check file permissions (755 for folders, 644 for .env)
3. Check server error logs in cPanel

### Problem: Frontend shows but API doesn't work

**Solution:**
1. Check `.htaccess` file is uploaded
2. Verify `wsgi.py` has correct permissions (755)
3. Check Python dependencies are installed

---

## 📞 Support

**Hosting**: zen-apps.com  
**Domain**: conlk.zen-apps.com  
**FTP User**: conlkaccountftp  
**Database**: conlkdb (MariaDB)

---

## 🎉 Congratulations!

Your Connect Link application is now deployed!

**Frontend**: https://conlk.zen-apps.com  
**Backend API**: https://conlk.zen-apps.com/api  
**Database**: MariaDB (conlkdb)

---

**Last Updated**: December 10, 2025  
**Version**: 1.0 - Complete Deployment
