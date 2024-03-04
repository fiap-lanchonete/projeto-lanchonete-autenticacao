import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True
