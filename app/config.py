import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-12345'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///security_app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_FILE_PATH = 'logs/app.log'