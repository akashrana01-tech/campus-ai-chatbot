from datetime import datetime
import json
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

# Association table for User <-> Skills (Many-to-Many)
user_skills = db.Table(
    "user_skills",
    db.Column("user_id", db.Integer, db.ForeignKey("users.user_id"), primary_key=True),
    db.Column("skill_id", db.Integer, db.ForeignKey("skills.skill_id"), primary_key=True)
)

# Association table for User <-> Career Roles (Many-to-Many)
user_career_preference = db.Table(
    "user_career_preference",
    db.Column("user_id", db.Integer, db.ForeignKey("users.user_id"), primary_key=True),
    db.Column("career_id", db.Integer, db.ForeignKey("career_roles.career_id"), primary_key=True)
)


class User(db.Model):
    """User account model (Report Page 11)."""
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default="student")  # 'student' or 'admin'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    skills = db.relationship("Skill", secondary=user_skills, backref=db.backref("users", lazy="dynamic"))
    preferred_careers = db.relationship("CareerRole", secondary=user_career_preference, backref=db.backref("interested_users", lazy="dynamic"))
    resumes = db.relationship("Resume", backref="user", cascade="all, delete-orphan", lazy="dynamic")
    test_results = db.relationship("InterviewTest", backref="user", cascade="all, delete-orphan", lazy="dynamic")
    recommendations = db.relationship("JobRecommendation", backref="user", cascade="all, delete-orphan", lazy="dynamic")

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "role": self.role,
            "skills": [s.skill_name for s in self.skills],
        }


class Skill(db.Model):
    """Skills reference table (Report Page 11)."""
    __tablename__ = "skills"

    skill_id = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String(80), unique=True, nullable=False, index=True)

    def to_dict(self):
        return {"skill_id": self.skill_id, "skill_name": self.skill_name}


class CareerRole(db.Model):
    """Career Roles and Roadmaps table (Report Page 12)."""
    __tablename__ = "career_roles"

    career_id = db.Column(db.Integer, primary_key=True)
    career_name = db.Column(db.String(100), unique=True, nullable=False, index=True)
    description = db.Column(db.Text, nullable=True)
    required_skills = db.Column(db.String(255), nullable=True)  # Comma-separated
    roadmap_json = db.Column(db.Text, nullable=True)  # JSON steps for timeline

    # Relationships
    jobs = db.relationship("Job", backref="career_role", lazy="dynamic")

    def get_roadmap(self):
        try:
            return json.loads(self.roadmap_json) if self.roadmap_json else []
        except Exception:
            return []

    def to_dict(self):
        return {
            "career_id": self.career_id,
            "career_name": self.career_name,
            "description": self.description,
            "required_skills": [s.strip() for s in (self.required_skills or "").split(",") if s.strip()],
            "roadmap": self.get_roadmap(),
        }


class Resume(db.Model):
    """User Resumes table (Report Page 12)."""
    __tablename__ = "resumes"

    resume_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    resume_content = db.Column(db.Text, nullable=False)  # JSON serialized resume structure
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def get_content(self):
        try:
            return json.loads(self.resume_content)
        except Exception:
            return {}

    def to_dict(self):
        return {
            "resume_id": self.resume_id,
            "user_id": self.user_id,
            "content": self.get_content(),
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M") if self.created_at else None,
        }


class Job(db.Model):
    """Jobs available for recommendation (Report Page 13)."""
    __tablename__ = "jobs"

    job_id = db.Column(db.Integer, primary_key=True)
    career_id = db.Column(db.Integer, db.ForeignKey("career_roles.career_id"), nullable=True)
    job_title = db.Column(db.String(120), nullable=False)
    company_name = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    required_skills = db.Column(db.String(255), nullable=False)  # e.g. "HTML, CSS, JavaScript, React"
    salary_range = db.Column(db.String(60), default="₹4.5 - ₹7.0 LPA")
    experience_level = db.Column(db.String(50), default="Fresher / 0-1 yr")

    def to_dict(self):
        return {
            "job_id": self.job_id,
            "career_id": self.career_id,
            "job_title": self.job_title,
            "company_name": self.company_name,
            "location": self.location,
            "required_skills": [s.strip() for s in self.required_skills.split(",") if s.strip()],
            "salary_range": self.salary_range,
            "experience_level": self.experience_level,
        }


class InterviewTest(db.Model):
    """Mock test results (Report Page 13)."""
    __tablename__ = "interview_tests"

    test_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    subject = db.Column(db.String(50), nullable=False)  # C, C++, Java, HTML, Python, SQL
    score = db.Column(db.Integer, nullable=False)
    total_questions = db.Column(db.Integer, default=5)
    result = db.Column(db.String(20), default="Pass")  # 'Pass' | 'Fail'
    test_date = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "test_id": self.test_id,
            "user_id": self.user_id,
            "subject": self.subject,
            "score": self.score,
            "total_questions": self.total_questions,
            "result": self.result,
            "test_date": self.test_date.strftime("%Y-%m-%d %H:%M") if self.test_date else None,
        }


class JobRecommendation(db.Model):
    """Job Recommendations with calculated match score (Report Page 13)."""
    __tablename__ = "job_recommendations"

    recommendation_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey("jobs.job_id"), nullable=False)
    match_score = db.Column(db.Float, nullable=False)  # 0.0 to 100.0

    # Relationship
    job = db.relationship("Job")

    def to_dict(self):
        return {
            "recommendation_id": self.recommendation_id,
            "user_id": self.user_id,
            "job": self.job.to_dict() if self.job else None,
            "match_score": round(self.match_score, 1),
        }
