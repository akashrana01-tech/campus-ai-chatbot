import os
import re
import logging
from typing import Optional, Dict, Any, List
from config import Config

logger = logging.getLogger(__name__)

CAREER_FAQ_KNOWLEDGE = [
    {
        "keywords": ["bca", "after bca", "scope", "career options", "degree", "opportunities"],
        "answer": (
            "After completing your Bachelor of Computer Applications (BCA) at G H Raisoni International Skill Tech University, "
            "you have several strong career paths:\n\n"
            "1. **Software & Web Development**: Junior Software Engineer, Frontend/React Developer, Backend/Node.js Developer.\n"
            "2. **Data & Analytics**: Data Analyst, Junior Python Developer, Business Intelligence Associate.\n"
            "3. **Cloud & Infrastructure**: Cloud Support Associate, DevOps Trainee, System Administrator.\n"
            "4. **Higher Studies**: MCA (Master of Computer Applications), M.Sc in Data Science / Computer Science, or MBA in IT.\n\n"
            "💡 *Tip: Work on 2-3 end-to-end practical projects and complete our Interview Preparation modules to stand out in campus drives!*"
        )
    },
    {
        "keywords": ["resume", "cv", "fresher", "projects", "template", "format"],
        "answer": (
            "Here are key tips for a winning Fresher Tech Resume:\n\n"
            "- **Clear Contact Details**: Name, professional email, GitHub, LinkedIn, and portfolio link.\n"
            "- **Technical Skills Section**: Categorize into Languages (Java, C++, Python), Web Tech (HTML, CSS, JS, React), and Tools (Git, VS Code, SQL).\n"
            "- **Academic Projects**: Detail 2-3 real projects (like Vaccicare+ or CareerPilot AI) using bullet points: problem solved, tech stack used, and key features.\n"
            "- **Education**: Degree name, University (G H Raisoni), CGPA/Percentage, and graduation year.\n\n"
            "👉 You can use our integrated **Resume Builder** tab to create, preview, and print your resume instantly!"
        )
    },
    {
        "keywords": ["interview", "mcq", "technical round", "prepare", "placement", "crack"],
        "answer": (
            "To crack campus placements and technical interviews:\n\n"
            "1. **Core Language Fundamentals**: Be thorough with OOP concepts in C++ or Java (Polymorphism, Inheritance, Encapsulation).\n"
            "2. **Data Structures**: Practice Arrays, Strings, Linked Lists, Stacks, and Trees.\n"
            "3. **DBMS & SQL**: Understand ACID properties, Normalization (1NF to 3NF), and practice writing Inner/Left joins.\n"
            "4. **Mock Practice**: Use our **Interview Prep** tab to test your speed and accuracy in C, C++, Java, and Web Technologies!"
        )
    },
    {
        "keywords": ["web development", "frontend", "full stack", "react", "html", "javascript"],
        "answer": (
            "To become an industry-ready Full Stack Web Developer:\n\n"
            "- **Stage 1 (Fundamentals)**: Master Semantic HTML5, CSS Flexbox/Grid, and responsive mobile-first design.\n"
            "- **Stage 2 (JavaScript)**: Master modern ES6+, DOM manipulation, asynchronous programming (Promises, async/await), and API integration.\n"
            "- **Stage 3 (Frontend Framework)**: Learn React.js (Component lifecycle, hooks like useState/useEffect, React Router).\n"
            "- **Stage 4 (Backend & DB)**: Learn Node.js with Express, plus MongoDB or MySQL/PostgreSQL for persistent data storage."
        )
    },
    {
        "keywords": ["salary", "package", "packages", "fresher salary", "earn"],
        "answer": (
            "For BCA / B.Sc graduates in Pune and top IT hubs:\n\n"
            "- **Entry-Level Developer**: ₹3.5 LPA - ₹6.5 LPA depending on coding skills and technical test performance.\n"
            "- **Junior Full Stack / React Dev**: ₹4.0 LPA - ₹7.5 LPA.\n"
            "- **Data Analyst Trainee**: ₹4.0 LPA - ₹6.0 LPA.\n\n"
            "Candidates with strong hands-on projects, Git portfolios, and clean coding fundamentals consistently command the higher salary brackets."
        )
    }
]


class AIAdvisorService:
    """Connects to Google Gemini AI API or provides offline career counseling responses."""

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or Config.GEMINI_API_KEY
        self.model = Config.GEMINI_MODEL
        self._client = None

        if self.api_key:
            try:
                from google import genai
                self._client = genai.Client(api_key=self.api_key)
            except Exception as e:
                logger.warning(f"Could not initialize GenAI: {e}")
                self._client = None

    def is_ai_online(self) -> bool:
        return bool(self.api_key and self._client)

    def get_advice(self, user_query: str, user_profile: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Generates contextual career guidance.
        """
        raw = (user_query or "").strip()
        if not raw:
            return {
                "answer": "Please ask a question about careers, roadmaps, technical skills, or interview preparation!",
                "source": "system"
            }

        # 1. Attempt Google Gemini AI if configured
        if self.is_ai_online():
            try:
                system_instruction = (
                    "You are CareerPilot AI, an intelligent, encouraging career advisor developed for "
                    "Bachelor of Computer Applications (Science) students at G H Raisoni International Skill Tech University, Pune. "
                    "Provide clear, concise, actionable advice for tech career planning, roadmaps, resume building, "
                    "and interview preparation. Use clean markdown bullet points."
                )
                prompt = f"{system_instruction}\n\nStudent Question: {raw}\n\nCareerPilot AI Guidance:"
                response = self._client.models.generate_content(
                    model=self.model,
                    contents=prompt
                )
                if response and hasattr(response, "text") and response.text:
                    return {
                        "answer": response.text.strip(),
                        "source": "gemini_ai"
                    }
            except Exception as e:
                logger.warning(f"AI Advisor API error: {e}")

        # 2. Rule-based intelligent offline matcher
        norm_query = raw.lower()
        for item in CAREER_FAQ_KNOWLEDGE:
            if any(k in norm_query for k in item["keywords"]):
                return {
                    "answer": item["answer"],
                    "source": "knowledge_base"
                }

        # 3. Default structured career counseling guidance
        default_answer = (
            f"Here is career guidance from **CareerPilot AI**:\n\n"
            f"For your inquiry regarding *'{raw}'*, we recommend:\n"
            f"1. **Explore Learning Roadmaps**: Check our **Career Guidance** tab to view structured step-by-step milestones for Web Development, Java Software Engineering, and Data Science.\n"
            f"2. **Assess Your Skills**: Test your technical readiness using our **Interview Prep** practice MCQs.\n"
            f"3. **Build Your Resume**: Use the **Resume Builder** to showcase your academic projects and skills to campus recruiters.\n\n"
            f"Have a specific question about roadmaps, salaries, or interview rounds? Ask below!"
        )

        return {
            "answer": default_answer,
            "source": "rule_based"
        }
