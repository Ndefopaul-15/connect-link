# 🚀 Deploy Backend to Render - Step by Step

## ✅ What You Need

Your setup:
- **Backend (Python)** → Deploy to Render.com
- **Frontend (Static)** → Upload to PHP server (conlk.zen-apps.com) via FileZilla
- **Database** → Use Render's PostgreSQL (free)

---

## STEP 1: Create Render Account

1. Go to: **https://render.com**
2. Click **"Get Started"**
3. Sign up with GitHub (recommended) or email

---

## STEP 2: Push Backend to GitHub

### Open Git Bash:

```bash
cd "/c/Users/HP/Desktop/connect link/backend"

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial backend for Render deployment"

# Create a new repo on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/connect-link-backend.git
git branch -M main
git push -u origin main
```

**Replace `YOUR_USERNAME` with your GitHub username**

---

## STEP 3: Deploy to Render

### In Render Dashboard:

1. Click **"New +"** → **"Web Service"**
2. Click **"Connect GitHub"** (or **"Public Git Repository"**)
3. Select your `connect-link-backend` repository
4. Configure:

```
Name:           connect-link-api
Environment:    Python 3
Region:         Oregon (US West)
Branch:         main
Build Command:  pip install -r requirements.txt
Start Command:  gunicorn wsgi:app --bind 0.0.0.0:$PORT
Instance Type:  Free
```

5. Click **"Create Web Service"**

---

## STEP 4: Add Environment Variables

In Render dashboard, go to **Environment** tab and add:

```
FLASK_ENV=production
SECRET_KEY=8792d9be31379225d922cd94e8b881efb1f77a3f59cba89e624b9a0f73048965
JWT_SECRET_KEY=85aac9cb3a0a7723ed665120d687e745b628ef579f120e1b2df971c5f0eddec3
DEFAULT_DOMAIN=https://conlk.zen-apps.com
FRONTEND_URL=https://conlk.zen-apps.com
```

---

## STEP 5: Add Database (PostgreSQL)

1. In Render dashboard, click **"New +"** → **"PostgreSQL"**
2. Configure:
   - Name: `connect-link-db`
   - Database: `conlkdb`
   - User: `conlkdbuser`
   - Region: Same as web service
   - Plan: **Free**
3. Click **"Create Database"**
4. Copy the **Internal Database URL**
5. Go back to your web service → **Environment** tab
6. Add:
   ```
   DATABASE_URL=<paste the Internal Database URL>
   ```

---

## STEP 6: Update Backend for PostgreSQL

Since Render uses PostgreSQL (not MariaDB), update `requirements.txt`:

```bash
# Add psycopg2 for PostgreSQL
echo "psycopg2-binary==2.9.9" >> requirements.txt
```

Then commit and push:

```bash
git add requirements.txt
git commit -m "Add PostgreSQL support"
git push
```

Render will automatically redeploy.

---

## STEP 7: Get Your Backend URL

After deployment completes, Render gives you a URL like:

```
https://connect-link-api.onrender.com
```

**Copy this URL!** You need it for the frontend.

---

## STEP 8: Test Backend

Visit: `https://connect-link-api.onrender.com/`

You should see:
```json
{
  "api": {
    "name": "Connect Link API",
    "version": "1.0.0",
    "status": "running"
  }
}
```

---

## STEP 9: Update Frontend Configuration

Edit `frontend/.env.production`:

```env
VITE_API_BASE_URL=https://connect-link-api.onrender.com/api
VITE_APP_NAME=Connect Link
VITE_APP_DOMAIN=conlk.zen-apps.com
```

**Replace `connect-link-api.onrender.com` with your actual Render URL**

---

## STEP 10: Rebuild Frontend

```bash
cd "/c/Users/HP/Desktop/connect link/frontend"
npm run build
```

---

## STEP 11: Upload Frontend to PHP Server

### Use FileZilla:

1. **Download FileZilla:** https://filezilla-project.org/
2. **Connect:**
   - Host: `conlk.zen-apps.com`
   - Username: `conlkaccountftp`
   - Password: `1xbz22B0?`
   - Port: `21`
3. **Upload:**
   - From: `C:\Users\HP\Desktop\connect link\frontend\dist\*`
   - To: `/conlk.zen-apps.com/`
   - Upload: `index.html` and `assets/` folder

---

## STEP 12: Initialize Database

In Render dashboard, go to your web service → **Shell** tab:

```bash
python init_database.py
```

Or use the Render PostgreSQL dashboard to run SQL directly.

---

## ✅ DONE!

Visit: **https://conlk.zen-apps.com**

Your app should now work with:
- Frontend on PHP server
- Backend on Render
- Database on Render PostgreSQL

---

## 🔧 Important Notes

### Render Free Tier Limitations:
- Spins down after 15 minutes of inactivity
- First request after spin-down takes ~30 seconds
- 750 hours/month free (enough for one service)

### Database:
- PostgreSQL instead of MariaDB (syntax is 99% the same)
- Free tier: 256 MB storage
- Automatically backed up

### CORS:
Backend already configured to allow `conlk.zen-apps.com`

---

## 🆘 Troubleshooting

### Build fails on Render
- Check `requirements.txt` is correct
- Check Python version compatibility
- View logs in Render dashboard

### Frontend can't connect to backend
- Verify `.env.production` has correct Render URL
- Rebuild frontend after changing env
- Check CORS in backend

### Database connection fails
- Use the **Internal Database URL** from Render
- Format: `postgresql://user:pass@host/dbname`
- Update `DATABASE_URL` environment variable

---

## 📝 Quick Reference

**Backend URL:** `https://connect-link-api.onrender.com`  
**Frontend URL:** `https://conlk.zen-apps.com`  
**Database:** Render PostgreSQL (internal)

---

**Ready to deploy?** Start with Step 1! 🚀
