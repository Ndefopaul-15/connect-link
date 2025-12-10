# Connect Link - Folder Organization Guide

## 📊 Clean Project Structure Overview

Your Connect Link project is now organized into **4 main sections**:

```
connect-link/
│
├── 📂 backend/          ← All backend code & configuration
├── 📂 frontend/         ← All frontend code & assets  
├── 📂 docs/             ← All documentation files
└── 📂 scripts/          ← Utility scripts & helpers
```

---

## 🎯 Section Breakdown

### 1️⃣ **Backend Folder** (`/backend`)

**Purpose**: Contains the complete Flask REST API and database

**What's Inside**:
```
backend/
├── app/                 # Flask application code
│   ├── models/         # Database models (User, Link, Click, etc.)
│   ├── routes/         # API endpoints (auth, links, analytics)
│   ├── core/           # Core functionality (database, config)
│   └── tests/          # Backend tests
├── instance/           # Database files (SQLite)
├── run.py              # Development server
├── wsgi.py             # Production server
├── requirements.txt    # Python dependencies
└── [utility scripts]   # Database management tools
```

**How to Use**:
```bash
cd backend
python run.py           # Start development server
```

**Access**: `http://localhost:5000`

---

### 2️⃣ **Frontend Folder** (`/frontend`)

**Purpose**: Contains the complete React TypeScript application

**What's Inside**:
```
frontend/
├── src/                # Source code
│   ├── components/    # React components (UI, forms, etc.)
│   ├── pages/         # Page components (Dashboard, Login, etc.)
│   ├── services/      # API client (axios)
│   ├── context/       # State management (Auth context)
│   └── assets/        # Images, fonts, etc.
├── public/            # Static files (logos, favicon)
├── package.json       # Node dependencies
└── vite.config.ts     # Build configuration
```

**How to Use**:
```bash
cd frontend
npm install            # Install dependencies (first time)
npm run dev            # Start development server
```

**Access**: `http://localhost:5173`

---

### 3️⃣ **Docs Folder** (`/docs`)

**Purpose**: All project documentation and guides

**What's Inside**:
```
docs/
├── PROJECT_STRUCTURE.md      # Complete structure guide
├── FOLDER_ORGANIZATION.md    # This file
├── QUICK_START.md            # Getting started guide
├── DEPLOYMENT.md             # Production deployment
├── READY_TO_DEPLOY.md        # Deployment checklist
├── FILEZILLA_GUIDE.md        # FTP upload guide
├── FRONTEND_COMPLETE.md      # Frontend architecture
├── LOGO_GUIDE.md             # Branding assets
└── [other guides]            # Additional documentation
```

**How to Use**:
- Read `QUICK_START.md` to get started
- Check `DEPLOYMENT.md` before deploying
- Refer to specific guides as needed

---

### 4️⃣ **Scripts Folder** (`/scripts`)

**Purpose**: Utility scripts and helper files

**What's Inside**:
```
scripts/
├── fix_slugs.bat      # Fix URL slugs
├── update_db.bat      # Update database
└── test.html          # Test file
```

**How to Use**:
- Run scripts when needed for maintenance
- Mostly for development/debugging

---

## 🎨 Visual Organization

```
┌─────────────────────────────────────────┐
│         CONNECT LINK PROJECT            │
└─────────────────────────────────────────┘
              │
    ┌─────────┼─────────┬─────────┐
    │         │         │         │
┌───▼───┐ ┌──▼───┐ ┌──▼────┐ ┌──▼──────┐
│Backend│ │Front │ │ Docs  │ │ Scripts │
│       │ │ end  │ │       │ │         │
│ Flask │ │React │ │Guides │ │Helpers  │
│  API  │ │  UI  │ │ .md   │ │  .bat   │
└───────┘ └──────┘ └───────┘ └─────────┘
```

---

## 🚀 Development Workflow

### Starting Development

**Step 1: Start Backend**
```bash
cd backend
python run.py
```
✅ Backend running on `localhost:5000`

**Step 2: Start Frontend** (in new terminal)
```bash
cd frontend
npm run dev
```
✅ Frontend running on `localhost:5173`

**Step 3: Access Application**
- Open browser: `http://localhost:5173`
- Frontend talks to backend automatically

---

## 📦 Production Deployment

### Backend Deployment
```bash
cd backend
# Upload all files to server
# Configure WSGI with wsgi.py
```

### Frontend Deployment
```bash
cd frontend
npm run build
# Upload dist/ folder to server
```

See `docs/DEPLOYMENT.md` for detailed instructions.

---

## 🔍 Finding Things

### "Where is...?"

| Looking for... | Location |
|---------------|----------|
| API endpoints | `backend/app/routes/` |
| Database models | `backend/app/models/` |
| React components | `frontend/src/components/` |
| Pages (Dashboard, Login) | `frontend/src/pages/` |
| API client | `frontend/src/services/api.ts` |
| Documentation | `docs/` |
| Python dependencies | `backend/requirements.txt` |
| Node dependencies | `frontend/package.json` |
| Environment config | `backend/.env.production` |
| Database file | `backend/instance/app.db` |

---

## ✅ Benefits of This Organization

1. **Clear Separation**: Backend and frontend are completely separate
2. **Easy Navigation**: Everything has its place
3. **Documentation Centralized**: All guides in one folder
4. **Scalable**: Easy to add new features
5. **Professional**: Industry-standard structure
6. **Team-Friendly**: New developers can understand quickly
7. **Deployment-Ready**: Each section can be deployed independently

---

## 🎯 Quick Reference

### Backend Commands
```bash
cd backend
python run.py                    # Dev server
python init_database.py          # Initialize DB
python create_test_user.py       # Create test user
pytest                           # Run tests
```

### Frontend Commands
```bash
cd frontend
npm install                      # Install dependencies
npm run dev                      # Dev server
npm run build                    # Production build
npm run preview                  # Preview build
```

### Documentation
```bash
cd docs
# Open any .md file to read
```

---

## 📝 Notes

- **Root folder is clean**: Only essential files at root level
- **No duplicates**: Each file exists in only one location
- **Git-ready**: `.gitignore` configured properly
- **Production-ready**: Separate dev and production configs
- **Well-documented**: Every section has README or guide

---

## 🆘 Need Help?

1. **Quick Start**: Read `docs/QUICK_START.md`
2. **Structure Details**: Read `docs/PROJECT_STRUCTURE.md`
3. **Deployment**: Read `docs/DEPLOYMENT.md`
4. **Frontend**: Read `docs/FRONTEND_COMPLETE.md`

---

**Last Updated**: December 10, 2025  
**Organization Version**: 2.0
