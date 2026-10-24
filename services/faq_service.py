import re
import difflib
from typing import List, Dict, Tuple, Optional
from models import FAQ, db

# Common English stop words
STOP_WORDS = {
    "a", "about", "an", "and", "are", "as", "at", "be", "by", "can", "could",
    "do", "does", "for", "from", "has", "have", "how", "i", "if", "in", "is",
    "it", "my", "of", "on", "or", "our", "tell", "that", "the", "there",
    "this", "to", "was", "we", "what", "when", "where", "which", "who", "will",
    "with", "would", "you", "your", "please", "want", "know", "give", "me"
}

# Domain synonym maps for college information queries
SYNONYM_GROUPS = [
    {"fee", "fees", "cost", "tuition", "payment", "installment", "scholarship", "dues", "charges", "pay"},
    {"admission", "admissions", "apply", "application", "enroll", "enrollment", "eligibility", "criteria", "cutoff"},
    {"course", "courses", "program", "programs", "degrees", "degree", "bba", "bca", "sybba", "bcom", "bsc", "syllabus", "curriculum", "subject", "subjects"},
    {"exam", "exams", "examination", "examinations", "schedule", "timetable", "dates", "date", "hallticket", "results", "midterm", "finals"},
    {"timing", "timings", "hours", "time", "schedule", "opening", "closing", "open", "close"},
    {"holiday", "holidays", "vacation", "vacations", "closed", "off", "leave", "calendar"},
    {"facility", "facilities", "library", "hostel", "canteen", "cafeteria", "lab", "labs", "laboratory", "gym", "wifi", "sports", "transport"},
    {"contact", "phone", "email", "address", "location", "helpline", "reach", "office", "desk", "number", "call"},
    {"placement", "placements", "jobs", "internship", "internships", "recruiters", "packages", "career"}
]


def normalize_text(text: str) -> str:
    """Normalize text by lowercasing, stripping punctuation, and compressing spaces."""
    if not text:
        return ""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return " ".join(text.split())


def extract_keywords(text: str) -> List[str]:
    """Tokenize and remove stop words."""
    tokens = normalize_text(text).split()
    return [t for t in tokens if t not in STOP_WORDS and len(t) > 1]


def compute_similarity(query: str, target: str) -> float:
    """
    Compute multi-signal similarity score between query and FAQ question:
    1. Exact normalized match = 1.0
    2. Substring containment = 0.90
    3. Token coverage + synonym matching
    4. F1 overlap score
    5. SequenceMatcher character-level alignment
    """
    norm_query = normalize_text(query)
    norm_target = normalize_text(target)

    if not norm_query or not norm_target:
        return 0.0

    if norm_query == norm_target:
        return 1.0

    q_keywords = extract_keywords(norm_query)
    t_keywords = extract_keywords(norm_target)

    if not q_keywords or not t_keywords:
        return difflib.SequenceMatcher(None, norm_query, norm_target).ratio()

    # Substring check on full keyword sequence
    q_str = " ".join(q_keywords)
    t_str = " ".join(t_keywords)
    if q_str in t_str:
        return 0.92
    if t_str in q_str:
        return 0.88

    q_set = set(q_keywords)
    t_set = set(t_keywords)

    # Calculate token match coverage with bounded synonym credit
    matched_q = 0.0
    for q in q_set:
        if q in t_set:
            matched_q += 1.0
        else:
            for group in SYNONYM_GROUPS:
                if q in group and any(t in group for t in t_set):
                    matched_q += 0.85
                    break

    q_coverage = matched_q / len(q_set)
    t_coverage = matched_q / len(t_set)
    f1 = (2 * q_coverage * t_coverage) / (q_coverage + t_coverage) if (q_coverage + t_coverage) > 0 else 0.0
    seq = difflib.SequenceMatcher(None, q_str, t_str).ratio()

    combined_score = (q_coverage * 0.45) + (f1 * 0.35) + (seq * 0.20)
    return min(1.0, max(0.0, combined_score))


class FAQService:
    """Encapsulates FAQ retrieval, searching, and similarity matching against the database."""

    @staticmethod
    def get_all_faqs(category: Optional[str] = None) -> List[FAQ]:
        """Fetch all FAQs, optionally filtered by category."""
        query = FAQ.query
        if category and category.lower() != "all":
            query = query.filter(FAQ.category.ilike(category))
        return query.order_by(FAQ.id.asc()).all()

    @staticmethod
    def get_faq_by_id(faq_id: int) -> Optional[FAQ]:
        """Fetch single FAQ by ID."""
        return FAQ.query.get(faq_id)

    @staticmethod
    def get_categories() -> List[Dict[str, any]]:
        """Return distinct categories along with FAQ count."""
        results = db.session.query(FAQ.category, db.func.count(FAQ.id)).group_by(FAQ.category).all()
        categories = [{"name": cat, "count": count} for cat, count in results]
        existing_names = {c["name"].lower() for c in categories}
        defaults = ["Admissions", "Courses", "Fees", "Examinations", "Facilities", "General"]
        for d in defaults:
            if d.lower() not in existing_names:
                categories.append({"name": d, "count": 0})
        return sorted(categories, key=lambda x: x["name"])

    @staticmethod
    def search_faqs(query_str: str, category: Optional[str] = None) -> List[FAQ]:
        """Search FAQs by query string and optional category filter."""
        all_faqs = FAQService.get_all_faqs(category=category)
        if not query_str or not query_str.strip():
            return all_faqs

        scored = []
        norm_q = normalize_text(query_str)
        q_keywords = set(extract_keywords(norm_q))

        for faq in all_faqs:
            q_score = compute_similarity(query_str, faq.question)
            
            # Answer content keyword match
            ans_keywords = set(extract_keywords(normalize_text(faq.answer)))
            ans_score = len(q_keywords.intersection(ans_keywords)) / len(q_keywords) if q_keywords else 0.0

            score = max(q_score, ans_score * 0.75)

            if norm_q and (norm_q in normalize_text(faq.question) or norm_q in normalize_text(faq.answer)):
                score = max(score, 0.80)

            if score >= 0.28:
                scored.append((score, faq))

        scored.sort(key=lambda x: x[0], reverse=True)
        return [faq for _, faq in scored]

    @staticmethod
    def match_best_faq(query_str: str, threshold: float = 0.58) -> Tuple[Optional[FAQ], float, List[FAQ]]:
        """
        Find the single best matching FAQ for a natural language user query.
        Returns (best_faq, confidence, top_candidates).
        """
        all_faqs = FAQ.query.all()
        if not all_faqs:
            return None, 0.0, []

        scored = []
        for faq in all_faqs:
            q_score = compute_similarity(query_str, faq.question)
            scored.append((q_score, faq))

        scored.sort(key=lambda x: x[0], reverse=True)
        top_candidates = [item[1] for item in scored[:3] if item[0] >= 0.35]

        best_score, best_faq = scored[0]
        if best_score >= threshold:
            return best_faq, best_score, top_candidates

        return None, best_score, top_candidates

    @staticmethod
    def get_context_for_ai(query_str: str, top_k: int = 5) -> str:
        """
        Build structured context from top relevant FAQs to pass into the AI LLM prompt.
        """
        all_faqs = FAQ.query.all()
        if not all_faqs:
            return "No official FAQ records currently available in the database."

        scored = []
        for faq in all_faqs:
            score = compute_similarity(query_str, faq.question)
            scored.append((score, faq))

        scored.sort(key=lambda x: x[0], reverse=True)
        top_faqs = [item[1] for item in scored[:top_k]]

        lines = ["=== VERIFIED COLLEGE KNOWLEDGE BASE RECORDS ==="]
        for idx, faq in enumerate(top_faqs, 1):
            lines.append(f"\n[Record #{idx} - Category: {faq.category}]")
            lines.append(f"Question: {faq.question}")
            lines.append(f"Official Answer: {faq.answer}")
        lines.append("\n================================================")
        return "\n".join(lines)
