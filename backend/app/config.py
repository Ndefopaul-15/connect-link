import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_very_secret_key_that_should_be_changed'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///./app.db'
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'super_secret_jwt_key'
    DEFAULT_DOMAIN = os.environ.get('DEFAULT_DOMAIN') or 'https://connect-link.onrender.com'
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class ProductionConfig(Config):
    # In a real application, you would configure production settings here
    # e.g., use a different database, disable debug, etc.
    pass

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
