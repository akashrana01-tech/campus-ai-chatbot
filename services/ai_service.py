import os
import logging
from typing import Optional
from config import Config

logger = logging.getLogger(__name__)


class AIService:
    """Service layer connecting to Gemini LLM API with strict grounding in college knowledge base."""

    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        self.api_key = api_key or Config.GEMINI_API_KEY
        self.model = model or Config.GEMINI_MODEL
        self._client = None

        if self.api_key:
            try:
                from google import genai
                self._client = genai.Client(api_key=self.api_key)
            except Exception as e:
                logger.warning(f"Could not initialize Google GenAI client: {e}")
                self._client = None

    def is_available(self) -> bool:
        """Returns True if an AI client is successfully configured."""
        return bool(self.api_key and self._client)

    def generate_response(self, user_query: str, kb_context: str) -> Optional[str]:
        """
        Calls Gemini API with strict system grounding.
        Returns generated answer string, or None if unavailable/failed.
        """
        if not self.is_available():
            return None

        college_name = Config.COLLEGE_NAME
        college_email = Config.COLLEGE_EMAIL
        college_phone = Config.COLLEGE_PHONE

        system_instruction = (
            f"You are CampusAI, the official 24/7 AI student assistant for {college_name}.\n"
            f"Your job is to assist college students with accurate, helpful, and concise answers.\n\n"
            f"STRICT COMPLIANCE RULES:\n"
            f"1. Ground all college-specific facts (such as eligibility criteria, course fees, exam dates, deadlines, "
            f"campus facilities, timings, and contact details) ONLY on the VERIFIED COLLEGE KNOWLEDGE BASE provided below.\n"
            f"2. NEVER invent, guess, or fabricate any numbers, dates, notices, rules, fees, or contact details.\n"
            f"3. If the user's question cannot be answered from the provided knowledge base, or if information is missing "
            f"or uncertain, do NOT guess. Instead, politely inform the student that verified information is unavailable "
            f"and guide them to contact the College Administration Office at {college_email} or {college_phone}.\n"
            f"4. Keep answers friendly, professional, clear, and well-structured with markdown bullet points where helpful.\n"
        )

        full_prompt = (
            f"{system_instruction}\n\n"
            f"{kb_context}\n\n"
            f"Student Question: {user_query}\n\n"
            f"CampusAI Verified Answer:"
        )

        try:
            # Using google-genai Client
            response = self._client.models.generate_content(
                model=self.model,
                contents=full_prompt,
            )
            if response and hasattr(response, "text") and response.text:
                return response.text.strip()
            return None
        except Exception as e:
            # Mask key in logs
            logger.warning(f"AI API request failed: {type(e).__name__}. Falling back to internal FAQ matching.")
            return None
