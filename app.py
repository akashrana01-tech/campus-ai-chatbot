import os
import json
import secrets
from functools import wraps
from pathlib import Path
from typing import Dict, Any

from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    session,
    redirect,
    url_for,
    Response
)

from config import Config
from models import (
    db,
    User,
    Skill,
    CareerRole,
    Job,
    Resume,
    InterviewTest,
    JobRecommendation
)
from services.career_service import CareerService, DEFAULT_ROADMAPS
from services.interview_service import InterviewService
from services.ai_advisor import AIAdvisorService


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("user_id"):
            if request.path.startswith("/api/"):
                return jsonify({"error": "Authentication required. Please log in."}), 401
            return redirect(url_for("login_page", next=request.path))
        return f(*args, **kwargs)
    return decorated_function


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_id = session.get("user_id")
        if not user_id:
            return redirect(url_for("login_page", next=request.path))
        user = User.query.get(user_id)
        if not user or user.role != "admin":
            return redirect(url_for("dashboard_page"))
        return f(*args, **kwargs)
    return decorated_function


def create_app(config_class=Config):
    """Application factory for CareerPilot AI."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Ensure instance directory exists
    Path(app.config.get("DB_PATH", "instance")).parent.mkdir(parents=True, exist_ok=True)
    db.init_app(app)

    # Initialize AI service
    ai_advisor = AIAdvisorService()

    @app.before_request
    def set_session_csrf():
        if "csrf_token" not in session:
            session["csrf_token"] = secrets.token_hex(24)

    @app.context_processor
    def inject_global_vars():
        current_user = None
        if session.get("user_id"):
            current_user = User.query.get(session.get("user_id"))
        return {
            "current_user": current_user,
            "project_name": app.config.get("PROJECT_NAME", "CareerPilot AI"),
            "institution": app.config.get("INSTITUTION"),
            "department": app.config.get("DEPARTMENT"),
            "academic_year": app.config.get("ACADEMIC_YEAR"),
            "students": app.config.get("STUDENTS"),
            "guide": app.config.get("GUIDE"),
            "ai_active": ai_advisor.is_ai_online(),
            "csrf_token": session.get("csrf_token", ""),
        }

    @app.route("/favicon.ico")
    def favicon():
        svg_icon = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#4f46e5" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>"""
        return Response(svg_icon, mimetype="image/svg+xml")

    # ==========================================
    # HTML Page Routes
    # ==========================================

    @app.route("/")
    def index():
        """Home Screen (Report Page 24)."""
        roles = CareerService.get_all_roles()
        total_jobs = Job.query.count()
        return render_template("index.html", roles=roles, total_jobs=total_jobs)

    @app.route("/guidance")
    def career_guidance_page():
        """Career Guidance Module (Report Page 25)."""
        roles = CareerService.get_all_roles()
        selected_role = request.args.get("role", "Web Developer")
        analysis = CareerService.analyze_skill_gap(
            user_skills=["HTML", "CSS", "JavaScript"],
            target_role_name=selected_role
        )
        return render_template(
            "career_guidance.html",
            roles=roles,
            selected_role=selected_role,
            analysis=analysis
        )

    @app.route("/resume")
    def resume_builder_page():
        """Resume Builder Module (Report Page 25 & 26)."""
        saved_resume = None
        if session.get("user_id"):
            resume_obj = Resume.query.filter_by(user_id=session.get("user_id")).order_by(Resume.resume_id.desc()).first()
            if resume_obj:
                saved_resume = resume_obj.get_content()

        # If no resume saved, populate with Prerna's demo data from report screenshot
        if not saved_resume:
            saved_resume = {
                "personal": {
                    "full_name": "Prerna Fartade",
                    "title": "Frontend Developer",
                    "email": "fartadeprerna@gmail.com",
                    "phone": "+91 98765 43210",
                    "location": "Pune, India",
                    "roll_no": "BC1013"
                },
                "education": {
                    "degree": "BCA in BCA (Science)",
                    "university": "G H Raisoni International Skill Tech University, Pune",
                    "years": "2024 - 2027",
                    "cgpa": "9.18"
                },
                "skills": {
                    "technical": ["javascript", "html", "css", "react", "c++"],
                    "interested_fields": "web development"
                },
                "experience": {
                    "level": "Fresher",
                    "projects": "vaccicare+ (Vaccine portal with modern UI), CareerPilot AI"
                }
            }

        return render_template("resume_builder.html", resume=saved_resume)

    @app.route("/interview")
    def interview_prep_page():
        """Interview Preparation Module (Report Page 13 & 19)."""
        subjects = InterviewService.get_subjects()
        selected_subject = request.args.get("subject", "JAVA")
        questions = InterviewService.get_test_questions(selected_subject)
        
        recent_tests = []
        if session.get("user_id"):
            recent_tests = InterviewTest.query.filter_by(user_id=session.get("user_id")).order_by(InterviewTest.test_id.desc()).limit(5).all()

        return render_template(
            "interview_prep.html",
            subjects=subjects,
            selected_subject=selected_subject,
            questions=questions,
            recent_tests=recent_tests
        )

    @app.route("/jobs")
    def jobs_page():
        """Job Recommendation Module (Report Page 13 & 19)."""
        user = None
        if session.get("user_id"):
            user = User.query.get(session.get("user_id"))

        if user:
            recommendations = CareerService.recommend_jobs_for_user(user)
        else:
            all_jobs = Job.query.all()
            recommendations = [{
                "job": j.to_dict(),
                "match_score": 85.0,
                "matched_skills": [s.strip() for s in j.required_skills.split(",")[:2]],
                "missing_skills": [s.strip() for s in j.required_skills.split(",")[2:]]
            } for j in all_jobs]

        return render_template("jobs.html", recommendations=recommendations)

    @app.route("/dashboard")
    @login_required
    def dashboard_page():
        """Student Dashboard (Report Page 16)."""
        user = User.query.get(session.get("user_id"))
        recent_tests = InterviewTest.query.filter_by(user_id=user.user_id).order_by(InterviewTest.test_id.desc()).all()
        saved_resume = Resume.query.filter_by(user_id=user.user_id).order_by(Resume.resume_id.desc()).first()
        recommendations = CareerService.recommend_jobs_for_user(user)

        return render_template(
            "dashboard.html",
            user=user,
            recent_tests=recent_tests,
            saved_resume=saved_resume.get_content() if saved_resume else None,
            recommendations=recommendations[:3]
        )

    @app.route("/admin")
    @admin_required
    def admin_dashboard_page():
        """Admin Dashboard (Report Page 15 & 16)."""
        users = User.query.all()
        jobs = Job.query.all()
        tests = InterviewTest.query.order_by(InterviewTest.test_id.desc()).limit(20).all()
        resumes = Resume.query.order_by(Resume.resume_id.desc()).limit(20).all()

        return render_template(
            "admin_dashboard.html",
            users=users,
            jobs=jobs,
            tests=tests,
            resumes=resumes,
            total_users=len(users),
            total_jobs=len(jobs),
            total_tests=InterviewTest.query.count()
        )

    @app.route("/login", methods=["GET", "POST"])
    def login_page():
        """Authentication page with demo pre-fill helper."""
        if session.get("user_id"):
            return redirect(url_for("dashboard_page"))

        error = None
        if request.method == "POST":
            email = request.form.get("email", "").strip()
            password = request.form.get("password", "").strip()
            user = User.query.filter_by(email=email).first()

            if user and user.check_password(password):
                session.permanent = True
                session["user_id"] = user.user_id
                session["user_name"] = user.name
                session["user_role"] = user.role

                if user.role == "admin":
                    return redirect(url_for("admin_dashboard_page"))
                return redirect(url_for("dashboard_page"))
            else:
                error = "Invalid email or password. Please verify your credentials."

        return render_template("login.html", error=error)

    @app.route("/register", methods=["POST"])
    def register_user():
        """Register new student."""
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        if not name or not email or not password:
            return render_template("login.html", register_error="All fields are required.")

        if User.query.filter_by(email=email).first():
            return render_template("login.html", register_error="An account with this email already exists.")

        user = User(name=name, email=email, role="student")
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        session["user_id"] = user.user_id
        session["user_name"] = user.name
        session["user_role"] = user.role
        return redirect(url_for("dashboard_page"))

    @app.route("/logout")
    def logout():
        session.clear()
        return redirect(url_for("index"))

    # ==========================================
    # REST API Endpoints
    # ==========================================

    @app.route("/api/health", methods=["GET"])
    def api_health():
        return jsonify({
            "status": "healthy",
            "project": "CareerPilot AI",
            "institution": app.config.get("INSTITUTION"),
            "ai_active": ai_advisor.is_ai_online(),
            "users_count": User.query.count(),
            "jobs_count": Job.query.count()
        }), 200

    @app.route("/api/guidance/analyze", methods=["POST"])
    def api_analyze_guidance():
        data = request.get_json(silent=True) or {}
        user_skills = data.get("skills", [])
        target_role = data.get("target_role", "Web Developer")
        result = CareerService.analyze_skill_gap(user_skills, target_role)
        return jsonify({"success": True, **result}), 200

    @app.route("/api/advisor/chat", methods=["POST"])
    def api_advisor_chat():
        data = request.get_json(silent=True) or {}
        query = data.get("query", "").strip()
        result = ai_advisor.get_advice(query)
        return jsonify({"success": True, **result}), 200

    @app.route("/api/interview/questions", methods=["GET"])
    def api_interview_questions():
        subject = request.args.get("subject", "JAVA")
        questions = InterviewService.get_test_questions(subject)
        return jsonify({"success": True, "subject": subject, "questions": questions}), 200

    @app.route("/api/interview/submit", methods=["POST"])
    def api_interview_submit():
        data = request.get_json(silent=True) or {}
        subject = data.get("subject", "C")
        answers = data.get("answers", {})
        user_id = session.get("user_id")

        evaluation = InterviewService.evaluate_test(subject, answers, user_id=user_id)
        return jsonify({"success": True, **evaluation}), 200

    @app.route("/api/resume/save", methods=["POST"])
    def api_save_resume():
        data = request.get_json(silent=True) or {}
        user_id = session.get("user_id")

        if not user_id:
            # Look up or create demo user
            prerna = User.query.filter_by(email="prerna@gmail.com").first()
            user_id = prerna.user_id if prerna else 1

        resume = Resume(
            user_id=user_id,
            resume_content=json.dumps(data)
        )
        db.session.add(resume)
        db.session.commit()

        return jsonify({
            "success": True,
            "message": "Resume successfully saved to backend database!",
            "resume_id": resume.resume_id
        }), 200

    # Auto-seed database if empty
    with app.app_context():
        db.create_all()
        if User.query.count() == 0 or Job.query.count() == 0:
            try:
                from seed_data import seed_database
                seed_database(app)
            except Exception as e:
                app.logger.warning(f"Auto-seed exception: {e}")

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
