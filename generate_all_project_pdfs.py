"""
Generator for additional project PDFs:
1. CampusAI_Project_Synopsis.pdf (Official Project Synopsis for College Submission)
2. CampusAI_Viva_Presentation_Guide.pdf (Viva Voce & Technical Demo Q&A Guide)
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfgen import canvas

TARGET_DIR = "/Users/kanishksingh/Downloads/momo ai chat bot /momo ki topri"

class NumberedCanvasSynopsis(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        self.drawString(54, 841.89 - 36, "CampusAI — Project Synopsis & Proposal (BBA-CA / BCA)")
        self.drawRightString(595.27 - 54, 841.89 - 36, "Academic Submission")
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(54, 841.89 - 42, 595.27 - 54, 841.89 - 42)

        self.line(54, 45, 595.27 - 54, 45)
        self.drawString(54, 32, "Department of Computer Applications | Semester III / IV")
        self.drawRightString(595.27 - 54, 32, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()


def build_synopsis_pdf():
    out_path = os.path.join(TARGET_DIR, "CampusAI_Project_Synopsis.pdf")
    doc = SimpleDocTemplate(
        out_path,
        pagesize=A4,
        leftMargin=54, rightMargin=54, topMargin=54, bottomMargin=54
    )
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'SynTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=22,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#1e1b4b")
    )
    center_text = ParagraphStyle(
        'SynCenter',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#334155")
    )
    h1 = ParagraphStyle(
        'SynH1',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#312e81"),
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )
    body = ParagraphStyle(
        'SynBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13.5,
        alignment=TA_JUSTIFY,
        textColor=colors.HexColor("#1e293b"),
        spaceAfter=5
    )
    bullet = ParagraphStyle(
        'SynBullet',
        parent=body,
        leftIndent=15,
        bulletIndent=5,
        spaceAfter=3
    )
    th = ParagraphStyle('TH', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8, leading=10, textColor=colors.white, alignment=TA_CENTER)
    td = ParagraphStyle('TD', parent=styles['Normal'], fontName='Helvetica', fontSize=8, leading=10, textColor=colors.HexColor("#0f172a"))

    story = []
    story.append(Paragraph("PROJECT SYNOPSIS & PROPOSAL", title_style))
    story.append(Paragraph("<b>CAMPUSAI: AN INTELLIGENT AI-POWERED COLLEGE ASSISTANT CHATBOT</b>", center_text))
    story.append(Spacer(1, 4))
    story.append(Paragraph("Bachelor of Business Administration (Computer Applications) — BBA (CA) / BCA", center_text))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#4f46e5"), spaceAfter=10, spaceBefore=4))

    meta_table = [
        [Paragraph("<b>Project Title:</b>", td), Paragraph("CampusAI: AI College Assistant Chatbot", td)],
        [Paragraph("<b>Domain:</b>", td), Paragraph("Artificial Intelligence & Web Application Development", td)],
        [Paragraph("<b>Students:</b>", td), Paragraph("Kanishk Singh (BBA-CA-301) & Akash Rana (BBA-CA-302)", td)],
        [Paragraph("<b>Project Guide:</b>", td), Paragraph("Prof. [Guide Name], Dept. of Computer Applications", td)],
        [Paragraph("<b>Technologies:</b>", td), Paragraph("Python 3, Flask, SQLite 3, SQLAlchemy, HTML5, CSS3, JavaScript, Gemini API", td)],
    ]
    t_meta = Table(meta_table, colWidths=[120, 367])
    t_meta.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor("#f1f5f9")),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 8))

    story.append(Paragraph("1. INTRODUCTION & PROBLEM CONTEXT", h1))
    story.append(Paragraph(
        "Collegiate administrative offices encounter hundreds of repetitive student inquiries every day concerning admissions, fees, "
        "examinations, course curriculums, and campus facilities. Manual resolution through office counters creates long queues, restricted working hours, "
        "and human fatigue. <b>CampusAI</b> solves this by delivering an automated, 24/7 web assistant that answers student questions instantaneously "
        "while enforcing a strict <i>Zero-Hallucination Policy</i> regarding institutional dates and fees.",
        body
    ))

    story.append(Paragraph("2. PROJECT OBJECTIVES", h1))
    story.append(Paragraph("• Provide 24/7 sub-second inquiry response via natural language processing.", bullet))
    story.append(Paragraph("• Implement a Dual-Tier response pipeline: deterministic FAQ token matching + context-bounded LLM fallback.", bullet))
    story.append(Paragraph("• Build an interactive FAQ directory with category filtering and real-time search.", bullet))
    story.append(Paragraph("• Engineer an authenticated Admin Dashboard for real-time CRUD management of FAQs.", bullet))
    story.append(Paragraph("• Maintain 100% factual accuracy by routing unknown questions to college office contacts.", bullet))

    story.append(Paragraph("3. SYSTEM ARCHITECTURE & KEY MODULES", h1))
    story.append(Paragraph("• <b>Student Chat Module:</b> Conversational UI with question suggestion chips, typing indicator, and clear chat option.", bullet))
    story.append(Paragraph("• <b>Smart FAQ Engine:</b> Tokenizer with punctuation stripping, stop-word filtering, domain synonym expansion, and Jaccard scoring.", bullet))
    story.append(Paragraph("• <b>AI Service Layer:</b> Bounded Gemini LLM fallback with low temperature (0.2) and prompt engineering against hallucination.", bullet))
    story.append(Paragraph("• <b>Admin Governance Portal:</b> Protected by PBKDF2:SHA256 password hashing and session tokens for real-time FAQ management.", bullet))
    story.append(Paragraph("• <b>Database (3NF):</b> Normalized SQLite schema (`admins`, `faqs`, `chat_messages`, `query_logs`).", bullet))

    story.append(Paragraph("4. SYSTEM SPECIFICATIONS", h1))
    spec_data = [
        [Paragraph("<b>Component</b>", th), Paragraph("<b>Minimum Requirement</b>", th), Paragraph("<b>Implemented Technology</b>", th)],
        [Paragraph("Operating System", td), Paragraph("Windows 10 / macOS / Linux", td), Paragraph("Cross-platform (macOS / Linux)", td)],
        [Paragraph("Backend Framework", td), Paragraph("Python 3.8+", td), Paragraph("Python 3.10+ / Flask 3.1.3", td)],
        [Paragraph("Database", td), Paragraph("Relational SQL store", td), Paragraph("SQLite 3 (ACID-compliant, embedded)", td)],
        [Paragraph("Frontend", td), Paragraph("Modern Web Browser", td), Paragraph("HTML5, Responsive CSS3, ES6 JavaScript", td)],
        [Paragraph("Deployment Server", td), Paragraph("WSGI compatible", td), Paragraph("Gunicorn 26.2+ / Render.com Cloud", td)]
    ]
    t_spec = Table(spec_data, colWidths=[120, 180, 187])
    t_spec.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#312e81")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t_spec)

    story.append(Spacer(1, 8))
    story.append(Paragraph("5. TESTING & VERIFICATION SUMMARY", h1))
    story.append(Paragraph(
        "The project was verified through <b>23 automated test cases</b> covering route availability, FAQ keyword searching, "
        "admin login authorization, CRUD lifecycles, and edge-case AI failure degradation. All 23 tests passed with a 100% success rate in 1.185 seconds.",
        body
    ))

    story.append(Spacer(1, 25))
    sign_table = [
        [Paragraph("____________________________<br/><b>Student Signature</b><br/>(Kanishk Singh / Akash Rana)", center_text),
         Paragraph("____________________________<br/><b>Project Guide Signature</b><br/>Prof. [Guide Name]", center_text)]
    ]
    t_sign = Table(sign_table, colWidths=[240, 247])
    story.append(t_sign)

    doc.build(story, canvasmaker=NumberedCanvasSynopsis)
    print(f"[✓] Synopsis PDF built: {out_path}")


def build_viva_guide_pdf():
    out_path = os.path.join(TARGET_DIR, "CampusAI_Viva_Presentation_Guide.pdf")
    doc = SimpleDocTemplate(
        out_path,
        pagesize=A4,
        leftMargin=54, rightMargin=54, topMargin=54, bottomMargin=54
    )
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'VivaTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=22,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#1e1b4b")
    )
    center_text = ParagraphStyle(
        'VivaCenter',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#334155")
    )
    h1 = ParagraphStyle(
        'VivaH1',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#312e81"),
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )
    q_style = ParagraphStyle(
        'VivaQ',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor("#4338ca"),
        spaceBefore=6,
        spaceAfter=2,
        keepWithNext=True
    )
    a_style = ParagraphStyle(
        'VivaA',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        alignment=TA_JUSTIFY,
        textColor=colors.HexColor("#1e293b"),
        spaceAfter=6
    )

    story = []
    story.append(Paragraph("PROJECT VIVA VOCE & TECHNICAL DEMO GUIDE", title_style))
    story.append(Paragraph("<b>CampusAI: Technical Architecture & Top 15 Viva Questions</b>", center_text))
    story.append(Paragraph("Prepared for Final Project Evaluation & External Viva Voce Examination", center_text))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#4f46e5"), spaceAfter=10, spaceBefore=4))

    viva_qa = [
        ("Q1: What is the core problem that CampusAI solves?",
         "Answer: Collegiate administrative offices are overwhelmed by repetitive inquiries regarding admissions, fees, and exams during working hours. CampusAI provides 24/7 instant, verified assistance via natural language, offloading administrative burdens and eliminating student queue delays."),

        ("Q2: What is your project's technology stack and why did you choose it?",
         "Answer: We selected Python with Flask for the backend because it is lightweight, modular, and offers minimal computational overhead. SQLite was selected as an embedded, zero-configuration 3NF relational database. Semantic HTML5, CSS3 Variables, and Vanilla ES6 JavaScript were used for a responsive, high-performance client without heavy Node.js framework overhead."),

        ("Q3: How does your chatbot prevent artificial intelligence hallucinations?",
         "Answer: CampusAI enforces a strict Dual-Tier response architecture. Tier 1 matches queries deterministically against indexed college FAQs in SQLite. If similarity is below 0.45, Tier 2 calls Gemini with a strict system prompt forbidding unverified facts. If the information is not in the knowledge base, the bot politely refers the student to official office contacts rather than fabricating answers."),

        ("Q4: Explain your NLP matching algorithm.",
         "Answer: In services/faq_service.py, raw text is normalized (lowercased, punctuation removed, stop words filtered). Keywords are expanded through an educational synonym dictionary (e.g., 'fee' maps to tuition, cost, payment). It computes token overlap and Jaccard similarity against all stored FAQs. A composite score >= 0.45 returns the verified database answer."),

        ("Q5: What happens if the external AI API is down or there is no internet connection?",
         "Answer: The system is designed with offline resilience. The Chatbot orchestrator wraps the AI service call in a try-except block. If the API fails, times out, or has no API key configured, it gracefully degrades to deterministic local FAQ matching without crashing or throwing HTTP 500 errors."),

        ("Q6: How is the database designed? Is it normalized?",
         "Answer: Yes, the database is normalized to Third Normal Form (3NF). We have separate tables: admins (credentials), faqs (categorized Q&A), chat_messages (chat logs with session UUIDs), and query_logs. All non-key attributes are fully functionally dependent on the primary key, with zero transitive dependencies."),

        ("Q7: How is the administrator authentication secured?",
         "Answer: Passwords are never stored in plaintext. We utilize Werkzeug's PBKDF2:SHA256 password hashing with unique cryptographic salts. User sessions are secured using HTTP-only cookies and validated on every administrative request."),

        ("Q8: How are FAQ changes updated in real-time?",
         "Answer: When an admin creates, edits, or deletes an FAQ via the dashboard, the changes are committed to SQLite via SQLAlchemy transactions. Because the chatbot queries the database dynamically on incoming messages, updates are reflected immediately without restarting the Flask server."),

        ("Q9: What automated testing did you perform?",
         "Answer: We constructed a comprehensive test suite using Python's unittest framework with 23 test cases (TC-01 to TC-23) covering route status, keyword search, admin login, full CRUD lifecycles, and edge-case AI failure fallback. All 23 tests pass with 100% success rate."),

        ("Q10: What are the main limitations and future scope?",
         "Answer: Current limitations include monolingual English NLP and manual FAQ entry. Future scope includes regional language support (Marathi, Hindi), voice/speech synthesis, webhook integration with WhatsApp/Telegram, and integration with the college ERP fee portal.")
    ]

    for q, a in viva_qa:
        story.append(Paragraph(q, q_style))
        story.append(Paragraph(a, a_style))

    doc.build(story, canvasmaker=NumberedCanvasSynopsis)
    print(f"[✓] Viva Guide PDF built: {out_path}")

if __name__ == '__main__':
    build_synopsis_pdf()
    build_viva_guide_pdf()
