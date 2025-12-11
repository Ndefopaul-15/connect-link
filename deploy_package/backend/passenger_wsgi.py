#!/usr/bin/env python3
"""
Passenger WSGI Entry Point for cPanel Deployment
This file is used by cPanel's Python application setup
"""
import sys
import os

# Add the backend directory to Python path
INTERP = os.path.join(os.environ['HOME'], 'virtualenv', 'conlk.zen-apps.com', 'backend', '3.11', 'bin', 'python3')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

# Load environment variables from .env.production
from dotenv import load_dotenv
env_path = os.path.join(os.path.dirname(__file__), '.env.production')
load_dotenv(env_path)

# Import the Flask application
from app import create_app

# Create the application instance
application = create_app('production')

# For debugging (remove in production)
if __name__ == "__main__":
    application.run()
