# Quick Deployment Guide

## 🚀 Deploy Connect Link in 5 Minutes

### Prerequisites
- Python 3.11+ installed
- Node.js 18+ installed
- MariaDB running on localhost
- Database `conlkdb` created with user `conlkdbuser`

---

## Backend Deployment

### Step 1: Install Dependencies
```bash
cd backend
pip install -r requirements.production.txt
```

### Step 2: Initialize Database
```bash
# Test database connection first
python test_db_connection.py

# If connection successful, initialize database
python init_database.py
```

### Step 3: Start Backend Server
```bash
# For production with Gunicorn
gunicorn --bind 0.0.0.0:5000 --workers 4 wsgi:app

# Or for testing
python run.py
```

**Backend will be running at:** `http://localhost:5000`

---

## Frontend Deployment

### Step 1: Install Dependencies
```bash
cd frontend
npm install
```

### Step 2: Build for Production
```bash
npm run build
```

### Step 3: Deploy
The `dist/` folder contains your production build. Upload it to your web server.

**For testing locally:**
```bash
npm run preview
```

---

## Verify Deployment

### Test Backend
```bash
# Test API is running
curl http://localhost:5000/

# Test user registration
curl -X POST http://localhost:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"testpass123"}'
```

### Test Frontend
1. Open browser to `http://localhost:5173` (dev) or your deployed URL
2. Try to register a new account
3. Create a short link
4. Test the redirect

---

## Production Checklist

- [ ] Backend running on port 5000
- [ ] Frontend built and deployed
- [ ] Database initialized with tables
- [ ] Can register and login
- [ ] Can create and access short links
- [ ] QR codes generate correctly
- [ ] Analytics show click data

---

## Troubleshooting

### "Module not found" errors
```bash
pip install -r requirements.production.txt
```

### Database connection fails
- Check MariaDB is running: `systemctl status mariadb`
- Verify credentials in `.env.production`
- Test with: `python test_db_connection.py`

### Frontend can't connect to backend
- Check `VITE_API_BASE_URL` in `.env.production`
- Verify CORS settings in backend
- Check backend is running

### QR codes don't generate
- Ensure Pillow and qrcode are installed
- Check backend logs for errors

---

## Quick Commands Reference

```bash
# Backend
cd backend
pip install -r requirements.production.txt
python init_database.py
gunicorn --bind 0.0.0.0:5000 wsgi:app

# Frontend
cd frontend
npm install
npm run build
npm run preview

# Database
python test_db_connection.py
python init_database.py
```

---

**Need help?** Check `FIXES_APPLIED.md` for detailed information about all fixes.
