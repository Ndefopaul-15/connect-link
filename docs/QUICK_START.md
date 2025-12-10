# 🚀 Quick Start Guide - Connect Link

## ⚡ Start Both Servers

### Terminal 1 - Backend (Flask)
```powershell
cd "c:\Users\HP\Desktop\connect link"
.venv\Scripts\Activate.ps1
python run.py
```
**Expected Output:**
```
* Running on http://127.0.0.1:5000
* Debugger is active!
```

### Terminal 2 - Frontend (React)
```powershell
cd "c:\Users\HP\Desktop\connect link\frontend"
npm run dev
```
**Expected Output:**
```
➜  Local:   http://localhost:5175/
```

---

## 🌐 Access Application

1. **Open Browser**: `http://localhost:5175`
2. **Register**: Create a new account
3. **Login**: Sign in with your credentials
4. **Create Links**: Start shortening URLs!

---

## 🐛 Troubleshooting CORS Errors

### If you see: "blocked by CORS policy"

**Solution:**
1. Make sure **BOTH** servers are running
2. Backend must be on: `http://127.0.0.1:5000`
3. Frontend must be on: `http://localhost:5175`
4. Restart backend if needed:
   ```powershell
   # Stop backend (Ctrl+C)
   # Then restart:
   .venv\Scripts\python.exe run.py
   ```

### If backend won't start:

**Error**: `ModuleNotFoundError: No module named 'flask_jwt_extended'`

**Solution**: Activate virtual environment first!
```powershell
.venv\Scripts\Activate.ps1
python run.py
```

---

## ✅ Verify Everything is Working

### 1. Check Backend
Open: `http://127.0.0.1:5000`

Should see:
```json
{
  "api": {
    "name": "Connect Link API",
    "status": "running"
  }
}
```

### 2. Check Frontend
Open: `http://localhost:5175`

Should see: **Connect Link logo** and login form

### 3. Test Registration
1. Click "Sign up"
2. Enter email and password
3. Should redirect to dashboard
4. If you see CORS error, restart backend

---

## 🎯 Common Issues & Solutions

### Issue: "Cannot connect to backend"
**Check:**
- ✅ Backend running on port 5000?
- ✅ Virtual environment activated?
- ✅ No firewall blocking?

### Issue: "CORS policy error"
**Fix:**
```powershell
# Restart backend with venv
cd "c:\Users\HP\Desktop\connect link"
.venv\Scripts\python.exe run.py
```

### Issue: "Module not found"
**Fix:**
```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Issue: "Port already in use"
**Fix:**
```powershell
# Find and kill process on port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Or use different port in run.py:
# app.run(debug=True, port=5001)
```

---

## 📝 Quick Commands Reference

### Backend Commands
```powershell
# Activate venv
.venv\Scripts\Activate.ps1

# Run server
python run.py

# Run tests
python -m pytest app/tests/ -v

# Install dependencies
pip install -r requirements.txt
```

### Frontend Commands
```powershell
# Install dependencies
npm install

# Run dev server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

---

## 🎉 Success Checklist

- [ ] Backend running on `http://127.0.0.1:5000`
- [ ] Frontend running on `http://localhost:5175`
- [ ] Can see Connect Link logo on login page
- [ ] Can register new account
- [ ] Can login successfully
- [ ] Can create short links
- [ ] Can view dashboard
- [ ] Can see analytics
- [ ] No CORS errors in console

---

## 💡 Pro Tips

1. **Keep both terminals open** while developing
2. **Backend auto-reloads** when you change Python files
3. **Frontend hot-reloads** when you change React files
4. **Check browser console** (F12) for errors
5. **Check backend terminal** for API errors

---

## 🚀 You're Ready!

Both servers should now be running without CORS errors. Open `http://localhost:5175` and start using your Connect Link application!

**Need help?** Check the browser console (F12) and backend terminal for error messages.
