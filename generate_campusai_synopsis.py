import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable, Image as RLImage
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfgen import canvas

WORKSPACE = "/Users/kanishksingh/Downloads/momo ai chat bot "
DIAGRAM_DIR = os.path.join(WORKSPACE, "scratch/campusai_diagrams")

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
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#064e3b"))
        self.drawString(54, 841.89 - 36, "G H RAISONI INTERNATIONAL SKILL TECH UNIVERSITY, PUNE")
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        self.drawRightString(595.27 - 54, 841.89 - 36, "CampusAI — Project Synopsis (SY BBA CA)")
        
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(54, 841.89 - 42, 595.27 - 54, 841.89 - 42)

        self.line(54, 45, 595.27 - 54, 45)
        self.drawString(54, 32, "Department of Computer Applications | Academic Year 2026-27")
        self.drawRightString(595.27 - 54, 32, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()

def build_synopsis():
    out_pdf = os.path.join(WORKSPACE, "CampusAI_Project_Synopsis.pdf")
    doc = SimpleDocTemplate(
        out_pdf,
        pagesize=A4,
        leftMargin=54, rightMargin=54, topMargin=54, bottomMargin=54
    )
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'SynTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=20,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#064e3b")
    )
    sub_title = ParagraphStyle(
        'SynSub',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#0f172a")
    )
    center_text = ParagraphStyle(
        'SynCenter',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#334155")
    )
    h1 = ParagraphStyle(
        'SynH1',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor("#064e3b"),
        spaceBefore=8,
        spaceAfter=3,
        keepWithNext=True
    )
    body = ParagraphStyle(
        'SynBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12.5,
        alignment=TA_JUSTIFY,
        textColor=colors.HexColor("#1e293b"),
        spaceAfter=4
    )
    bullet = ParagraphStyle(
        'SynBullet',
        parent=body,
        leftIndent=12,
        bulletIndent=4,
        spaceAfter=2
    )
    th = ParagraphStyle('TH', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8, leading=10, textColor=colors.white, alignment=TA_CENTER)
    td = ParagraphStyle('TD', parent=styles['Normal'], fontName='Helvetica', fontSize=7.8, leading=10, textColor=colors.HexColor("#0f172a"))
    td_b = ParagraphStyle('TDB', parent=td, fontName='Helvetica-Bold')

    story = []

    # =========================================================================
    # HEADER & TITLE BLOCK
    # =========================================================================
    story.append(Paragraph("<b>G H RAISONI INTERNATIONAL SKILL TECH UNIVERSITY, PUNE</b>", title_style))
    story.append(Paragraph("DEPARTMENT OF COMPUTER APPLICATIONS", center_text))
    story.append(Spacer(1, 3))
    story.append(Paragraph("<b>PROJECT SYNOPSIS & PROPOSAL</b>", sub_title))
    story.append(Paragraph("<b>CampusAI: Intelligent College Assistant Chatbot</b>", ParagraphStyle('ProjTitle', parent=sub_title, fontSize=11, textColor=colors.HexColor("#0f766e"))))
    story.append(Paragraph("Submitted in Partial Fulfillment of Bachelor of Business Administration (Computer Applications) — BBA (CA)", center_text))
    story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor("#064e3b"), spaceAfter=8, spaceBefore=4))

    meta_table = [
        [Paragraph("<b>Project Title:</b>", td_b), Paragraph("CampusAI: Intelligent College Assistant Chatbot", td)],
        [Paragraph("<b>Domain & Area:</b>", td_b), Paragraph("Artificial Intelligence, Natural Language Processing & Full-Stack Web Development", td)],
        [Paragraph("<b>Students / Candidates:</b>", td_b), Paragraph("<b>1. Akash Rana</b> (PRN: ISTU25010120004) &nbsp;|&nbsp; <b>2. Shreyash Katke</b> (PRN: ISTU25010120003)", td)],
        [Paragraph("<b>Class & Academic Year:</b>", td_b), Paragraph("S.Y. BBA (Computer Applications) — Semester III &nbsp;|&nbsp; Academic Year: 2026-27", td)],
        [Paragraph("<b>Internal Project Guide:</b>", td_b), Paragraph("<b>Asst. Prof. Sheela Satav</b>, Department of Computer Applications", td)],
        [Paragraph("<b>Core Technology Stack:</b>", td_b), Paragraph("Python 3.11, Flask 3.1.3, SQLite 3, SQLAlchemy ORM, Google Gemini 2.5 Flash API, Web Speech API, HTML5/CSS3/ES6", td)],
    ]
    t_meta = Table(meta_table, colWidths=[125, 362])
    t_meta.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor("#f1f5f9")),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 6))

    # =========================================================================
    # 1. ABSTRACT & INTRODUCTION
    # =========================================================================
    story.append(Paragraph("1. INTRODUCTION & PROJECT OVERVIEW", h1))
    story.append(Paragraph(
        "Collegiate academic environments process thousands of inquiries each academic term regarding admissions criteria, tuition fees, "
        "examination timetables, scholarship programs, syllabus regulations, and hostel facilities. Conventional institutional response "
        "mechanisms—such as physical inquiry windows, telephone switchboards, and email helpdesks—suffer from chronic staffing bottlenecks, "
        "long physical queues, restricted operating hours (10:00 AM – 4:00 PM), and delayed response cycles exceeding 24–48 hours. "
        "<b>CampusAI</b> is an automated, 24/7 web-based artificial intelligence assistant engineered to solve these challenges. "
        "The system deploys a high-performance <b>Dual-Tier Architecture</b>: an indexed local SQLite FAQ repository that resolves verified "
        "institutional questions with sub-15ms latency, backed by Google's state-of-the-art <b>Gemini 2.5 Flash LLM</b> for dynamic contextual reasoning "
        "with an enforced <i>Zero-Hallucination Policy</i> on official dates and fee structures.",
        body
    ))

    # =========================================================================
    # 2. PROBLEM STATEMENT & NEED FOR NEW SYSTEM
    # =========================================================================
    story.append(Paragraph("2. PROBLEM STATEMENT & NEED FOR SYSTEM", h1))
    story.append(Paragraph(
        "<b>Problem Statement:</b> Traditional manual information dissemination in higher educational institutions leads to student frustration, "
        "administrative burnout, and high rates of misinformation. During critical admission and examination windows, administrative staff "
        "spend over 70% of their working hours repeatedly answering the same 25–30 routine questions.<br/>"
        "<b>Need for New System:</b> CampusAI replaces manual counter queuing with an instant, intelligent self-service digital assistant. "
        "By integrating voice read-aloud via the HTML5 Web Speech API, suggestion chips, and an authenticated administrative CRUD portal, "
        "the application ensures that students receive accurate, authoritative answers 24/7 on any device while reducing the administrative counter load.",
        body
    ))

    # =========================================================================
    # 3. PROJECT OBJECTIVES & SCOPE
    # =========================================================================
    story.append(Paragraph("3. PROJECT OBJECTIVES & SCOPE", h1))
    story.append(Paragraph("• <b>Sub-Second Response Delivery:</b> Deliver verified institutional answers in &lt;15ms via local tokenized SQLite indexing.", bullet))
    story.append(Paragraph("• <b>Context-Bounded Generative AI Fallback:</b> Route complex inquiries to Google Gemini 2.5 Flash with strict prompt safety guidelines.", bullet))
    story.append(Paragraph("• <b>Zero-Hallucination Governance:</b> Restrict AI responses to verified institutional data, directing unknown queries to official contacts.", bullet))
    story.append(Paragraph("• <b>Voice Accessibility:</b> Provide client-side Text-to-Speech (TTS) voice synthesis via the Web Speech API.", bullet))
    story.append(Paragraph("• <b>Real-Time Administrative Control:</b> Implement an authenticated web portal (PBKDF2:SHA256) for live CRUD operations on FAQs.", bullet))
    story.append(Paragraph("• <b>Scope Boundaries:</b> Covers 8 institutional categories: Admissions, Fees, Examinations, Placements, Library, Hostels, Timetable, and Scholarships.", bullet))

    # =========================================================================
    # 4. SYSTEM SPECIFICATIONS
    # =========================================================================
    story.append(Paragraph("4. HARDWARE & SOFTWARE SPECIFICATIONS", h1))
    spec_data = [
        [Paragraph("<b>Component</b>", th), Paragraph("<b>Minimum Specification</b>", th), Paragraph("<b>Implemented / Target Environment</b>", th)],
        [Paragraph("Client Hardware", td_b), Paragraph("Dual-Core CPU, 2 GB RAM, 1024x768 Display", td), Paragraph("Standard PC, Laptop, Tablet, or Smartphone", td)],
        [Paragraph("Server Hardware", td_b), Paragraph("Dual-Core 2.0 GHz+, 2 GB RAM, 500 MB Disk", td), Paragraph("Modern Multi-Core Processor, 8 GB RAM, SSD Storage", td)],
        [Paragraph("Operating System", td_b), Paragraph("Windows 10 / macOS 11+ / Ubuntu 20.04+", td), Paragraph("Cross-platform portable (macOS / Linux / Windows)", td)],
        [Paragraph("Backend Framework", td_b), Paragraph("Python 3.8+", td), Paragraph("<b>Python 3.11</b> with <b>Flask 3.1.3</b> WSGI microframework", td)],
        [Paragraph("Database Engine", td_b), Paragraph("Relational SQL RDBMS", td), Paragraph("<b>SQLite 3</b> with SQLAlchemy ORM (ACID Compliant)", td)],
        [Paragraph("AI / LLM Service", td_b), Paragraph("Cloud API Connectivity", td), Paragraph("<b>Google Gemini 2.5 Flash API</b> (Temperature: 0.2)", td)],
        [Paragraph("Frontend Technologies", td_b), Paragraph("HTML5, CSS3, JavaScript (ES6)", td), Paragraph("Semantic HTML5, CSS Flexbox/Grid, Web Speech API", td)],
        [Paragraph("Testing Suite", td_b), Paragraph("Standard Test Runner", td), Paragraph("Python unittest (23 automated test cases, 100% pass)", td)],
    ]
    t_spec = Table(spec_data, colWidths=[110, 175, 202])
    t_spec.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#064e3b")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
    ]))
    story.append(t_spec)


    # =========================================================================
    # 5. SYSTEM ARCHITECTURE & DATA FLOW
    # =========================================================================
    story.append(Paragraph("5. SYSTEM ARCHITECTURE & MODULAR DESIGN", h1))
    story.append(Paragraph(
        "CampusAI utilizes a modular three-tier client-server architecture separating presentation, business application logic, "
        "and data persistence layers:",
        body
    ))
    story.append(Paragraph("• <b>Tier 1 (Presentation Layer):</b> Responsive chat viewport with dynamic message bubbles, category chips, typing indicators, and Web Speech voice controls.", bullet))
    story.append(Paragraph("• <b>Tier 2 (Application & Routing Logic):</b> Flask WSGI service comprising input tokenization, Jaccard similarity matcher ($S \\ge 0.58$), and Gemini 2.5 Flash proxy.", bullet))
    story.append(Paragraph("• <b>Tier 3 (Data Persistence Layer):</b> Normalized SQLite database managing tables for administrators, FAQs, categories, chat message logs, and feedback.", bullet))

    dfd_path = os.path.join(DIAGRAM_DIR, "campusai_dfd.png")
    if os.path.exists(dfd_path):
        story.append(Spacer(1, 4))
        story.append(RLImage(dfd_path, width=470, height=210))
        story.append(Paragraph("<b>Fig 1: Data Flow Diagram (DFD Level 0 & Level 1) of CampusAI</b>", ParagraphStyle('Cap', parent=center_text, fontSize=8, fontName='Helvetica-Bold')))
        story.append(Spacer(1, 4))

    # =========================================================================
    # 6. DATABASE DESIGN & ENTITY RELATIONSHIP
    # =========================================================================
    story.append(Paragraph("6. DATABASE SCHEMA & ENTITIES", h1))
    story.append(Paragraph(
        "The application database is structured in Third Normal Form (3NF) to ensure data integrity and avoid redundancy. "
        "Primary entities include <b>Admin</b> (credential management with PBKDF2 hashing), <b>Category</b> (domain taxonomy), "
        "<b>FAQ</b> (indexed institutional questions and answers), and <b>QueryLog</b> (telemetry and analytics tracking).",
        body
    ))
    er_path = os.path.join(DIAGRAM_DIR, "campusai_er_diagram.png")
    if os.path.exists(er_path):
        story.append(RLImage(er_path, width=470, height=195))
        story.append(Paragraph("<b>Fig 2: Entity-Relationship (ER) Diagram of CampusAI Database</b>", ParagraphStyle('Cap2', parent=center_text, fontSize=8, fontName='Helvetica-Bold')))
        story.append(Spacer(1, 4))

    # =========================================================================
    # 7. METHODOLOGY & SPRINT WORK PLAN
    # =========================================================================
    story.append(Paragraph("7. METHODOLOGY & PROJECT WORK PLAN", h1))
    story.append(Paragraph(
        "The project follows the <b>Agile / Iterative SDLC model</b>, dividing development into four progressive two-week sprints. "
        "This iterative framework allowed rapid prototyping, continuous requirement validation with college stakeholders, and progressive testing.",
        body
    ))
    sprint_data = [
        [Paragraph("<b>Phase / Sprint</b>", th), Paragraph("<b>Key Activities & Milestones</b>", th), Paragraph("<b>Deliverables</b>", th)],
        [Paragraph("Sprint 1: Inception", td_b), Paragraph("Stakeholder interviews, helpdesk logs survey, requirements analysis, SQLite 3NF schema design.", td), Paragraph("SRS & Schema Design", td)],
        [Paragraph("Sprint 2: Core Chatbot", td_b), Paragraph("Flask backend setup, tokenization engine, Jaccard matching ($S \\ge 0.58$), responsive chat UI.", td), Paragraph("Working Local FAQ Chat", td)],
        [Paragraph("Sprint 3: AI & Voice", td_b), Paragraph("Google Gemini 2.5 Flash integration, zero-hallucination prompt guardrails, Web Speech TTS.", td), Paragraph("Hybrid AI & Voice UI", td)],
        [Paragraph("Sprint 4: Admin & QA", td_b), Paragraph("PBKDF2 admin portal, CRUD management, 23 automated unit & integration tests, documentation.", td), Paragraph("Final System & Report", td)],
    ]
    t_sprint = Table(sprint_data, colWidths=[95, 292, 100])
    t_sprint.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#064e3b")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
    ]))
    story.append(t_sprint)
    story.append(Spacer(1, 4))

    # =========================================================================
    # 8. TESTING STRATEGY & RESULTS
    # =========================================================================
    story.append(Paragraph("8. TESTING & QUALITY ASSURANCE", h1))
    story.append(Paragraph(
        "CampusAI incorporates a comprehensive test suite of <b>23 automated test cases</b> built using Python's native <code>unittest</code> framework. "
        "Testing covers unit-level string normalization and similarity thresholds, API endpoint status codes (`/api/chat`, `/api/faqs`), "
        "admin session security (PBKDF2 validation and unauthenticated route redirection), and AI service failure degradation. "
        "<b>Result:</b> All 23 tests execute in 1.28 seconds with a <b>100% pass rate</b>.",
        body
    ))

    # =========================================================================
    # 9. EXPECTED OUTCOMES & FUTURE SCOPE
    # =========================================================================
    story.append(Paragraph("9. EXPECTED OUTCOMES & FUTURE ENHANCEMENTS", h1))
    story.append(Paragraph("• <b>Deliverables:</b> Complete source codebase, SQLite database, 23 automated tests, and 34-page official project report.", bullet))
    story.append(Paragraph("• <b>Institutional Impact:</b> Over 70% reduction in counter queuing; 24/7 student inquiry resolution with zero delay.", bullet))
    story.append(Paragraph("• <b>Future Enhancement 1:</b> Integration with College ERP / Student Information System (SIS) for personal marks and fee dues.", bullet))
    story.append(Paragraph("• <b>Future Enhancement 2:</b> Multilingual conversational capability in Hindi, Marathi, and regional languages.", bullet))
    story.append(Paragraph("• <b>Future Enhancement 3:</b> Deployment as cross-platform mobile app and WhatsApp/Telegram enterprise bot.", bullet))

    # =========================================================================
    # 10. SIGNATURE BLOCK
    # =========================================================================
    story.append(Spacer(1, 15))
    sign_table = [
        [
            Paragraph("____________________________<br/><b>Akash Rana</b><br/>(Candidate 1 — ISTU25010120004)", center_text),
            Paragraph("____________________________<br/><b>Shreyash Katke</b><br/>(Candidate 2 — ISTU25010120003)", center_text),
            Paragraph("____________________________<br/><b>Asst. Prof. Sheela Satav</b><br/>(Internal Project Guide)", center_text)
        ]
    ]
    t_sign = Table(sign_table, colWidths=[162, 162, 163])
    story.append(t_sign)

    doc.build(story, canvasmaker=NumberedCanvasSynopsis)
    print(f"[✓] Project Synopsis PDF built: {out_pdf}")

if __name__ == "__main__":
    build_synopsis()
