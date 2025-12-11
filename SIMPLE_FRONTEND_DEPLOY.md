# 🚀 Simple Frontend Deployment to conlk.zen-apps.com

## ✅ What You Have
- **Backend**: Already on Render.com (`https://connect-link.onrender.com`) ✅
- **Frontend**: Built and ready to upload

---

## 📤 Upload Frontend via FileZilla

### Step 1: Files to Upload
Location: `C:\Users\HP\Desktop\connect link\frontend\dist\`

Upload these files:
- `index.html`
- `assets/` folder (entire folder)
- `vite.svg`

### Step 2: Where to Upload
Remote location: `/public_html/` (or `/www/` or `/htdocs/`)

### Step 3: Upload .htaccess
Also upload: `C:\Users\HP\Desktop\connect link\frontend\.htaccess`
To: `/public_html/.htaccess`

---

## 🎯 That's It!

Your frontend will be at: `https://conlk.zen-apps.com`

It will automatically connect to your Render backend at: `https://connect-link.onrender.com/api`

---

## ✅ Test After Upload

1. Visit: `https://conlk.zen-apps.com`
2. Register a new account
3. Create a short link
4. Check if data is saved in your Render database

---

## 🐛 If Something Doesn't Work

1. **Check browser console** (F12) for errors
2. **Check Network tab** - verify API calls go to `connect-link.onrender.com`
3. **Clear browser cache**
4. **Verify .htaccess was uploaded**

---

## 📝 Summary

- **Backend**: Render.com (no changes needed)
- **Frontend**: Upload `dist/` folder to cPanel
- **Database**: Already on Render (will store data automatically)

No backend deployment needed on cPanel! 🎉
