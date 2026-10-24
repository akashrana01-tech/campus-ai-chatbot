import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
INSTANCE_DIR = BASE_DIR / "instance"
INSTANCE_DIR.mkdir(parents=True, exist_ok=True)

load_dotenv(BASE_DIR / ".env")


class Config:
    """Base application configuration."""
    SECRET_KEY = os.environ.get("SECRET_KEY", "campusai-dev-secret-key-2026")
    
    # SQLite Database configuration - use absolute path to handle directory spaces safely
    DB_PATH = INSTANCE_DIR / "campus_assistant.db"
    _env_db = os.environ.get("DATABASE_URI")
    SQLALCHEMY_DATABASE_URI = _env_db if _env_db and _env_db.startswith("sqlite:////") else f"sqlite:///{DB_PATH}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Session Security
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    PERMANENT_SESSION_LIFETIME = 3600 * 4  # 4 hours
    
    # AI Service Settings
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()
    GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-3.8-flash")
    
    # College Metadata (Customizable via environment variables)
    COLLEGE_NAME = os.environ.get("COLLEGE_NAME", "CampusAI College of Arts, Science & Technology")
    COLLEGE_EMAIL = os.environ.get("COLLEGE_EMAIL", "admin@campusai.edu")
    COLLEGE_PHONE = os.environ.get("COLLEGE_PHONE", "+1-800-555-CAMPUS")
    COLLEGE_ADDRESS = os.environ.get("COLLEGE_ADDRESS", "100 University Avenue, Academic Hills, NY 10001")
    COLLEGE_HOURS = os.environ.get("COLLEGE_HOURS", "Monday - Friday: 8:30 AM - 5:00 PM | Saturday: 9:00 AM - 1:00 PM")
    
    # Rate Limiting Settings
    CHAT_RATE_LIMIT_PER_MINUTE = 30
    LOGIN_RATE_LIMIT_PER_MINUTE = 10


class TestConfig(Config):
    """Configuration for unit and integration testing."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False
    SECRET_KEY = "test-secret-key"
