# Connect Link - Project Structure

## 📁 Complete Directory Structure

```
connect-link/
│
├── 📂 backend/                    # Backend Application (Flask + Python)
│   │
│   ├── 📂 app/                    # Main Flask Application
│   │   ├── __init__.py           # App factory & initialization
│   │   ├── config.py             # Configuration classes
│   │   │
│   │   ├── 📂 api/               # API endpoints (future use)
│   │   │   └── __init__.py
│   │   │
│   │   ├── 📂 core/              # Core functionality
│   │   │   ├── __init__.py
│   │   │   ├── config.py         # Core configuration
│   │   │   └── db.py             # Database initialization
│   │   │
│   │   ├── 📂 crud/              # CRUD operations
│   │   │   └── __init__.py
│   │   │
│   │   ├── 📂 models/            # SQLAlchemy Models
│   │   │   ├── __init__.py
│   │   │   ├── user.py           # User model
│   │   │   ├── link.py           # Link model
│   │   │   ├── click.py          # Click tracking model
│   │   │   ├── domain.py         # Custom domain model
│   │   │   ├── qr_code.py        # QR code model
│   │   │   ├── targeting_rule.py # Targeting rules model
│   │   │   ├── reward.py         # Rewards model
│   │   │   ├── points_ledger.py  # Points tracking model
│   │   │   └── link_daily_stats.py # Daily statistics model
│   │   │
│   │   ├── 📂 routes/            # API Route Blueprints
│   │   │   ├── __init__.py
│   │   │   ├── auth.py           # Authentication routes
│   │   │   ├── links.py          # Link management routes
│   │   │   ├── clicks.py         # Click tracking routes
│   │   │   ├── analytics.py      # Analytics routes
│   │   │   ├── domains.py        # Domain management routes
│   │   │   ├── qr_codes.py       # QR code routes
│   │   │   ├── targeting_rules.py # Targeting rules routes
│   │   │   └── rewards.py        # Rewards routes
│   │   │
│   │   ├── 📂 schemas/           # Data validation schemas
│   │   │   └── __init__.py
│   │   │
│   │   └── 📂 tests/             # Backend tests
│   │       └── test_auth_links.py
│   │
│   ├── 📂 instance/              # Instance-specific files
│   │   └── app.db                # SQLite database (development)
│   │
│   ├── run.py                    # Development server entry point
│   ├── wsgi.py                   # Production WSGI entry point
│   ├── requirements.txt          # Python dependencies (dev)
│   ├── requirements.production.txt # Python dependencies (prod)
│   ├── .env.production           # Production environment config
│   ├── .env.server               # Server environment config
│   ├── .htaccess                 # Apache configuration
│   ├── setup_server.sh           # Server setup script
│   │
│   └── 📂 [Utility Scripts]      # Database & testing utilities
│       ├── create_test_user.py
│       ├── init_database.py
│       ├── init_fresh_db.py
│       ├── generate_keys.py
│       ├── test_db_connection.py
│       ├── migrate_password_reset.py
│       ├── update_database.py
│       └── fix_invalid_slugs.py
│
├── 📂 frontend/                   # Frontend Application (React + TypeScript)
│   │
│   ├── 📂 src/                   # Source code
│   │   ├── main.tsx              # Application entry point
│   │   ├── App.tsx               # Root component
│   │   ├── index.css             # Global styles
│   │   │
│   │   ├── 📂 components/        # React components
│   │   │   ├── 📂 ui/           # shadcn/ui components
│   │   │   ├── 📂 layout/       # Layout components
│   │   │   ├── 📂 dashboard/    # Dashboard components
│   │   │   ├── 📂 links/        # Link management components
│   │   │   ├── 📂 analytics/    # Analytics components
│   │   │   └── 📂 auth/         # Authentication components
│   │   │
│   │   ├── 📂 pages/            # Page components
│   │   │   ├── Dashboard.tsx
│   │   │   ├── Login.tsx
│   │   │   ├── Register.tsx
│   │   │   ├── Links.tsx
│   │   │   ├── Analytics.tsx
│   │   │   └── Settings.tsx
│   │   │
│   │   ├── 📂 context/          # React Context providers
│   │   │   └── AuthContext.tsx
│   │   │
│   │   ├── 📂 services/         # API services
│   │   │   └── api.ts
│   │   │
│   │   ├── 📂 hooks/            # Custom React hooks
│   │   │
│   │   ├── 📂 utils/            # Utility functions
│   │   │
│   │   ├── 📂 types/            # TypeScript type definitions
│   │   │
│   │   └── 📂 assets/           # Static assets (images, fonts)
│   │
│   ├── 📂 public/                # Public static files
│   │   ├── favicon.svg
│   │   ├── logo-no-bg.svg
│   │   ├── logo-white.svg
│   │   ├── logo.svg
│   │   └── background.jpg
│   │
│   ├── index.html                # HTML template
│   ├── package.json              # Node dependencies & scripts
│   ├── tsconfig.json             # TypeScript configuration
│   ├── vite.config.ts            # Vite configuration
│   ├── tailwind.config.js        # TailwindCSS configuration
│   ├── postcss.config.js         # PostCSS configuration
│   ├── components.json           # shadcn/ui configuration
│   └── .gitignore                # Git ignore rules
│
├── 📂 docs/                      # Documentation
│   ├── README.md                 # Main documentation (moved from root)
│   ├── QUICK_START.md            # Quick start guide
│   ├── DEPLOYMENT.md             # Deployment instructions
│   ├── READY_TO_DEPLOY.md        # Deployment checklist
│   ├── UPLOAD_CHECKLIST.md       # Upload checklist
│   ├── FILEZILLA_GUIDE.md        # FTP deployment guide
│   ├── SETUP_PASSWORD_RESET.md   # Email configuration
│   ├── FRONTEND_COMPLETE.md      # Frontend documentation
│   ├── LOGO_GUIDE.md             # Branding guidelines
│   ├── ANIMATED_BACKGROUND.md    # Background customization
│   ├── DASHBOARD_BACKGROUND.md   # Dashboard styling
│   ├── DEEP_CHECK_REPORT.md      # System check report
│   └── PROJECT_STRUCTURE.md      # This file
│
├── 📂 scripts/                   # Utility scripts
│   ├── fix_slugs.bat
│   ├── update_db.bat
│   └── test.html
│
├── 📂 .pytest_cache/             # Pytest cache
├── 📂 .venv/                     # Python virtual environment (local)
├── 📂 venv/                      # Alternative venv (local)
│
├── .gitignore                    # Git ignore rules
└── README.md                     # Project overview & quick start
```

## 🎯 Key Directories Explained

### Backend (`/backend`)
Contains the entire Flask REST API, database models, and server configuration.

**Key Files:**
- `run.py` - Start development server
- `wsgi.py` - Production WSGI entry point
- `app/__init__.py` - Flask app factory
- `app/routes/` - All API endpoints
- `app/models/` - Database models

### Frontend (`/frontend`)
Contains the React TypeScript application with modern UI.

**Key Files:**
- `src/main.tsx` - Application entry
- `src/App.tsx` - Root component with routing
- `src/components/` - Reusable UI components
- `src/pages/` - Page-level components
- `src/services/api.ts` - API client

### Documentation (`/docs`)
All project documentation, guides, and references.

### Scripts (`/scripts`)
Helper scripts for development and maintenance.

## 🔄 Data Flow

```
User Browser
    ↓
Frontend (React)
    ↓
API Service (axios)
    ↓
Backend Routes (Flask)
    ↓
Models & Database (SQLAlchemy)
    ↓
SQLite/MariaDB
```

## 🚀 Development Workflow

1. **Backend**: `cd backend && python run.py`
2. **Frontend**: `cd frontend && npm run dev`
3. **Access**: Frontend at `localhost:5173`, Backend at `localhost:5000`

## 📦 Production Build

1. **Backend**: Deploy via WSGI (Apache/Nginx)
2. **Frontend**: Build with `npm run build`, deploy `dist/` folder
3. **Database**: Migrate to MariaDB for production

## 🔐 Environment Files

- `backend/.env.production` - Backend production config
- `backend/.env.server` - Server-specific config
- `frontend/.env.production` - Frontend production config

## 📝 Notes

- Keep backend and frontend completely separate
- All documentation in `/docs` folder
- Utility scripts in `/scripts` folder
- Environment files are gitignored for security
- Database files (`instance/`) are gitignored
