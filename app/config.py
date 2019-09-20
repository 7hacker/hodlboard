"""Flask config class."""
import os

class Config:
    """
    Base Configuration Vars
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')

class Production(Config):
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.environ.get('PRODUCTION_DATABASE_URI')

class Staging(Config):
    DEBUG = True
    TESTING = True
    DATABASE_URI = os.environ.get('STAGING_DATABASE_URI')
