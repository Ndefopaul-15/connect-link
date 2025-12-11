# 🚀 SIMPLE DEPLOYMENT INSTRUCTIONS

## The Problem
You're trying to access https://conlk.zen-apps.com but getting 127.0.0.1 error because:
**THE FILES ARE NOT ON THE SERVER YET!**

The production build is ready on your computer, but you need to UPLOAD it.

---

## ✅ WHAT'S READY (On Your Computer)

1. **Backend Files:** `C:\Users\HP\Desktop\connect link\backend\`
2. **Frontend Build:** `C:\Users\HP\Desktop\connect link\frontend\dist\`
3. **All configurations are correct**
4. **All dependencies installed**

---

## 📤 UPLOAD TO SERVER NOW

### Step 1: Open FileZilla

Download FileZilla if you don't have it: https://filezilla-project.org/

### Step 2: Connect to Your Server

```
Host:     conlk.zen-apps.com
Username: conlkaccountftp
Password: 1xbz22B0?
Port:     21
```

Click "Quickconnect"

### Step 3: Upload Backend

**Left side (Local):** Navigate to `C:\Users\HP\Desktop\connect link\backend\`

**Right side (Server):** Navigate to `/conlk.zen-apps.com/`

**Drag and drop these folders/files from LEFT to RIGHT:**

```
✅ app/                          (entire folder - drag it)
✅ wsgi.py                       (drag it)
✅ .htaccess                     (drag it)
✅ .env.production               (drag it, then RENAME to .env on server)
✅ requirements.production.txt   (drag it, then RENAME to requirements.txt)
✅ init_database.py              (drag it)
```

### Step 4: Upload Frontend

**Left side (Local):** Navigate to `C:\Users\HP\Desktop\connect link\frontend\dist\`

**Right side (Server):** Stay in `/conlk.zen-apps.com/`

**Drag ALL files from dist/ folder:**

```
✅ index.html                    (drag it)
✅ assets/                       (entire folder - drag it)
```

### Step 5: Rename Files on Server

In FileZilla (right side - server):
1. Right-click `.env.production` → Rename to `.env`
2. Right-click `requirements.production.txt` → Rename to `requirements.txt`

### Step 6: Set Up Database (via SSH or cPanel)

**Option A - SSH:**
```bash
ssh conlkaccountftp@conlk.zen-apps.com
cd /conlk.zen-apps.com
python3 -m pip install -r requirements.txt --user
python3 init_database.py
```

**Option B - cPanel:**
1. Login to your hosting cPanel
2. Find "Terminal" or "SSH Access"
3. Run the commands above

### Step 7: Test!

Visit: **https://conlk.zen-apps.com**

You should see the Connect Link homepage!

---

## 🎯 THAT'S IT!

Once files are uploaded:
- ✅ Frontend will load from the server
- ✅ Backend API will work
- ✅ Database will connect
- ✅ Everything will function normally

**The error you're seeing is because the files are still on your local computer, not on the server!**

---

## 📞 Quick Check

Before uploading, verify these files exist on your computer:

```bash
# Check backend files exist
dir "C:\Users\HP\Desktop\connect link\backend\app"
dir "C:\Users\HP\Desktop\connect link\backend\wsgi.py"

# Check frontend build exists
dir "C:\Users\HP\Desktop\connect link\frontend\dist\index.html"
dir "C:\Users\HP\Desktop\connect link\frontend\dist\assets"
```

If all exist → **You're ready to upload!**

---

**REMEMBER:** The production site won't work until you upload the files to the server!
