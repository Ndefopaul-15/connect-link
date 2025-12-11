# 🚀 Simple Deployment Guide - Step by Step

## 📋 Overview

You have 3 main tasks:
1. Deploy backend to Render
2. Update frontend with Render URL
3. Upload frontend to your PHP server

---

## TASK 1: Deploy Backend to Render

### Step 1.1: Create Render Account
1. Go to: **https://render.com**
2. Click "Get Started"
3. Sign up with GitHub or email

### Step 1.2: Push Backend to GitHub

Open Git Bash and run:

```bash
cd "/c/Users/HP/Desktop/connect link/backend"

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Deploy backend to Render"
```

Now create a GitHub repository:
1. Go to https://github.com
2. Click "+" → "New repository"
3. Name it: `connect-link-backend`
4. Click "Create repository"

Then in Git Bash:

```bash
# Replace YOUR_USERNAME with your GitHub username
git remote add origin https://github.com/YOUR_USERNAME/connect-link-backend.git
git branch -M main
git push -u origin main
```

### Step 1.3: Deploy on Render

1. Go to Render dashboard: https://dashboard.render.com
2. Click **"New +"** → **"Web Service"**
3. Click **"Connect GitHub"**
4. Select your `connect-link-backend` repository
5. Fill in:
   - **Name:** `connect-link-api` (or any name you want)
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn wsgi:app --bind 0.0.0.0:$PORT`
   - **Plan:** Free
6. Click **"Advanced"** and add these environment variables:

```
FLASK_ENV=production
SECRET_KEY=8792d9be31379225d922cd94e8b881efb1f77a3f59cba89e624b9a0f73048965
JWT_SECRET_KEY=85aac9cb3a0a7723ed665120d687e745b628ef579f120e1b2df971c5f0eddec3
DEFAULT_DOMAIN=https://conlk.zen-apps.com
FRONTEND_URL=https://conlk.zen-apps.com
```

7. Click **"Create Web Service"**

### Step 1.4: Add Database

1. In Render dashboard, click **"New +"** → **"PostgreSQL"**
2. Fill in:
   - **Name:** `connect-link-db`
   - **Database:** `conlkdb`
   - **Plan:** Free
3. Click **"Create Database"**
4. After creation, click on the database
5. Copy the **Internal Database URL** (looks like: `postgresql://user:pass@host/db`)
6. Go back to your web service → **Environment** tab
7. Add new environment variable:
   - **Key:** `DATABASE_URL`
   - **Value:** Paste the Internal Database URL
8. Click **"Save Changes"**

### Step 1.5: Get Your Backend URL

After deployment completes (takes 2-5 minutes), you'll see:

```
Your service is live at https://connect-link-api.onrender.com
```

**COPY THIS URL!** You need it for the next task.

Example URLs:
- `https://connect-link-api.onrender.com`
- `https://connect-link-api-xyz.onrender.com`

---

## TASK 2: Update Frontend Configuration

### Step 2.1: Edit .env.production File

Open this file in your editor:
```
C:\Users\HP\Desktop\connect link\frontend\.env.production
```

Change line 4 from:
```
VITE_API_BASE_URL=https://YOUR-RENDER-APP-NAME.onrender.com/api
```

To (using YOUR actual Render URL):
```
VITE_API_BASE_URL=https://connect-link-api.onrender.com/api
```

**Replace `connect-link-api.onrender.com` with YOUR actual Render URL!**

Save the file.

### Step 2.2: Rebuild Frontend

Open Git Bash and run:

```bash
cd "/c/Users/HP/Desktop/connect link/frontend"
npm run build
```

This creates a new `dist/` folder with updated configuration.

---

## TASK 3: Upload Frontend to PHP Server

### Step 3.1: Download FileZilla

If you don't have it: https://filezilla-project.org/download.php?type=client

### Step 3.2: Connect to Your Server

Open FileZilla and enter:
- **Host:** `conlk.zen-apps.com`
- **Username:** `conlkaccountftp`
- **Password:** `1xbz22B0?`
- **Port:** `21`

Click **"Quickconnect"**

### Step 3.3: Upload Files

**Left side (Your Computer):**
Navigate to: `C:\Users\HP\Desktop\connect link\frontend\dist\`

**Right side (Server):**
Navigate to: `/conlk.zen-apps.com/`

**Drag and drop from left to right:**
- `index.html`
- `assets/` folder (entire folder)

Wait for upload to complete.

---

## ✅ DONE! Test Your App

Visit: **https://conlk.zen-apps.com**

You should see your Connect Link app running!

---

## 🔍 What Just Happened?

```
User visits: https://conlk.zen-apps.com
    ↓
PHP Server serves: Frontend (HTML/CSS/JS)
    ↓
Frontend makes API calls to: https://connect-link-api.onrender.com/api
    ↓
Render serves: Backend (Python/Flask)
    ↓
Backend connects to: PostgreSQL Database (on Render)
```

---

## 🆘 Troubleshooting

### "Build failed" on Render
- Check that `requirements.txt` exists in backend folder
- Check Render logs for specific error
- Make sure all environment variables are set

### "Frontend shows error"
- Make sure you updated `.env.production` with correct Render URL
- Make sure you ran `npm run build` after updating
- Check browser console for errors

### "Can't connect to API"
- Verify Render backend is running (green status)
- Check that CORS is configured in backend
- Make sure `.env.production` has `/api` at the end of URL

---

## 📝 Summary

1. ✅ Backend on Render: `https://connect-link-api.onrender.com`
2. ✅ Frontend on PHP Server: `https://conlk.zen-apps.com`
3. ✅ Database on Render: PostgreSQL (free tier)

**Total time:** 20-30 minutes

---

Need help with any step? Let me know! 🚀
