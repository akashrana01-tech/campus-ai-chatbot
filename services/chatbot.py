import uuid
from typing import Dict, Any, List
from config import Config
from models import db, ChatMessage, QueryLog, FAQ
from services.faq_service import FAQService, normalize_text
from services.ai_service import AIService

# Common Conversational Intent Map
GREETING_WORDS = {"hi", "hello", "hey", "hola", "greetings", "good morning", "good afternoon", "good evening", "namaste"}
THANKS_WORDS = {"thank you", "thanks", "thx", "appreciate it", "thank you so much", "thank u"}
ABOUT_WORDS = {"who are you", "what are you", "what can you do", "introduce yourself", "help me", "what is this"}
BYE_WORDS = {"bye", "goodbye", "see you", "cya", "have a good day", "exit"}

DEFAULT_SUGGESTIONS = [
    "What courses does the college offer?",
    "How can I apply for admission?",
    "What are the college fees?",
    "When are the examinations?",
    "What facilities are available?",
    "How can I contact the college?",
]

CATEGORY_SUGGESTIONS = {
    "Admissions": [
        "What are the eligibility criteria for BCA/BBA?",
        "What documents are required for admission?",
        "When is the last date to apply for admission?",
    ],
    "Courses": [
        "Tell me about the SYBBA (CA) curriculum",
        "What are the graduation requirements?",
        "Does the college offer internship support?",
    ],
    "Fees": [
        "Can college fees be paid in installments?",
        "What are the payment methods accepted?",
        "Are there any merit scholarships available?",
    ],
    "Examinations": [
        "When is the next semester examination?",
        "How do I download my exam hall ticket?",
        "What are the passing criteria for exams?",
    ],
    "Facilities": [
        "What are the library timings and rules?",
        "Is there a hostel facility for students?",
        "Is high-speed Wi-Fi available on campus?",
    ],
    "General": [
        "What are the college working hours?",
        "What is the official college email address?",
        "What holidays is the college closed?",
    ],
}


class ChatbotService:
    """Orchestrates query parsing, AI generation, FAQ matching, and persistent logging."""

    def __init__(self, ai_service: AIService = None):
        self.ai_service = ai_service or AIService()

    def process_message(self, message: str, session_id: str = None) -> Dict[str, Any]:
        """
        Process student message and generate safe, verified conversational response.
        Returns dictionary with response text, source, confidence, suggestions, and session_id.
        """
        session_id = session_id or str(uuid.uuid4())
        raw_msg = (message or "").strip()

        if not raw_msg:
            return {
                "response": "Please type a question, and I'll be glad to help you find college information!",
                "source": "greeting",
                "confidence": 1.0,
                "suggestions": DEFAULT_SUGGESTIONS[:4],
                "session_id": session_id,
            }

        norm_msg = normalize_text(raw_msg)

        # 1. Check conversational chit-chat / greetings
        if norm_msg in GREETING_WORDS:
            greeting_resp = (
                f"Hello! Welcome to **{Config.COLLEGE_NAME}**.\n\n"
                f"I am CampusAI, your 24/7 college virtual assistant. I can help you with "
                f"admissions, courses, fee structures, exam schedules, campus facilities, and college notices. "
                f"How may I assist you today?"
            )
            self._persist_exchange(session_id, raw_msg, greeting_resp, "greeting", 1.0)
            return {
                "response": greeting_resp,
                "source": "greeting",
                "confidence": 1.0,
                "suggestions": DEFAULT_SUGGESTIONS,
                "session_id": session_id,
            }

        if norm_msg in THANKS_WORDS:
            thanks_resp = (
                "You are very welcome! If you have any more questions about your courses, "
                "fees, exams, or campus life, feel free to ask anytime. Have a wonderful day!"
            )
            self._persist_exchange(session_id, raw_msg, thanks_resp, "greeting", 1.0)
            return {
                "response": thanks_resp,
                "source": "greeting",
                "confidence": 1.0,
                "suggestions": ["What are the college timings?", "What facilities are available?"],
                "session_id": session_id,
            }

        if any(trigger in norm_msg for trigger in ABOUT_WORDS):
            about_resp = (
                f"I am **CampusAI**, an automated virtual assistant developed for **{Config.COLLEGE_NAME}**.\n\n"
                f"Here are some topics you can ask me about:\n"
                f"- **Admissions**: Eligibility, application procedure, dates\n"
                f"- **Courses**: BBA, BCA, SYBBA (CA), B.Com, syllabus details\n"
                f"- **Fees & Payment**: Tuition rates, installment schemes, payment options\n"
                f"- **Examinations**: Timetables, hall tickets, grading policies\n"
                f"- **Campus Facilities**: Library, computer labs, hostel, cafeteria, Wi-Fi\n"
                f"- **College Contact & Timings**: Office hours, phone lines, email addresses\n\n"
                f"How can I help you right now?"
            )
            self._persist_exchange(session_id, raw_msg, about_resp, "greeting", 1.0)
            return {
                "response": about_resp,
                "source": "greeting",
                "confidence": 1.0,
                "suggestions": DEFAULT_SUGGESTIONS[:4],
                "session_id": session_id,
            }

        if norm_msg in BYE_WORDS:
            bye_resp = "Goodbye! Best wishes for your studies at CampusAI. Reach back out anytime you need assistance!"
            self._persist_exchange(session_id, raw_msg, bye_resp, "greeting", 1.0)
            return {
                "response": bye_resp,
                "source": "greeting",
                "confidence": 1.0,
                "suggestions": ["Start a new conversation"],
                "session_id": session_id,
            }

        # 2. Match database FAQs
        best_faq, confidence, candidate_faqs = FAQService.match_best_faq(raw_msg, threshold=0.58)
        kb_context = FAQService.get_context_for_ai(raw_msg, top_k=4)

        # 3. Attempt AI generation if configured
        if self.ai_service.is_available():
            try:
                ai_reply = self.ai_service.generate_response(raw_msg, kb_context)
                if ai_reply:
                    category = best_faq.category if best_faq else "General"
                    suggestions = CATEGORY_SUGGESTIONS.get(category, DEFAULT_SUGGESTIONS)[:3]
                    self._persist_exchange(session_id, raw_msg, ai_reply, "ai", confidence, faq_id=best_faq.id if best_faq else None)
                    return {
                        "response": ai_reply,
                        "source": "ai",
                        "confidence": confidence,
                        "suggestions": suggestions,
                        "session_id": session_id,
                        "faq_id": best_faq.id if best_faq else None,
                    }
            except Exception:
                # Seamless fallback to FAQ matching on AI error
                pass

        # 4. Fallback to FAQ matching if AI is unavailable or failed
        if best_faq and confidence >= 0.58:
            faq_reply = best_faq.answer
            category = best_faq.category
            suggestions = CATEGORY_SUGGESTIONS.get(category, DEFAULT_SUGGESTIONS)[:3]
            self._persist_exchange(session_id, raw_msg, faq_reply, "faq", confidence, faq_id=best_faq.id)
            return {
                "response": faq_reply,
                "source": "faq",
                "confidence": confidence,
                "suggestions": suggestions,
                "session_id": session_id,
                "faq_id": best_faq.id,
            }

        # 5. Polite Fallback for Unknown / Out-of-Scope queries (Never hallucinate!)
        fallback_msg = (
            f"I apologize, but verified information regarding your question is not currently available "
            f"in my knowledge base.\n\n"
            f"To prevent misinformation and ensure you receive accurate, official details, please contact "
            f"the **College Administration Office** directly:\n"
            f"- **Email**: [{Config.COLLEGE_EMAIL}](mailto:{Config.COLLEGE_EMAIL})\n"
            f"- **Phone**: {Config.COLLEGE_PHONE}\n"
            f"- **In-Person**: Administrative Block, Admissions Desk (Ground Floor)\n"
            f"- **Office Hours**: {Config.COLLEGE_HOURS}\n\n"
            f"You can also check our official FAQ directory or rephrase your question using common keywords "
            f"such as *fees*, *admission*, *exam*, *course*, or *timings*."
        )

        self._persist_exchange(session_id, raw_msg, fallback_msg, "fallback", confidence)
        return {
            "response": fallback_msg,
            "source": "fallback",
            "confidence": confidence,
            "suggestions": DEFAULT_SUGGESTIONS[:4],
            "session_id": session_id,
        }

    def _persist_exchange(self, session_id: str, query: str, response: str, status: str, confidence: float, faq_id: int = None):
        """Save query logs and chat messages to SQLite database."""
        try:
            # Store user message
            user_msg = ChatMessage(session_id=session_id, role="user", content=query)
            # Store assistant message
            assistant_msg = ChatMessage(
                session_id=session_id,
                role="assistant",
                content=response,
                matched_by=status,
                faq_id=faq_id
            )
            # Store query log
            query_log = QueryLog(
                session_id=session_id,
                query_text=query,
                response_text=response[:500],  # truncate snippet for log
                status=status,
                confidence=confidence
            )

            db.session.add(user_msg)
            db.session.add(assistant_msg)
            db.session.add(query_log)
            db.session.commit()
        except Exception:
            db.session.rollback()
