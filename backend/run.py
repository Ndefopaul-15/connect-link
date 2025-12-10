import os
from app import create_app

# Set environment variables for Flask
os.environ['FLASK_APP'] = 'app'
os.environ['FLASK_ENV'] = 'development'

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
