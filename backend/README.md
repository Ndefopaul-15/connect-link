# Connect Link - Backend

This folder contains all the backend components for the Connect Link URL shortener application.

## Structure

```
backend/
├── app/                          # Main Flask application
│   ├── __init__.py              # App factory
│   ├── config.py                # Configuration
│   ├── api/                     # API endpoints
│   ├── core/                    # Core functionality (db, config)
│   ├── crud/                    # CRUD operations
│   ├── models/                  # Database models
│   ├── routes/                  # Route blueprints
│   ├── schemas/                 # Data schemas
│   └── tests/                   # Test files
├── instance/                    # Instance-specific files (database)
├── run.py                       # Development server entry point
├── wsgi.py                      # Production WSGI entry point
├── requirements.txt             # Python dependencies (development)
├── requirements.production.txt  # Python dependencies (production)
├── .env.production             # Production environment variables
├── .env.server                 # Server environment variables
├── .htaccess                   # Apache configuration
├── setup_server.sh             # Server setup script
└── [utility scripts]           # Database and testing utilities
```

## Utility Scripts

- `create_test_user.py` - Create test users
- `init_database.py` - Initialize database
- `init_fresh_db.py` - Create fresh database
- `generate_keys.py` - Generate secret keys
- `test_db_connection.py` - Test database connection
- `migrate_password_reset.py` - Password reset migration
- `update_database.py` - Database update script
- `fix_invalid_slugs.py` - Fix invalid URL slugs

## Running the Backend

### Development
```bash
cd backend
python run.py
```

### Production
The application uses WSGI for production deployment. See `wsgi.py` for configuration.

## Database

- **Development**: SQLite (instance/app.db)
- **Production**: MariaDB (configured in .env.production)
