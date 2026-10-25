import unittest
from unittest.mock import MagicMock
from app import create_app
from config import TestConfig
from models import db, FAQ, ChatMessage, QueryLog
from seed_data import seed_database
from services.chatbot import ChatbotService
from services.ai_service import AIService


class ChatbotTestCase(unittest.TestCase):
    """Tests for student chatbot NLP processing, FAQ matching, and fallback handling."""

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

    def test_chatbot_greeting_response(self):
        """Conversational greeting like 'hello' should return friendly greeting with 1.0 confidence."""
        with self.app.app_context():
            service = ChatbotService()
            result = service.process_message("hello")
            self.assertEqual(result["source"], "greeting")
            self.assertIn("CampusAI", result["response"])
            self.assertGreater(len(result["suggestions"]), 0)

    def test_chatbot_known_fees_question(self):
        """Questions about college fees should match the fees FAQ."""
        with self.app.app_context():
            service = ChatbotService()
            result = service.process_message("What are the college fees for courses?")
            self.assertEqual(result["source"], "faq")
            self.assertIn("DEMO RECORD", result["response"])
            self.assertIn("fees", result["response"].lower())

    def test_chatbot_known_admissions_question(self):
        """Questions about admission application should match admission FAQ."""
        with self.app.app_context():
            service = ChatbotService()
            result = service.process_message("How do I apply for admission?")
            self.assertEqual(result["source"], "faq")
            self.assertIn("admission", result["response"].lower())

    def test_chatbot_unknown_question_fallback_no_hallucination(self):
        """Unrelated / unknown questions must trigger polite fallback directing to college office."""
        with self.app.app_context():
            service = ChatbotService()
            result = service.process_message("Can I launch a spaceship from the college campus?")
            self.assertEqual(result["source"], "fallback")
            self.assertIn("verified information", result["response"].lower())
            self.assertIn("College Administration Office", result["response"])
            self.assertIn("admin@campusai.edu", result["response"])

    def test_chatbot_api_endpoint(self):
        """POST /api/chat should return a 200 JSON response with answer, source, and suggestions."""
        response = self.client.post("/api/chat", json={
            "message": "When are the examinations conducted?",
            "session_id": "test_session_123"
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data.get("success"))
        self.assertEqual(data.get("source"), "faq")
        self.assertIn("examination", data.get("response").lower())

    def test_chatbot_api_empty_message_validation(self):
        """POST /api/chat with empty message should return 400 Bad Request."""
        response = self.client.post("/api/chat", json={
            "message": "",
            "session_id": "test_session_empty"
        })
        self.assertEqual(response.status_code, 400)

    def test_ai_provider_failure_graceful_fallback(self):
        """When AI service raises an exception or fails, chatbot must gracefully fall back to FAQ matching."""
        with self.app.app_context():
            # Mock AI service that throws an error
            failing_ai = MagicMock(spec=AIService)
            failing_ai.is_available.return_value = True
            failing_ai.generate_response.side_effect = Exception("Simulated API Connection Timeout")

            cb = ChatbotService(ai_service=failing_ai)
            result = cb.process_message("What are the college fees?")

            # Should fall back cleanly to database FAQ match
            self.assertEqual(result["source"], "faq")
            self.assertIn("DEMO RECORD", result["response"])

    def test_faq_update_immediately_reflected_in_chatbot(self):
        """When an admin creates or edits an FAQ, the chatbot should immediately return the new answer."""
        with self.app.app_context():
            # Add brand new custom FAQ
            new_faq = FAQ(
                category="Examinations",
                question="What is the special re-examination timetable for 2026?",
                answer="Special supplementary re-examinations begin on December 15th in Hall B."
            )
            db.session.add(new_faq)
            db.session.commit()

            service = ChatbotService()
            result = service.process_message("When does the special re-examination timetable start?")
            self.assertEqual(result["source"], "faq")
            self.assertIn("December 15th", result["response"])


if __name__ == "__main__":
    unittest.main()
