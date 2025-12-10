# 📤 FileZilla Deployment Checklist - Connect Link

## 🔐 FTP Connection Details

```
Host:        conlk.zen-apps.com
Username:    conlkaccountftp
Password:    1xbz22B0?
Port:        21
Protocol:    FTP (standard)
Root Dir:    /conlk.zen-apps.com
```

---

## ✅ Pre-Deployment Checklist

### 1. Frontend Built ✅
- [x] Frontend production build completed
- [x] Files located in: `frontend/dist/`
- [x] Build size: ~871 KB (JavaScript) + ~38 KB (CSS)

### 2. Backend Files Ready
- [x] Backend files in: `backend/` folder
- [x] Configuration files prepared
- [x] Database scripts ready

---

## 📁 Files to Upload via FileZilla

### Backend Files (from `backend/` folder)

Upload these to: `/conlk.zen-apps.com/`

```
✅ app/                          (entire folder - Flask application)
✅ instance/                     (database folder - optional for production)
✅ wsgi.py                       (production entry point)
✅ .htaccess                     (Apache configuration)
✅ requirements.production.txt   (rename to requirements.txt on server)
✅ init_database.py              (database initialization script)
✅ setup_server.sh               (server setup script)
```

**DO NOT UPLOAD:**
- ❌ venv/ (virtual environment)
- ❌ __pycache__/ (Python cache)
- ❌ *.pyc files
- ❌ .env.server (local config)

### Frontend Files (from `frontend/dist/` folder)

Upload these to: `/conlk.zen-apps.com/public_html/`

```
✅ index.html                    (main HTML file)
✅ assets/                       (entire folder - JS, CSS, images)
✅ favicon.svg
✅ logo-no-bg.svg
✅ logo.svg
✅ logo-white.svg
✅ background.jpg
```

---

## 🔧 FileZilla Upload Steps

### Step 1: Connect to Server

1. Open FileZilla
2. Click "Site Manager" (top left icon)
3. Click "New Site"
4. Enter connection details (see above)
5. Click "Connect"

### Step 2: Navigate to Correct Folders

**Local (Left Side):**
- Navigate to: `C:\Users\HP\Desktop\connect link\backend`

**Remote (Right Side):**
- You should see: `/conlk.zen-apps.com/`

### Step 3: Upload Backend Files

1. **Upload `app/` folder:**
   - Drag `app/` from left to right
   - Wait for upload to complete (~2-3 minutes)

2. **Upload `wsgi.py`:**
   - Drag `wsgi.py` from left to right

3. **Upload `.htaccess`:**
   - Drag `.htaccess` from left to right

4. **Upload `requirements.production.txt`:**
   - Drag to server
   - **IMPORTANT:** Rename on server to `requirements.txt`

5. **Upload `init_database.py`:**
   - Drag from left to right

6. **Upload `setup_server.sh`:**
   - Drag from left to right

### Step 4: Create .env File on Server

**IMPORTANT:** Cannot upload .env, must create on server!

1. Right-click in server panel (right side)
2. Choose "Create new file"
3. Name it: `.env`
4. Right-click on `.env` → "View/Edit"
5. Paste this content:

```env
FLASK_ENV=production
FLASK_DEBUG=False

SECRET_KEY=0cc77ae1bbdda1c1a89d087550cd5bedc6abe27bf022051ae2d9095a17c8b3ee
JWT_SECRET_KEY=3e37307a56af10b69cd3a26a396b1bae4e62151a94480002c1aea3e82b21bbfb

DATABASE_URL=mysql+pymysql://conlkdbuser:l0X&Vo$6pok0Wqii@localhost:3306/conlkdb

DEFAULT_DOMAIN=https://conlk.zen-apps.com
FRONTEND_URL=https://conlk.zen-apps.com
```

6. Save (Ctrl+S) and close
7. Click "Yes" when asked to upload changes

### Step 5: Upload Frontend Files

1. **On Local (Left):**
   - Navigate to: `C:\Users\HP\Desktop\connect link\frontend\dist\`

2. **On Server (Right):**
   - Create folder: `public_html` (if doesn't exist)
   - Double-click to enter `public_html/`

3. **Upload ALL files from dist/:**
   - Select ALL files in `dist/` folder
   - Drag from left to right
   - Wait for upload (~2-3 minutes)

---

## 🎯 Final Server Structure

After upload, your server should look like this:

```
/conlk.zen-apps.com/
│
├── app/                         # Flask application
│   ├── __init__.py
│   ├── config.py
│   ├── models/
│   ├── routes/
│   ├── core/
│   └── ...
│
├── public_html/                 # Frontend (React build)
│   ├── index.html
│   ├── assets/
│   │   ├── index-C_q2G9SE.js
│   │   └── index-C_put5pW.css
│   ├── favicon.svg
│   └── logo files...
│
├── wsgi.py                      # Production entry point
├── .htaccess                    # Apache config
├── .env                         # Environment variables
├── requirements.txt             # Python dependencies
├── init_database.py             # DB initialization
└── setup_server.sh              # Setup script
```

---

## 🔐 Set File Permissions

### Via FileZilla:

**Folders (755):**
- Right-click on `app/` → Permissions → 755
- Right-click on `public_html/` → Permissions → 755

**Python Files (755):**
- Right-click on `wsgi.py` → Permissions → 755
- Right-click on `init_database.py` → Permissions → 755

**Config Files (644):**
- Right-click on `.env` → Permissions → 644
- Right-click on `.htaccess` → Permissions → 644

---

## 📊 Upload Progress Tracking

### Backend Upload (~5-10 minutes)
- [ ] app/ folder uploaded
- [ ] wsgi.py uploaded
- [ ] .htaccess uploaded
- [ ] requirements.txt uploaded (renamed)
- [ ] init_database.py uploaded
- [ ] .env created on server

### Frontend Upload (~2-3 minutes)
- [ ] public_html/ folder created
- [ ] index.html uploaded
- [ ] assets/ folder uploaded
- [ ] Logo files uploaded
- [ ] Background image uploaded

### Verification
- [ ] All files visible on server
- [ ] File sizes match local files
- [ ] Permissions set correctly
- [ ] .env file exists and has correct content

---

## 🚀 After Upload - Next Steps

1. **SSH into server** (or use cPanel terminal)

2. **Install Python dependencies:**
   ```bash
   cd /conlk.zen-apps.com
   pip install -r requirements.txt
   ```

3. **Initialize database:**
   ```bash
   python init_database.py
   ```

4. **Restart web server:**
   ```bash
   # Via cPanel or SSH
   touch tmp/restart.txt
   ```

5. **Test the application:**
   - Visit: https://conlk.zen-apps.com
   - Try logging in
   - Create a test link

---

## 🐛 Troubleshooting

### Upload Fails
- Check FTP credentials
- Verify internet connection
- Try passive mode: Edit → Settings → Connection → FTP → Passive mode

### Files Not Visible
- Show hidden files: Server → Force showing hidden files
- Refresh server view: F5

### Permission Denied
- Contact hosting support
- Verify you're in correct directory

### .env Not Working
- Verify file name is exactly `.env` (with dot)
- Check file content has no extra spaces
- Verify file is in root directory `/conlk.zen-apps.com/`

---

## 📞 Support Information

**Hosting:** zen-apps.com  
**Domain:** conlk.zen-apps.com  
**FTP User:** conlkaccountftp  

**Database:**
- Type: MariaDB
- Name: conlkdb
- User: conlkdbuser

---

## ✅ Deployment Complete!

Once all files are uploaded and configured:

1. ✅ Backend API accessible at: `https://conlk.zen-apps.com/api`
2. ✅ Frontend accessible at: `https://conlk.zen-apps.com`
3. ✅ Database connected and initialized
4. ✅ Application ready for use!

---

**Last Updated:** December 10, 2025  
**Build Version:** Production v1.0  
**Frontend Build:** 871 KB (JS) + 38 KB (CSS)
