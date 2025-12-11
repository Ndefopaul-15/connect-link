# 🚀 DEPLOY FRONTEND TO CONLK.ZEN-APPS.COM - COMPLETE GUIDE

## ✅ BACKEND STATUS
**Backend URL:** `https://connect-link.onrender.com`  
**Status:** ✅ LIVE AND RUNNING  
**API Endpoint:** `https://connect-link.onrender.com/api`

## ✅ FRONTEND BUILD STATUS
**Build Status:** ✅ COMPLETED  
**Build Location:** `C:\Users\HP\Desktop\connect link\frontend\dist\`  
**Configuration:** Using Render backend URL  
**Ready to Deploy:** YES

---

## 📤 STEP-BY-STEP DEPLOYMENT

### STEP 1: Open FileZilla

1. Download FileZilla if you don't have it: https://filezilla-project.org/
2. Open FileZilla

### STEP 2: Connect to Your Server

Enter these details in FileZilla:

```
Host:     conlk.zen-apps.com
Username: conlkaccountftp
Password: 1xbz22B0?
Port:     21
```

Click **"Quickconnect"**

### STEP 3: Navigate to Correct Directories

**LEFT SIDE (Your Computer):**
Navigate to: `C:\Users\HP\Desktop\connect link\frontend\dist\`

You should see:
- `index.html`
- `assets/` folder
- `.htaccess`
- Other files (logo.svg, background.jpg, etc.)

**RIGHT SIDE (Server):**
Navigate to: `/conlk.zen-apps.com/` or `/public_html/`

⚠️ **IMPORTANT:** If there are OLD files from previous uploads, **DELETE THEM ALL FIRST**

### STEP 4: Delete Old Files on Server (CRITICAL!)

On the **RIGHT SIDE (Server)**, delete these if they exist:
- Old `index.html`
- Old `assets/` folder
- Any old JavaScript/CSS files
- **Keep only:** Database files, `.htaccess` (if it's for backend)

### STEP 5: Upload ALL Files from dist/

**Select ALL files from LEFT SIDE:**
- `index.html`
- `assets/` folder (entire folder)
- `.htaccess`
- `background.jpg`
- `favicon.svg`
- `logo.svg`
- `logo-no-bg.svg`
- `vite.svg`

**Drag and drop to RIGHT SIDE**

Wait for upload to complete (should take 1-2 minutes)

### STEP 6: Verify Upload

On the **RIGHT SIDE (Server)**, you should now see:
```
/conlk.zen-apps.com/
├── index.html          ✅
├── assets/
│   ├── index-C_put5pW.css    ✅
│   └── index-Cl1oThLM.js     ✅
├── .htaccess           ✅
├── background.jpg      ✅
├── favicon.svg         ✅
├── logo.svg            ✅
└── logo-no-bg.svg      ✅
```

---

## 🧪 TEST YOUR DEPLOYMENT

### Test 1: Open Your Website

Visit: **https://conlk.zen-apps.com**

**Expected:** You should see the Connect Link login/register page

### Test 2: Open Browser Console

1. Press **F12** to open Developer Tools
2. Go to **Console** tab
3. Look for any errors (should be NONE)

### Test 3: Register a New Account

1. Click "Register"
2. Enter email: `test@example.com`
3. Enter password: `Test123456`
4. Click "Register"

**Expected:** 
- Registration successful
- Redirects to dashboard
- No errors in console

### Test 4: Create a Short Link

1. Click "Create New Link"
2. Enter URL: `https://www.google.com`
3. Click "Create"

**Expected:**
- Link created successfully
- Shows in your dashboard
- No errors

---

## 🔍 TROUBLESHOOTING

### Problem: Website shows blank page

**Solution:**
1. Check if `index.html` is in the root directory
2. Clear browser cache (Ctrl + Shift + Delete)
3. Try incognito/private window

### Problem: "Failed to fetch" or Network Error

**Solution:**
1. Open browser console (F12)
2. Check the error message
3. Verify it's trying to connect to: `https://connect-link.onrender.com/api`
4. If it's trying to connect to a different URL, the build used wrong .env file

**Fix:**
```bash
# In frontend folder
cd C:\Users\HP\Desktop\connect link\frontend
npm run build
# Then re-upload dist/ folder
```

### Problem: CORS Error in Console

**Error message:** "Access to fetch at 'https://connect-link.onrender.com/api/...' from origin 'https://conlk.zen-apps.com' has been blocked by CORS policy"

**Solution:**
Your backend needs to allow `conlk.zen-apps.com`. I've already updated the backend code, but you need to redeploy it to Render:

1. Go to Render dashboard
2. Find your `connect-link` service
3. Click "Manual Deploy" → "Deploy latest commit"
4. Wait for deployment to complete

### Problem: 404 Not Found on page refresh

**Solution:**
Make sure `.htaccess` file is uploaded and contains:
```apache
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ /index.html [L]
```

---

## 📋 QUICK CHECKLIST

Before testing, verify:

- [ ] All old files deleted from server
- [ ] `index.html` uploaded to root directory
- [ ] `assets/` folder uploaded completely
- [ ] `.htaccess` uploaded
- [ ] Backend is running on Render (https://connect-link.onrender.com)
- [ ] Browser cache cleared

---

## 🎯 WHAT HAPPENS AFTER DEPLOYMENT

```
User visits: https://conlk.zen-apps.com
    ↓
PHP Server serves: Frontend files (HTML/CSS/JS)
    ↓
Frontend makes API calls to: https://connect-link.onrender.com/api
    ↓
Backend (Render) processes requests
    ↓
Backend sends response back to Frontend
    ↓
User sees data on screen
```

---

## 📞 NEED HELP?

### Check Backend Status
Visit: https://connect-link.onrender.com

Should show:
```json
{
  "api": {
    "name": "Connect Link API",
    "status": "running",
    "version": "1.0.0"
  }
}
```

### Check Frontend Files
Use FileZilla to verify all files are uploaded correctly

### Check Browser Console
Press F12 and look for error messages

---

## ✅ SUCCESS INDICATORS

Your deployment is successful when:

1. ✅ Website loads at https://conlk.zen-apps.com
2. ✅ No errors in browser console
3. ✅ Can register new account
4. ✅ Can login
5. ✅ Can create short links
6. ✅ Dashboard shows your links
7. ✅ Short links redirect properly

---

## 🔐 IMPORTANT NOTES

1. **Backend Location:** Render (Python/Flask) - `https://connect-link.onrender.com`
2. **Frontend Location:** conlk.zen-apps.com (PHP Server) - Static files only
3. **Database:** On Render (PostgreSQL)
4. **CORS:** Backend allows requests from `conlk.zen-apps.com`

---

## 📝 FILES TO UPLOAD (FROM dist/ FOLDER)

```
✅ index.html                    (Main HTML file)
✅ assets/index-C_put5pW.css    (Styles)
✅ assets/index-Cl1oThLM.js     (JavaScript)
✅ .htaccess                     (URL rewriting)
✅ background.jpg                (Background image)
✅ favicon.svg                   (Favicon)
✅ logo.svg                      (Logo)
✅ logo-no-bg.svg               (Logo without background)
✅ vite.svg                      (Vite logo)
```

**DO NOT UPLOAD:**
- `node_modules/` folder
- `src/` folder
- `.env` files
- `package.json`
- Any development files

---

**Last Updated:** December 11, 2025  
**Build Version:** Latest  
**Backend:** Render (Live)  
**Status:** ✅ READY TO DEPLOY
