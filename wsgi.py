#!/usr/bin/env python3
"""
WSGI Entry Point for Connect Link Application
Render.com Production Deployment
"""
import sys
import os

# Add the backend directory to the Python path
backend_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backend')
sys.path.insert(0, backend_dir)

# Import the Flask application factory
from app import create_app

# Create the application instance for production
app = create_app(os.getenv('FLASK_ENV', 'production'))

# For development/testing
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=False)
