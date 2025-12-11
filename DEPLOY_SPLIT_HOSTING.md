# 🚀 Split Deployment Guide - Backend on Render, Frontend on PHP Server

## 📋 Architecture

```
Frontend (Static Files)  →  PHP Server (conlk.zen-apps.com)
Backend (Python/Flask)   →  Render.com
Database (MariaDB)       →  Your choice (Render or external)
```

---

## PART 1: Deploy Backend to Render

### Step 1: Create Render Account

1. Go to: https://render.com
2. Sign up (free tier available)
3. Connect your GitHub account (or deploy manually)

---

### Step 2: Prepare Backend for Render

Create `render.yaml` in your backend folder:

```yaml
services:
  - type: web
    name: connect-link-api
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn wsgi:app
    envVars:
      - key: FLASK_ENV
        value: production
      - key: SECRET_KEY
        generateValue: true
      - key: JWT_SECRET_KEY
        generateValue: true
      - key: DATABASE_URL
        value: mysql+pymysql://conlkdbuser:l0X&Vo$6pok0Wqii@localhost:3306/conlkdb
      - key: DEFAULT_DOMAIN
        value: https://conlk.zen-apps.com
      - key: FRONTEND_URL
        value: https://conlk.zen-apps.com
```

---

### Step 3: Deploy to Render

#### Option A: Via GitHub (Recommended)

```bash
# Initialize git in backend folder
cd "/c/Users/HP/Desktop/connect link/backend"
git init
git add .
git commit -m "Initial backend deployment"

# Create GitHub repo and push
# Then connect to Render
```

#### Option B: Manual Deploy

1. Go to Render Dashboard
2. Click "New +" → "Web Service"
3. Choose "Deploy from Git" or "Deploy manually"
4. Select Python environment
5. Set build command: `pip install -r requirements.txt`
6. Set start command: `gunicorn wsgi:app`
7. Add environment variables

---

### Step 4: Get Your Render Backend URL

After deployment, Render will give you a URL like:
```
https://connect-link-api.onrender.com
```

**Save this URL!** You'll need it for the frontend.

---

## PART 2: Update Frontend Configuration

### Update Frontend to Point to Render Backend

Edit `frontend/.env.production`:

```env
# Change from local domain to Render backend
VITE_API_BASE_URL=https://connect-link-api.onrender.com/api
VITE_APP_NAME=Connect Link
VITE_APP_DOMAIN=conlk.zen-apps.com
```

**Replace `connect-link-api.onrender.com` with your actual Render URL**

---

### Rebuild Frontend

```bash
cd "/c/Users/HP/Desktop/connect link/frontend"
npm run build
```

---

## PART 3: Deploy Frontend to PHP Server via FTP

### Use FileZilla or Git Bash FTP

Upload ONLY frontend files to your PHP server:

```
From: frontend/dist/*
To:   /conlk.zen-apps.com/
```

Files to upload:
- `index.html`
- `assets/` folder
- `.htaccess` (for routing)

---

## PART 4: Configure CORS on Backend

Update `backend/app/__init__.py` to allow your frontend domain:

```python
# Update CORS configuration
CORS(app, resources={
    r"/api/*": {
        "origins": ["https://conlk.zen-apps.com"],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})
```

---

## 📁 Final Architecture

```
User visits: https://conlk.zen-apps.com
    ↓
PHP Server serves: index.html + assets (frontend)
    ↓
Frontend makes API calls to: https://connect-link-api.onrender.com/api
    ↓
Render serves: Python Flask backend
    ↓
Backend connects to: Database (MariaDB)
```

---

## 🗄️ Database Options

### Option 1: Use Render's Database (Recommended)

1. In Render Dashboard, create a PostgreSQL database
2. Update `DATABASE_URL` in backend to use Render's database
3. Update SQLAlchemy to use PostgreSQL instead of MariaDB

### Option 2: Use External MariaDB

1. Get a MariaDB hosting service (like PlanetScale, Railway, etc.)
2. Update `DATABASE_URL` with external database credentials
3. Ensure database is accessible from Render

### Option 3: Use SQLite (Development Only)

For testing, you can use SQLite on Render (not recommended for production)

---

## ✅ Deployment Checklist

### Backend (Render)
- [ ] Create Render account
- [ ] Deploy backend to Render
- [ ] Get Render backend URL
- [ ] Configure environment variables
- [ ] Test API endpoint: `https://your-app.onrender.com/`

### Frontend (PHP Server)
- [ ] Update `.env.production` with Render backend URL
- [ ] Rebuild frontend: `npm run build`
- [ ] Upload `dist/*` to PHP server via FileZilla
- [ ] Test frontend: `https://conlk.zen-apps.com`

### Database
- [ ] Choose database option
- [ ] Update DATABASE_URL
- [ ] Run migrations/initialization

---

## 🚀 Quick Deployment Commands

### 1. Deploy Backend to Render

```bash
cd "/c/Users/HP/Desktop/connect link/backend"

# Option A: Push to GitHub
git init
git add .
git commit -m "Deploy to Render"
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main

# Then connect GitHub repo to Render
```

### 2. Update and Build Frontend

```bash
cd "/c/Users/HP/Desktop/connect link/frontend"

# Update .env.production with Render URL
# Then rebuild
npm run build
```

### 3. Upload Frontend via FileZilla

- Connect to `conlk.zen-apps.com` with FTP
- Upload `frontend/dist/*` to `/conlk.zen-apps.com/`

---

## 🔧 Testing

### Test Backend (Render)
```bash
curl https://your-app.onrender.com/
```

Should return API info.

### Test Frontend (PHP Server)
Visit: `https://conlk.zen-apps.com`

Should load the app and connect to Render backend.

---

## 💡 Why This Setup?

✅ **Backend on Render:**
- Supports Python/Flask
- Free tier available
- Easy deployment
- Handles Python dependencies

✅ **Frontend on PHP Server:**
- Static files (HTML, CSS, JS)
- Works on any server (PHP, Apache, etc.)
- Uses your existing domain

✅ **Separated Concerns:**
- Frontend and backend can be updated independently
- Better scalability
- Professional architecture

---

## 📝 Important Notes

1. **Render Free Tier:** Spins down after inactivity (may take 30s to wake up)
2. **CORS:** Make sure backend allows requests from your frontend domain
3. **HTTPS:** Both frontend and backend should use HTTPS
4. **Database:** Choose a persistent database solution (not SQLite on Render)

---

## 🆘 Troubleshooting

### Frontend can't connect to backend
- Check `.env.production` has correct Render URL
- Rebuild frontend after changing env
- Check CORS settings in backend

### Backend not responding
- Check Render logs
- Verify environment variables are set
- Check database connection

### Database connection fails
- Use Render's PostgreSQL instead of MariaDB
- Or use external database service
- Update DATABASE_URL accordingly

---

**Next Steps:**
1. Deploy backend to Render
2. Get Render backend URL
3. Update frontend config
4. Upload frontend to PHP server

Let me know when you're ready to start! 🚀
