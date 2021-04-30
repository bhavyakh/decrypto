"""Flask configuration."""
import os


class Config:
    """Base config."""
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
