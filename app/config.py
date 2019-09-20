"""Flask config class."""
import os

class Config:
    """
    Base Configuration Vars
    """
    DEBUG = False
    TESTING = True
    DATABASE_URI = os.environ.get('LOCAL_DATABASE_URI')

class Production(Config):
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.environ.get('PRODUCTION_DATABASE_URI')

class Staging(Config):
    DEBUG = False
    TESTING = True
    DATABASE_URI = os.environ.get('STAGING_DATABASE_URI')

class Local(Config):
    DEBUG = True
    TESTING = True
    DATABASE_URI = os.environ.get('LOCAL_DATABASE_URI')
