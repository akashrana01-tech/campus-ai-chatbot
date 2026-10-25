import os
import time
import secrets
from functools import wraps
from pathlib import Path
from typing import Dict

from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    session,
    redirect,
    url_for,
    abort
)
from werkzeug.security import check_password_hash

from config import Config
from models import db, FAQ, Admin, ChatMessage, QueryLog
from services.faq_service import FAQService
from services.chatbot import ChatbotService
from services.ai_service import AIService

# In-memory simple rate limiter: ip -> [(timestamp, count)]
_rate_limits: Dict[str, list] = {}


def check_rate_limit(key: str, max_requests: int = 30, window_seconds: int = 60) -> bool:
    """Returns True if within rate limit, False if limit exceeded."""
    now = time.time()
    timestamps = _rate_limits.get(key, [])
    # Keep only timestamps in current window
    valid_timestamps = [t for t in timestamps if now - t < window_seconds]
    if len(valid_timestamps) >= max_requests:
        _rate_limits[key] = valid_timestamps
        return False
    valid_timestamps.append(now)
    _rate_limits[key] = valid_timestamps
    return True


def admin_required(f):
    """Decorator to protect admin routes."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        admin_id = session.get("admin_id")
        if not admin_id:
            if request.path.startswith("/api/"):
                return jsonify({"error": "Unauthorized access. Please log in as an administrator."}), 401
            return redirect(url_for("admin_login_page", next=request.path))
        
        # Verify admin still exists
        admin = Admin.query.get(admin_id)
        if not admin:
            session.clear()
            if request.path.startswith("/api/"):
                return jsonify({"error": "Admin account not found."}), 401
            return redirect(url_for("admin_login_page"))
        return f(*args, **kwargs)
    return decorated_function


def verify_csrf(f):
    """Decorator to verify CSRF token for state-changing admin API requests."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.method in ["POST", "PUT", "DELETE"]:
            # Check custom header, JSON body, or form data
            token = (
                request.headers.get("X-CSRFToken") or
                (request.is_json and request.json.get("csrf_token")) or
                request.form.get("csrf_token")
            )
            expected = session.get("csrf_token")
            if not expected or token != expected:
                return jsonify({"error": "Invalid or missing CSRF token. Please refresh and try again."}), 403
        return f(*args, **kwargs)
    return decorated_function


def create_app(config_class=Config):
    """Flask Application Factory."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Ensure SQLite instance folder exists
    Path(app.config.get("DB_PATH", "instance")).parent.mkdir(parents=True, exist_ok=True)

    db.init_app(app)

    # Instantiate services
    ai_service = AIService()
    chatbot_service = ChatbotService(ai_service=ai_service)

    @app.before_request
    def set_session_csrf():
        if "csrf_token" not in session:
            session["csrf_token"] = secrets.token_hex(24)

    @app.context_processor
    def inject_global_template_vars():
        return {
            "college_name": app.config.get("COLLEGE_NAME", "CampusAI College"),
            "college_email": app.config.get("COLLEGE_EMAIL", "admin@campusai.edu"),
            "college_phone": app.config.get("COLLEGE_PHONE", "+1-800-555-CAMPUS"),
            "college_address": app.config.get("COLLEGE_ADDRESS", "100 University Ave"),
            "college_hours": app.config.get("COLLEGE_HOURS", "Mon-Fri: 8:30 AM - 5:00 PM"),
            "ai_active": ai_service.is_available(),
            "csrf_token": session.get("csrf_token", ""),
            "current_admin": session.get("admin_username") if session.get("admin_id") else None,
        }

    # ==========================================
    # HTML Page Routes
    # ==========================================

    @app.route("/favicon.ico")
    def favicon():
        """Serve a minimal SVG graduation cap favicon."""
        svg_icon = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#4f46e5" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>"""
        from flask import Response
        return Response(svg_icon, mimetype="image/svg+xml")

    @app.route("/")
    def index():
        """Landing / Home page."""
        popular_faqs = FAQ.query.limit(6).all()
        categories = FAQService.get_categories()
        total_faqs = FAQ.query.count()
        return render_template(
            "index.html",
            popular_faqs=popular_faqs,
            categories=categories,
            total_faqs=total_faqs
        )

    @app.route("/chat")
    def chat_page():
        """Student Chatbot page."""
        initial_query = request.args.get("q", "").strip()
        return render_template("chat.html", initial_query=initial_query)

    @app.route("/faqs")
    def faqs_page():
        """Searchable FAQ directory page."""
        category = request.args.get("category", "All").strip()
        search_query = request.args.get("q", "").strip()
        categories = FAQService.get_categories()
        faqs = FAQService.search_faqs(search_query, category=None if category == "All" else category)
        return render_template(
            "faqs.html",
            faqs=faqs,
            categories=categories,
            selected_category=category,
            search_query=search_query
        )

    @app.route("/admin/login")
    def admin_login_page():
        """Admin login page."""
        if session.get("admin_id"):
            return redirect(url_for("admin_dashboard_page"))
        return render_template("admin_login.html")

    @app.route("/admin/dashboard")
    @admin_required
    def admin_dashboard_page():
        """Admin FAQ management and analytics dashboard."""
        faqs = FAQ.query.order_by(FAQ.id.desc()).all()
        categories = FAQService.get_categories()
        total_faqs = len(faqs)
        total_queries = QueryLog.query.count()
        recent_logs = QueryLog.query.order_by(QueryLog.id.desc()).limit(15).all()
        
        return render_template(
            "admin_dashboard.html",
            faqs=faqs,
            categories=categories,
            total_faqs=total_faqs,
            total_queries=total_queries,
            recent_logs=recent_logs,
            ai_status="Online" if ai_service.is_available() else "Offline (FAQ Fallback)"
        )

    @app.route("/admin/logout")
    def admin_logout():
        """Log out the administrator and redirect to login."""
        session.clear()
        return redirect(url_for("admin_login_page"))

    # ==========================================
    # REST API Endpoints
    # ==========================================

    @app.route("/api/health", methods=["GET"])
    def api_health():
        """Health check endpoint."""
        return jsonify({
            "status": "healthy",
            "app": "CampusAI College Assistant",
            "ai_active": ai_service.is_available(),
            "faq_count": FAQ.query.count(),
        }), 200

    @app.route("/api/faqs", methods=["GET"])
    def api_list_faqs():
        """List FAQs with optional category filter."""
        category = request.args.get("category")
        faqs = FAQService.get_all_faqs(category)
        return jsonify({
            "success": True,
            "count": len(faqs),
            "faqs": [f.to_dict() for f in faqs]
        }), 200

    @app.route("/api/faqs/search", methods=["GET"])
    def api_search_faqs():
        """Search FAQs by query string and optional category filter."""
        q = request.args.get("q", "").strip()
        category = request.args.get("category")
        results = FAQService.search_faqs(q, category=category)
        return jsonify({
            "success": True,
            "query": q,
            "count": len(results),
            "faqs": [f.to_dict() for f in results]
        }), 200

    @app.route("/api/chat", methods=["POST"])
    def api_chat():
        """Student Chat endpoint."""
        client_ip = request.remote_addr or "127.0.0.1"
        if not check_rate_limit(f"chat_{client_ip}", max_requests=app.config.get("CHAT_RATE_LIMIT_PER_MINUTE", 30)):
            return jsonify({
                "error": "Rate limit exceeded. Please wait a moment before sending more messages."
            }), 429

        data = request.get_json(silent=True) or {}
        message = data.get("message", "").strip()
        session_id = data.get("session_id", "").strip()

        if not message:
            return jsonify({
                "error": "Message content cannot be empty."
            }), 400

        result = chatbot_service.process_message(message=message, session_id=session_id)
        return jsonify({
            "success": True,
            **result
        }), 200

    @app.route("/api/admin/login", methods=["POST"])
    def api_admin_login():
        """Authenticate administrator."""
        client_ip = request.remote_addr or "127.0.0.1"
        if not check_rate_limit(f"login_{client_ip}", max_requests=app.config.get("LOGIN_RATE_LIMIT_PER_MINUTE", 10)):
            return jsonify({
                "error": "Too many failed login attempts. Please wait 1 minute."
            }), 429

        data = request.get_json(silent=True) or {}
        username_or_email = data.get("username", "").strip()
        password = data.get("password", "").strip()

        if not username_or_email or not password:
            return jsonify({"error": "Please enter both username/email and password."}), 400

        admin = Admin.query.filter(
            (Admin.username == username_or_email) | (Admin.email == username_or_email)
        ).first()

        if not admin or not admin.check_password(password):
            return jsonify({"error": "Invalid credentials. Please verify username and password."}), 401

        session.permanent = True
        session["admin_id"] = admin.id
        session["admin_username"] = admin.username
        session["admin_email"] = admin.email

        return jsonify({
            "success": True,
            "message": "Login successful.",
            "admin": admin.to_dict(),
            "redirect_url": url_for("admin_dashboard_page")
        }), 200

    @app.route("/api/admin/logout", methods=["POST"])
    def api_admin_logout():
        """Log out administrator."""
        session.clear()
        return jsonify({"success": True, "message": "Logged out successfully."}), 200

    @app.route("/api/admin/stats", methods=["GET"])
    @admin_required
    def api_admin_stats():
        """Return admin analytics and counts."""
        total_faqs = FAQ.query.count()
        total_queries = QueryLog.query.count()
        categories = FAQService.get_categories()
        recent_logs = QueryLog.query.order_by(QueryLog.id.desc()).limit(15).all()

        return jsonify({
            "success": True,
            "total_faqs": total_faqs,
            "total_queries": total_queries,
            "categories": categories,
            "ai_active": ai_service.is_available(),
            "recent_logs": [log.to_dict() for log in recent_logs]
        }), 200

    @app.route("/api/admin/faqs", methods=["POST"])
    @admin_required
    @verify_csrf
    def api_create_faq():
        """Create a new FAQ record."""
        data = request.get_json(silent=True) or {}
        question = data.get("question", "").strip()
        answer = data.get("answer", "").strip()
        category = data.get("category", "General").strip()

        if not question or not answer:
            return jsonify({"error": "Both question and answer fields are required."}), 400

        faq = FAQ(
            question=question,
            answer=answer,
            category=category or "General"
        )
        db.session.add(faq)
        db.session.commit()

        return jsonify({
            "success": True,
            "message": "FAQ created successfully.",
            "faq": faq.to_dict()
        }), 201

    @app.route("/api/admin/faqs/<int:faq_id>", methods=["PUT"])
    @admin_required
    @verify_csrf
    def api_update_faq(faq_id: int):
        """Update an existing FAQ record."""
        faq = FAQ.query.get(faq_id)
        if not faq:
            return jsonify({"error": f"FAQ with ID {faq_id} not found."}), 404

        data = request.get_json(silent=True) or {}
        question = data.get("question", "").strip()
        answer = data.get("answer", "").strip()
        category = data.get("category", "").strip()

        if not question or not answer:
            return jsonify({"error": "Question and answer fields cannot be empty."}), 400

        faq.question = question
        faq.answer = answer
        if category:
            faq.category = category

        db.session.commit()

        return jsonify({
            "success": True,
            "message": "FAQ updated successfully.",
            "faq": faq.to_dict()
        }), 200

    @app.route("/api/admin/faqs/<int:faq_id>", methods=["DELETE"])
    @admin_required
    @verify_csrf
    def api_delete_faq(faq_id: int):
        """Delete an FAQ record."""
        faq = FAQ.query.get(faq_id)
        if not faq:
            return jsonify({"error": f"FAQ with ID {faq_id} not found."}), 404

        db.session.delete(faq)
        db.session.commit()

        return jsonify({
            "success": True,
            "message": f"FAQ #{faq_id} deleted successfully."
        }), 200

    # Auto-initialize database tables and seed if database is empty
    with app.app_context():
        db.create_all()
        # Seed default admin if missing
        if Admin.query.count() == 0 or FAQ.query.count() == 0:
            try:
                from seed_data import seed_database
                seed_database(app)
            except Exception as e:
                app.logger.warning(f"Auto-seed exception: {e}")

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
