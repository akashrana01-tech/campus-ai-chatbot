import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
INSTANCE_DIR = BASE_DIR / "instance"
INSTANCE_DIR.mkdir(parents=True, exist_ok=True)

load_dotenv(BASE_DIR / ".env")


class Config:
    """Application configuration for CareerPilot AI."""
    PROJECT_NAME = "CareerPilot AI"
    INSTITUTION = "G H Raisoni International Skill Tech University, Pune"
    DEPARTMENT = "Bachelor of Computer Applications (Science)"
    ACADEMIC_YEAR = "2025-26"
    STUDENTS = "Prerna Fartade (BC1013) & Shubham Panchal (BC1029)"
    GUIDE = "Prof. Vaishnavi Lokhande"

    SECRET_KEY = os.environ.get("SECRET_KEY", "careerpilot-ai-secret-key-2026")

    # SQLite Database
    DB_PATH = INSTANCE_DIR / "careerpilot.db"
    _env_db = os.environ.get("DATABASE_URI")
    SQLALCHEMY_DATABASE_URI = _env_db if _env_db and _env_db.startswith("sqlite:////") else f"sqlite:///{DB_PATH}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Session Security
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    PERMANENT_SESSION_LIFETIME = 3600 * 8  # 8 hours

    # AI Service Settings
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()
    GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-3.8-flash")


class TestConfig(Config):
    """Configuration for automated tests."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False
    SECRET_KEY = "test-secret-key"
