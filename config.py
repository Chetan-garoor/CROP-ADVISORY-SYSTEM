import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Security
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # File Uploads
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    UPLOAD_FOLDER = os.path.join(basedir, 'static/images/uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    
    # Session
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    
    # API Keys (set in .env)
    WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')
    MARKET_API_KEY = os.environ.get('MARKET_API_KEY')
    
    # Model paths
    CROP_MODEL_PATH = os.path.join(basedir, 'models/crop_recommendation.pkl')
    DISEASE_MODEL_PATH = os.path.join(basedir, 'models/disease_detection.h5')
    YIELD_MODEL_PATH = os.path.join(basedir, 'models/yield_prediction.pkl')