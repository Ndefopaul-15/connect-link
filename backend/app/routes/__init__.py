from flask import Blueprint

# Create main blueprint
api = Blueprint('api', __name__)

# Import all route modules here
from . import auth, links, domains, qr_codes, targeting_rules, clicks, rewards, analytics

# Register blueprints
def register_blueprints(app):
    app.register_blueprint(api)
