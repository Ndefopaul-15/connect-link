#!/usr/bin/env python3
"""
WSGI Entry Point for Connect Link Application
Production deployment on conlk.zen-apps.com
"""
import sys
import os

# Add the project directory to the Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_dir)

# Import the Flask application factory
from app import create_app

# Create the application instance for production
# The environment is determined by FLASK_ENV in .env file
app = create_app(os.getenv('FLASK_ENV', 'production'))

# For development/testing
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
