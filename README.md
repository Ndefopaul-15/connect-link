# Connect Link - URL Shortener Platform

A modern, full-stack URL shortening platform with advanced analytics, QR code generation, and custom domains.

> **✨ Project Status**: Production Ready - All Issues Fixed ✅  
> **📅 Last Updated**: December 11, 2025  
> **📂 Structure Version**: 2.0  
> **🔧 Recent Fixes**: See [FIXES_APPLIED.md](FIXES_APPLIED.md) for details

## 🎉 Recent Updates (Dec 11, 2025)

All critical issues have been identified and fixed:
- ✅ Production dependencies completed (Flask-Bcrypt, dnspython, Pillow, qrcode)
- ✅ Secure cryptographic keys generated
- ✅ Database initialization corrected
- ✅ All hardcoded URLs updated to production domain
- ✅ Unused configuration files removed
- ✅ Model constraints optimized

**Quick Start:** See [QUICK_DEPLOY.md](QUICK_DEPLOY.md) for 5-minute deployment guide.

## 🚀 Project Structure

```
connect-link/
├── backend/              # Flask REST API & Database
│   ├── app/             # Main application code
│   ├── instance/        # Database files
│   ├── run.py          # Development server
│   ├── wsgi.py         # Production WSGI entry
│   └── requirements.txt # Python dependencies
│
├── frontend/            # React TypeScript Application
│   ├── src/            # Source code
│   ├── public/         # Static assets
│   └── package.json    # Node dependencies
│
├── docs/               # Documentation
│   ├── DEPLOYMENT.md
│   ├── QUICK_START.md
│   └── [other guides]
│
└── scripts/            # Utility scripts
    └── [helper scripts]
```

## 📋 Features

- **URL Shortening**: Create short, memorable links
- **Custom Domains**: Use your own branded domains
- **QR Codes**: Auto-generate QR codes for links
- **Analytics**: Track clicks, locations, devices, and more
- **Targeting Rules**: Device, location, and time-based redirects
- **Rewards System**: Gamification with points and achievements
- **User Management**: Secure authentication and authorization

## 🛠️ Technology Stack

### Backend
- **Framework**: Flask (Python)
- **Database**: SQLite (dev) / MariaDB (production)
- **ORM**: SQLAlchemy
- **Authentication**: JWT tokens
- **API**: RESTful architecture

### Frontend
- **Framework**: React 18 with TypeScript
- **Styling**: TailwindCSS
- **UI Components**: shadcn/ui
- **Icons**: Lucide React
- **State Management**: React Context
- **Routing**: React Router v6
- **HTTP Client**: Axios

## 🚦 Quick Start

### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Initialize database
python init_database.py

# Run development server
python run.py
```

Backend will run on `http://localhost:5000`

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

Frontend will run on `http://localhost:5173`

## 📚 Documentation

Detailed documentation is available in the `docs/` folder:

- **[Quick Start Guide](docs/QUICK_START.md)** - Get started quickly
- **[Deployment Guide](docs/DEPLOYMENT.md)** - Production deployment
- **[Setup Password Reset](docs/SETUP_PASSWORD_RESET.md)** - Configure email
- **[FileZilla Guide](docs/FILEZILLA_GUIDE.md)** - FTP deployment
- **[Frontend Guide](docs/FRONTEND_COMPLETE.md)** - Frontend architecture
- **[Logo Guide](docs/LOGO_GUIDE.md)** - Branding assets

## 🌐 Deployment

### Production Environment

- **Domain**: conlk.zen-apps.com
- **Backend**: Flask with WSGI
- **Frontend**: Static build served via CDN/Web server
- **Database**: MariaDB

See `docs/DEPLOYMENT.md` for complete deployment instructions.

## 🔧 Configuration

### Backend Environment Variables

Create `.env.production` in the backend folder:

```env
FLASK_ENV=production
SECRET_KEY=your-secret-key
DATABASE_URL=mysql+pymysql://user:pass@localhost/dbname
JWT_SECRET_KEY=your-jwt-secret
```

### Frontend Environment Variables

Create `.env.production` in the frontend folder:

```env
VITE_API_URL=https://conlk.zen-apps.com/api
```

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

## 📦 Building for Production

### Backend
```bash
cd backend
pip install -r requirements.production.txt
```

### Frontend
```bash
cd frontend
npm run build
```

Build output will be in `frontend/dist/`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is proprietary software.

## 👥 Support

For support and questions, please refer to the documentation in the `docs/` folder.

---

**Version**: 1.0.0  
**Last Updated**: December 2025
