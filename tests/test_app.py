import unittest
from app import create_app
from config import TestConfig
from models import db, Admin, FAQ
from seed_data import seed_database


class AppTestCase(unittest.TestCase):
    """Tests for basic application routes and health checks."""

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

    def test_homepage_status(self):
        """Verify landing page loads with status 200."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"CampusAI", response.data)
        self.assertIn(b"Your College. Your Questions. Instant Answers.", response.data)

    def test_chat_page_status(self):
        """Verify student chat page loads with status 200."""
        response = self.client.get("/chat")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Student Chatbot", response.data)
        self.assertIn(b"CampusAI Assistant", response.data)

    def test_faqs_page_status(self):
        """Verify FAQ directory page loads with status 200."""
        response = self.client.get("/faqs")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Frequently Asked Questions", response.data)

    def test_admin_login_page_status(self):
        """Verify admin login page loads with status 200."""
        response = self.client.get("/admin/login")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Administrative Portal", response.data)

    def test_api_health(self):
        """Verify health check endpoint returns 200 and healthy status."""
        response = self.client.get("/api/health")
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertEqual(json_data.get("status"), "healthy")
        self.assertGreater(json_data.get("faq_count"), 0)


if __name__ == "__main__":
    unittest.main()
