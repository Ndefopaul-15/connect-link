# 🔧 Frontend-Backend Communication Setup Guide

## ✅ Issue Fixed

**Problem:** Frontend was trying to connect to `https://conlk.zen-apps.com/api` but getting 500 errors.

**Root Cause:** Environment configuration mismatch between local development and production deployment.

**Solution:** Updated environment files and CORS configuration for proper communication.

---

## 📁 Configuration Files Updated

### 1. Frontend Environment Files

#### `.env.local` (Local Development)
```env
VITE_API_BASE_URL=http://127.0.0.1:5000/api
VITE_APP_NAME=Connect Link
VITE_APP_DOMAIN=localhost:5173
```
**Use this when:** Running frontend and backend locally on your machine.

#### `.env` (Production - Default)
```env
VITE_API_BASE_URL=https://connect-link.onrender.com/api
VITE_APP_NAME=Connect Link
VITE_APP_DOMAIN=conlk.zen-apps.com
```
**Use this when:** Deploying frontend to conlk.zen-apps.com with backend on Render.

#### `.env.production` (Alternative Production)
```env
VITE_API_BASE_URL=https://connect-link.onrender.com/api
VITE_APP_NAME=Connect Link
VITE_APP_DOMAIN=conlk.zen-apps.com
```
**Use this when:** Building for production deployment.

### 2. Backend CORS Configuration

Updated `backend/app/__init__.py` to allow these origins:
- `http://localhost:5173` (Local frontend dev)
- `http://127.0.0.1:5173` (Local frontend dev alternative)
- `https://conlk.zen-apps.com` (Production frontend)
- `https://connect-link.onrender.com` (Production backend)

---

## 🚀 How to Run Locally

### Step 1: Start Backend Server

```bash
cd backend
python run.py
```

**Expected output:**
```
* Running on http://127.0.0.1:5000
```

### Step 2: Start Frontend Development Server

```bash
cd frontend
npm run dev
```

**Expected output:**
```
VITE v5.x.x ready in xxx ms
➜ Local: http://localhost:5173/
```

### Step 3: Test the Connection

1. Open browser: `http://localhost:5173`
2. Try to register/login
3. Check browser console for any errors

**If you see CORS errors:**
- Make sure backend is running on `http://127.0.0.1:5000`
- Verify `.env.local` has `VITE_API_BASE_URL=http://127.0.0.1:5000/api`
- Restart both servers

---

## 🌐 Production Deployment Options

### Option A: Frontend on conlk.zen-apps.com + Backend on Render

**Best for:** Reliable backend with free hosting

**Steps:**

1. **Deploy Backend to Render:**
   - Go to https://render.com
   - Create new Web Service
   - Connect your GitHub repo
   - Set environment variables from `backend/.env.production`
   - Deploy

2. **Build Frontend:**
   ```bash
   cd frontend
   npm run build
   ```

3. **Upload Frontend to conlk.zen-apps.com:**
   - Use FileZilla
   - Upload all files from `frontend/dist/` to `/conlk.zen-apps.com/`

4. **Update Frontend .env:**
   - Make sure `.env` or `.env.production` points to your Render backend URL
   - Example: `VITE_API_BASE_URL=https://your-app.onrender.com/api`

### Option B: Both on conlk.zen-apps.com

**Best for:** Single server deployment

**Steps:**

1. **Upload Backend:**
   - Upload `backend/` folder to `/conlk.zen-apps.com/`
   - Configure `.htaccess` for Python/Flask
   - Install dependencies: `pip install -r requirements.txt`

2. **Upload Frontend:**
   - Build: `npm run build`
   - Upload `dist/` contents to `/conlk.zen-apps.com/public_html/`

3. **Update Frontend .env:**
   ```env
   VITE_API_BASE_URL=https://conlk.zen-apps.com/api
   ```

---

## 🔍 Troubleshooting

### Error: "Failed to fetch" or "Network Error"

**Cause:** Frontend can't reach backend

**Fix:**
1. Check backend is running: Visit `http://127.0.0.1:5000/` (should show API info)
2. Check `.env.local` has correct backend URL
3. Check browser console for CORS errors
4. Restart both servers

### Error: "CORS policy blocked"

**Cause:** Backend doesn't allow frontend origin

**Fix:**
1. Check `backend/app/__init__.py` CORS configuration
2. Add your frontend URL to `allowed_origins` list
3. Restart backend server

### Error: "500 Internal Server Error"

**Cause:** Backend error (database, missing dependencies, etc.)

**Fix:**
1. Check backend terminal for error messages
2. Verify database is initialized: `python init_database.py`
3. Check all dependencies installed: `pip install -r requirements.txt`
4. Check `.env` file exists with correct values

### Dashboard shows "Loading..." forever

**Cause:** API call failing silently

**Fix:**
1. Open browser DevTools (F12)
2. Go to Network tab
3. Refresh page
4. Look for failed API calls (red entries)
5. Check the error message in the response

---

## 📝 Quick Reference

### Local Development URLs
- **Frontend:** http://localhost:5173
- **Backend API:** http://127.0.0.1:5000/api
- **Backend Root:** http://127.0.0.1:5000

### Production URLs
- **Frontend:** https://conlk.zen-apps.com
- **Backend (Render):** https://connect-link.onrender.com/api
- **Backend (Same server):** https://conlk.zen-apps.com/api

### Environment Files
- **Local Dev:** Use `.env.local`
- **Production Build:** Use `.env` or `.env.production`
- **Backend:** Use `.env` (created from `.env.production`)

---

## ✅ Verification Checklist

Before deploying, verify:

- [ ] Backend runs locally without errors
- [ ] Frontend runs locally and connects to backend
- [ ] Can register/login locally
- [ ] Can create links locally
- [ ] Environment files have correct URLs
- [ ] CORS allows your frontend domain
- [ ] Production build completes without errors
- [ ] All dependencies installed

---

## 🎯 Next Steps

1. **Test Locally First:**
   - Start backend: `cd backend && python run.py`
   - Start frontend: `cd frontend && npm run dev`
   - Test all features

2. **Deploy Backend:**
   - Choose Render.com or conlk.zen-apps.com
   - Set environment variables
   - Initialize database

3. **Deploy Frontend:**
   - Build: `npm run build`
   - Upload to conlk.zen-apps.com
   - Test production site

4. **Monitor:**
   - Check browser console for errors
   - Check backend logs for issues
   - Test all features in production

---

**Last Updated:** December 11, 2025  
**Status:** ✅ Configuration Fixed and Ready
