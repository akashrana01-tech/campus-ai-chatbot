import unittest
import json
from app import create_app
from config import TestConfig
from models import db, User, CareerRole, Job, Resume, InterviewTest
from seed_data import seed_database


class CareerPilotTestCase(unittest.TestCase):
    """Test suite for CareerPilot AI application modules."""

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

    def test_homepage_loads(self):
        """Verify home screen loads with CareerPilot AI title and navigation."""
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"CareerPilot", res.data)
        self.assertIn(b"Welcome to your", res.data)

    def test_guidance_page_loads(self):
        """Verify career guidance page loads with roadmap milestones."""
        res = self.client.get("/guidance")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Web Developer Roadmap", res.data)
        self.assertIn(b"Step 1: Learn HTML, CSS", res.data)

    def test_resume_builder_page_loads(self):
        """Verify resume builder page loads with 4-step wizard and live preview."""
        res = self.client.get("/resume")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Step-by-step Resume Builder", res.data)
        self.assertIn(b"Print Preview", res.data)

    def test_interview_prep_page_loads(self):
        """Verify interview preparation page displays technical MCQs."""
        res = self.client.get("/interview?subject=JAVA")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Technical Test", res.data)

    def test_jobs_page_loads(self):
        """Verify jobs recommendation page renders available industry roles."""
        res = self.client.get("/jobs")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Intelligent Job Recommendations", res.data)

    def test_skill_gap_analysis_api(self):
        """POST /api/guidance/analyze should compute match score and missing skills."""
        payload = {
            "skills": ["HTML", "CSS", "JavaScript"],
            "target_role": "Web Developer"
        }
        res = self.client.post("/api/guidance/analyze", json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data.get("success"))
        self.assertIn("match_percentage", data)
        self.assertIn("acquired_skills", data)
        self.assertIn("missing_skills", data)

    def test_ai_advisor_chat_api(self):
        """POST /api/advisor/chat should return structured career counseling guidance."""
        payload = {"query": "What career options are available after BCA?"}
        res = self.client.post("/api/advisor/chat", json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data.get("success"))
        self.assertIn("answer", data)
        self.assertIn("G H Raisoni", data["answer"])

    def test_interview_test_submission_and_scoring(self):
        """POST /api/interview/submit should evaluate answers and return percentage score."""
        payload = {
            "subject": "C",
            "answers": {
                "1": 1,  # Correct
                "2": 2,  # Correct
                "3": 2,  # Correct
                "4": 1,  # Correct
                "5": 2   # Correct
            }
        }
        res = self.client.post("/api/interview/submit", json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data.get("success"))
        self.assertEqual(data.get("score"), 100)
        self.assertEqual(data.get("result"), "Pass")

    def test_resume_save_api(self):
        """POST /api/resume/save should persist resume content to database."""
        payload = {
            "personal": {"full_name": "Test Student", "title": "Developer"},
            "education": {"degree": "BCA"},
            "skills": {"technical": ["Java", "SQL"]},
            "experience": {"level": "Fresher"}
        }
        res = self.client.post("/api/resume/save", json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data.get("success"))
        self.assertIn("resume_id", data)

    def test_student_authentication(self):
        """Test authentication with pre-seeded student account (Prerna Fartade)."""
        res = self.client.post("/login", data={
            "email": "prerna@gmail.com",
            "password": "Prerna@123"
        }, follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Prerna", res.data)

    def test_guide_admin_access(self):
        """Test admin login with project guide credentials (Prof. Vaishnavi Lokhande)."""
        res = self.client.post("/login", data={
            "email": "guide@raisoni.edu",
            "password": "Admin@123"
        }, follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Admin Control Panel", res.data)


if __name__ == "__main__":
    unittest.main()
