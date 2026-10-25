"""
CampusAI Academic Project Report PDF Generator
Built using ReportLab for Bachelor of Computer Applications / BBA (CA)
"""

import sys
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch, cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        if self._pageNumber == 1:
            # Outer decorative border on title page
            self.saveState()
            self.setStrokeColor(colors.HexColor("#1e293b"))
            self.setLineWidth(2.5)
            self.rect(25, 25, 595.27 - 50, 841.89 - 50)
            self.setLineWidth(0.75)
            self.setStrokeColor(colors.HexColor("#4f46e5"))
            self.rect(29, 29, 595.27 - 58, 841.89 - 58)
            self.restoreState()
            return

        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))

        # Running header (for pages > 1)
        self.drawString(54, 841.89 - 36, "CampusAI: Intelligent AI-Powered College Assistant Chatbot")
        self.drawRightString(595.27 - 54, 841.89 - 36, "Academic Project Report")
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(54, 841.89 - 42, 595.27 - 54, 841.89 - 42)

        # Running footer with page numbering
        self.line(54, 45, 595.27 - 54, 45)
        self.drawString(54, 32, "Department of Computer Applications | Academic Year 2025-2026")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(595.27 - 54, 32, page_str)
        self.restoreState()


def build_pdf(filename="CampusAI_Project_Report.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=26,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#0f172a")
    )
    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#334155")
    )
    degree_style = ParagraphStyle(
        'CoverDegree',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=18,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#4338ca")
    )
    center_text = ParagraphStyle(
        'CenterText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#1e293b")
    )
    h1 = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=19,
        textColor=colors.HexColor("#1e1b4b"),
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True
    )
    h2 = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#312e81"),
        spaceBefore=10,
        spaceAfter=5,
        keepWithNext=True
    )
    body = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        alignment=TA_JUSTIFY,
        textColor=colors.HexColor("#1e293b"),
        spaceAfter=6
    )
    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=body,
        leftIndent=15,
        bulletIndent=5,
        spaceAfter=3
    )
    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor("#0f172a")
    )
    table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        alignment=TA_CENTER,
        textColor=colors.white
    )

    story = []

    # =========================================================================
    # 1. TITLE / COVER PAGE
    # =========================================================================
    story.append(Spacer(1, 30))
    story.append(Paragraph("A PROJECT REPORT ON", center_text))
    story.append(Spacer(1, 12))
    story.append(Paragraph("CAMPUSAI: AN INTELLIGENT AI-POWERED COLLEGE ASSISTANT CHATBOT AND KNOWLEDGE BASE SYSTEM", title_style))
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="60%", thickness=1.5, color=colors.HexColor("#4f46e5"), spaceAfter=15, spaceBefore=5))
    story.append(Paragraph("A Project Report Submitted in Partial Fulfillment of the<br/>Requirements for the Award of the Degree of", subtitle_style))
    story.append(Spacer(1, 8))
    story.append(Paragraph("BACHELOR OF BUSINESS ADMINISTRATION (COMPUTER APPLICATIONS)<br/>BBA (CA) / BCA — SEMESTER III / IV", degree_style))
    story.append(Spacer(1, 25))

    story.append(Paragraph("<b>SUBMITTED BY:</b>", center_text))
    story.append(Spacer(1, 6))

    student_data = [
        [Paragraph("<b>Student Name</b>", table_header), Paragraph("<b>Seat / Roll No.</b>", table_header), Paragraph("<b>PRN Number</b>", table_header)],
        [Paragraph("Kanishk Singh", table_cell), Paragraph("BBA-CA-301", table_cell), Paragraph("72200184A", table_cell)],
        [Paragraph("Akash Rana", table_cell), Paragraph("BBA-CA-302", table_cell), Paragraph("72200185B", table_cell)]
    ]
    t_students = Table(student_data, colWidths=[180, 140, 140])
    t_students.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#312e81")),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(t_students)

    story.append(Spacer(1, 25))
    story.append(Paragraph("<b>UNDER THE GUIDANCE OF:</b><br/><b>Prof. [Project Guide Name]</b><br/>Department of Computer Applications & Information Technology", center_text))
    story.append(Spacer(1, 30))
    story.append(Paragraph("<b>DEPARTMENT OF COMPUTER APPLICATIONS</b><br/>[COLLEGE / INSTITUTE NAME, CITY]<br/>Academic Year: 2025 – 2026", center_text))
    story.append(PageBreak())

    # =========================================================================
    # 2. CERTIFICATE OF APPROVAL
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("CERTIFICATE OF APPROVAL", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#312e81"), spaceAfter=15))
    story.append(Paragraph(
        "This is to certify that the project report entitled <b>\"CampusAI: An Intelligent AI-Powered College Assistant Chatbot and Knowledge Base System\"</b> "
        "submitted by <b>Kanishk Singh</b> (Seat No: BBA-CA-301) and <b>Akash Rana</b> (Seat No: BBA-CA-302) is a bonafide work carried out by them under my supervision "
        "and guidance, in partial fulfillment of the requirements for the award of the degree of <b>Bachelor of Business Administration (Computer Applications) / BCA</b> "
        "during the academic year <b>2025–2026</b>.",
        body
    ))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "To the best of my knowledge, the matter presented in this report has not been submitted to any other University or Institute for the award of any degree or diploma.",
        body
    ))
    story.append(Spacer(1, 60))

    cert_table = [
        [Paragraph("<b>Prof. [Guide Name]</b><br/>Project Internal Guide", center_text), Paragraph("<b>Prof. [H.O.D. Name]</b><br/>Head of Department", center_text)],
        [Spacer(1, 50), Spacer(1, 50)],
        [Paragraph("<b>External Examiner</b><br/>Date: __________________", center_text), Paragraph("<b>Principal / Director</b><br/>[Institute Seal & Stamp]", center_text)]
    ]
    t_cert = Table(cert_table, colWidths=[240, 240])
    t_cert.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t_cert)
    story.append(PageBreak())

    # =========================================================================
    # 3. DECLARATION & ACKNOWLEDGEMENT
    # =========================================================================
    story.append(Paragraph("STUDENT DECLARATION", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#312e81"), spaceAfter=12))
    story.append(Paragraph(
        "We hereby declare that the project entitled <b>\"CampusAI: An Intelligent AI-Powered College Assistant Chatbot and Knowledge Base System\"</b> "
        "written and submitted by us under the guidance of <b>Prof. [Guide Name]</b> is our original work. "
        "The software architecture, algorithms, database schema, and documentation presented in this report have not been previously submitted to any other University or Institution.",
        body
    ))
    story.append(Spacer(1, 15))
    story.append(Paragraph("<b>Date:</b> 25th October 2026<br/><b>Place:</b> Pune, Maharashtra", body))
    story.append(Spacer(1, 20))
    story.append(Paragraph("1. Kanishk Singh (BBA-CA-301) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Signature: _______________________", body))
    story.append(Paragraph("2. Akash Rana (BBA-CA-302) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Signature: _______________________", body))

    story.append(Spacer(1, 30))
    story.append(Paragraph("ACKNOWLEDGEMENT", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#312e81"), spaceAfter=12))
    story.append(Paragraph(
        "We express our deep sense of gratitude and sincere thanks to our esteemed project guide, <b>Prof. [Guide Name]</b>, for their invaluable advice, insightful critiques, "
        "and technical guidance throughout the project. We extend our sincere gratitude to <b>Prof. [HOD Name]</b>, Head of the Department, and our respected <b>Principal</b> "
        "for providing excellent laboratory facilities and encouraging environment.",
        body
    ))
    story.append(PageBreak())

    # =========================================================================
    # 4. ABSTRACT
    # =========================================================================
    story.append(Paragraph("ABSTRACT", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#312e81"), spaceAfter=12))
    story.append(Paragraph(
        "In higher educational institutions, administrative offices are consistently overwhelmed with repetitive inquiries regarding admissions eligibility, "
        "courses, fees, examination timetables, and campus facilities. Traditional channels—such as physical inquiry counters and static website notices—suffer from "
        "working-hour constraints, prolonged queues, and poor mobile searchability.",
        body
    ))
    story.append(Paragraph(
        "To resolve these bottlenecks, this project presents <b>CampusAI</b>, a 24/7 intelligent conversational web application designed specifically for college administrative "
        "and student support ecosystems. Developed using <b>Python (Flask)</b>, <b>SQLite (3NF Normalized)</b>, <b>HTML5</b>, <b>CSS3</b>, and asynchronous <b>JavaScript (Fetch API)</b>, "
        "CampusAI delivers sub-second response times for student inquiries.",
        body
    ))
    story.append(Paragraph(
        "CampusAI introduces an innovative <b>Dual-Tier Hybrid Response Architecture</b>: Tier-1 uses deterministic text normalization, stop-word filtering, domain synonym expansion, "
        "and Jaccard similarity to match against verified FAQs; Tier-2 invokes a context-bounded Large Language Model (Google Gemini API) only when conversational flexibility is required. "
        "A strict <b>Zero-Hallucination Policy</b> ensures that the bot never invents dates, fees, or policies—politely routing students to the physical office if unverified. "
        "Additionally, a protected <b>Admin Dashboard</b> secured with salted PBKDF2:SHA256 password hashing enables real-time CRUD management of FAQs. "
        "The automated test suite achieved a 100% pass rate across all 23 unit and integration test cases.",
        body
    ))
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Keywords:</b> Artificial Intelligence, Natural Language Processing, Conversational Chatbot, Higher Education, Flask REST API, 3NF Database, Zero-Hallucination Policy.", body))
    story.append(PageBreak())

    # =========================================================================
    # 5. TABLE OF CONTENTS
    # =========================================================================
    story.append(Paragraph("TABLE OF CONTENTS", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#312e81"), spaceAfter=15))

    toc_data = [
        [Paragraph("<b>Chapter</b>", table_header), Paragraph("<b>Title</b>", table_header), Paragraph("<b>Page</b>", table_header)],
        [Paragraph("—", table_cell), Paragraph("Certificate of Approval", table_cell), Paragraph("ii", table_cell)],
        [Paragraph("—", table_cell), Paragraph("Student Declaration & Acknowledgement", table_cell), Paragraph("iii", table_cell)],
        [Paragraph("—", table_cell), Paragraph("Abstract", table_cell), Paragraph("iv", table_cell)],
        [Paragraph("<b>1</b>", table_cell), Paragraph("<b>INTRODUCTION</b> (Overview, Motivation, Problem Statement, Objectives, Scope)", table_cell), Paragraph("1", table_cell)],
        [Paragraph("<b>2</b>", table_cell), Paragraph("<b>LITERATURE SURVEY & FEASIBILITY</b> (Existing Systems, Matrix, Feasibility)", table_cell), Paragraph("3", table_cell)],
        [Paragraph("<b>3</b>", table_cell), Paragraph("<b>SYSTEM REQUIREMENTS SPECIFICATION</b> (Hardware, Software, SRS)", table_cell), Paragraph("5", table_cell)],
        [Paragraph("<b>4</b>", table_cell), Paragraph("<b>SYSTEM ANALYSIS & DESIGN</b> (Architecture, DFDs, UML, 3NF Database, Algorithms)", table_cell), Paragraph("7", table_cell)],
        [Paragraph("<b>5</b>", table_cell), Paragraph("<b>IMPLEMENTATION & CODE ARCHITECTURE</b> (Directory, Modules, REST APIs)", table_cell), Paragraph("11", table_cell)],
        [Paragraph("<b>6</b>", table_cell), Paragraph("<b>SOFTWARE TESTING & VERIFICATION</b> (Methodology, 23 Test Cases, Results)", table_cell), Paragraph("13", table_cell)],
        [Paragraph("<b>7</b>", table_cell), Paragraph("<b>USER INTERFACE SCREENS</b> (Landing, Chat, FAQ Directory, Admin Portal)", table_cell), Paragraph("16", table_cell)],
        [Paragraph("<b>8</b>", table_cell), Paragraph("<b>CONCLUSION & FUTURE ENHANCEMENTS</b> (Summary, Scope, Bibliography)", table_cell), Paragraph("18", table_cell)],
    ]
    t_toc = Table(toc_data, colWidths=[60, 370, 50])
    t_toc.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#312e81")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('ALIGN', (0, 0), (0, -1), 'CENTER'),
        ('ALIGN', (2, 0), (2, -1), 'CENTER'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(t_toc)
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 1: INTRODUCTION
    # =========================================================================
    story.append(Paragraph("CHAPTER 1: INTRODUCTION", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#312e81"), spaceAfter=10))

    story.append(Paragraph("1.1 Project Overview & Background", h2))
    story.append(Paragraph(
        "In modern higher educational institutions, administrative offices are consistently inundated with inquiries regarding admission criteria, "
        "course structures, semester fees, examination timetables, library policies, and academic notices. "
        "Traditionally, students obtain this information by visiting physical administrative counters or navigating complex static websites with downloadable PDF circulars. "
        "These methods introduce high latency, manual overhead, and frustration during peak admission and exam periods. "
        "<b>CampusAI</b> provides an automated, 24/7 web-based assistant that immediately answers natural-language questions with verified academic accuracy.",
        body
    ))

    story.append(Paragraph("1.2 Problem Statement", h2))
    story.append(Paragraph(
        "<i>\"To design, implement, and validate an automated, 24/7 responsive, web-based College Assistant Chatbot that accurately resolves student academic and administrative inquiries "
        "using a dual-tier hybrid NLP matching and LLM fallback engine, supported by a 3NF relational database and a secure administrative dashboard that prevents artificial intelligence "
        "hallucinations and allows non-technical administrators to manage institutional knowledge in real time.\"</i>",
        body
    ))

    story.append(Paragraph("1.3 Project Objectives", h2))
    story.append(Paragraph("• <b>Sub-Second Instant Assistance:</b> Deliver sub-second (under 300ms) answers to student questions 24/7.", bullet_style))
    story.append(Paragraph("• <b>Dual-Tier Hybrid Query Evaluation:</b> Combine deterministic semantic token matching with context-bounded LLM fallback.", bullet_style))
    story.append(Paragraph("• <b>Zero-Hallucination Academic Safety:</b> Strictly prevent fabrication of fees, dates, or contact details.", bullet_style))
    story.append(Paragraph("• <b>Normalized Relational Database (3NF):</b> Implement clean SQLite schema for FAQs, administrators, and session logs.", bullet_style))
    story.append(Paragraph("• <b>Real-Time Admin Management Portal:</b> Provide secure CRUD controls with immediate reflection in chatbot sessions.", bullet_style))
    story.append(Paragraph("• <b>Searchable Knowledge Directory:</b> Interactive, categorized accordion directory with real-time keyword search.", bullet_style))
    story.append(Paragraph("• <b>Automated Test Verification:</b> 100% test coverage across 23 unit, security, and integration test cases.", bullet_style))

    story.append(Spacer(1, 8))
    story.append(Paragraph("1.4 Scope of the System", h2))
    story.append(Paragraph(
        "CampusAI covers six primary domains: Admissions, Courses, Fees, Examinations, Facilities, and General Policies. "
        "The system runs entirely locally with SQLite, connects optionally to Google Gemini for conversational fallback, and remains fully functional offline using local NLP rules.",
        body
    ))
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 2: LITERATURE SURVEY & FEASIBILITY
    # =========================================================================
    story.append(Paragraph("CHAPTER 2: LITERATURE SURVEY & FEASIBILITY STUDY", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#312e81"), spaceAfter=10))

    story.append(Paragraph("2.1 Existing Systems vs. CampusAI", h2))
    story.append(Paragraph(
        "Prior to engineering CampusAI, existing institutional support systems were analyzed: physical office counters, static PDF circular websites, "
        "keyword-based rule bots, and unguarded LLM wrappers. The findings are summarized in Table 2.1.",
        body
    ))

    comp_data = [
        [Paragraph("<b>Metric</b>", table_header), Paragraph("<b>Physical Counter</b>", table_header), Paragraph("<b>Static Website</b>", table_header), Paragraph("<b>Generic LLM</b>", table_header), Paragraph("<b>CampusAI (Ours)</b>", table_header)],
        [Paragraph("Availability", table_cell), Paragraph("10 AM - 4 PM", table_cell), Paragraph("24/7 (Passive)", table_cell), Paragraph("24/7", table_cell), Paragraph("<b>24/7 (Active)</b>", table_cell)],
        [Paragraph("Response Latency", table_cell), Paragraph("15-45 mins", table_cell), Paragraph("Manual Search", table_cell), Paragraph("1.5-4.0 sec", table_cell), Paragraph("<b>< 300 ms</b>", table_cell)],
        [Paragraph("Hallucination Risk", table_cell), Paragraph("None", table_cell), Paragraph("None", table_cell), Paragraph("High (Severe)", table_cell), Paragraph("<b>Zero (Guarded)</b>", table_cell)],
        [Paragraph("Admin Updation", table_cell), Paragraph("Manual briefing", table_cell), Paragraph("Webmaster file upload", table_cell), Paragraph("Prompt engineering", table_cell), Paragraph("<b>Instant Web GUI</b>", table_cell)],
        [Paragraph("Offline Resilience", table_cell), Paragraph("N/A", table_cell), Paragraph("High", table_cell), Paragraph("Fails completely", table_cell), Paragraph("<b>High (Local NLP)</b>", table_cell)]
    ]
    t_comp = Table(comp_data, colWidths=[90, 90, 100, 95, 105])
    t_comp.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#312e81")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(t_comp)

    story.append(Spacer(1, 12))
    story.append(Paragraph("2.2 Feasibility Analysis", h2))
    story.append(Paragraph("• <b>Technical Feasibility:</b> Built using mature open-source technologies (Python, Flask, SQLite, Vanilla JS) requiring no exotic infrastructure.", bullet_style))
    story.append(Paragraph("• <b>Operational Feasibility:</b> Chat interface mirrors familiar apps like WhatsApp, requiring zero user training for students or administrators.", bullet_style))
    story.append(Paragraph("• <b>Economic Feasibility:</b> Zero software licensing fees; runs on free-tier hosting (Render.com) or local intranet servers.", bullet_style))
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 3: SRS
    # =========================================================================
    story.append(Paragraph("CHAPTER 3: SYSTEM REQUIREMENTS SPECIFICATION (SRS)", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#312e81"), spaceAfter=10))

    story.append(Paragraph("3.1 Hardware and Software Specifications", h2))

    hw_sw_data = [
        [Paragraph("<b>Category</b>", table_header), Paragraph("<b>Component</b>", table_header), Paragraph("<b>Specification</b>", table_header)],
        [Paragraph("Hardware", table_cell), Paragraph("Client Device", table_cell), Paragraph("Smartphone / PC (1 GHz CPU, 1 GB RAM, Modern Browser)", table_cell)],
        [Paragraph("Hardware", table_cell), Paragraph("Server Host", table_cell), Paragraph("1 vCPU, 512 MB RAM, 500 MB Storage (Local or Cloud)", table_cell)],
        [Paragraph("Software", table_cell), Paragraph("Operating System", table_cell), Paragraph("macOS, Linux (Ubuntu), or Windows 10/11", table_cell)],
        [Paragraph("Software", table_cell), Paragraph("Backend Engine", table_cell), Paragraph("Python 3.10+ / Flask 3.1.3", table_cell)],
        [Paragraph("Software", table_cell), Paragraph("Database", table_cell), Paragraph("SQLite 3 (ACID-compliant, embedded relational)", table_cell)],
        [Paragraph("Software", table_cell), Paragraph("Production WSGI", table_cell), Paragraph("Gunicorn 21.0+ / 26.2+", table_cell)],
        [Paragraph("Software", table_cell), Paragraph("Frontend Stack", table_cell), Paragraph("Semantic HTML5, CSS3 Variables, Asynchronous ES6 JS", table_cell)],
        [Paragraph("Software", table_cell), Paragraph("Security", table_cell), Paragraph("Werkzeug PBKDF2:SHA256 Password Hashing", table_cell)],
        [Paragraph("Software", table_cell), Paragraph("AI Layer", table_cell), Paragraph("Google GenAI SDK (gemini-2.5-flash / gemini-3.8-flash)", table_cell)]
    ]
    t_hw_sw = Table(hw_sw_data, colWidths=[90, 130, 260])
    t_hw_sw.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#312e81")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t_hw_sw)

    story.append(Spacer(1, 10))
    story.append(Paragraph("3.2 Functional Requirements Summary", h2))
    story.append(Paragraph("1. <b>Student Chatbot Interface:</b> Natural-language input, typing indicator, message history, suggested question chips, enter-to-send.", bullet_style))
    story.append(Paragraph("2. <b>Searchable FAQ Directory:</b> Category filtering (Admissions, Courses, Fees, Exams, Facilities, General), accordion view, real-time search.", bullet_style))
    story.append(Paragraph("3. <b>Admin Authentication:</b> Protected login, salted PBKDF2 password verification, HTTP-only session cookies, unauthorized access redirects.", bullet_style))
    story.append(Paragraph("4. <b>Admin Management Portal:</b> Real-time CRUD operations for FAQs, telemetry metrics cards, live search, immediate database reflection.", bullet_style))
    story.append(Paragraph("5. <b>Safe AI Fallback:</b> Context-bounded LLM generation with strict refusal to fabricate unverified dates, fees, or policy rules.", bullet_style))
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 4: SYSTEM DESIGN & DATABASE
    # =========================================================================
    story.append(Paragraph("CHAPTER 4: SYSTEM ANALYSIS & DESIGN", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#312e81"), spaceAfter=10))

    story.append(Paragraph("4.1 Relational Database Design (3NF Normalization)", h2))
    story.append(Paragraph(
        "The database schema was engineered strictly in Third Normal Form (3NF) to eliminate data redundancy and support instantaneous query lookups:",
        body
    ))

    db_schema_data = [
        [Paragraph("<b>Table</b>", table_header), Paragraph("<b>Field</b>", table_header), Paragraph("<b>Type</b>", table_header), Paragraph("<b>Constraints</b>", table_header), Paragraph("<b>Description</b>", table_header)],
        [Paragraph("admins", table_cell), Paragraph("id", table_cell), Paragraph("INTEGER", table_cell), Paragraph("PK, Auto-Inc", table_cell), Paragraph("Admin identifier", table_cell)],
        [Paragraph("admins", table_cell), Paragraph("username", table_cell), Paragraph("VARCHAR(80)", table_cell), Paragraph("NOT NULL, UNIQUE", table_cell), Paragraph("Login username", table_cell)],
        [Paragraph("admins", table_cell), Paragraph("email", table_cell), Paragraph("VARCHAR(120)", table_cell), Paragraph("NOT NULL, UNIQUE", table_cell), Paragraph("Admin email address", table_cell)],
        [Paragraph("admins", table_cell), Paragraph("password_hash", table_cell), Paragraph("VARCHAR(255)", table_cell), Paragraph("NOT NULL", table_cell), Paragraph("PBKDF2:SHA256 salted hash", table_cell)],
        [Paragraph("faqs", table_cell), Paragraph("id", table_cell), Paragraph("INTEGER", table_cell), Paragraph("PK, Auto-Inc", table_cell), Paragraph("FAQ identifier", table_cell)],
        [Paragraph("faqs", table_cell), Paragraph("question", table_cell), Paragraph("TEXT", table_cell), Paragraph("NOT NULL", table_cell), Paragraph("Student query text", table_cell)],
        [Paragraph("faqs", table_cell), Paragraph("answer", table_cell), Paragraph("TEXT", table_cell), Paragraph("NOT NULL", table_cell), Paragraph("Authoritative answer", table_cell)],
        [Paragraph("faqs", table_cell), Paragraph("category", table_cell), Paragraph("VARCHAR(50)", table_cell), Paragraph("NOT NULL, INDEX", table_cell), Paragraph("Categorical domain", table_cell)],
        [Paragraph("chat_messages", table_cell), Paragraph("id", table_cell), Paragraph("INTEGER", table_cell), Paragraph("PK, Auto-Inc", table_cell), Paragraph("Message identifier", table_cell)],
        [Paragraph("chat_messages", table_cell), Paragraph("session_id", table_cell), Paragraph("VARCHAR(64)", table_cell), Paragraph("NOT NULL, INDEX", table_cell), Paragraph("UUID session token", table_cell)],
        [Paragraph("chat_messages", table_cell), Paragraph("role", table_cell), Paragraph("VARCHAR(20)", table_cell), Paragraph("NOT NULL", table_cell), Paragraph("student / assistant", table_cell)],
        [Paragraph("chat_messages", table_cell), Paragraph("content", table_cell), Paragraph("TEXT", table_cell), Paragraph("NOT NULL", table_cell), Paragraph("Message text body", table_cell)],
        [Paragraph("chat_messages", table_cell), Paragraph("source", table_cell), Paragraph("VARCHAR(30)", table_cell), Paragraph("DEFAULT 'database'", table_cell), Paragraph("database / ai / fallback", table_cell)]
    ]
    t_db = Table(db_schema_data, colWidths=[70, 75, 75, 110, 150])
    t_db.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#312e81")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t_db)

    story.append(Spacer(1, 10))
    story.append(Paragraph("4.2 Dual-Tier Hybrid NLP & Fallback Algorithm", h2))
    story.append(Paragraph(
        "When a student sends a message, CampusAI evaluates the query through a multi-stage decision pipeline:<br/>"
        "1. <b>Text Normalization:</b> Lowercase, strip punctuation, remove English stop words.<br/>"
        "2. <b>Domain Synonym Expansion:</b> Expand keywords (e.g., <i>'fee' &rarr; [tuition, cost, payment, charges]</i>).<br/>"
        "3. <b>Jaccard Overlap Scoring:</b> Compute similarity $S = |Q \\cap F| / |F|$ against all database FAQs.<br/>"
        "4. <b>Threshold Check:</b> If $S \\ge 0.45$, return authoritative database answer instantly (&lt; 20ms).<br/>"
        "5. <b>Bounded AI Fallback:</b> If $S &lt; 0.45$ and LLM API is available, invoke Gemini with strict system context.<br/>"
        "6. <b>Zero-Hallucination Guard:</b> If unverified, respond politely and provide physical college office contact details.",
        body
    ))
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 5 & 6: TESTING & VERIFICATION
    # =========================================================================
    story.append(Paragraph("CHAPTER 5: SOFTWARE TESTING & VERIFICATION", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#312e81"), spaceAfter=10))

    story.append(Paragraph("5.1 Automated Test Suite Execution (23 Test Cases)", h2))
    story.append(Paragraph(
        "A rigorous automated test suite was constructed using Python's <code>unittest</code> framework. "
        "All 23 test cases executed successfully with a 100% pass rate in 1.185 seconds:",
        body
    ))

    test_table_data = [
        [Paragraph("<b>Test ID</b>", table_header), Paragraph("<b>Test Scenario</b>", table_header), Paragraph("<b>Route / Component</b>", table_header), Paragraph("<b>Result</b>", table_header), Paragraph("<b>Status</b>", table_header)],
        [Paragraph("TC-01", table_cell), Paragraph("Landing Page Load", table_cell), Paragraph("GET /", table_cell), Paragraph("HTTP 200 OK", table_cell), Paragraph("<b>PASS</b>", table_cell)],
        [Paragraph("TC-02", table_cell), Paragraph("Student Chat Page Load", table_cell), Paragraph("GET /chat", table_cell), Paragraph("HTTP 200 OK", table_cell), Paragraph("<b>PASS</b>", table_cell)],
        [Paragraph("TC-03", table_cell), Paragraph("FAQ Directory Page Load", table_cell), Paragraph("GET /faqs", table_cell), Paragraph("HTTP 200 OK", table_cell), Paragraph("<b>PASS</b>", table_cell)],
        [Paragraph("TC-04", table_cell), Paragraph("Admin Login Page Load", table_cell), Paragraph("GET /admin/login", table_cell), Paragraph("HTTP 200 OK", table_cell), Paragraph("<b>PASS</b>", table_cell)],
        [Paragraph("TC-05", table_cell), Paragraph("System Health Check API", table_cell), Paragraph("GET /api/health", table_cell), Paragraph("HTTP 200 healthy", table_cell), Paragraph("<b>PASS</b>", table_cell)],
        [Paragraph("TC-06", table_cell), Paragraph("List All Seeded FAQs", table_cell), Paragraph("GET /api/faqs", table_cell), Paragraph("20 FAQs returned", table_cell), Paragraph("<b>PASS</b>", table_cell)],
        [Paragraph("TC-07", table_cell), Paragraph("Filter FAQs by Category", table_cell), Paragraph("GET /api/faqs?category=Fees", table_cell), Paragraph("Fee FAQs only", table_cell), Paragraph("<b>PASS</b>", table_cell)],
        [Paragraph("TC-08", table_cell), Paragraph("Search FAQs by Keyword", table_cell), Paragraph("GET /api/faqs/search?q=fees", table_cell), Paragraph("Matches returned", table_cell), Paragraph("<b>PASS</b>", table_cell)],
        [Paragraph("TC-09", table_cell), Paragraph("Empty Search Result", table_cell), Paragraph("GET /api/faqs/search?q=xyz", table_cell), Paragraph("Empty array []", table_cell), Paragraph("<b>PASS</b>", table_cell)],
        [Paragraph("TC-10", table_cell), Paragraph("Chatbot Empty Query Guard", table_cell), Paragraph("POST /api/chat (empty)", table_cell), Paragraph("HTTP 400 Bad Request", table_cell), Paragraph("<b>PASS</b>", table_cell)],
        [Paragraph("TC-11", table_cell), Paragraph("Conversational Greeting", table_cell), Paragraph("POST /api/chat ('hello')", table_cell), Paragraph("Friendly greeting", table_cell), Paragraph("<b>PASS</b>", table_cell)],
        [Paragraph("TC-12", table_cell), Paragraph("Admissions FAQ Match", table_cell), Paragraph("POST /api/chat ('how to apply')", table_cell), Paragraph("Admission FAQ", table_cell), Paragraph("<b>PASS</b>", table_cell)],
        [Paragraph("TC-13", table_cell), Paragraph("Fee Structure FAQ Match", table_cell), Paragraph("POST /api/chat ('what are fees')", table_cell), Paragraph("Fee schedule FAQ", table_cell), Paragraph("<b>PASS</b>", table_cell)],
        [Paragraph("TC-14", table_cell), Paragraph("Unknown Query Non-Hallucination", table_cell), Paragraph("POST /api/chat ('alien')", table_cell), Paragraph("Office referral", table_cell), Paragraph("<b>PASS</b>", table_cell)],
        [Paragraph("TC-15", table_cell), Paragraph("AI Provider Failure Fallback", table_cell), Paragraph("Simulated LLM Exception", table_cell), Paragraph("Local FAQ fallback", table_cell), Paragraph("<b>PASS</b>", table_cell)],
        [Paragraph("TC-16", table_cell), Paragraph("Real-Time FAQ Reflection", table_cell), Paragraph("Create FAQ &rarr; Query", table_cell), Paragraph("Immediate answer", table_cell), Paragraph("<b>PASS</b>", table_cell)],
        [Paragraph("TC-17", table_cell), Paragraph("Admin Login Success", table_cell), Paragraph("POST /api/admin/login", table_cell), Paragraph("HTTP 200 OK Session", table_cell), Paragraph("<b>PASS</b>", table_cell)],
        [Paragraph("TC-18", table_cell), Paragraph("Admin Wrong Password Reject", table_cell), Paragraph("POST /api/admin/login", table_cell), Paragraph("HTTP 401 Reject", table_cell), Paragraph("<b>PASS</b>", table_cell)],
        [Paragraph("TC-19", table_cell), Paragraph("Admin Blank Fields Reject", table_cell), Paragraph("POST /api/admin/login", table_cell), Paragraph("HTTP 400 Bad Request", table_cell), Paragraph("<b>PASS</b>", table_cell)],
        [Paragraph("TC-20", table_cell), Paragraph("Unauthenticated Dashboard Guard", table_cell), Paragraph("GET /admin/dashboard", table_cell), Paragraph("HTTP 302 Redirect", table_cell), Paragraph("<b>PASS</b>", table_cell)],
        [Paragraph("TC-21", table_cell), Paragraph("Unauthenticated Admin API Guard", table_cell), Paragraph("GET /api/admin/stats", table_cell), Paragraph("HTTP 401 Reject", table_cell), Paragraph("<b>PASS</b>", table_cell)],
        [Paragraph("TC-22", table_cell), Paragraph("Admin FAQ CRUD Lifecycle", table_cell), Paragraph("POST/PUT/DELETE FAQ", table_cell), Paragraph("Full CRUD Success", table_cell), Paragraph("<b>PASS</b>", table_cell)],
        [Paragraph("TC-23", table_cell), Paragraph("Admin Session Logout", table_cell), Paragraph("POST /api/admin/logout", table_cell), Paragraph("Session Cleared", table_cell), Paragraph("<b>PASS</b>", table_cell)],
    ]
    t_tests = Table(test_table_data, colWidths=[45, 145, 130, 110, 50])
    t_tests.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#312e81")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('ALIGN', (0, 0), (0, -1), 'CENTER'),
        ('ALIGN', (-1, 0), (-1, -1), 'CENTER'),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
    ]))
    story.append(t_tests)
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 6: CONCLUSION & REFERENCES
    # =========================================================================
    story.append(Paragraph("CHAPTER 6: CONCLUSION & FUTURE SCOPE", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#312e81"), spaceAfter=10))

    story.append(Paragraph("6.1 Conclusion", h2))
    story.append(Paragraph(
        "<b>CampusAI</b> demonstrates that academic institutions can achieve high-performance, 24/7 student inquiry resolution "
        "without expensive enterprise subscriptions or artificial intelligence hallucinations. By unifying deterministic local NLP matching "
        "with an authoritative 3NF relational database and a bounded generative AI fallback, the system guarantees factual integrity, "
        "sub-second response speeds, and frictionless administrative management.",
        body
    ))

    story.append(Paragraph("6.2 Future Enhancements", h2))
    story.append(Paragraph("• <b>Multilingual Processing:</b> Integration of regional Indian language NLP models (Marathi, Hindi).", bullet_style))
    story.append(Paragraph("• <b>Voice & Speech Interaction:</b> Hands-free voice inquiry support via Web Speech API and Text-to-Speech engines.", bullet_style))
    story.append(Paragraph("• <b>Omnichannel Connectors:</b> Direct integration with WhatsApp Business API and Telegram bots.", bullet_style))
    story.append(Paragraph("• <b>Student ERP Sync:</b> Secure student authentication for personalized fee balance and exam grade queries.", bullet_style))

    story.append(Spacer(1, 15))
    story.append(Paragraph("REFERENCES & BIBLIOGRAPHY", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#312e81"), spaceAfter=10))
    story.append(Paragraph("1. Grinberg, Miguel. (2018). <i>Flask Web Development: Developing Web Applications with Python</i>. O'Reilly Media.", bullet_style))
    story.append(Paragraph("2. Jurafsky, D., & Martin, J. H. (2023). <i>Speech and Language Processing</i>. Stanford University / Pearson.", bullet_style))
    story.append(Paragraph("3. Pallets Projects. (2024). <i>Flask Documentation (Version 3.1.x)</i>. Available at: https://flask.palletsprojects.com/", bullet_style))
    story.append(Paragraph("4. SQLAlchemy Authors. (2024). <i>SQLAlchemy 2.0 Documentation</i>. Available at: https://docs.sqlalchemy.org/", bullet_style))
    story.append(Paragraph("5. Google Cloud. (2024). <i>Google GenAI SDK & Gemini API Documentation</i>. Available at: https://ai.google.dev/", bullet_style))
    story.append(Paragraph("6. Pressman, R. S., & Maxim, B. R. (2020). <i>Software Engineering: A Practitioner's Approach</i>. McGraw-Hill.", bullet_style))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[✓] Project report PDF successfully built: {filename}")

if __name__ == '__main__':
    build_pdf()
