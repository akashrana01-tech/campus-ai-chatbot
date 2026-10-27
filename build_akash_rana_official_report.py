"""
CampusAI Official 35-Page Project Report Generator
Specifically authored for:
- Akash rana (ISTU25010120004)
- Shreyash katke (ISTU25010120003)
Course: BBA CA (Semester III, 2025-26)
Institution: G H Raisoni International Skill Tech University, Pune-412207
Project Guide: Prof. Sheela Satav

Contains:
- Double border on every single page
- G H Raisoni Logo on Cover and Certificate
- Official running footer: "G H Raisoni International Skill Tech University, Pune" | "Page X"
- All 29 academic topics in dedicated pages
- 100% pure CampusAI features: admissions, fees, courses, exams, facilities,
  dual-tier NLP + Gemini fallback, zero-hallucination policy, 3NF database, 23 test cases.
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfgen import canvas

BASE_DIR = "/Users/kanishksingh/Downloads/momo ai chat bot "
IMG_DIR = os.path.join(BASE_DIR, "scratch/campusai_diagrams")
LOGO_PATH = os.path.join(BASE_DIR, "scratch/pdf2_images/page_1_0_X6.png")

PAGE_W, PAGE_H = 594.96, 841.92

class AcademicNumberedCanvas(canvas.Canvas):
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
            self.draw_page_decorations()
            super().showPage()
        super().save()

    def draw_page_decorations(self):
        # 1. Double line border on EVERY page
        self.saveState()
        self.setStrokeColor(colors.black)
        
        # Outer rectangle
        self.setLineWidth(1.5)
        self.rect(28, 28, PAGE_W - 56, PAGE_H - 56)
        
        # Inner rectangle (3.5pt inside)
        self.setLineWidth(0.75)
        self.rect(31.5, 31.5, PAGE_W - 63, PAGE_H - 63)
        
        # 2. Running footer (Only for content pages 7 to 35)
        if self._pageNumber >= 7:
            arabic_page = self._pageNumber - 6
            self.setFont("Times-Roman", 8)
            self.setFillColor(colors.HexColor("#334155"))
            
            # Line above footer
            self.setLineWidth(0.5)
            self.setStrokeColor(colors.HexColor("#94a3b8"))
            self.line(45, 45, PAGE_W - 45, 45)
            
            # Left footer
            self.drawString(45, 35, "G H Raisoni International Skill Tech University, Pune")
            # Right footer
            self.drawRightString(PAGE_W - 45, 35, f"Page {arabic_page}")
            
        self.restoreState()


def build_akash_report(out_path):
    doc = SimpleDocTemplate(
        out_path,
        pagesize=(PAGE_W, PAGE_H),
        leftMargin=45,
        rightMargin=45,
        topMargin=45,
        bottomMargin=55
    )

    styles = getSampleStyleSheet()

    # Academic Typography Styles
    title_main = ParagraphStyle(
        'TitleMain',
        fontName='Times-Bold',
        fontSize=18,
        leading=24,
        alignment=TA_CENTER,
        textColor=colors.black
    )
    center_text = ParagraphStyle(
        'CenterText',
        fontName='Times-Roman',
        fontSize=11,
        leading=16,
        alignment=TA_CENTER,
        textColor=colors.black
    )
    center_bold = ParagraphStyle(
        'CenterBold',
        fontName='Times-Bold',
        fontSize=11.5,
        leading=16,
        alignment=TA_CENTER,
        textColor=colors.black
    )
    h1 = ParagraphStyle(
        'H1',
        fontName='Times-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.black,
        spaceBefore=0,
        spaceAfter=12,
        keepWithNext=True
    )
    h2 = ParagraphStyle(
        'H2',
        fontName='Times-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.black,
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )
    body = ParagraphStyle(
        'Body',
        fontName='Times-Roman',
        fontSize=9.5,
        leading=15,
        alignment=TA_JUSTIFY,
        textColor=colors.black,
        spaceAfter=8
    )
    bullet = ParagraphStyle(
        'Bullet',
        parent=body,
        leftIndent=15,
        bulletIndent=5,
        spaceAfter=4
    )
    th = ParagraphStyle(
        'TH',
        fontName='Times-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white,
        alignment=TA_CENTER
    )
    td = ParagraphStyle(
        'TD',
        fontName='Times-Roman',
        fontSize=8,
        leading=11,
        textColor=colors.black
    )
    td_center = ParagraphStyle(
        'TDCenter',
        fontName='Times-Roman',
        fontSize=8,
        leading=11,
        textColor=colors.black,
        alignment=TA_CENTER
    )

    story = []

    # =========================================================================
    # PAGE 1: COVER PAGE
    # =========================================================================
    if os.path.exists(LOGO_PATH):
        story.append(Spacer(1, 15))
        story.append(Image(LOGO_PATH, width=170, height=57))
    else:
        story.append(Spacer(1, 40))
        story.append(Paragraph("<b>G H RAISONI INTERNATIONAL SKILL TECH UNIVERSITY</b>", center_bold))

    story.append(Spacer(1, 35))
    story.append(Paragraph("A<br/>Project report on", center_text))
    story.append(Spacer(1, 20))
    story.append(Paragraph("<u><b>CampusAI: College Assistant Chatbot</b></u>", title_main))
    story.append(Spacer(1, 35))

    story.append(Paragraph("<b>Submitted To :</b>", center_bold))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>G H Raisoni International Skill Tech University.</b><br/><b>PUNE-412207</b>", center_text))
    story.append(Spacer(1, 25))

    story.append(Paragraph("<b>For: BBA CA</b>", center_bold))
    story.append(Spacer(1, 25))

    story.append(Paragraph("<b>Submitted By :</b>", center_bold))
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Akash rana (ISTU25010120004)</b><br/><b>Shreyash katke (ISTU25010120003)</b>", center_bold))
    story.append(Spacer(1, 35))

    story.append(Paragraph("<b>Semester III<br/>Year 2025-26</b>", center_text))
    story.append(Spacer(1, 25))

    story.append(Paragraph("<b>Under the Guidance of :</b><br/>Prof. Sheela Satav", center_text))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 2: CERTIFICATE OF APPROVAL
    # =========================================================================
    if os.path.exists(LOGO_PATH):
        story.append(Spacer(1, 10))
        story.append(Image(LOGO_PATH, width=150, height=50))
    story.append(Spacer(1, 15))
    story.append(Paragraph("<b>G H Raisoni International Skill Tech University.</b><br/><b>PUNE-412207</b>", center_bold))
    story.append(Spacer(1, 20))
    story.append(Paragraph("<u><b>CERTIFICATE</b></u>", title_main))
    story.append(Spacer(1, 25))

    cert_text = (
        "This is to certify that <b>Mr. Akash rana (Roll No: ISTU25010120004)</b> and "
        "<b>Mr. Shreyash katke (Roll No: ISTU25010120003)</b>, students of <b>SY BBA CA</b>, "
        "have satisfactorily completed their Project entitled <b>“CampusAI: College Assistant Chatbot”</b> "
        "and submitted this project report in partial fulfillment of the requirements for "
        "the award of the degree of <b>BBA CA</b> for the academic Year <b>2025-26</b>."
    )
    story.append(Paragraph(cert_text, body))
    story.append(Spacer(1, 40))

    cert_signs = [
        [Paragraph("Date: ________________________", td), Paragraph("<b>Project Guide</b><br/>Prof. Sheela Satav", td_center)],
        [Spacer(1, 50), Spacer(1, 50)],
        [Paragraph("__________________________<br/><b>Internal Examiner</b>", td_center), Paragraph("__________________________<br/><b>External Examiner</b>", td_center)],
        [Spacer(1, 45), Spacer(1, 45)],
        [Paragraph("__________________________<br/><b>HOD</b>", td_center), Paragraph("__________________________<br/><b>Dean</b>", td_center)],
    ]
    t_cert = Table(cert_signs, colWidths=[240, 240])
    t_cert.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ]))
    story.append(t_cert)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 3: ACKNOWLEDGEMENT
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<u><b>ACKNOWLEDGEMENT</b></u>", title_main))
    story.append(Spacer(1, 20))

    ack_p1 = (
        "A successful project is always the result of sincere teamwork, persistent dedication, and the collective guidance "
        "of esteemed mentors who provided technical insights and inspiration throughout our development journey."
    )
    ack_p2 = (
        "First and foremost, we would like to express our deepest gratitude to our <b>Honourable Vice Chancellor</b> for "
        "providing us the opportunity and state-of-the-art technological infrastructure to study and innovate at <b>G H "
        "Raisoni International Skill Tech University, Pune</b>."
    )
    ack_p3 = (
        "We are immensely grateful and indebted to our project guide, <b>Prof. Sheela Satav</b>, for her invaluable advice, "
        "constant encouragement, rigorous scrutiny, and technical assistance during the design and implementation of "
        "the <i>CampusAI: College Assistant Chatbot</i>. Her profound insights into software engineering standards, natural "
        "language processing pipelines, and web security architectures helped us overcome key challenges in query classification "
        "and zero-hallucination guardrail design."
    )
    ack_p4 = (
        "We also extend our sincere appreciation to the <b>Head of Department (HOD)</b>, respected faculty members, "
        "laboratory staff, and academic coordinators for their sustained cooperation and resources during the project "
        "lifecycle."
    )
    ack_p5 = (
        "Last but not least, we express our heartfelt gratitude to the Almighty and our parents for their unconditional "
        "blessings, patience, and moral support, without which this academic endeavor would not have been possible."
    )
    for p in [ack_p1, ack_p2, ack_p3, ack_p4, ack_p5]:
        story.append(Paragraph(p, body))
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 35))
    story.append(Paragraph("<b>Signature of Students:</b>", ParagraphStyle('SignHead', fontName='Times-Bold', fontSize=10, alignment=TA_RIGHT)))
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>Akash rana (ISTU25010120004)</b><br/><b>Shreyash katke (ISTU25010120003)</b>", ParagraphStyle('SignBody', fontName='Times-Bold', fontSize=10, alignment=TA_RIGHT, leading=15)))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 4: ABSTRACT
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<u><b>ABSTRACT</b></u>", title_main))
    story.append(Spacer(1, 20))

    abs_p1 = (
        "In modern higher educational environments, accessing real-time, authoritative academic information remains a "
        "persistent operational challenge for students and administrative personnel alike. Collegiate administrative counters "
        "are inundated with hundreds of recurring student queries regarding admissions eligibility, course curricula, "
        "semester fee schedules, examination timetables, library policies, and campus facilities. Traditional inquiry channels "
        "—such as in-person administrative visits, telephone switchboards, and static PDF notice boards—suffer from working-hour "
        "constraints (10:00 AM to 5:00 PM), prolonged physical queues, and poor mobile searchability."
    )
    abs_p2 = (
        "To resolve these systemic bottlenecks, <b>CampusAI (AI-Powered College Assistant Chatbot)</b> has been conceptualized "
        "and engineered as an intelligent, conversational, full-stack web application designed to deliver instantaneous, "
        "verified institutional assistance 24/7. Developed using <b>Python (Flask)</b>, <b>SQLite (Third Normal Form - 3NF)</b>, "
        "<b>HTML5</b>, <b>CSS3</b>, and asynchronous <b>JavaScript (Fetch API)</b>, CampusAI delivers sub-second response times (<300ms)."
    )
    abs_p3 = (
        "The centerpiece architectural innovation of CampusAI is its <b>Dual-Tier Hybrid Query Evaluation Engine</b>: "
        "Tier-1 employs text normalization, stop-word filtering, domain synonym expansion, and Jaccard similarity scoring to match "
        "against verified college FAQs stored in SQLite. If conversational ambiguity necessitates, Tier-2 intelligently routes the "
        "query to a context-bounded Large Language Model (Google Gemini API). A strict <b>Zero-Hallucination Policy</b> ensures that the "
        "chatbot never fabricates fee figures, dates, or institutional rules—gracefully referring students to official office contacts "
        "if verified information is unavailable."
    )
    abs_p4 = (
        "Furthermore, CampusAI provides an interactive, searchable FAQ directory with dynamic category filtering and an "
        "authenticated <b>Admin Command Center</b> secured with salted <b>PBKDF2:SHA256</b> password hashing. Administrative coordinators "
        "can execute real-time CRUD operations on FAQs, audit query logs, and inspect telemetry KPIs with zero server downtime. "
        "The automated test suite achieved a 100% pass rate across all 23 unit, security, and integration test cases."
    )
    for p in [abs_p1, abs_p2, abs_p3, abs_p4]:
        story.append(Paragraph(p, body))
        story.append(Spacer(1, 4))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 5: TABLE OF CONTENT (PART 1)
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<u><b>TABLE OF CONTENT</b></u>", title_main))
    story.append(Spacer(1, 15))

    toc1_data = [
        [Paragraph("<b>Sr No</b>", th), Paragraph("<b>Topic</b>", th), Paragraph("<b>Page No</b>", th)],
        [Paragraph("1", td_center), Paragraph("Introduction", td), Paragraph("1", td_center)],
        [Paragraph("2", td_center), Paragraph("Problem Definition", td), Paragraph("2", td_center)],
        [Paragraph("3", td_center), Paragraph("Existing System & Need for New System", td), Paragraph("3", td_center)],
        [Paragraph("4", td_center), Paragraph("Scope of System", td), Paragraph("4", td_center)],
        [Paragraph("5", td_center), Paragraph("Feasibility Study", td), Paragraph("5", td_center)],
        [Paragraph("6", td_center), Paragraph("Hardware Requirements", td), Paragraph("6", td_center)],
        [Paragraph("7", td_center), Paragraph("Software Requirements", td), Paragraph("7", td_center)],
        [Paragraph("8", td_center), Paragraph("Requirement Analysis", td), Paragraph("8", td_center)],
        [Paragraph("9", td_center), Paragraph("Decision Table (Dual-Tier Query Routing)", td), Paragraph("9", td_center)],
        [Paragraph("10", td_center), Paragraph("Decision Tree (Zero-Hallucination Guard)", td), Paragraph("10", td_center)],
        [Paragraph("11", td_center), Paragraph("Normalized Database Design (3NF) — Admins & FAQs Tables", td), Paragraph("11", td_center)],
        [Paragraph("12", td_center), Paragraph("Normalized Database Design (3NF) — Chat Messages & Query Logs Tables", td), Paragraph("12", td_center)],
        [Paragraph("13", td_center), Paragraph("System Architecture Diagram", td), Paragraph("13", td_center)],
        [Paragraph("14", td_center), Paragraph("ER Diagram", td), Paragraph("14", td_center)],
        [Paragraph("15", td_center), Paragraph("Use Case Diagram", td), Paragraph("15", td_center)],
        [Paragraph("16", td_center), Paragraph("Class Diagram", td), Paragraph("16", td_center)],
        [Paragraph("17", td_center), Paragraph("Object Diagram", td), Paragraph("17", td_center)],
        [Paragraph("18", td_center), Paragraph("Sequence Diagram", td), Paragraph("18", td_center)],
    ]
    t_toc1 = Table(toc1_data, colWidths=[55, 375, 60])
    t_toc1.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1e1b4b")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#334155")),
        ('TOPPADDING', (0, 0), (-1, -1), 4.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4.5),
    ]))
    story.append(t_toc1)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 6: TABLE OF CONTENT (CONTD.)
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<u><b>TABLE OF CONTENT (CONTD.)</b></u>", title_main))
    story.append(Spacer(1, 15))

    toc2_data = [
        [Paragraph("<b>Sr No</b>", th), Paragraph("<b>Topic</b>", th), Paragraph("<b>Page No</b>", th)],
        [Paragraph("19", td_center), Paragraph("Activity Diagram (Query Processing Lifecycle)", td), Paragraph("19", td_center)],
        [Paragraph("20", td_center), Paragraph("Component Diagram", td), Paragraph("20", td_center)],
        [Paragraph("21", td_center), Paragraph("Data Flow Diagram (DFD Level 0 & Level 1)", td), Paragraph("21", td_center)],
        [Paragraph("22", td_center), Paragraph("Data Flow Diagram (DFD Level 2: NLP Matcher Pipeline)", td), Paragraph("22", td_center)],
        [Paragraph("23", td_center), Paragraph("Home Screen UI", td), Paragraph("23", td_center)],
        [Paragraph("24", td_center), Paragraph("Student Portal & Chatbot Interface UI", td), Paragraph("24", td_center)],
        [Paragraph("25", td_center), Paragraph("Searchable FAQ Directory & Accordion UI", td), Paragraph("25", td_center)],
        [Paragraph("26", td_center), Paragraph("Admin Command Center & Management Dashboard UI", td), Paragraph("26", td_center)],
        [Paragraph("27", td_center), Paragraph("Testing & Implementation (23 Automated Test Cases)", td), Paragraph("27", td_center)],
        [Paragraph("28", td_center), Paragraph("Drawbacks & Limitations", td), Paragraph("28", td_center)],
        [Paragraph("29", td_center), Paragraph("Proposed Enhancements", td), Paragraph("29", td_center)],
        [Paragraph("30", td_center), Paragraph("Conclusion", td), Paragraph("30", td_center)],
        [Paragraph("31", td_center), Paragraph("Bibliography", td), Paragraph("31", td_center)],
    ]
    t_toc2 = Table(toc2_data, colWidths=[55, 375, 60])
    t_toc2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1e1b4b")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#334155")),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(t_toc2)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 7: 1. INTRODUCTION (Page 1)
    # =========================================================================
    story.append(Paragraph("<u><b>INTRODUCTION :</b></u>", h1))
    story.append(Paragraph(
        "In today's fast-changing and competitive higher education landscape, university campuses are vibrant hubs of academic, "
        "extracurricular, and administrative activities. Institutions cater to thousands of students across diverse disciplines "
        "including Computer Applications, Information Technology, Engineering, Management, and Sciences. With such scale comes a "
        "massive volume of recurring student inquiries regarding admission eligibility, semester fees, lecture timetables, "
        "examination schedules, syllabus details, faculty contacts, and campus facility availability.",
        body
    ))
    story.append(Paragraph(
        "Traditional university helpdesks and administrative inquiry counters are heavily overburdened, leading to long queues, delayed "
        "responses, and student dissatisfaction. Staff members are repeatedly engaged in answering identical routine questions "
        "(e.g., <i>\"What is the last date for fee payment?\"</i> or <i>\"How do I apply for internal exams?\"</i>), detracting from "
        "critical administrative duties. Furthermore, conventional student portals are often text-heavy, non-intuitive on mobile devices, "
        "and require multiple navigation steps to locate basic institutional details.",
        body
    ))
    story.append(Paragraph(
        "With the rapid emergence of Artificial Intelligence (AI) and Natural Language Processing (NLP), conversational AI assistants "
        "have transformed modern user experiences. AI-powered chatbots provide round-the-clock, real-time, interactive responses, "
        "democratizing information access while reducing administrative overhead. By analyzing user intent from free-form text inputs, "
        "intelligent agents can instantly locate relevant knowledge records and provide verified, context-aware answers.",
        body
    ))
    story.append(Paragraph(
        "<b>CampusAI</b> is specifically designed as an authoritative digital concierge and intelligent knowledge base system for college "
        "students. It serves as an institutional digital guide, bridging the communication gap between students and university authorities. "
        "The system centralizes campus inquiries across Admissions, Courses, Fees, Examinations, Facilities, and General Policies, providing "
        "instantaneous verified responses while strictly preventing artificial intelligence hallucinations.",
        body
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 8: 2. PROBLEM DEFINITION (Page 2)
    # =========================================================================
    story.append(Paragraph("<u><b>PROBLEM DEFINITION :</b></u>", h1))
    story.append(Paragraph(
        "In modern collegiate environments, students face notable hurdles in retrieving accurate, prompt, and verified academic "
        "information. During peak admission windows, semester exam enrollments, and fee payment deadlines, physical administrative desks "
        "become severe operational bottlenecks.",
        body
    ))
    story.append(Paragraph(
        "A critical vulnerability in contemporary campus inquiry systems lies in the dispersion and fragmentation of academic data. "
        "Important notices, fee circulars, examination guidelines, and holiday notices are scattered across physical noticeboards, "
        "buried inside multi-page PDF documents, or uploaded to siloed departmental web pages. Students frequently fail to locate these "
        "circulars in a timely manner, resulting in missed administrative deadlines, late fee penalties, and unnecessary academic anxiety.",
        body
    ))
    story.append(Paragraph("Furthermore, traditional campus inquiry mechanisms suffer from distinct structural limitations:", body))
    story.append(Paragraph("• <b>Administrative Queue Bottlenecks:</b> Student inquiry desks are accessible only during fixed office hours (10:00 AM to 5:00 PM), leaving evening, weekend, and holiday queries completely unattended.", bullet))
    story.append(Paragraph("• <b>The \"Hallucination\" Threat of Generic AI:</b> While off-the-shelf generative chatbots (such as raw ChatGPT or standard LLM wrappers) offer conversational fluency, they frequently hallucinate incorrect fee amounts, wrong exam dates, and non-existent college rules, causing severe administrative liabilities.", bullet))
    story.append(Paragraph("• <b>Absence of Real-Time Knowledge Governance:</b> When college policies, fee structures, or exam schedules are updated, notifying students instantaneously requires manual website redeployments or physical circular distribution.", bullet))
    story.append(Paragraph("• <b>Lack of Centralized Telemetry & Audit:</b> Administrative coordinators lack unified telemetry to track trending student inquiries, unresolved questions, or peak inquiry hours in downloadable report formats.", bullet))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 9: 3. EXISTING SYSTEM & NEED FOR NEW SYSTEM (Page 3)
    # =========================================================================
    story.append(Paragraph("<u><b>EXISTING SYSTEM :</b></u>", h1))
    story.append(Paragraph(
        "The existing information dissemination framework at the university relies primarily on traditional methods: physical "
        "noticeboards, in-person administrative visits, telephone inquiries, and static enterprise ERP web pages. Inquiries regarding "
        "admissions eligibility, fee schedules, examination timetables, and campus facilities require students to physically visit the "
        "administration block or call departmental helplines during working hours.",
        body
    ))
    story.append(Paragraph(
        "When circulars are issued, administrative personnel print physical copies and post them outside HOD offices or upload static PDF "
        "scans to an unindexed webpage archive. There is no automated, conversational self-service portal where a student can type their "
        "query in natural language and instantly obtain verified answers. Overall, the existing approach is time-consuming, prone to "
        "delays, labor-intensive, and non-interactive.",
        body
    ))
    story.append(Paragraph("<u><b>NEED FOR NEW SYSTEM :</b></u>", h1))
    story.append(Paragraph(
        "Modern students expect immediate, mobile-first, conversational digital services. To eliminate operational inefficiencies and "
        "provide round-the-clock accessibility, an intelligent software solution is required. The key motivations for developing the new "
        "system include:",
        body
    ))
    story.append(Paragraph("• <b>Instant 24/7 Availability:</b> Immediate answers to frequent college inquiries without queuing or calling staff.", bullet))
    story.append(Paragraph("• <b>Dual-Tier Hybrid Query Evaluation:</b> Unifying fast deterministic database matching with context-bounded LLM fallback for nuanced inquiries.", bullet))
    story.append(Paragraph("• <b>Zero-Hallucination Academic Integrity:</b> Strict programmatic safeguards ensuring the system never invents dates, fees, or policy rules.", bullet))
    story.append(Paragraph("• <b>Interactive Knowledge Directory:</b> A clean, categorized FAQ accordion allowing students to browse questions or search in real time.", bullet))
    story.append(Paragraph("• <b>Administrative Governance & Reporting:</b> An admin console with salted password encryption for instant CRUD updates and telemetry monitoring.", bullet))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 10: 4. SCOPE OF SYSTEM (Page 4)
    # =========================================================================
    story.append(Paragraph("<u><b>SCOPE OF SYSTEM :</b></u>", h1))
    story.append(Paragraph(
        "The primary scope of <b>CampusAI</b> is to establish an intelligent, reliable, and accessible conversational platform that "
        "simplifies campus navigation, resolves academic queries, and automates administrative knowledge governance. The system serves "
        "as a 24/7 virtual assistant for prospective applicants, enrolled students, faculty, and administrators.",
        body
    ))
    story.append(Paragraph("The major functional scope of the system includes:", body))
    story.append(Paragraph("• <b>Admissions & Eligibility Assistance:</b> Instant guidance on eligibility requirements, entrance criteria, application procedure, required documents, and reservation policies.", bullet))
    story.append(Paragraph("• <b>Course & Curriculum Information:</b> Comprehensive details on undergraduate and postgraduate degree programs, semester credit distribution, elective choices, and syllabus structure.", bullet))
    story.append(Paragraph("• <b>Fee Structures & Payment Guidelines:</b> Authoritative fee breakdowns, installment schedules, scholarship options, and administrative payment modes.", bullet))
    story.append(Paragraph("• <b>Examinations & Academic Notices:</b> Schedules for mid-term tests, final university semester exams, hall ticket distribution, and re-evaluation circulars.", bullet))
    story.append(Paragraph("• <b>Campus Facilities & Amenities:</b> Operational guidelines for the central library, computer labs, hostel accommodation, sports grounds, cafeteria, and student clubs.", bullet))
    story.append(Paragraph("• <b>General Policies & Timings:</b> College office working hours, public holidays, transportation routes, and emergency contact details.", bullet))
    story.append(Paragraph("• <b>Zero-Hallucination Safeguard:</b> Automatic detection of out-of-scope inquiries with courteous referral to official college office desks.", bullet))
    story.append(Paragraph("• <b>Administrative Control & Live Reflection:</b> Real-time FAQ authoring, modification, and deletion reflected instantly in student chat sessions without server restarts.", bullet))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 11: 5. FEASIBILITY STUDY (Page 5)
    # =========================================================================
    story.append(Paragraph("<u><b>FEASIBILITY STUDY :</b></u>", h1))
    story.append(Paragraph(
        "Before initiating software development, a thorough feasibility study was conducted to evaluate the technical, economic, "
        "operational, and time viability of the CampusAI project. The findings are summarized below:",
        body
    ))
    story.append(Paragraph("1. Technical Feasibility :", h2))
    story.append(Paragraph(
        "The project is highly feasible technically. The system is architected using established, robust technologies including Python 3.10+, "
        "Flask 3.1, SQLite 3, HTML5, CSS3, ES6 JavaScript, and the Google GenAI SDK. These technologies are open-source, well-documented, "
        "cross-platform, and boast strong developer community support. The modular architecture ensures that NLP keyword matching and database "
        "queries execute locally with sub-second latency (<300ms) on standard computer hardware.",
        body
    ))
    story.append(Paragraph("2. Economic Feasibility :", h2))
    story.append(Paragraph(
        "The system is exceptionally cost-effective. Built entirely upon open-source software, libraries, and frameworks, there are zero "
        "third-party licensing fees or proprietary software costs. The lightweight SQLite database and Flask server run efficiently on existing "
        "university intranet infrastructure or low-cost cloud hosting (such as Render.com or PythonAnywhere) without requiring expensive GPU clusters.",
        body
    ))
    story.append(Paragraph("3. Operational Feasibility :", h2))
    story.append(Paragraph(
        "Operationally, the solution seamlessly integrates into daily campus routines. Students interact through a clean, conversational web "
        "interface accessible across laptops, tablets, and smartphones without needing to install dedicated apps. For administrative staff, "
        "the intuitive admin command center enables effortless FAQ updates without specialized technical training.",
        body
    ))
    story.append(Paragraph("4. Time Feasibility :", h2))
    story.append(Paragraph(
        "The project development was structured into incremental milestone phases (Analysis, Schema Design, Core NLP Engine, AI Service Layer, "
        "Admin Portal, Automated Testing) across the academic semester, successfully concluding within the stipulated timeline for Semester III, 2025-26.",
        body
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 12: 6. HARDWARE REQUIREMENTS (Page 6)
    # =========================================================================
    story.append(Paragraph("<u><b>HARDWARE REQUIREMENTS :</b></u>", h1))
    story.append(Paragraph(
        "The development, hosting, and client-side execution of the CampusAI system require standard, widely available hardware components. "
        "Because the system is built as a lightweight web application with an optimized Python backend, it does not demand high-end computing "
        "clusters or specialized accelerators.",
        body
    ))

    hw_table_data = [
        [Paragraph("<b>Component</b>", th), Paragraph("<b>Minimum Specification</b>", th), Paragraph("<b>Recommended Specification</b>", th)],
        [Paragraph("Processor", td), Paragraph("Intel Core i3 (6th Gen) / AMD Ryzen 3 / Apple M1", td), Paragraph("Intel Core i5 / AMD Ryzen 5 / Apple M2/M3", td)],
        [Paragraph("System RAM", td), Paragraph("4 GB RAM", td), Paragraph("8 GB or 16 GB DDR4/DDR5", td)],
        [Paragraph("Storage Disk", td), Paragraph("256 GB SSD / HDD with min. 1 GB free space", td), Paragraph("512 GB NVMe SSD", td)],
        [Paragraph("System Architecture", td), Paragraph("64-bit x86 or ARM64 Architecture", td), Paragraph("64-bit ARM64 / x86_64", td)],
        [Paragraph("Input Devices", td), Paragraph("Standard Keyboard & Optical Mouse / Touchscreen", td), Paragraph("Standard Keyboard & Precision Trackpad", td)],
        [Paragraph("Output Devices", td), Paragraph("Color Display Monitor (1366x768 min resolution)", td), Paragraph("Full HD Display (1920x1080 resolution)", td)],
        [Paragraph("Network Interface", td), Paragraph("Standard 3G/4G/5G or Wi-Fi Adapter (10 Mbps)", td), Paragraph("Broadband / Gigabit Ethernet (100 Mbps+)", td)]
    ]
    t_hw = Table(hw_table_data, colWidths=[110, 185, 185])
    t_hw.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1e1b4b")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#334155")),
        ('TOPPADDING', (0, 0), (-1, -1), 4.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4.5),
    ]))
    story.append(t_hw)
    story.append(Spacer(1, 15))
    story.append(Paragraph(
        "Standard institutional lab workstations, student personal laptops, and mobile smartphones easily satisfy these criteria. "
        "The client-side footprint is strictly browser-based, ensuring zero hardware installation barriers for end users.",
        body
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 13: 7. SOFTWARE REQUIREMENTS (Page 7)
    # =========================================================================
    story.append(Paragraph("<u><b>SOFTWARE REQUIREMENTS :</b></u>", h1))
    story.append(Paragraph(
        "The CampusAI system is developed using modern, cross-platform software technologies designed for high responsiveness, "
        "maintainability, and data security. The entire software stack is composed of proven open-source frameworks:",
        body
    ))

    sw_table_data = [
        [Paragraph("<b>Category</b>", th), Paragraph("<b>Software Tool / Technology Used</b>", th)],
        [Paragraph("Operating System", td), Paragraph("macOS Sonoma / Sequoia, Windows 10/11 (64-bit), or Ubuntu Linux 22.04 LTS", td)],
        [Paragraph("Frontend Technologies", td), Paragraph("Semantic HTML5, Responsive CSS3 (Custom Variables, Flexbox/Grid), Modern ES6 JavaScript", td)],
        [Paragraph("Backend Framework", td), Paragraph("Python 3.10+ with Flask 3.1 Micro-framework (WSGI Compliant)", td)],
        [Paragraph("Database Engine", td), Paragraph("SQLite 3 (ACID-compliant, embedded relational database) with SQLAlchemy ORM", td)],
        [Paragraph("Security & Hashing", td), Paragraph("Werkzeug Security (Salted PBKDF2:SHA256 Cryptographic Password Hashes)", td)],
        [Paragraph("AI Generative Layer", td), Paragraph("Google GenAI SDK (`google-genai` 2.23.0+) calling Gemini 2.5/3.8 Flash", td)],
        [Paragraph("Development Editor", td), Paragraph("Visual Studio Code (VS Code) / Antigravity IDE with Python & HTML extensions", td)],
        [Paragraph("Web Browsers", td), Paragraph("Google Chrome 110+, Microsoft Edge 110+, Apple Safari 16+, Mozilla Firefox 115+", td)],
        [Paragraph("WSGI Server", td), Paragraph("Python Werkzeug Development Server / Gunicorn 26.2+ Production WSGI", td)],
        [Paragraph("Version Control", td), Paragraph("Git Distributed Version Control & GitHub Repository Cloud Hosting", td)],
        [Paragraph("Automated Testing", td), Paragraph("Python standard `unittest` framework (23 Automated Unit & Integration Tests)", td)]
    ]
    t_sw = Table(sw_table_data, colWidths=[140, 340])
    t_sw.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1e1b4b")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#334155")),
        ('TOPPADDING', (0, 0), (-1, -1), 4.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4.5),
    ]))
    story.append(t_sw)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 14: 8. REQUIREMENT ANALYSIS (Page 8)
    # =========================================================================
    story.append(Paragraph("<u><b>REQUIREMENT ANALYSIS :</b></u>", h1))
    story.append(Paragraph(
        "Requirement analysis is a vital software engineering phase where user expectations, system capabilities, and operational "
        "constraints are defined. For CampusAI, requirements were derived by evaluating daily student inquiries at the university and "
        "classifying them into functional and non-functional specifications.",
        body
    ))
    story.append(Paragraph("1. Functional Requirements :", h2))
    story.append(Paragraph("• <b>Natural Language Processing:</b> The system must accept free-form natural language text queries, normalize punctuation, eliminate stop words, and expand domain synonyms.", bullet))
    story.append(Paragraph("• <b>Dual-Tier Query Routing:</b> High-confidence matches (score >= 0.45) must return database FAQs immediately; low-confidence queries must route through context-bounded Gemini LLM fallback.", bullet))
    story.append(Paragraph("• <b>Zero-Hallucination Guardrail:</b> The system must refuse to invent fees, dates, or contact details, referring students to official college office contacts.", bullet))
    story.append(Paragraph("• <b>Interactive Question Chips:</b> The system must render one-click recommendation chips to guide students toward common queries.", bullet))
    story.append(Paragraph("• <b>Searchable FAQ Directory:</b> The system must provide a categorized accordion FAQ directory with real-time keyword search.", bullet))
    story.append(Paragraph("• <b>Admin Authentication & CRUD:</b> Administrative coordinators must authenticate via PBKDF2:SHA256 password hashing and execute full CRUD operations on FAQs.", bullet))

    story.append(Paragraph("2. Non-Functional Requirements :", h2))
    story.append(Paragraph("• <b>Performance & Latency:</b> Database-matched responses must return within 300 milliseconds under standard server loads.", bullet))
    story.append(Paragraph("• <b>Availability & Reliability:</b> The system must provide 99.9% uptime during semester exam and admission periods, degrading gracefully to local NLP during internet disruptions.", bullet))
    story.append(Paragraph("• <b>Security & Data Integrity:</b> Passwords must never be stored in plaintext; SQL injection risks must be mitigated via SQLAlchemy parameterized ORM queries.", bullet))
    story.append(Paragraph("• <b>Usability & Responsiveness:</b> The web interface must be clean, mobile-first, and fully responsive across smartphones, tablets, and desktop displays.", bullet))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 15: 9. DECISION TABLE (Page 9)
    # =========================================================================
    story.append(Paragraph("<u><b>DECISION TABLE :</b></u>", h1))
    story.append(Paragraph(
        "The decision table below formalizes the core query routing logic implemented by the CampusAI orchestrator. "
        "It specifies the input conditions evaluated during each conversational turn and maps them directly to the corresponding "
        "subsystem actions executed by the dual-tier engine.",
        body
    ))

    dt_data = [
        [Paragraph("<b>Conditions Evaluated</b>", th), Paragraph("<b>Case 1<br/>(Direct Match)</b>", th), Paragraph("<b>Case 2<br/>(AI Fallback)</b>", th), Paragraph("<b>Case 3<br/>(AI Outage)</b>", th), Paragraph("<b>Case 4<br/>(Out-of-Scope)</b>", th)],
        [Paragraph("Jaccard Overlap Score S >= 0.45", td), Paragraph("Yes", td_center), Paragraph("No", td_center), Paragraph("No", td_center), Paragraph("No", td_center)],
        [Paragraph("Gemini AI API Key Configured & Online", td), Paragraph("Irrelevant", td_center), Paragraph("Yes", td_center), Paragraph("No / Error", td_center), Paragraph("Yes", td_center)],
        [Paragraph("Query Semantics Within College Domain", td), Paragraph("Yes", td_center), Paragraph("Yes", td_center), Paragraph("Yes", td_center), Paragraph("No", td_center)],
        [Paragraph("Factual Academic Answer Available in DB", td), Paragraph("Yes", td_center), Paragraph("Context Found", td_center), Paragraph("Partial", td_center), Paragraph("No", td_center)],
        [Paragraph("<b>ACTIONS EXECUTED BY SYSTEM</b>", ParagraphStyle('ActH', fontName='Times-Bold', fontSize=8, textColor=colors.HexColor("#1e1b4b"))), Paragraph("—", td_center), Paragraph("—", td_center), Paragraph("—", td_center), Paragraph("—", td_center)],
        [Paragraph("Return Authoritative Database FAQ Answer (<20ms)", td), Paragraph("<b>YES</b>", td_center), Paragraph("No", td_center), Paragraph("Best Guess", td_center), Paragraph("No", td_center)],
        [Paragraph("Execute Bounded Generative Synthesis (Gemini)", td), Paragraph("No", td_center), Paragraph("<b>YES</b>", td_center), Paragraph("No", td_center), Paragraph("Attempted", td_center)],
        [Paragraph("Trigger Zero-Hallucination College Office Referral", td), Paragraph("No", td_center), Paragraph("No", td_center), Paragraph("Fallback", td_center), Paragraph("<b>YES</b>", td_center)],
        [Paragraph("Render Formatted Bubble with Suggestion Chips", td), Paragraph("Yes", td_center), Paragraph("Yes", td_center), Paragraph("Yes", td_center), Paragraph("Yes", td_center)],
        [Paragraph("Persist Turn to SQLite Store (`chat_messages`)", td), Paragraph("Yes", td_center), Paragraph("Yes", td_center), Paragraph("Yes", td_center), Paragraph("Yes", td_center)],
    ]
    t_dt = Table(dt_data, colWidths=[170, 75, 75, 80, 80])
    t_dt.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1e1b4b")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#334155")),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('BACKGROUND', (0, 5), (-1, 5), colors.HexColor("#e2e8f0")),
    ]))
    story.append(t_dt)
    story.append(Spacer(1, 15))
    story.append(Paragraph(
        "<b>Rule Summary:</b> Case 1 achieves sub-20ms instant responses for verified FAQs. Case 2 handles nuanced rephrasings with factual "
        "context bounding. Case 3 ensures offline resilience without server crashes. Case 4 enforces strict zero-hallucination compliance.",
        body
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 16: 10. DECISION TREE (Page 10)
    # =========================================================================
    story.append(Paragraph("<u><b>DECISION TREE :</b></u>", h1))
    dt_img = os.path.join(IMG_DIR, "campusai_decision_tree.png")
    if os.path.exists(dt_img):
        story.append(Image(dt_img, width=460, height=520))
    else:
        story.append(Paragraph("[Decision Tree Diagram Image]", center_bold))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 17: 11. 3NF DATABASE DESIGN — ADMINS & FAQS (Page 11)
    # =========================================================================
    story.append(Paragraph("<u><b>NORMALIZED DATABASE DESIGN (3NF) :</b></u>", h1))
    story.append(Paragraph(
        "To ensure high relational data integrity, eliminate data anomalies (insertion, update, and deletion anomalies), and optimize "
        "search query latency, the database is normalized to Third Normal Form (3NF). Every non-key attribute is strictly functionally "
        "dependent upon the primary key alone.",
        body
    ))
    story.append(Paragraph("ADMINS TABLE :", h2))
    admin_table = [
        [Paragraph("<b>Column Name</b>", th), Paragraph("<b>Data Type</b>", th), Paragraph("<b>Constraints & Rules</b>", th)],
        [Paragraph("id", td), Paragraph("INTEGER", td), Paragraph("PRIMARY KEY, AUTOINCREMENT", td)],
        [Paragraph("username", td), Paragraph("VARCHAR(80)", td), Paragraph("NOT NULL, UNIQUE, INDEXED", td)],
        [Paragraph("email", td), Paragraph("VARCHAR(120)", td), Paragraph("NOT NULL, UNIQUE, INDEXED", td)],
        [Paragraph("password_hash", td), Paragraph("VARCHAR(255)", td), Paragraph("NOT NULL (Salted PBKDF2:SHA256)", td)],
        [Paragraph("created_at", td), Paragraph("DATETIME", td), Paragraph("NOT NULL, DEFAULT CURRENT_TIMESTAMP", td)]
    ]
    t_adm = Table(admin_table, colWidths=[120, 120, 240])
    t_adm.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1e1b4b")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#334155")),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(t_adm)

    story.append(Spacer(1, 15))
    story.append(Paragraph("COLLEGE INFO (FAQS) TABLE :", h2))
    faqs_table = [
        [Paragraph("<b>Column Name</b>", th), Paragraph("<b>Data Type</b>", th), Paragraph("<b>Constraints & Rules</b>", th)],
        [Paragraph("id", td), Paragraph("INTEGER", td), Paragraph("PRIMARY KEY, AUTOINCREMENT", td)],
        [Paragraph("question", td), Paragraph("TEXT", td), Paragraph("NOT NULL (Indexed for text normalization)", td)],
        [Paragraph("answer", td), Paragraph("TEXT", td), Paragraph("NOT NULL (Authoritative college response)", td)],
        [Paragraph("category", td), Paragraph("VARCHAR(50)", td), Paragraph("NOT NULL, INDEXED ('Admissions', 'Fees', 'Courses', etc.)", td)],
        [Paragraph("created_at", td), Paragraph("DATETIME", td), Paragraph("NOT NULL, DEFAULT CURRENT_TIMESTAMP", td)],
        [Paragraph("updated_at", td), Paragraph("DATETIME", td), Paragraph("NOT NULL, ON UPDATE CURRENT_TIMESTAMP", td)]
    ]
    t_faq = Table(faqs_table, colWidths=[120, 120, 240])
    t_faq.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1e1b4b")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#334155")),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(t_faq)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 18: 12. 3NF DATABASE DESIGN — CHAT & LOGS (Page 12)
    # =========================================================================
    story.append(Paragraph("<u><b>NORMALIZED DATABASE DESIGN (3NF) (CONTD.) :</b></u>", h1))
    story.append(Paragraph("CHAT SESSIONS & MESSAGES TABLE :", h2))
    msg_table = [
        [Paragraph("<b>Column Name</b>", th), Paragraph("<b>Data Type</b>", th), Paragraph("<b>Constraints & Rules</b>", th)],
        [Paragraph("id", td), Paragraph("INTEGER", td), Paragraph("PRIMARY KEY, AUTOINCREMENT", td)],
        [Paragraph("session_id", td), Paragraph("VARCHAR(64)", td), Paragraph("NOT NULL, INDEXED (UUIDv4 Client Token)", td)],
        [Paragraph("role", td), Paragraph("VARCHAR(20)", td), Paragraph("NOT NULL ('student' or 'assistant')", td)],
        [Paragraph("content", td), Paragraph("TEXT", td), Paragraph("NOT NULL (Message payload text)", td)],
        [Paragraph("source", td), Paragraph("VARCHAR(30)", td), Paragraph("DEFAULT 'database' ('database', 'ai', 'fallback')", td)],
        [Paragraph("timestamp", td), Paragraph("DATETIME", td), Paragraph("NOT NULL, DEFAULT CURRENT_TIMESTAMP", td)]
    ]
    t_msg = Table(msg_table, colWidths=[120, 120, 240])
    t_msg.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1e1b4b")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#334155")),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(t_msg)

    story.append(Spacer(1, 15))
    story.append(Paragraph("QUERY TELEMETRY AUDIT LOGS TABLE :", h2))
    log_table = [
        [Paragraph("<b>Column Name</b>", th), Paragraph("<b>Data Type</b>", th), Paragraph("<b>Constraints & Rules</b>", th)],
        [Paragraph("id", td), Paragraph("INTEGER", td), Paragraph("PRIMARY KEY, AUTOINCREMENT", td)],
        [Paragraph("query_text", td), Paragraph("TEXT", td), Paragraph("NOT NULL (Raw student question)", td)],
        [Paragraph("matched_faq_id", td), Paragraph("INTEGER", td), Paragraph("NULLABLE, FOREIGN KEY REFERENCES faqs(id)", td)],
        [Paragraph("confidence", td), Paragraph("FLOAT", td), Paragraph("NOT NULL (Similarity Score 0.0 to 1.0)", td)],
        [Paragraph("source_engine", td), Paragraph("VARCHAR(30)", td), Paragraph("NOT NULL ('nlp_matcher', 'gemini_llm', 'office_referral')", td)],
        [Paragraph("timestamp", td), Paragraph("DATETIME", td), Paragraph("NOT NULL, DEFAULT CURRENT_TIMESTAMP", td)]
    ]
    t_log = Table(log_table, colWidths=[120, 120, 240])
    t_log.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1e1b4b")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#334155")),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(t_log)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 19: 13. SYSTEM ARCHITECTURE (Page 13)
    # =========================================================================
    story.append(Paragraph("<u><b>SYSTEM ARCHITECTURE DIAGRAM :</b></u>", h1))
    arch_img = os.path.join(IMG_DIR, "campusai_architecture.png")
    if os.path.exists(arch_img):
        story.append(Image(arch_img, width=460, height=480))
    else:
        story.append(Paragraph("[System Architecture Diagram]", center_bold))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 20: 14. ER DIAGRAM (Page 14)
    # =========================================================================
    story.append(Paragraph("<u><b>ER DIAGRAM :</b></u>", h1))
    er_img = os.path.join(IMG_DIR, "campusai_er_diagram.png")
    if os.path.exists(er_img):
        story.append(Image(er_img, width=460, height=480))
    else:
        story.append(Paragraph("[ER Diagram Image]", center_bold))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 21: 15. USE CASE DIAGRAM (Page 15)
    # =========================================================================
    story.append(Paragraph("<u><b>USE CASE DIAGRAM :</b></u>", h1))
    uc_img = os.path.join(IMG_DIR, "campusai_use_case.png")
    if os.path.exists(uc_img):
        story.append(Image(uc_img, width=460, height=480))
    else:
        story.append(Paragraph("[Use Case Diagram Image]", center_bold))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 22: 16. CLASS DIAGRAM (Page 16)
    # =========================================================================
    story.append(Paragraph("<u><b>CLASS DIAGRAM :</b></u>", h1))
    cls_img = os.path.join(IMG_DIR, "campusai_class_diagram.png")
    if os.path.exists(cls_img):
        story.append(Image(cls_img, width=460, height=480))
    else:
        story.append(Paragraph("[Class Diagram Image]", center_bold))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 23: 17. OBJECT DIAGRAM (Page 17)
    # =========================================================================
    story.append(Paragraph("<u><b>OBJECT DIAGRAM :</b></u>", h1))
    story.append(Paragraph(
        "The object diagram below models the specific runtime instances, slot values, and active object associations during a live "
        "student inquiry turn in the CampusAI environment:",
        body
    ))
    
    obj_data = [
        [Paragraph("<b>Instance Object</b>", th), Paragraph("<b>Class Type</b>", th), Paragraph("<b>Slot Values & Runtime Attributes</b>", th)],
        [Paragraph("stu_session_914", td), Paragraph("ChatSession", td), Paragraph("session_id = 'c84a2f1e-914b-4b1a'<br/>created_at = '2026-10-27 10:14:02'<br/>active_domain = 'Fees'", td)],
        [Paragraph("msg_turn_104", td), Paragraph("ChatMessage", td), Paragraph("id = 104<br/>session_id = 'c84a2f1e-914b-4b1a'<br/>role = 'student'<br/>content = 'What are BBA (CA) semester fees?'", td)],
        [Paragraph("faq_entity_03", td), Paragraph("FAQ", td), Paragraph("id = 3<br/>question = 'What are the fees for BBA (CA)?'<br/>answer = 'Rs. 45,000 per semester'<br/>category = 'Fees'", td)],
        [Paragraph("matcher_engine", td), Paragraph("FAQService", td), Paragraph("normalized_tokens = {'fee', 'tuition', 'cost', 'bca'}<br/>computed_overlap_score = 0.88<br/>confidence_tier = 'High (Tier 1)'", td)],
        [Paragraph("admin_super", td), Paragraph("Admin", td), Paragraph("id = 1<br/>username = 'akash_admin'<br/>email = 'admin@college.edu'<br/>session_token = 'eyJhbGciOiJIUzI1...'", td)]
    ]
    t_obj = Table(obj_data, colWidths=[120, 110, 250])
    t_obj.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1e1b4b")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#334155")),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(t_obj)
    story.append(Spacer(1, 20))
    story.append(Paragraph(
        "<b>Object Associations:</b> `stu_session_914` contains `msg_turn_104` (Composition); `matcher_engine` references `faq_entity_03` "
        "(Association); `admin_super` manages the collection of `FAQ` entities (Aggregation).",
        body
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 24: 18. SEQUENCE DIAGRAM (Page 18)
    # =========================================================================
    story.append(Paragraph("<u><b>SEQUENCE DIAGRAM :</b></u>", h1))
    seq_img = os.path.join(IMG_DIR, "campusai_sequence_diagram.png")
    if os.path.exists(seq_img):
        story.append(Image(seq_img, width=460, height=480))
    else:
        story.append(Paragraph("[Sequence Diagram Image]", center_bold))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 25: 19. ACTIVITY DIAGRAM (Page 19)
    # =========================================================================
    story.append(Paragraph("<u><b>ACTIVITY DIAGRAM :</b></u>", h1))
    story.append(Paragraph(
        "The activity diagram models the operational workflow and control logic executed when a student dispatches a question:",
        body
    ))
    act_data = [
        [Paragraph("<b>Step No</b>", th), Paragraph("<b>Activity State</b>", th), Paragraph("<b>Subsystem & Branching Logic</b>", th)],
        [Paragraph("1", td_center), Paragraph("Student Submits Query", td), Paragraph("Browser captures keystroke / enter-to-send action", td)],
        [Paragraph("2", td_center), Paragraph("Display Typing Indicator", td), Paragraph("UI renders three-dot animated bounce simulation", td)],
        [Paragraph("3", td_center), Paragraph("Dispatch AJAX HTTP POST", td), Paragraph("Asynchronous `fetch('/api/chat')` sent to Flask", td)],
        [Paragraph("4", td_center), Paragraph("Normalize & Tokenize", td), Paragraph("Lowercase, strip punctuation, remove stop words", td)],
        [Paragraph("5", td_center), Paragraph("Domain Synonym Expansion", td), Paragraph("Expand keywords: fee -> tuition/cost, exam -> test", td)],
        [Paragraph("6", td_center), Paragraph("Jaccard Overlap Evaluation", td), Paragraph("Compute similarity score across all FAQs in SQLite", td)],
        [Paragraph("7", td_center), Paragraph("Decision: Score >= 0.45?", td), Paragraph("[YES] Retrieve verified database answer<br/>[NO] Route to context-bounded Gemini AI API", td)],
        [Paragraph("8", td_center), Paragraph("Format Response JSON", td), Paragraph("Assemble answer, confidence score, and suggested chips", td)],
        [Paragraph("9", td_center), Paragraph("Persist Turn to Database", td), Paragraph("Commit record to `chat_messages` table in SQLite", td)],
        [Paragraph("10", td_center), Paragraph("Render Bubble & Auto-Scroll", td), Paragraph("Remove typing indicator, append card, scroll to bottom", td)]
    ]
    t_act = Table(act_data, colWidths=[55, 160, 265])
    t_act.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1e1b4b")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#334155")),
        ('TOPPADDING', (0, 0), (-1, -1), 4.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4.5),
    ]))
    story.append(t_act)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 26: 20. COMPONENT DIAGRAM (Page 20)
    # =========================================================================
    story.append(Paragraph("<u><b>COMPONENT DIAGRAM :</b></u>", h1))
    story.append(Paragraph(
        "The component diagram details the physical and logical software modules that constitute the CampusAI deployment environment:",
        body
    ))
    comp_spec = [
        [Paragraph("<b>Component Module</b>", th), Paragraph("<b>Runtime Environment</b>", th), Paragraph("<b>Responsibilities & Interfaces</b>", th)],
        [Paragraph("ChatbotUI (Client)", td), Paragraph("Web Browser (Chrome/Safari)", td), Paragraph("HTML5 semantic layout, CSS3 responsive grid, JS Fetch client", td)],
        [Paragraph("FlaskServer (WSGI)", td), Paragraph("Python 3.10+ / Gunicorn", td), Paragraph("HTTP route dispatching, session cookies, CSRF protection", td)],
        [Paragraph("NLP Matcher Engine", td), Paragraph("services/faq_service.py", td), Paragraph("Text normalization, synonym expansion, Jaccard similarity scoring", td)],
        [Paragraph("AI Service Layer", td), Paragraph("services/ai_service.py", td), Paragraph("Google GenAI client, zero-hallucination prompt bounds", td)],
        [Paragraph("Database Engine", td), Paragraph("SQLite 3 (instance/db)", td), Paragraph("Persistent storage of admins, faqs, messages, and telemetry", td)],
        [Paragraph("Admin Controller", td), Paragraph("Flask Blueprints / REST", td), Paragraph("Protected CRUD endpoints (`/api/admin/*`) with PBKDF2 verification", td)]
    ]
    t_cs = Table(comp_spec, colWidths=[130, 140, 210])
    t_cs.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1e1b4b")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#334155")),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(t_cs)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 27: 21. DATA FLOW DIAGRAM (DFD 0 & 1) (Page 21)
    # =========================================================================
    story.append(Paragraph("<u><b>DATA FLOW DIAGRAM (DFD LEVEL 0 & LEVEL 1) :</b></u>", h1))
    dfd_img = os.path.join(IMG_DIR, "campusai_dfd.png")
    if os.path.exists(dfd_img):
        story.append(Image(dfd_img, width=460, height=480))
    else:
        story.append(Paragraph("[DFD Diagram Image]", center_bold))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 28: 22. DFD LEVEL 2 (NLP PIPELINE) (Page 22)
    # =========================================================================
    story.append(Paragraph("<u><b>DATA FLOW DIAGRAM (DFD LEVEL 2: NLP PIPELINE) :</b></u>", h1))
    story.append(Paragraph(
        "DFD Level 2 decomposes Process 2.0 (Query Evaluation Engine) into its internal algorithmic sub-processes:",
        body
    ))
    dfd2_data = [
        [Paragraph("<b>Sub-Process ID</b>", th), Paragraph("<b>Algorithmic Function</b>", th), Paragraph("<b>Data Input & Transformation Output</b>", th)],
        [Paragraph("2.1", td_center), Paragraph("Punctuation Stripping & Lowercasing", td), Paragraph("Raw string converted to lowercase; non-alphanumerics replaced with whitespace", td)],
        [Paragraph("2.2", td_center), Paragraph("Stop-Word Elimination", td), Paragraph("Removes common English prepositions ('is', 'the', 'at', 'what', 'are')", td)],
        [Paragraph("2.3", td_center), Paragraph("Collegiate Synonym Expansion", td), Paragraph("Expands canonical domain terms (e.g., 'fee' -> {'tuition', 'cost', 'payment'})", td)],
        [Paragraph("2.4", td_center), Paragraph("Token Set Intersection", td), Paragraph("Calculates intersection set $I = \\tilde{Q} \\cap F_i$ for each FAQ in SQLite", td)],
        [Paragraph("2.5", td_center), Paragraph("Jaccard Overlap Scoring", td), Paragraph("Computes score $S = |I| / |F_i|$; tracks maximum score $S_{max}$ and best FAQ entity", td)],
        [Paragraph("2.6", td_center), Paragraph("Confidence Threshold Gate", td), Paragraph("If $S_{max} \\ge 0.45$, dispatch verified answer; else route to Process 3.0 (AI Layer)", td)]
    ]
    t_d2 = Table(dfd2_data, colWidths=[70, 170, 240])
    t_d2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1e1b4b")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#334155")),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(t_d2)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 29: 23. HOME SCREEN UI (Page 23)
    # =========================================================================
    story.append(Paragraph("<u><b>HOME SCREEN UI :</b></u>", h1))
    ui_home = os.path.join(IMG_DIR, "campusai_ui_home.png")
    if os.path.exists(ui_home):
        story.append(Image(ui_home, width=470, height=310))
    story.append(Spacer(1, 10))
    story.append(Paragraph("UI Architectural Features :", h2))
    story.append(Paragraph("• <b>Navy & Indigo Gradient Banner:</b> Professional tech styling featuring the CampusAI branding and health badge.", bullet))
    story.append(Paragraph("• <b>Dual Call-to-Action (CTA):</b> Direct buttons to \"Start Chatting\" or \"Explore FAQs\".", bullet))
    story.append(Paragraph("• <b>4 Value Pillars:</b> Highlighting 24/7 Availability, Verified Academic Data, Zero Hallucination, and Real-Time Admin Governance.", bullet))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 30: 24. STUDENT PORTAL UI (Page 24)
    # =========================================================================
    story.append(Paragraph("<u><b>STUDENT PORTAL & CHATBOT INTERFACE UI :</b></u>", h1))
    ui_chat = os.path.join(IMG_DIR, "campusai_ui_chat.png")
    if os.path.exists(ui_chat):
        story.append(Image(ui_chat, width=470, height=310))
    story.append(Spacer(1, 10))
    story.append(Paragraph("Interactive Conversational Features :", h2))
    story.append(Paragraph("• <b>Chat Bubbles:</b> Distinct right-aligned indigo bubbles for students and left-aligned white/green cards for the bot.", bullet))
    story.append(Paragraph("• <b>Question Suggestion Chips:</b> One-click chips for popular inquiries (Admissions, Fees, Exam Schedules).", bullet))
    story.append(Paragraph("• <b>Typing Indicator:</b> Animated 3-dot bounce showing cognitive response state during fetch requests.", bullet))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 31: 25. FAQ DIRECTORY UI (Page 25)
    # =========================================================================
    story.append(Paragraph("<u><b>SEARCHABLE FAQ DIRECTORY & ACCORDION UI :</b></u>", h1))
    story.append(Paragraph(
        "The FAQ directory (`templates/faqs.html`) provides students with a structured, self-service knowledge base:",
        body
    ))
    faq_ui_data = [
        [Paragraph("<b>Category Domain</b>", th), Paragraph("<b>Sample FAQ Queries Indexed</b>", th), Paragraph("<b>Direct Chat Action</b>", th)],
        [Paragraph("Admissions", td), Paragraph("Eligibility criteria, BCA cutoffs, application procedure, documents", td), Paragraph("One-Click 'Ask in Chat'", td_center)],
        [Paragraph("Courses", td), Paragraph("BBA (CA) curriculum, syllabus subjects, semester credit distribution", td), Paragraph("One-Click 'Ask in Chat'", td_center)],
        [Paragraph("Fees", td), Paragraph("Tuition fee amount, examination charges, installment deadlines", td), Paragraph("One-Click 'Ask in Chat'", td_center)],
        [Paragraph("Examinations", td), Paragraph("Internal test dates, university semester timetable, hall ticket rules", td), Paragraph("One-Click 'Ask in Chat'", td_center)],
        [Paragraph("Facilities", td), Paragraph("Central library timings, computer laboratories, hostel amenities", td), Paragraph("One-Click 'Ask in Chat'", td_center)],
        [Paragraph("General", td), Paragraph("College administrative office hours, holiday calendar, contact phone", td), Paragraph("One-Click 'Ask in Chat'", td_center)],
    ]
    t_fui = Table(faq_ui_data, colWidths=[100, 270, 110])
    t_fui.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1e1b4b")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#334155")),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(t_fui)
    story.append(Spacer(1, 15))
    story.append(Paragraph("• <b>Real-Time Search Bar:</b> Dynamically filters matching accordion cards as the student types each character.", bullet))
    story.append(Paragraph("• <b>Category Filter Pills:</b> Instant single-click filtering across the six primary collegiate domains.", bullet))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 32: 26. ADMIN DASHBOARD UI (Page 26)
    # =========================================================================
    story.append(Paragraph("<u><b>ADMIN COMMAND CENTER & DASHBOARD UI :</b></u>", h1))
    ui_admin = os.path.join(IMG_DIR, "campusai_ui_admin.png")
    if os.path.exists(ui_admin):
        story.append(Image(ui_admin, width=470, height=310))
    story.append(Spacer(1, 10))
    story.append(Paragraph("Administrative Governance Capabilities :", h2))
    story.append(Paragraph("• <b>Live Telemetry KPIs:</b> Displays Total FAQs, Active Categories, Inquiries Answered, and Uptime Health.", bullet))
    story.append(Paragraph("• <b>Real-Time CRUD Modals:</b> Instant authoring, editing, and deletion of FAQs with immediate database commit.", bullet))
    story.append(Paragraph("• <b>Zero-Downtime Synchronization:</b> FAQ edits immediately update student chat sessions without server restarts.", bullet))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 33: 27. TESTING & IMPLEMENTATION (Page 27)
    # =========================================================================
    story.append(Paragraph("<u><b>TESTING AND IMPLEMENTATION :</b></u>", h1))
    story.append(Paragraph(
        "A rigorous automated test suite was constructed using Python's `unittest` framework. All 23 test cases executed successfully "
        "with a 100% pass rate in 1.185 seconds:",
        body
    ))

    test_rows = [
        [Paragraph("<b>Test ID</b>", th), Paragraph("<b>Test Description</b>", th), Paragraph("<b>Route / Input</b>", th), Paragraph("<b>Expected Output</b>", th), Paragraph("<b>Status</b>", th)],
        [Paragraph("TC_01", td_center), Paragraph("Landing Page Accessibility", td), Paragraph("GET /", td), Paragraph("HTTP 200 OK", td), Paragraph("<b>PASS</b>", td_center)],
        [Paragraph("TC_02", td_center), Paragraph("Student Chatbot Interface", td), Paragraph("GET /chat", td), Paragraph("HTTP 200 OK", td), Paragraph("<b>PASS</b>", td_center)],
        [Paragraph("TC_03", td_center), Paragraph("Searchable FAQ Directory", td), Paragraph("GET /faqs", td), Paragraph("HTTP 200 OK", td), Paragraph("<b>PASS</b>", td_center)],
        [Paragraph("TC_04", td_center), Paragraph("Admin Authentication Portal", td), Paragraph("GET /admin/login", td), Paragraph("HTTP 200 OK", td), Paragraph("<b>PASS</b>", td_center)],
        [Paragraph("TC_05", td_center), Paragraph("System Health Telemetry", td), Paragraph("GET /api/health", td), Paragraph("status: 'healthy'", td), Paragraph("<b>PASS</b>", td_center)],
        [Paragraph("TC_06", td_center), Paragraph("List All Seeded FAQs", td), Paragraph("GET /api/faqs", td), Paragraph("20 FAQs array", td), Paragraph("<b>PASS</b>", td_center)],
        [Paragraph("TC_07", td_center), Paragraph("Filter FAQs by Category", td), Paragraph("category='Fees'", td), Paragraph("Fee FAQs only", td), Paragraph("<b>PASS</b>", td_center)],
        [Paragraph("TC_08", td_center), Paragraph("Search FAQs by Keyword", td), Paragraph("q='fees'", td), Paragraph("Matches returned", td), Paragraph("<b>PASS</b>", td_center)],
        [Paragraph("TC_09", td_center), Paragraph("Empty Search Handling", td), Paragraph("q='xyzgibberish'", td), Paragraph("Empty array []", td), Paragraph("<b>PASS</b>", td_center)],
        [Paragraph("TC_10", td_center), Paragraph("Empty Chat Validation", td), Paragraph("message=''", td), Paragraph("HTTP 400 Bad Req", td), Paragraph("<b>PASS</b>", td_center)],
        [Paragraph("TC_11", td_center), Paragraph("Conversational Greeting", td), Paragraph("'hello'", td), Paragraph("Friendly greeting", td), Paragraph("<b>PASS</b>", td_center)],
        [Paragraph("TC_12", td_center), Paragraph("Admissions FAQ Match", td), Paragraph("'how to apply'", td), Paragraph("Admission criteria", td), Paragraph("<b>PASS</b>", td_center)],
        [Paragraph("TC_13", td_center), Paragraph("Fee Structure FAQ Match", td), Paragraph("'what are fees'", td), Paragraph("Rs. 45,000 details", td), Paragraph("<b>PASS</b>", td_center)],
        [Paragraph("TC_14", td_center), Paragraph("Zero-Hallucination Fallback", td), Paragraph("'alien invasion'", td), Paragraph("Office referral", td), Paragraph("<b>PASS</b>", td_center)],
        [Paragraph("TC_15", td_center), Paragraph("AI Outage Degradation", td), Paragraph("Simulated Exception", td), Paragraph("Local FAQ fallback", td), Paragraph("<b>PASS</b>", td_center)],
        [Paragraph("TC_16", td_center), Paragraph("Real-Time FAQ Reflection", td), Paragraph("Create FAQ -> Query", td), Paragraph("Instant new answer", td), Paragraph("<b>PASS</b>", td_center)],
        [Paragraph("TC_17", td_center), Paragraph("Valid Admin Authentication", td), Paragraph("'admin', 'Admin@123'", td), Paragraph("HTTP 200 Session", td), Paragraph("<b>PASS</b>", td_center)],
        [Paragraph("TC_18", td_center), Paragraph("Invalid Password Rejection", td), Paragraph("'admin', 'WrongPass'", td), Paragraph("HTTP 401 Reject", td), Paragraph("<b>PASS</b>", td_center)],
        [Paragraph("TC_19", td_center), Paragraph("Blank Credentials Check", td), Paragraph("'', ''", td), Paragraph("HTTP 400 Bad Req", td), Paragraph("<b>PASS</b>", td_center)],
        [Paragraph("TC_20", td_center), Paragraph("Protected Route Guard", td), Paragraph("GET /admin/dashboard", td), Paragraph("HTTP 302 Redirect", td), Paragraph("<b>PASS</b>", td_center)],
        [Paragraph("TC_21", td_center), Paragraph("Protected Admin API Guard", td), Paragraph("GET /api/admin/stats", td), Paragraph("HTTP 401 Reject", td), Paragraph("<b>PASS</b>", td_center)],
        [Paragraph("TC_22", td_center), Paragraph("Full Admin CRUD Lifecycle", td), Paragraph("POST/PUT/DELETE", td), Paragraph("Full CRUD Success", td), Paragraph("<b>PASS</b>", td_center)],
        [Paragraph("TC_23", td_center), Paragraph("Admin Session Logout", td), Paragraph("POST /api/admin/logout", td), Paragraph("Session Cleared", td), Paragraph("<b>PASS</b>", td_center)],
    ]
    t_test = Table(test_rows, colWidths=[45, 125, 105, 155, 50])
    t_test.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1e1b4b")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#334155")),
        ('TOPPADDING', (0, 0), (-1, -1), 2.2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.2),
    ]))
    story.append(t_test)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 34: 28. DRAWBACKS & LIMITATIONS (Page 28)
    # =========================================================================
    story.append(Paragraph("<u><b>DRAWBACKS AND LIMITATIONS :</b></u>", h1))
    story.append(Paragraph(
        "While CampusAI provides comprehensive, 24/7 college administrative assistance and zero-hallucination factual safety, like any "
        "software system, it operates under certain inherent technical and operational limitations:",
        body
    ))
    story.append(Paragraph("1. Monolingual Semantic Lexicon :", h2))
    story.append(Paragraph(
        "The current deterministic synonym expansion dictionary is tailored primarily for English language queries. If a student uses "
        "highly regional colloquial terms or vernacular languages (such as Marathi or Hindi), the Tier-1 matcher cannot evaluate the query "
        "and must rely on the external LLM layer.",
        body
    ))
    story.append(Paragraph("2. Internet Connectivity Requirement for Generative Fallback :", h2))
    story.append(Paragraph(
        "While deterministic FAQ matching executes locally on the Python Flask server without internet, invoking the Google Gemini API for "
        "Tier-2 conversational fallback requires outbound HTTPS internet access. In the event of network disruption, the system falls back "
        "strictly to local database matching.",
        body
    ))
    story.append(Paragraph("3. Single-Tenant Database Concurrency Constraints :", h2))
    story.append(Paragraph(
        "The application currently deploys SQLite 3 as its persistence store. While exceptionally fast for read-heavy operations, SQLite "
        "employs file-level database locking during concurrent write operations, which could cause latency bottlenecks if thousands of students "
        "simultaneously submit ratings.",
        body
    ))
    story.append(Paragraph("4. Manual FAQ Curation Overhead :", h2))
    story.append(Paragraph(
        "New institutional circulars and policies currently require an administrative coordinator to enter the FAQ via the dashboard. The system "
        "does not autonomously ingest or parse external university circular PDF files.",
        body
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 35: 29. PROPOSED ENHANCEMENTS (Page 29)
    # =========================================================================
    story.append(Paragraph("<u><b>PROPOSED ENHANCEMENTS :</b></u>", h1))
    story.append(Paragraph(
        "To build upon the successful implementation of the CampusAI College Assistant Chatbot, several progressive architectural "
        "enhancements are planned for future versions:",
        body
    ))
    story.append(Paragraph("1. Multilingual Support (Marathi, Hindi & English) :", h2))
    story.append(Paragraph(
        "Recognizing the demographic diversity across Pune and Maharashtra, the natural language understanding engine can be expanded "
        "with IndicNLP tokenizers to support Marathi and Hindi conversational queries and responses, greatly enhancing accessibility for "
        "parents and rural students.",
        body
    ))
    story.append(Paragraph("2. Voice Speech-to-Text & Text-to-Speech Integration :", h2))
    story.append(Paragraph(
        "Integrating browser Web Speech API for voice recognition and server-side text-to-speech voice playback will provide a hands-free, "
        "auditory interface for visually impaired students.",
        body
    ))
    story.append(Paragraph("3. Omnichannel Messaging Webhooks (WhatsApp & Telegram) :", h2))
    story.append(Paragraph(
        "Integrating with WhatsApp Business API and Telegram bot webhooks will allow students to query the college assistant directly through "
        "their preferred instant messaging applications.",
        body
    ))
    story.append(Paragraph("4. Enterprise ERP & Fee Gateway Integration :", h2))
    story.append(Paragraph(
        "Migrating the backend persistence layer from SQLite to PostgreSQL for high-concurrency scaling, and securely integrating with the "
        "college ERP database to answer personalized inquiries (e.g., pending semester fee balances or internal exam grades).",
        body
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 36: 30. CONCLUSION (Page 30)
    # =========================================================================
    story.append(Paragraph("<u><b>CONCLUSION :</b></u>", h1))
    story.append(Paragraph(
        "The <b>CampusAI: Intelligent College Assistant Chatbot</b> has been conceptualized, engineered, and validated as an effective "
        "conversational AI solution addressing critical information distribution challenges at higher educational institutions.",
        body
    ))
    story.append(Paragraph(
        "The platform successfully bridges communication barriers between students and university departments. By automating routine inquiries "
        "regarding admissions eligibility, semester fee schedules, course syllabi, examination timetables, and campus facilities, the chatbot "
        "significantly mitigates administrative desk congestion, allowing administrative staff to dedicate their attention to higher-order governance.",
        body
    ))
    story.append(Paragraph(
        "A standout accomplishment is the implementation of the <b>Dual-Tier Hybrid Query Evaluation Engine</b> combined with a strict "
        "<b>Zero-Hallucination Policy</b>. By guaranteeing that students never receive fabricated dates or fees, CampusAI replaces misinformation "
        "with authoritative institutional facts. High-confidence queries receive sub-20ms instant database matches, while complex phrasings "
        "benefit from context-bounded generative synthesis.",
        body
    ))
    story.append(Paragraph(
        "Coupled with an authenticated administrative control center providing real-time CRUD capabilities and telemetry tracking, the system "
        "establishes a robust technological foundation for next-generation digital campus operations.",
        body
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 37: 31. BIBLIOGRAPHY (Page 31)
    # =========================================================================
    story.append(Paragraph("<u><b>BIBLIOGRAPHY :</b></u>", h1))
    story.append(Spacer(1, 10))

    refs = [
        "1. Sommerville, I. (2015). <i>Software Engineering</i> (10th Edition). Pearson Education.",
        "2. Pressman, R. S., & Maxim, B. R. (2019). <i>Software Engineering: A Practitioner’s Approach</i> (9th Edition). McGraw-Hill.",
        "3. Jurafsky, D., & Martin, J. H. (2023). <i>Speech and Language Processing</i> (3rd Edition). Stanford University / Pearson.",
        "4. Grinberg, M. (2018). <i>Flask Web Development: Developing Web Applications with Python</i> (2nd Edition). O’Reilly Media.",
        "5. Pallets Projects. (2024). <i>Flask Documentation (Version 3.1.x)</i>. Available at: https://flask.palletsprojects.com/",
        "6. SQLAlchemy Authors. (2024). <i>SQLAlchemy 2.0 Documentation</i>. Available at: https://docs.sqlalchemy.org/",
        "7. Google Cloud. (2024). <i>Google GenAI SDK & Gemini API Documentation</i>. Available at: https://ai.google.dev/",
        "8. Myers, G. J., Sandler, C., & Badgett, T. (2011). <i>The Art of Software Testing</i> (3rd Edition). John Wiley & Sons.",
        "9. Beck, K. (2002). <i>Test-Driven Development: By Example</i>. Addison-Wesley Professional.",
        "10. IEEE Computer Society. (2024). <i>SWEBOK: Guide to the Software Engineering Body of Knowledge</i> (Version 4.0). IEEE."
    ]
    for r in refs:
        story.append(Paragraph(r, bullet))
        story.append(Spacer(1, 4))

    doc.build(story, canvasmaker=AcademicNumberedCanvas)
    print(f"[✓] Official 35-page CampusAI report successfully built: {out_path}")


if __name__ == '__main__':
    out_pdf = "/Users/kanishksingh/Downloads/momo ai chat bot /CampusAI_Project_Report.pdf"
    build_akash_report(out_pdf)
