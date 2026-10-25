import unittest
from app import create_app
from config import TestConfig
from models import db, FAQ
from seed_data import seed_database


class FAQTestCase(unittest.TestCase):
    """Tests for FAQ listing, retrieval, and search endpoints."""

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

    def test_list_all_faqs_api(self):
        """GET /api/faqs should return all seeded FAQs."""
        response = self.client.get("/api/faqs")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data.get("success"))
        self.assertGreaterEqual(data.get("count"), 15)

    def test_filter_faqs_by_category(self):
        """GET /api/faqs?category=Fees should return only fee-related FAQs."""
        response = self.client.get("/api/faqs?category=Fees")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data.get("success"))
        for faq in data.get("faqs"):
            self.assertEqual(faq.get("category"), "Fees")

    def test_search_faqs_by_keyword(self):
        """GET /api/faqs/search?q=fees should match fee questions."""
        response = self.client.get("/api/faqs/search?q=fees")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data.get("success"))
        self.assertGreater(data.get("count"), 0)

    def test_search_faqs_empty_result(self):
        """Search with nonexistent gibberish should return 0 results cleanly."""
        response = self.client.get("/api/faqs/search?q=xyzqwertynonexistentquery123")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data.get("count"), 0)


if __name__ == "__main__":
    unittest.main()
