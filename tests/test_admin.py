import unittest
from app import create_app
from config import TestConfig
from models import db, Admin, FAQ
from seed_data import seed_database


class AdminTestCase(unittest.TestCase):
    """Tests for Admin authentication, session protection, and FAQ CRUD management."""

    def setUp(self):
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            seed_database(self.app)

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_successful_admin_login(self):
        """Admin login with correct credentials should succeed."""
        response = self.client.post("/api/admin/login", json={
            "username": "admin",
            "password": "Admin@123"
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data.get("success"))
        self.assertEqual(data["admin"]["username"], "admin")

    def test_unsuccessful_admin_login_wrong_password(self):
        """Admin login with wrong password should return 401."""
        response = self.client.post("/api/admin/login", json={
            "username": "admin",
            "password": "WrongPassword999"
        })
        self.assertEqual(response.status_code, 401)
        data = response.get_json()
        self.assertIn("error", data)

    def test_unsuccessful_admin_login_empty_fields(self):
        """Admin login with empty fields should return 400."""
        response = self.client.post("/api/admin/login", json={
            "username": "",
            "password": ""
        })
        self.assertEqual(response.status_code, 400)

    def test_protected_dashboard_redirects_unauthenticated(self):
        """Accessing /admin/dashboard without active session should redirect to /admin/login."""
        response = self.client.get("/admin/dashboard")
        self.assertEqual(response.status_code, 302)
        self.assertIn("/admin/login", response.headers.get("Location"))

    def test_protected_api_route_unauthenticated(self):
        """Calling /api/admin/stats without authentication should return 401."""
        response = self.client.get("/api/admin/stats")
        self.assertEqual(response.status_code, 401)

    def _login_as_admin(self):
        """Helper to establish admin session and obtain CSRF token."""
        # Visit page to set session CSRF
        self.client.get("/admin/login")
        self.client.post("/api/admin/login", json={
            "username": "admin",
            "password": "Admin@123"
        })
        with self.client.session_transaction() as sess:
            return sess.get("csrf_token")

    def test_admin_faq_crud_lifecycle(self):
        """Full test of FAQ creation, updating, and deletion by authenticated admin."""
        csrf_token = self._login_as_admin()
        headers = {"X-CSRFToken": csrf_token}

        # 1. CREATE FAQ
        create_payload = {
            "question": "What is the dress code on campus?",
            "answer": "Casual but formal attire on Mondays and during university presentations.",
            "category": "General",
            "csrf_token": csrf_token
        }
        res_create = self.client.post("/api/admin/faqs", json=create_payload, headers=headers)
        self.assertEqual(res_create.status_code, 201)
        created_data = res_create.get_json()
        self.assertTrue(created_data.get("success"))
        faq_id = created_data["faq"]["id"]
        self.assertEqual(created_data["faq"]["question"], create_payload["question"])

        # 2. UPDATE FAQ
        update_payload = {
            "question": "What is the updated college dress code?",
            "answer": "Smart casual attire is permitted throughout the week.",
            "category": "General",
            "csrf_token": csrf_token
        }
        res_update = self.client.put(f"/api/admin/faqs/{faq_id}", json=update_payload, headers=headers)
        self.assertEqual(res_update.status_code, 200)
        updated_data = res_update.get_json()
        self.assertEqual(updated_data["faq"]["question"], update_payload["question"])

        # 3. VERIFY IN DATABASE
        with self.app.app_context():
            faq_db = FAQ.query.get(faq_id)
            self.assertIsNotNone(faq_db)
            self.assertEqual(faq_db.question, update_payload["question"])

        # 4. DELETE FAQ
        res_delete = self.client.delete(f"/api/admin/faqs/{faq_id}", headers=headers)
        self.assertEqual(res_delete.status_code, 200)
        delete_data = res_delete.get_json()
        self.assertTrue(delete_data.get("success"))

        # 5. VERIFY DELETED
        with self.app.app_context():
            faq_db_after = FAQ.query.get(faq_id)
            self.assertIsNone(faq_db_after)


if __name__ == "__main__":
    unittest.main()
