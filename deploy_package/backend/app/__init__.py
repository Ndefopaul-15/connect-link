from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from .config import config
import os

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
bcrypt = Bcrypt()

def create_app(config_name='default'):
    """Application factory function"""
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)
    
    # Configure CORS to allow frontend access
    CORS(app, 
         resources={r"/*": {"origins": "*"}},
         supports_credentials=True,
         allow_headers=["Content-Type", "Authorization"],
         methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"]
    )
    
    # Register blueprints
    from .routes import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')
    
    # Root route
    @app.route('/')
    def index():
        return jsonify({
            "api": {
                "name": "Connect Link API",
                "version": "1.0.0",
                "description": "A powerful URL shortening and link management API with advanced features",
                "status": "running",
                "documentation": "https://github.com/your-repo/connect-link-api"
            },
            "endpoints": {
                "authentication": {
                    "path": "/api/auth",
                    "description": "User authentication and authorization",
                    "routes": {
                        "register": "POST /api/auth/register - Create new user account",
                        "login": "POST /api/auth/login - User login and token generation",
                        "profile": "GET /api/auth/me - Get current user profile",
                        "change_password": "PUT /api/auth/change-password - Update user password"
                    }
                },
                "links": {
                    "path": "/api/links",
                    "description": "URL shortening and link management",
                    "routes": {
                        "create": "POST /api/links - Create shortened link",
                        "list": "GET /api/links - Get all user links",
                        "get": "GET /api/links/{slug} - Get link details",
                        "update": "PUT /api/links/{slug} - Update link settings",
                        "delete": "DELETE /api/links/{slug} - Delete link",
                        "redirect": "GET /{slug} - Redirect to original URL"
                    }
                },
                "domains": {
                    "path": "/api/domains",
                    "description": "Custom domain management",
                    "routes": {
                        "create": "POST /api/domains - Add custom domain",
                        "list": "GET /api/domains - Get user domains",
                        "get": "GET /api/domains/{id} - Get domain details",
                        "update": "PUT /api/domains/{id} - Update domain settings",
                        "delete": "DELETE /api/domains/{id} - Remove domain",
                        "verify": "POST /api/domains/verify - Verify domain ownership"
                    }
                },
                "qr_codes": {
                    "path": "/api/links/{slug}/qr-code",
                    "description": "QR code generation for links",
                    "routes": {
                        "get": "GET /api/links/{slug}/qr-code - Get QR code",
                        "create": "POST /api/links/{slug}/qr-code - Generate QR code",
                        "update": "PUT /api/links/{slug}/qr-code - Update QR code settings"
                    }
                },
                "targeting_rules": {
                    "path": "/api/targeting-rules",
                    "description": "Advanced link targeting and rules",
                    "routes": {
                        "list": "GET /api/links/{slug}/targeting-rules - Get link targeting rules",
                        "create": "POST /api/links/{slug}/targeting-rules - Create targeting rule",
                        "update": "PUT /api/targeting-rules/{id} - Update targeting rule",
                        "delete": "DELETE /api/targeting-rules/{id} - Delete targeting rule"
                    }
                },
                "analytics": {
                    "path": "/api/links/{slug}/stats",
                    "description": "Link analytics and statistics",
                    "routes": {
                        "daily": "GET /api/links/{slug}/stats/daily - Daily click statistics",
                        "summary": "GET /api/links/{slug}/stats/summary - Link performance summary"
                    }
                },
                "clicks": {
                    "path": "/api/links/{slug}/clicks",
                    "description": "Click tracking and data",
                    "routes": {
                        "list": "GET /api/links/{slug}/clicks - Get click history"
                    }
                },
                "rewards": {
                    "path": "/api/rewards",
                    "description": "User rewards and gamification",
                    "routes": {
                        "list": "GET /api/rewards - Get user rewards",
                        "redeem": "POST /api/rewards/redeem - Redeem reward points"
                    }
                }
            },
            "usage": {
                "base_url": "http://127.0.0.1:5000",
                "authentication": "JWT Bearer Token required for protected endpoints",
                "content_type": "application/json",
                "example_usage": {
                    "create_link": "POST /api/links with {\"url\": \"https://example.com\", \"slug\": \"my-link\"}",
                    "get_link": "GET /api/links/my-link",
                    "redirect": "GET /my-link"
                }
            }
        })
    
    # Root-level redirect route for short URLs (must be after API blueprint registration)
    @app.route('/<string:slug>')
    def redirect_short_url(slug):
        """Redirect short URL to original URL - root level for cleaner QR codes"""
        from flask import redirect as flask_redirect
        from .models import Link, Click, LinkDailyStats
        from datetime import datetime
        
        # Find the link
        link = Link.query.filter_by(short_url_slug=slug).first()
        
        if not link or link.is_expired():
            return jsonify({"error": "Link not found or expired"}), 404
        
        # Determine redirect URL
        redirect_url = link.long_url
        
        # For dynamic links, check targeting rules
        if link.is_dynamic and link.targeting_rules:
            rules = sorted(link.targeting_rules, key=lambda x: x.priority)
            rule = rules[0] if rules else None
            if rule:
                redirect_url = rule.redirect_url
        
        # Record the click
        try:
            click = Click(
                link_id=link.link_id,
                hashed_ip=hash(request.remote_addr) if request.remote_addr else None,
                browser=request.user_agent.browser,
                os=request.user_agent.platform,
                referrer=request.referrer
            )
            
            # Update daily stats
            today = datetime.utcnow().date()
            stats = LinkDailyStats.query.filter_by(
                link_id=link.link_id,
                date=today
            ).first()
            
            if not stats:
                stats = LinkDailyStats(link_id=link.link_id, date=today)
                db.session.add(stats)
            
            stats.total_clicks = (stats.total_clicks or 0) + 1
            stats.unique_clicks = (stats.unique_clicks or 0) + 1
            
            db.session.add(click)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            app.logger.error(f"Error recording click: {str(e)}")
        
        return flask_redirect(redirect_url)
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Not found"}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return jsonify({"error": "Internal server error"}), 500
    
    # Import models to ensure they are registered with SQLAlchemy
    from . import models
    
    # Shell context for flask shell
    @app.shell_context_processor
    def make_shell_context():
        return {
            'db': db,
            'User': models.User,
            'Domain': models.Domain,
            'Link': models.Link
        }
    
    return app