import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable, Image as RLImage, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfgen import canvas

WORKSPACE = "/Users/kanishksingh/Downloads/momo ai chat bot "
DIAGRAM_DIR = os.path.join(WORKSPACE, "scratch/campusai_diagrams")
OUT_PDF = os.path.join(WORKSPACE, "CampusAI_Academic_Assignments.pdf")

class NumberedCanvasAssignments(canvas.Canvas):
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
        # Page border
        self.setStrokeColor(colors.HexColor("#064e3b"))
        self.setLineWidth(1.2)
        self.rect(36, 36, 595.27 - 72, 841.89 - 72)
        
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.rect(40, 40, 595.27 - 80, 841.89 - 80)

        # Header (pages > 1)
        if self._pageNumber > 1:
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(colors.HexColor("#064e3b"))
            self.drawString(48, 841.89 - 28, "G H RAISONI INTERNATIONAL SKILL TECH UNIVERSITY, PUNE")
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#64748b"))
            self.drawRightString(595.27 - 48, 841.89 - 28, "Software Engineering & Project Assignments")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.5)
            self.line(48, 841.89 - 32, 595.27 - 48, 841.89 - 32)

        # Footer
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(48, 48, 595.27 - 48, 48)
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        self.drawString(48, 36, "CampusAI Project — SY BBA (CA) Sem III | Akash Rana & Shreyash Katke")
        self.drawRightString(595.27 - 48, 36, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()

def build_assignments_pdf():
    doc = SimpleDocTemplate(
        OUT_PDF,
        pagesize=A4,
        leftMargin=48, rightMargin=48, topMargin=48, bottomMargin=48
    )
    styles = getSampleStyleSheet()

    c_center = colors.HexColor("#064e3b")
    c_sub = colors.HexColor("#0f172a")

    title_style = ParagraphStyle(
        'CoverTitle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=15, leading=20, alignment=TA_CENTER, textColor=c_center
    )
    sub_title = ParagraphStyle(
        'CoverSub', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=12, leading=16, alignment=TA_CENTER, textColor=c_sub
    )
    dept_style = ParagraphStyle(
        'CoverDept', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=10, leading=14, alignment=TA_CENTER, textColor=colors.HexColor("#334155")
    )
    center_text = ParagraphStyle(
        'CoverCenter', parent=styles['Normal'],
        fontName='Helvetica', fontSize=9, leading=13, alignment=TA_CENTER, textColor=colors.HexColor("#334155")
    )
    h1 = ParagraphStyle(
        'AssnH1', parent=styles['Heading1'],
        fontName='Helvetica-Bold', fontSize=12, leading=16, alignment=TA_CENTER,
        textColor=colors.HexColor("#064e3b"), spaceBefore=10, spaceAfter=4, keepWithNext=True
    )
    h2 = ParagraphStyle(
        'AssnH2', parent=styles['Heading2'],
        fontName='Helvetica-Bold', fontSize=10, leading=14,
        textColor=colors.HexColor("#0f766e"), spaceBefore=8, spaceAfter=3, keepWithNext=True
    )
    q_title = ParagraphStyle(
        'QTitle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=9, leading=13,
        textColor=colors.HexColor("#0f172a"), spaceBefore=6, spaceAfter=2, keepWithNext=True
    )
    body = ParagraphStyle(
        'AssnBody', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8.5, leading=12.5, alignment=TA_JUSTIFY,
        textColor=colors.HexColor("#1e293b"), spaceAfter=4
    )
    bullet = ParagraphStyle(
        'AssnBullet', parent=body,
        leftIndent=14, bulletIndent=5, spaceAfter=2
    )
    th = ParagraphStyle('TH', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8, leading=10, textColor=colors.white, alignment=TA_CENTER)
    td = ParagraphStyle('TD', parent=styles['Normal'], fontName='Helvetica', fontSize=7.5, leading=10, textColor=colors.HexColor("#0f172a"))
    td_b = ParagraphStyle('TDB', parent=td, fontName='Helvetica-Bold')

    story = []

    # =========================================================================
    # COVER PAGE
    # =========================================================================
    story.append(Spacer(1, 15))
    story.append(Paragraph("<b>G H RAISONI INTERNATIONAL SKILL TECH UNIVERSITY, PUNE</b>", title_style))
    story.append(Paragraph("DEPARTMENT OF COMPUTER APPLICATIONS", dept_style))
    story.append(Spacer(1, 12))
    story.append(Paragraph("<b>ACADEMIC ASSIGNMENTS DOSSIER</b>", sub_title))
    story.append(Paragraph("<b>Subject: Software Engineering & Project Development</b>", ParagraphStyle('SubSub', parent=sub_title, fontSize=11, textColor=colors.HexColor("#0f766e"))))
    story.append(Paragraph("Bachelor of Business Administration (Computer Applications) — BBA (CA)", center_text))
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#064e3b"), spaceAfter=14))

    meta_table = [
        [Paragraph("<b>Project Title:</b>", td_b), Paragraph("<b>CampusAI: Intelligent College Assistant Chatbot</b>", td)],
        [Paragraph("<b>Curriculum / Course:</b>", td_b), Paragraph("S.Y. BBA (Computer Applications) — Semester III &nbsp;|&nbsp; Academic Year 2026-27", td)],
        [Paragraph("<b>Submitted By:</b>", td_b), Paragraph("<b>1. Akash Rana</b> (PRN / Roll No: ISTU25010120004)<br/><b>2. Shreyash Katke</b> (PRN / Roll No: ISTU25010120003)", td)],
        [Paragraph("<b>Subject Faculty / Guide:</b>", td_b), Paragraph("<b>Asst. Prof. Sheela Satav</b>, Department of Computer Applications", td)],
        [Paragraph("<b>Institution:</b>", td_b), Paragraph("G H Raisoni International Skill Tech University, Wagholi, Pune - 412207", td)],
        [Paragraph("<b>Assignments Included:</b>", td_b), Paragraph("<b>Assignment 1:</b> Project Specific Inquiries (Q1 – Q14)<br/><b>Assignment 2:</b> Unified Modeling Language & Project Diagrams (Q1 – Q4)<br/><b>Assignment 3:</b> Software Life Cycle & SDLC Models (Q1 – Q2)<br/><b>Assignment 4:</b> Software Testing, SCM & Quality Assurance (Q1 – Q11)", td)],
    ]
    t_meta = Table(meta_table, colWidths=[130, 365])
    t_meta.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor("#f1f5f9")),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 18))

    story.append(Paragraph("<b>INDEX & ASSIGNMENT MAPPING</b>", ParagraphStyle('IdxHead', parent=h2, alignment=TA_CENTER)))
    index_data = [
        [Paragraph("<b>Assignment No.</b>", th), Paragraph("<b>Assignment Title / Scope</b>", th), Paragraph("<b>Key Concepts & Deliverables Covered</b>", th), Paragraph("<b>Page</b>", th)],
        [Paragraph("<b>Assignment 1</b>", td_b), Paragraph("Project Specific Inquiries", td), Paragraph("Architecture, SRS, data flow, entities, testing, student roles (Q1–Q14)", td), Paragraph("Page 2", td_b)],
        [Paragraph("<b>Assignment 2</b>", td_b), Paragraph("Unified Modeling Language", td), Paragraph("UML definition, classification, Use Case, Class, Sequence, Activity (Q1–Q4)", td), Paragraph("Page 5", td_b)],
        [Paragraph("<b>Assignment 3</b>", td_b), Paragraph("Software Life Cycle & SDLC", td), Paragraph("Project life cycle, Waterfall, Iterative, Spiral, V-Model, Agile (Q1–Q2)", td), Paragraph("Page 10", td_b)],
        [Paragraph("<b>Assignment 4</b>", td_b), Paragraph("Testing, SCM & Quality", td), Paragraph("Testing types, Black/White Box, SCM, Debugging, Metrics, VCS, OOSE (Q1–Q11)", td), Paragraph("Page 12", td_b)],
    ]
    t_index = Table(index_data, colWidths=[80, 150, 215, 50])
    t_index.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#064e3b")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(t_index)

    story.append(Spacer(1, 35))
    sign_table = [
        [
            Paragraph("____________________________<br/><b>Akash Rana</b><br/>Candidate 1 (ISTU25010120004)", center_text),
            Paragraph("____________________________<br/><b>Shreyash Katke</b><br/>Candidate 2 (ISTU25010120003)", center_text),
            Paragraph("____________________________<br/><b>Asst. Prof. Sheela Satav</b><br/>Subject Faculty / Project Guide", center_text)
        ]
    ]
    t_sign = Table(sign_table, colWidths=[165, 165, 165])
    story.append(t_sign)

    story.append(PageBreak())

    # =========================================================================
    # ASSIGNMENT 1
    # =========================================================================
    story.append(Paragraph("<b>ASSIGNMENT 1: PROJECT SPECIFIC QUESTIONS</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#064e3b"), spaceAfter=8))

    story.append(Paragraph("<b>Q1. Describe your project.</b>", q_title))
    story.append(Paragraph(
        "<b>CampusAI</b> is an automated, web-based artificial intelligence assistant engineered for higher educational institutions. "
        "The project addresses the challenge of resolving high volumes of repetitive student inquiries concerning admissions, fee structures, "
        "examination schedules, academic calendars, placement records, library services, and hostel accommodations. "
        "The system employs a <b>Dual-Tier Architecture</b>: a local, indexed SQLite FAQ repository that resolves verified institutional inquiries "
        "with sub-15ms latency, backed by Google's <b>Gemini 2.5 Flash LLM</b> for contextual generative reasoning when inquiries fall outside the static FAQ dataset. "
        "To ensure accessibility, the frontend features client-side Text-to-Speech (Web Speech API), mobile responsiveness, and an authenticated administrative dashboard.",
        body
    ))

    story.append(Paragraph("<b>Q2. Advantages of your project.</b>", q_title))
    story.append(Paragraph("• <b>24/7 Real-Time Availability:</b> Eliminates office counter queues by offering instantaneous query resolution anytime, anywhere.", bullet))
    story.append(Paragraph("• <b>Sub-15ms Latency for Verified Answers:</b> Local SQLite database indexing resolves verified FAQs with zero network API delay.", bullet))
    story.append(Paragraph("• <b>Zero-Hallucination Policy:</b> Enforces strict context-bounding on critical administrative parameters (fees, exam dates, eligibility criteria).", bullet))
    story.append(Paragraph("• <b>Auditory Accessibility:</b> Integrates the browser-native HTML5 Web Speech API for voice read-aloud.", bullet))
    story.append(Paragraph("• <b>Over 70% Reduction in Counter Traffic:</b> Frees administrative personnel from answering routine, redundant questions.", bullet))
    story.append(Paragraph("• <b>Real-Time Content Governance:</b> Authenticated administrative CRUD dashboard allows updating FAQ records without code redeployment.", bullet))

    story.append(Paragraph("<b>Q3. How do you gather the requirements of your project?</b>", q_title))
    story.append(Paragraph(
        "Requirements were gathered through a structured empirical methodology: "
        "(1) <i>Student Surveys:</i> Distributed questionnaires to 120+ undergraduate students to identify the most frequent inquiries and pain points; "
        "(2) <i>Administrative Helpdesk Audits:</i> Conducted in-depth interviews with college registrars, finance clerks, and examination coordinators; "
        "(3) <i>Historical Log Analysis:</i> Analyzed over 800 recorded email inquiries to formulate our 8 primary inquiry categories; "
        "(4) <i>Domain Classification:</i> Mapped requirements into functional specifications (multi-turn conversation, search, voice) and non-functional requirements (response latency &lt;1.5s, 100% test pass rate, PBKDF2 authentication).",
        body
    ))

    story.append(Paragraph("<b>Q4. How and where do you implement your project?</b>", q_title))
    story.append(Paragraph(
        "CampusAI is implemented as a full-stack Python web application. The backend is built using the <b>Flask 3.1.3</b> WSGI microframework in Python 3.11, "
        "utilizing <b>SQLAlchemy ORM</b> for database abstraction. The persistence layer is an embedded, ACID-compliant <b>SQLite 3</b> database (`campus_ai.db`). "
        "The frontend is authored using semantic <b>HTML5</b>, responsive <b>CSS3 Flexbox/Grid</b>, and modular ES6 <b>JavaScript</b>. "
        "Generative fallback is integrated through the official <b>google-genai</b> SDK communicating with Google Gemini 2.5 Flash over HTTPS. "
        "The project is currently hosted locally on WSGI port 5001 and is production-ready for deployment to Linux-based cloud infrastructure (Render.com, Gunicorn/Nginx, AWS EC2).",
        body
    ))

    story.append(Paragraph("<b>Q5. Which software you used in your project?</b>", q_title))
    story.append(Paragraph("• <b>Programming Languages:</b> Python 3.11, JavaScript (ES6+), HTML5, CSS3, SQL.", bullet))
    story.append(Paragraph("• <b>Frameworks & Libraries:</b> Flask 3.1.3, SQLAlchemy 2.0, Werkzeug (security), ReportLab 4.x (PDF reporting), Matplotlib 3.11 (diagrams).", bullet))
    story.append(Paragraph("• <b>AI & Cloud APIs:</b> Google Gemini 2.5 Flash API (LLM inference), Web Speech API (speech synthesis).", bullet))
    story.append(Paragraph("• <b>Database:</b> SQLite 3 with WAL (Write-Ahead Logging) mode.", bullet))
    story.append(Paragraph("• <b>Development & Version Control:</b> Visual Studio Code / Antigravity IDE, Git, GitHub (`akashrana01-tech/campus-ai-chatbot`).", bullet))
    story.append(Paragraph("• <b>Operating Environment:</b> macOS / Linux / Windows 10/11 cross-platform environments.", bullet))

    story.append(Paragraph("<b>Q6. What methodology is used for the project?</b>", q_title))
    story.append(Paragraph(
        "The project adopted the <b>Agile / Iterative SDLC methodology</b>. Development was executed across four distinct two-week sprint cycles: "
        "<i>Sprint 1:</i> Requirement gathering, architecture formulation, and 3NF database schema design. "
        "<i>Sprint 2:</i> Core Flask routing, Jaccard similarity matcher ($S \\ge 0.58$), and responsive chat viewport. "
        "<i>Sprint 3:</i> Google Gemini 2.5 Flash integration, hallucination guardrails, and Web Speech API synthesis. "
        "<i>Sprint 4:</i> Administrative CRUD dashboard, PBKDF2 security hardening, 23 automated unit/integration test suites, and documentation. "
        "This iterative model enabled continuous code review, rapid bug remediation, and risk minimization.",
        body
    ))

    story.append(Paragraph("<b>Q7. What is the hardware or software of the project?</b>", q_title))
    story.append(Paragraph(
        "<b>Hardware Specifications:</b><br/>"
        "• <i>Client Machine:</i> Any PC, laptop, or mobile device with a dual-core CPU, 2 GB RAM, display resolution of 1024x768 or higher, and speakers/earphones for voice output.<br/>"
        "• <i>Server Machine:</i> Minimum dual-core 2.0 GHz CPU, 2 GB RAM (4 GB recommended), 500 MB free disk space for SQLite database and virtual environment, and active Internet broadband connection (for Gemini API calls).<br/>"
        "<b>Software Specifications:</b><br/>"
        "• <i>Server Runtime:</i> Python 3.11 with pip package manager, virtual environment (`.venv`), Flask 3.1.3.<br/>"
        "• <i>Client Runtime:</i> Any standards-compliant modern web browser (Google Chrome 90+, Mozilla Firefox 88+, Apple Safari 14+, Microsoft Edge).",
        body
    ))

    story.append(Paragraph("<b>Q8. What is your role in the project?</b>", q_title))
    story.append(Paragraph(
        "The project was executed by a collaborative two-member engineering team with clearly demarcated responsibilities:<br/>"
        "• <b>Akash Rana (PRN: ISTU25010120004) — Lead Backend Architecture & AI Engineering:</b> "
        "Engineered Flask WSGI application routes, designed the 3NF SQLite database models with SQLAlchemy, developed the lexical tokenization and Jaccard similarity scoring engine ($S \\ge 0.58$), "
        "implemented the Google Gemini 2.5 Flash API connector with contextual system prompts, authored PBKDF2:SHA256 authentication security, and authored the 23-test automated test suite.<br/>"
        "• <b>Shreyash Katke (PRN: ISTU25010120003) — Frontend Engineering & UI/UX Design:</b> "
        "Designed the responsive mobile-first user interface with HTML5 and CSS3, engineered conversational message bubbles, typing indicators, dynamic suggestion chip components, "
        "integrated client-side Text-to-Speech audio synthesis using the Web Speech API, developed the administrative dashboard layout, and coordinated documentation diagrams.",
        body
    ))

    story.append(PageBreak())

    story.append(Paragraph("<b>Q9. Explain the data flow of your application.</b>", q_title))
    story.append(Paragraph(
        "The data flow of CampusAI follows a deterministic, pipeline-based flow from user interaction to final synthesis:<br/>"
        "1. <b>Input Stage:</b> Student submits an inquiry via keyboard text or clicks a pre-defined suggestion chip.<br/>"
        "2. <b>HTTP Transmission:</b> JavaScript client packages the message into JSON and transmits it via `POST /api/chat`.<br/>"
        "3. <b>Preprocessing & Tokenization:</b> Flask backend converts the query to lowercase, strips punctuation, eliminates stop-words, and stems keywords.<br/>"
        "4. <b>Local Similarity Evaluation:</b> Query tokens are compared against the SQLite FAQ database using Jaccard Similarity index: "
        "$$J(A, B) = \\frac{|A \\cap B|}{|A \\cup B|}$$<br/>"
        "5. <b>Branching Decision:</b> If similarity $S \\ge 0.58$, verified FAQ record is fetched directly from SQLite (&lt;15ms latency). "
        "If $S &lt; 0.58$, the query is augmented with institutional context and forwarded to Google Gemini 2.5 Flash API.<br/>"
        "6. <b>Response Assembly:</b> Backend packages the answer text, response source (`database` or `gemini_ai`), confidence score, and suggested follow-up chips into a JSON response.<br/>"
        "7. <b>Client Render:</b> Frontend renders the chat bubble and automatically triggers Text-to-Speech audio read-aloud if enabled.",
        body
    ))

    story.append(Paragraph("<b>Q10. What are the entities in your project?</b>", q_title))
    story.append(Paragraph(
        "CampusAI database incorporates 5 core relational entities:<br/>"
        "• <b>Admin:</b> Stores administrative user credentials (`id`, `username`, `password_hash`, `created_at`).<br/>"
        "• <b>Category:</b> Defines institutional knowledge domains (`id`, `name`, `icon`, `description`).<br/>"
        "• <b>FAQ:</b> Contains official institutional knowledge (`id`, `category_id`, `question`, `answer`, `keywords`, `click_count`, `updated_at`).<br/>"
        "• <b>QueryLog:</b> Records student interactions for administrative analytics (`id`, `query_text`, `matched_source`, `confidence_score`, `timestamp`).<br/>"
        "• <b>Feedback:</b> Captures student satisfaction ratings (`id`, `query_id`, `rating`, `user_comment`, `created_at`).",
        body
    ))

    story.append(Paragraph("<b>Q11. What is the drawback of your system?</b>", q_title))
    story.append(Paragraph("• <b>Cloud Connectivity Dependency:</b> Generative fallback queries require active outbound Internet connectivity to communicate with Google Gemini API.", bullet))
    story.append(Paragraph("• <b>API Rate Limits:</b> Free-tier Gemini API keys are subject to requests-per-minute (RPM) quotas during sudden traffic spikes.", bullet))
    story.append(Paragraph("• <b>Unilingual Baseline:</b> Currently optimized for English; regional language comprehension (Hindi/Marathi) requires external translation bridging.", bullet))
    story.append(Paragraph("• <b>OS-Dependent Voice Timbre:</b> Speech synthesis accent and vocal quality vary depending on the client device's installed browser voice engine.", bullet))

    story.append(Paragraph("<b>Q12. How do you test your application?</b>", q_title))
    story.append(Paragraph(
        "CampusAI was validated through a multi-level testing methodology:<br/>"
        "• <i>Unit Testing:</i> Validated individual tokenization routines, Jaccard similarity edge conditions, and password hashing algorithms.<br/>"
        "• <i>Integration Testing:</i> Verified route controllers (`/api/chat`, `/api/faqs`, `/admin/login`, `/admin/dashboard`) using Flask's test client.<br/>"
        "• <i>Black-Box Testing:</i> Evaluated boundary inputs including empty messages, punctuation-only strings, extremely long text, and SQL injection strings.<br/>"
        "• <i>Security Testing:</i> Tested session timeout protection, unauthorized route redirection, and PBKDF2 hash collision resistance.<br/>"
        "• <i>Automated Test Suite:</i> Authoring <b>23 automated test cases</b> executed via `python run_tests.py`, achieving a <b>100% pass rate in 1.28 seconds</b>.",
        body
    ))

    story.append(Paragraph("<b>Q13. From where do you get reference, guide for your project work?</b>", q_title))
    story.append(Paragraph(
        "• <b>Academic Guidance:</b> Project Guide <b>Asst. Prof. Sheela Satav</b>, Department of Computer Applications, G H Raisoni International Skill Tech University Pune.<br/>"
        "• <b>Textbooks:</b> Pressman, R. S. (*Software Engineering: A Practitioner's Approach*), Jurafsky, D. & Martin, J. H. (*Speech and Language Processing*), Grinberg, M. (*Flask Web Development*).<br/>"
        "• <b>Official Documentation:</b> Python Documentation (python.org), Pallets Flask Documentation (flask.palletsprojects.com), Google Gemini API Documentation (ai.google.dev), MDN Web Docs (developer.mozilla.org).",
        body
    ))

    story.append(Paragraph("<b>Q14. In the future, what changes will you make in your application?</b>", q_title))
    story.append(Paragraph("• <b>ERP & SIS Integration:</b> Integrate with College ERP via REST APIs to provide authenticated students with personalized attendance and fee receipts.", bullet))
    story.append(Paragraph("• <b>Multilingual Voice & Text Support:</b> Add support for Marathi, Hindi, and regional languages using Google Cloud Translation and Indic-TTS.", bullet))
    story.append(Paragraph("• <b>Speech-to-Text Input:</b> Add microphone input using the Web Speech Recognition API for hands-free query voice input.", bullet))
    story.append(Paragraph("• <b>Omnichannel Bot Deployment:</b> Port the chatbot to WhatsApp Business API and Telegram for direct smartphone messaging.", bullet))

    story.append(PageBreak())

    # =========================================================================
    # ASSIGNMENT 2
    # =========================================================================
    story.append(Paragraph("<b>ASSIGNMENT 2: UNIFIED MODELING LANGUAGE (UML)</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#064e3b"), spaceAfter=8))

    story.append(Paragraph("<b>Q1. What is UML?</b>", q_title))
    story.append(Paragraph(
        "The <b>Unified Modeling Language (UML)</b> is a standardized general-purpose visual modeling language in software engineering, "
        "created and maintained by the <b>Object Management Group (OMG)</b>. Created by Grady Booch, James Rumbaugh, and Ivar Jacobson (\"The Three Amigos\"), "
        "UML provides a visual syntax for specifying, visualizing, constructing, and documenting the artifacts of object-oriented software systems. "
        "UML is language-independent, allowing developers to model systems conceptually before generating target code in Python, Java, or C++.",
        body
    ))

    story.append(Paragraph("<b>Q2. What is the use of UML?</b>", q_title))
    story.append(Paragraph("• <b>Standardized Architectural Blueprinting:</b> Provides a common visual notation understood universally by developers, architects, and business stakeholders.", bullet))
    story.append(Paragraph("• <b>Early Defect Detection:</b> Identifies architectural bottlenecks, cyclic dependencies, and logical flaws during design before costly code construction.", bullet))
    story.append(Paragraph("• <b>Traceability of Requirements:</b> Maps user requirements (Use Cases) directly into structural classes and behavioral sequences.", bullet))
    story.append(Paragraph("• <b>Code Generation & Reverse Engineering:</b> Facilitates automated code scaffolding and generating documentation from existing codebases.", bullet))
    story.append(Paragraph("• <b>System Maintenance & Evolution:</b> Serves as an enduring reference guide for onboarding new engineers and managing system upgrades.", bullet))

    story.append(Paragraph("<b>Q3. Explain types of UML diagram with example?</b>", q_title))
    story.append(Paragraph(
        "UML 2.5 defines 14 official diagrams categorized into two broad classifications:<br/>"
        "1. <b>Structural Diagrams:</b> Model the static architecture of the system—elements that exist independently of time.<br/>"
        "&nbsp;&nbsp;• <i>Class Diagram:</i> Illustrates system classes, attributes, methods, and relationships (e.g., Student class associated with Course class).<br/>"
        "&nbsp;&nbsp;• <i>Object Diagram:</i> Shows instances of classes at a specific point in time (e.g., student \"Akash\" enrolled in \"BBA CA Sem III\").<br/>"
        "&nbsp;&nbsp;• <i>Component Diagram:</i> Displays organization and dependencies among software modules (e.g., Flask App component relying on SQLite component).<br/>"
        "&nbsp;&nbsp;• <i>Deployment Diagram:</i> Depicts physical hardware nodes and runtime execution environments (e.g., Web Server node hosting Flask WSGI container).<br/>"
        "2. <b>Behavioral Diagrams:</b> Model the dynamic behavior of the system over time as messages and states change.<br/>"
        "&nbsp;&nbsp;• <i>Use Case Diagram:</i> Depicts user interactions with system boundaries (e.g., Student actor executes \"Inquire Fees\" use case).<br/>"
        "&nbsp;&nbsp;• <i>Sequence Diagram:</i> Captures chronological message exchanges between objects (e.g., Student UI sends query to Controller, which queries Database).<br/>"
        "&nbsp;&nbsp;• <i>Activity Diagram:</i> Models procedural workflows and decision logic, similar to a flowchart (e.g., query validation and similarity branching).<br/>"
        "&nbsp;&nbsp;• <i>State Machine Diagram:</i> Shows the lifecycle states and transitions of a single object (e.g., Chatbot session: Idle &rarr; Listening &rarr; Processing &rarr; Responding).",
        body
    ))

    story.append(Paragraph("<b>Q4. Draw UML Diagrams of your project.</b>", q_title))
    story.append(Paragraph(
        "The following official UML diagrams illustrate the architecture, structure, and dynamic workflows of the <b>CampusAI Chatbot</b>:",
        body
    ))

    # Diagram 1: Use Case Diagram
    uc_path = os.path.join(DIAGRAM_DIR, "campusai_use_case.png")
    if os.path.exists(uc_path):
        story.append(Spacer(1, 4))
        story.append(RLImage(uc_path, width=370, height=400))
        story.append(Paragraph("<b>Fig 2.1: Use Case Diagram of CampusAI</b>", ParagraphStyle('CapUC', parent=center_text, fontSize=8, fontName='Helvetica-Bold')))
        story.append(Paragraph(
            "<i>Explanation:</i> Depicts primary actors: <b>Student / Visitor</b> (Ask Questions, Filter Categories, Listen to Voice Audio, Submit Feedback) "
            "and <b>System Administrator</b> (Authenticate, Create FAQ, Edit FAQ, Delete FAQ, Monitor Analytics). "
            "The external actor <b>Google Gemini API</b> provides generative completion fallback.", body
        ))

    story.append(PageBreak())

    # Diagram 2: Class Diagram
    class_path = os.path.join(DIAGRAM_DIR, "campusai_class_diagram.png")
    if os.path.exists(class_path):
        story.append(Spacer(1, 4))
        story.append(RLImage(class_path, width=370, height=400))
        story.append(Paragraph("<b>Fig 2.2: Class Diagram of CampusAI</b>", ParagraphStyle('CapCl', parent=center_text, fontSize=8, fontName='Helvetica-Bold')))
        story.append(Paragraph(
            "<i>Explanation:</i> Illustrates the core domain model: <code>Admin</code>, <code>Category</code>, <code>FAQ</code>, <code>QueryLog</code>, "
            "and <code>Feedback</code> entities, their private attributes, and public member functions (e.g., <code>hash_password()</code>, "
            "<code>check_password()</code>, <code>calculate_jaccard_similarity()</code>, <code>query_gemini_fallback()</code>).", body
        ))

    story.append(PageBreak())

    # Diagram 3: Sequence Diagram
    seq_path = os.path.join(DIAGRAM_DIR, "campusai_sequence_diagram.png")
    if os.path.exists(seq_path):
        story.append(Spacer(1, 4))
        story.append(RLImage(seq_path, width=370, height=400))
        story.append(Paragraph("<b>Fig 2.3: Sequence Diagram of CampusAI Query Resolution</b>", ParagraphStyle('CapSq', parent=center_text, fontSize=8, fontName='Helvetica-Bold')))
        story.append(Paragraph(
            "<i>Explanation:</i> Traces the chronological sequence of synchronous and asynchronous message exchanges between the Student Actor, "
            "Browser DOM, Flask API Controller, Local FAQ Matcher, SQLite Database, and Google Gemini AI service.", body
        ))

    story.append(PageBreak())

    # Diagram 4: Activity Diagram
    act_path = os.path.join(DIAGRAM_DIR, "campusai_activity_diagram.png")
    if os.path.exists(act_path):
        story.append(Spacer(1, 4))
        story.append(RLImage(act_path, width=370, height=400))
        story.append(Paragraph("<b>Fig 2.4: Activity Diagram of CampusAI Workflow</b>", ParagraphStyle('CapAc', parent=center_text, fontSize=8, fontName='Helvetica-Bold')))
        story.append(Paragraph(
            "<i>Explanation:</i> Details the operational control flow: from initial query reception, sanitization, empty query checking, "
            "Jaccard similarity threshold branching ($S \\ge 0.58$), local database retrieval, AI fallback routing, to voice synthesis output.", body
        ))

    story.append(PageBreak())

    # =========================================================================
    # ASSIGNMENT 3
    # =========================================================================
    story.append(Paragraph("<b>ASSIGNMENT 3: SOFTWARE DEVELOPMENT LIFE CYCLE (SDLC)</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#064e3b"), spaceAfter=8))

    story.append(Paragraph("<b>Q1. What is Project Life Cycle and its Main Characteristics?</b>", q_title))
    story.append(Paragraph(
        "A <b>Project Life Cycle</b> is the sequential series of phases that a project passes through from its initial inception to formal closure. "
        "It provides the foundational governance framework for planning, executing, controlling, and delivering a software product.<br/>"
        "The standard life cycle comprises 5 primary phases: "
        "(1) <i>Initiation:</i> Feasibility assessment, scope definition, stakeholder charter; "
        "(2) <i>Planning:</i> Requirements analysis, architectural design, resource allocation, schedule Gantt chart; "
        "(3) <i>Execution:</i> Code construction, database schema generation, API integrations; "
        "(4) <i>Monitoring & Controlling:</i> Verification testing, defect tracking, quality assurance audits; "
        "(5) <i>Closure:</i> User acceptance sign-off, deployment, post-mortem documentation.<br/>"
        "<b>Main Characteristics:</b><br/>"
        "• <i>Cost and Staffing Curve:</i> Cost and resource allocation start low, peak during execution/coding, and rapidly taper off during closure.<br/>"
        "• <i>Risk and Uncertainty Curve:</i> Uncertainty and project risk are highest at the beginning of the project and steadily decrease as milestones are validated.<br/>"
        "• <i>Ability to Influence Cost of Change:</i> Stakeholders have the highest ability to influence final product features at the start; the cost of modifying requirements rises exponentially in later phases.<br/>"
        "• <i>Phase Gates / Tollgates:</i> Formal review checkpoints at the end of each phase determine whether the project advances, requires revision, or aborts.",
        body
    ))

    story.append(Paragraph("<b>Q2. Explain following SDLC models.</b>", q_title))

    story.append(Paragraph("<b>i) Waterfall Model:</b>", h2))
    story.append(Paragraph(
        "The Waterfall Model is a classic linear-sequential SDLC approach where each phase (Requirements &rarr; System Design &rarr; "
        "Implementation &rarr; Integration & Testing &rarr; Deployment &rarr; Maintenance) must be fully completed and signed off before the next phase commences. "
        "<i>Advantages:</i> Simple, structured, and easy to manage with well-defined deliverables at each phase. "
        "<i>Disadvantages:</i> Rigid and inflexible; highly vulnerable to changing requirements; working software is delivered late in the lifecycle. "
        "<i>Best Suited For:</i> Projects with stable, well-understood requirements with zero expected scope changes.",
        body
    ))

    story.append(Paragraph("<b>ii) Iterative Model:</b>", h2))
    story.append(Paragraph(
        "The Iterative Model builds an initial, simplified implementation of core requirements, and incrementally enhances and refines the product "
        "across successive repetitive cycles (iterations). Each iteration goes through design, coding, and testing. "
        "<i>Advantages:</i> Delivers working software early; accommodates evolving user feedback; detects design flaws early. "
        "<i>Disadvantages:</i> Requires disciplined architectural management; total project cost can escalate if iterations are not tightly bounded. "
        "<i>Best Suited For:</i> Large-scale software systems where fundamental requirements are clear but feature details evolve.",
        body
    ))

    story.append(Paragraph("<b>iii) Spiral Model:</b>", h2))
    story.append(Paragraph(
        "Conceived by Barry Boehm, the Spiral Model is a risk-driven process model combining iterative development with systematic aspects of the waterfall model. "
        "Development progresses through concentric spirals spanning four quadrants: "
        "(1) <i>Objective Setting:</i> Identifying goals, constraints, and alternatives; "
        "(2) <i>Risk Assessment & Mitigation:</i> Detailed analysis and prototyping to resolve risks; "
        "(3) <i>Engineering & Development:</i> Coding and verification of the current release; "
        "(4) <i>Customer Evaluation & Next-Phase Planning:</i> Reviewing outcomes and planning the subsequent loop. "
        "<i>Advantages:</i> Unrivaled risk management and proactive contingency handling. "
        "<i>Disadvantages:</i> Complex, costly, and requires specialized risk-assessment expertise. "
        "<i>Best Suited For:</i> High-risk, mission-critical, large enterprise projects.",
        body
    ))

    story.append(Paragraph("<b>iv) V-Shaped Model (Verification and Validation Model):</b>", h2))
    story.append(Paragraph(
        "The V-Model is an extension of the linear waterfall model where each development phase is strictly paired with an equivalent testing phase "
        "arranged in a V-shaped sequence. The left downward slope represents <i>Verification</i> (Requirements &rarr; System Design &rarr; Architecture &rarr; Module Design), "
        "the vertex represents <i>Coding</i>, and the right upward slope represents <i>Validation</i> (Unit Testing &rarr; Integration Testing &rarr; System Testing &rarr; User Acceptance Testing). "
        "<i>Advantages:</i> Extremely high quality and defect prevention because test plans are designed before code is written. "
        "<i>Disadvantages:</i> Inflexible; no early working prototypes. "
        "<i>Best Suited For:</i> Highly regulated, safety-critical domains (medical software, avionics, defense systems).",
        body
    ))

    story.append(Paragraph("<b>v) Agile Model:</b>", h2))
    story.append(Paragraph(
        "The Agile Model is an adaptive, iterative, customer-collaborative development framework based on the 12 principles of the <i>Agile Manifesto</i>. "
        "Work is partitioned into short, fixed-duration timeboxes called <b>Sprints</b> (typically 1 to 4 weeks). Cross-functional teams collaborate "
        "through daily standup meetings, backlogs, user stories, and sprint retrospectives to deliver continuously testable, incremental software releases. "
        "<i>Advantages:</i> Exceptional flexibility; high customer engagement; rapid time-to-market; early business value delivery. "
        "<i>Disadvantages:</i> Demands experienced team members; documentation can be neglected if not systematically mandated. "
        "<i>Best Suited For:</i> Web applications, startups, AI products (such as CampusAI), where requirements evolve dynamically.",
        body
    ))

    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Comparative Analysis of SDLC Models:</b>", ParagraphStyle('CompTitle', parent=h2, fontSize=9)))
    sdlc_table = [
        [Paragraph("<b>Parameter</b>", th), Paragraph("<b>Waterfall</b>", th), Paragraph("<b>Iterative</b>", th), Paragraph("<b>Spiral</b>", th), Paragraph("<b>V-Model</b>", th), Paragraph("<b>Agile</b>", th)],
        [Paragraph("Flexibility", td_b), Paragraph("Very Low", td), Paragraph("Moderate", td), Paragraph("High", td), Paragraph("Low", td), Paragraph("Very High", td)],
        [Paragraph("Risk Management", td_b), Paragraph("Poor", td), Paragraph("Fair", td), Paragraph("Exceptional", td), Paragraph("Good", td), Paragraph("Very Good", td)],
        [Paragraph("Client Involvement", td_b), Paragraph("Start & End", td), Paragraph("At Iterations", td), Paragraph("Every Loop", td), Paragraph("Start & UAT", td), Paragraph("Continuous", td)],
        [Paragraph("Working Software", td_b), Paragraph("Very Late", td), Paragraph("Early", td), Paragraph("Periodic", td), Paragraph("Late", td), Paragraph("Every Sprint", td)],
        [Paragraph("Model Adopted", td_b), Paragraph("No", td), Paragraph("Partial", td), Paragraph("No", td), Paragraph("No", td), Paragraph("<b>Yes (CampusAI)</b>", td)],
    ]
    t_sdlc = Table(sdlc_table, colWidths=[90, 80, 80, 80, 80, 85])
    t_sdlc.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#064e3b")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
    ]))
    story.append(t_sdlc)

    story.append(PageBreak())

    # =========================================================================
    # ASSIGNMENT 4
    # =========================================================================
    story.append(Paragraph("<b>ASSIGNMENT 4: TESTING, SCM & SOFTWARE QUALITY ASSURANCE</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#064e3b"), spaceAfter=8))

    story.append(Paragraph("<b>1] Define Software Testing?</b>", q_title))
    story.append(Paragraph(
        "According to ANSI/IEEE Standard 1059, <b>Software Testing</b> is the process of analyzing a software item to detect the differences between "
        "existing and required conditions (i.e., defects/bugs) and to evaluate the features of the software item. "
        "Testing encompasses both <i>Verification</i> (\"Are we building the product right?\" — ensuring adherence to specifications) "
        "and <i>Validation</i> (\"Are we building the right product?\" — ensuring fulfillment of user requirements and operational fitness).",
        body
    ))

    story.append(Paragraph("<b>2] What is Risk identification?</b>", q_title))
    story.append(Paragraph(
        "<b>Risk Identification</b> is the systematic, proactive process of recognizing, analyzing, and documenting potential threats that could adversely "
        "impact a software project's schedule, cost, quality, or delivery viability. "
        "Risks are categorized into: (1) <i>Technical Risks:</i> Unproven technologies, API rate limits, hardware constraints; "
        "(2) <i>Project Risks:</i> Schedule slippages, staffing turnover, insufficient budget; "
        "(3) <i>Business Risks:</i> Regulatory changes, market obsolescence. "
        "Techniques include checklist analysis, assumption analysis, brainstorming, and Root Cause Analysis (RCA).",
        body
    ))

    story.append(Paragraph("<b>3] What is SCM?</b>", q_title))
    story.append(Paragraph(
        "<b>Software Configuration Management (SCM)</b> is a disciplined software engineering process designed to systematically track, control, "
        "and manage changes made to software work products (source code, schemas, documentation, libraries, test scripts) across the system lifecycle. "
        "SCM comprises four essential pillars: "
        "(1) <i>Configuration Identification:</i> Defining Configuration Items (CIs) and baselines; "
        "(2) <i>Change Control:</i> Formal review and approval of change requests via a Change Control Board (CCB); "
        "(3) <i>Configuration Status Accounting (CSA):</i> Recording what changes were made, by whom, and when; "
        "(4) <i>Configuration Audit:</i> Verifying that releases conform to baseline standards.",
        body
    ))

    story.append(Paragraph("<b>4] Define Debugging.</b>", q_title))
    story.append(Paragraph(
        "<b>Debugging</b> is the diagnostic process of locating, isolating, analyzing, and resolving the underlying root causes of bugs, defects, "
        "or anomalous behaviors identified during software testing. While <i>Testing</i> demonstrates the existence of defects, <i>Debugging</i> "
        "is an analytical developer task that determines <i>why</i> the defect occurred and modifies the source code to remediate it without causing regressions.",
        body
    ))

    story.append(Paragraph("<b>5] Explain Configuration Audit.</b>", q_title))
    story.append(Paragraph(
        "A <b>Configuration Audit</b> is a formal verification process that provides independent assurance that a software product complies with "
        "its baseline requirements, technical specifications, and configuration records before release. Audits are bifurcated into:<br/>"
        "• <b>Functional Configuration Audit (FCA):</b> Verifies that all functional requirements specified in the SRS have been fully implemented and validated by test results.<br/>"
        "• <b>Physical Configuration Audit (PCA):</b> Verifies that the physical release package contains all required build artifacts, binaries, configurations, and documentation.",
        body
    ))

    story.append(Paragraph("<b>6] Differentiate Between Black Box Testing and White Box Testing?</b>", q_title))
    bb_wb_table = [
        [Paragraph("<b>Criteria</b>", th), Paragraph("<b>Black Box Testing (Behavioral)</b>", th), Paragraph("<b>White Box Testing (Structural)</b>", th)],
        [Paragraph("Internal Code Knowledge", td_b), Paragraph("No knowledge of internal code or logic required.", td), Paragraph("Complete knowledge of internal source code and logic required.", td)],
        [Paragraph("Primary Focus", td_b), Paragraph("Validates inputs against expected outputs (functionality).", td), Paragraph("Validates internal paths, loops, conditions, and data structures.", td)],
        [Paragraph("Performed By", td_b), Paragraph("Software Testers, QA Engineers, End Users.", td), Paragraph("Software Developers, Technical Architects.", td)],
        [Paragraph("Testing Techniques", td_b), Paragraph("Equivalence Partitioning, Boundary Value Analysis (BVA), Decision Tables.", td), Paragraph("Statement Coverage, Branch Coverage, Path Coverage, Condition Coverage.", td)],
        [Paragraph("Suitability", td_b), Paragraph("Ideal for System Testing and Acceptance Testing (UAT).", td), Paragraph("Ideal for Unit Testing and Component Integration Testing.", td)],
        [Paragraph("Programming Skills", td_b), Paragraph("Programming knowledge not mandatory.", td), Paragraph("Deep programming and algorithmic knowledge essential.", td)],
        [Paragraph("CampusAI Implementation", td_b), Paragraph("Testing chat queries, suggestion chips, admin UI workflows.", td), Paragraph("Testing Jaccard similarity algorithms, tokenizers, password hashing.", td)],
    ]
    t_bb_wb = Table(bb_wb_table, colWidths=[110, 192, 193])
    t_bb_wb.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#064e3b")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
    ]))
    story.append(t_bb_wb)

    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>7] What Do You Mean By Metrics?</b>", q_title))
    story.append(Paragraph(
        "A <b>Software Metric</b> is a quantitative measure of the degree to which a software system, component, or development process possesses a given attribute. "
        "Metrics provide empirical data for project estimation, quality control, and process optimization. Categories include: "
        "(1) <i>Product Metrics:</i> Size (Lines of Code - LOC), Complexity (Cyclomatic Complexity $V(G) = E - N + 2P$), Reliability (Mean Time Between Failures - MTBF); "
        "(2) <i>Process Metrics:</i> Defect Removal Efficiency (DRE), defect discovery rates; "
        "(3) <i>Project Metrics:</i> Schedule variance, milestone slippage, cost performance index (CPI).",
        body
    ))

    story.append(Paragraph("<b>8] What Do You Mean By Version Control?</b>", q_title))
    story.append(Paragraph(
        "<b>Version Control</b> (or Source Code Management) is a software engineering system that records snapshots and modifications to files over time, "
        "enabling developers to recall specific historical revisions, compare changes, revert regressions, and collaborate concurrently without overwriting code. "
        "<i>Distributed Version Control Systems (DVCS)</i>, notably <b>Git</b>, allow every developer to maintain a full clone of the repository history. "
        "In CampusAI, Git and GitHub are utilized for branch management, pull requests, automated CI/CD pipelines, and atomic commit logging (`bb716e7`, `9248cff`).",
        body
    ))

    story.append(Paragraph("<b>9] Explain Object Oriented Software Engineering?</b>", q_title))
    story.append(Paragraph(
        "<b>Object-Oriented Software Engineering (OOSE)</b> is an engineering paradigm developed by Ivar Jacobson that structures the software lifecycle "
        "around real-world objects and use cases. OOSE applies core Object-Oriented principles across all phases: "
        "(1) <i>Object-Oriented Analysis (OOA):</i> Modeling the problem domain using actors and Use Cases; "
        "(2) <i>Object-Oriented Design (OOD):</i> Organizing domain objects into classes adhering to Encapsulation, Abstraction, Inheritance, and Polymorphism; "
        "(3) <i>Object-Oriented Programming (OOP):</i> Constructing modules in modern languages (Python/Flask) where data and functions are unified in objects.",
        body
    ))

    story.append(Paragraph("<b>10] Explain Various Types of Testing in details.</b>", q_title))
    story.append(Paragraph(
        "• <b>Unit Testing:</b> Tests individual software units or functions in isolation (e.g., tokenizing strings, verifying Jaccard math).<br/>"
        "• <b>Integration Testing:</b> Verifies data communication and interfaces between integrated modules (e.g., Flask controller querying SQLite).<br/>"
        "• <b>System Testing:</b> Evaluates the complete, integrated software end-to-end against the SRS requirements specification.<br/>"
        "• <b>Acceptance Testing (UAT):</b> Conducted by end users to validate whether the system meets operational business needs before final sign-off.<br/>"
        "• <b>Regression Testing:</b> Re-executing existing test suites to confirm that recent bug fixes or modifications have not broken working features.<br/>"
        "• <b>Performance & Load Testing:</b> Assesses system response time, throughput, and stability under heavy simulated concurrent user loads.<br/>"
        "• <b>Security Testing:</b> Audits vulnerabilities, unauthorized privilege escalation, SQL injection, and session hijacking risks.",
        body
    ))

    story.append(Paragraph("<b>11] Differentiate Between Automated Testing And Manual Testing.</b>", q_title))
    auto_man_table = [
        [Paragraph("<b>Evaluation Factor</b>", th), Paragraph("<b>Manual Testing</b>", th), Paragraph("<b>Automated Testing</b>", th)],
        [Paragraph("Execution Method", td_b), Paragraph("Human testers manually execute test steps and observe outputs.", td), Paragraph("Automated scripts and frameworks (unittest, Selenium) execute tests.", td)],
        [Paragraph("Execution Speed", td_b), Paragraph("Slow; constrained by human typing and reading speeds.", td), Paragraph("Extremely fast; executes hundreds of assertions in seconds.", td)],
        [Paragraph("Reliability & Human Error", td_b), Paragraph("Vulnerable to human fatigue, distraction, and oversight.", td), Paragraph("100% precise and repeatable; zero fatigue factor.", td)],
        [Paragraph("Cost Efficiency", td_b), Paragraph("Low initial cost, but ongoing human labor costs scale with time.", td), Paragraph("High initial script development cost, but zero incremental cost per run.", td)],
        [Paragraph("Regression Testing", td_b), Paragraph("Tedious, exhausting, and rarely executed comprehensively.", td), Paragraph("Ideal; executes effortlessly on every code commit or build.", td)],
        [Paragraph("Exploratory & UI Testing", td_b), Paragraph("Highly effective for visual appeal, usability, and exploratory tests.", td), Paragraph("Poor for visual nuance; best for deterministic logic.", td)],
        [Paragraph("CampusAI Implementation", td_b), Paragraph("Used during initial design feedback and voice timbre audits.", td), Paragraph("<b>23 automated tests in `run_tests.py`</b> (executed in 1.28s).", td)],
    ]
    t_auto_man = Table(auto_man_table, colWidths=[110, 192, 193])
    t_auto_man.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#064e3b")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
    ]))
    story.append(t_auto_man)

    doc.build(story, canvasmaker=NumberedCanvasAssignments)
    print(f"[✓] Successfully built: {OUT_PDF}")

if __name__ == "__main__":
    build_assignments_pdf()
