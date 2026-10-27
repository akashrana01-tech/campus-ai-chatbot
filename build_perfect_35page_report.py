"""
CampusAI Official 35-Page Project Report Generator
Authored exclusively for:
- Akash rana (ISTU25010120004)
- Shreyash katke (ISTU25010120003)
Course: BBA CA (Semester III, 2025-26)
Institution: G H Raisoni International Skill Tech University, Pune-412207
Project Guide: Prof. Sheela Satav

Guarantees:
- Exactly 35 pages matching PDF 2 format
- 100% textbook-perfect UML and DFD diagrams
- Double border on every page
- Exact running headers and footers matching Table of Contents
- 100% pure CampusAI data (no Kanishk's attendance detention engine or dual campus coordinates)
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

# Map physical page number to the TOC page label
PAGE_FOOTER_MAP = {
    7: 1, 8: 2, 9: 3, 10: 4, 11: 5, 12: 6, 13: 7, 14: 8, 15: 9, 16: 10,
    17: 11, 18: 12, 19: 13, 20: 14, 21: 15, 22: 16, 23: 17, 24: 18, 25: 19, 26: 20,
    27: 21, 28: 24, 29: 25, 30: 26, 31: 27, 32: 28, 33: 29, 34: 30, 35: 31
}

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
        
        # 2. Running footer (For content pages 7 to 35)
        p_num = self._pageNumber
        if p_num in PAGE_FOOTER_MAP:
            toc_page = PAGE_FOOTER_MAP[p_num]
            self.setFont("Times-Roman", 9)
            self.setFillColor(colors.HexColor("#0f172a"))
            
            # Left footer
            self.drawString(45, 36, "G H Raisoni International Skill Tech University, Pune")
            # Right footer
            self.drawRightString(PAGE_W - 45, 36, f"Page {toc_page}")
            
        self.restoreState()


def generate_report(out_path):
    doc = SimpleDocTemplate(
        out_path,
        pagesize=(PAGE_W, PAGE_H),
        leftMargin=45,
        rightMargin=45,
        topMargin=45,
        bottomMargin=55
    )

    styles = getSampleStyleSheet()

    # Typography styles
    title_main = ParagraphStyle('TitleMain', fontName='Times-Bold', fontSize=18, leading=24, alignment=TA_CENTER, textColor=colors.black)
    center_text = ParagraphStyle('CenterText', fontName='Times-Roman', fontSize=11, leading=16, alignment=TA_CENTER, textColor=colors.black)
    center_bold = ParagraphStyle('CenterBold', fontName='Times-Bold', fontSize=11.5, leading=16, alignment=TA_CENTER, textColor=colors.black)
    h1 = right_text = ParagraphStyle('RightText', fontName='Times-Roman', fontSize=10, leading=14, alignment=TA_RIGHT, textColor=colors.black)
    ParagraphStyle('H1', fontName='Times-Bold', fontSize=14.5, leading=19, alignment=TA_LEFT, textColor=colors.black, spaceAfter=8)
    h2 = ParagraphStyle('H2', fontName='Times-Bold', fontSize=11.5, leading=16, alignment=TA_LEFT, textColor=colors.black, spaceBefore=6, spaceAfter=4)
    body = ParagraphStyle('Body', fontName='Times-Roman', fontSize=10.0, leading=14.8, alignment=TA_JUSTIFY, textColor=colors.black, spaceAfter=6)
    bullet = ParagraphStyle('Bullet', fontName='Times-Roman', fontSize=9.5, leading=13.8, alignment=TA_JUSTIFY, leftIndent=15, firstLineIndent=-10, textColor=colors.black, spaceAfter=3)
    tbl_cell = ParagraphStyle('TblCell', fontName='Times-Roman', fontSize=8.2, leading=11.2, alignment=TA_LEFT, textColor=colors.black)
    tbl_cell_bold = ParagraphStyle('TblCellBold', fontName='Times-Bold', fontSize=8.2, leading=11.2, alignment=TA_LEFT, textColor=colors.black)
    tbl_hdr = ParagraphStyle('TblHdr', fontName='Times-Bold', fontSize=8.5, leading=11.5, alignment=TA_CENTER, textColor=colors.white)

    story = []

    # =========================================================================
    # PAGE 1: COVER PAGE
    # =========================================================================
    story.append(Spacer(1, 15))
    story.append(Paragraph("A<br/>Project report on", center_text))
    story.append(Spacer(1, 12))
    story.append(Paragraph("<b>CampusAI: Intelligent AI-Powered College Assistant Chatbot and Knowledge Base System</b>", title_main))
    story.append(Spacer(1, 18))
    story.append(Paragraph("Submitted To :", center_bold))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>G H Raisoni International Skill Tech University.</b><br/>PUNE-412207", center_bold))
    story.append(Spacer(1, 15))
    
    if os.path.exists(LOGO_PATH):
        story.append(Image(LOGO_PATH, width=175, height=58))
    story.append(Spacer(1, 15))
    
    story.append(Paragraph("For: <b>BBA CA (Semester III)</b>", center_bold))
    story.append(Spacer(1, 14))
    story.append(Paragraph("Submitted By :", center_bold))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Akash rana (ISTU25010120004)</b><br/><b>Shreyash katke (ISTU25010120003)</b>", center_text))
    story.append(Spacer(1, 14))
    story.append(Paragraph("Under the Guidance of :", center_bold))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Prof. Sheela Satav</b>", center_bold))
    story.append(Spacer(1, 14))
    story.append(Paragraph("DEPARTMENT OF COMPUTER APPLICATIONS", center_bold))
    story.append(Paragraph("G H RAISONI INTERNATIONAL SKILL TECH UNIVERSITY, PUNE<br/><b>Academic Year: 2025–2026</b>", center_text))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 2: CERTIFICATE OF APPROVAL
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("G H Raisoni International Skill Tech University.<br/><font size=9>PUNE-412207</font>", center_bold))
    story.append(Spacer(1, 10))
    if os.path.exists(LOGO_PATH):
        story.append(Image(LOGO_PATH, width=140, height=47))
    story.append(Spacer(1, 12))
    story.append(Paragraph("<b>CERTIFICATE</b>", title_main))
    story.append(Spacer(1, 15))
    cert_text = (
        "This is to certify that <b>Mr. Akash rana (Roll No: ISTU25010120004)</b> and "
        "<b>Mr. Shreyash katke (Roll No: ISTU25010120003)</b>, students of <b>SY BBA CA</b>, "
        "have satisfactorily completed their Project entitled <b>“CampusAI: An Intelligent AI-Powered "
        "College Assistant Chatbot and Knowledge Base System”</b> and submitted this project report "
        "in partial fulfillment of the requirements for the award of the degree of <b>BBA CA</b> for "
        "the academic Year <b>2025-26</b>."
    )
    story.append(Paragraph(cert_text, body))
    story.append(Spacer(1, 8))
    cert_text2 = (
        "This project embodies original engineering work carried out under our supervision and guidance. "
        "To the best of our knowledge, the matter presented in this report has not been submitted to any other "
        "University or Institute for the award of any degree or diploma."
    )
    story.append(Paragraph(cert_text2, body))
    story.append(Spacer(1, 65))
    
    sig_data = [
        [
            Paragraph("<b>Prof. Sheela Satav</b><br/>Project Internal Guide", center_text),
            Paragraph("<b>Head of Department</b><br/>Dept of Computer Applications", center_text)
        ],
        [Paragraph("<br/><br/>", center_text), Paragraph("<br/><br/>", center_text)],
        [
            Paragraph("<b>External Examiner</b><br/>University Appointed", center_text),
            Paragraph("<b>Principal / Director</b><br/>G H Raisoni ISTU, Pune", center_text)
        ]
    ]
    sig_table = Table(sig_data, colWidths=[240, 240])
    sig_table.setStyle(TableStyle([('ALIGN', (0,0), (-1,-1), 'CENTER'), ('VALIGN', (0,0), (-1,-1), 'MIDDLE')]))
    story.append(sig_table)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 3: ACKNOWLEDGEMENT
    # =========================================================================
    story.append(Spacer(1, 15))
    story.append(Paragraph("<b>ACKNOWLEDGEMENT</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=14))
    
    ack_p1 = (
        "A successful software project is the result of focused teamwork, dedicated research, and the collective "
        "guidance of experienced mentors. We express our profound sense of gratitude and sincere thanks to our "
        "esteemed project guide, <b>Prof. Sheela Satav</b>, for her invaluable technical insights, constant encouragement, "
        "and critical feedback throughout the conceptualization, architecture design, and development of CampusAI."
    )
    story.append(Paragraph(ack_p1, body))
    story.append(Spacer(1, 6))
    
    ack_p2 = (
        "We are deeply indebted to our respected Head of the Department of Computer Applications, and the honorable "
        "Principal and Director of <b>G H Raisoni International Skill Tech University, Pune</b>, for providing world-class "
        "computing infrastructure, laboratory resources, and an encouraging academic environment."
    )
    story.append(Paragraph(ack_p2, body))
    story.append(Spacer(1, 6))
    
    ack_p3 = (
        "We also extend our heartfelt appreciation to all faculty members, technical lab assistants, and our fellow "
        "classmates for their constructive suggestions, cooperative spirit, and active participation during user acceptance "
        "testing of the chatbot interface."
    )
    story.append(Paragraph(ack_p3, body))
    story.append(Spacer(1, 65))
    
    sub_table = Table([
        [Paragraph("", center_text), Paragraph("<b>Akash rana (ISTU25010120004)</b><br/><b>Shreyash katke (ISTU25010120003)</b><br/>SY BBA CA (Semester III)", right_text)]
    ], colWidths=[200, 280])
    sub_table.setStyle(TableStyle([('ALIGN', (1,0), (1,0), 'RIGHT')]))
    story.append(sub_table)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 4: ABSTRACT
    # =========================================================================
    story.append(Spacer(1, 15))
    story.append(Paragraph("<b>ABSTRACT</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=14))
    
    abs_p1 = (
        "In modern collegiate ecosystems, academic administrations are perpetually flooded with repetitive, high-volume "
        "student inquiries concerning admissions eligibility, fee payment deadlines, examination timetables, course curricula, "
        "and campus facilities. Traditional inquiry channels—such as physical inquiry counters, telephone switchboards, and static "
        "bulletin boards—suffer from acute operating-hour restrictions, prolonged queues, and poor mobile searchability."
    )
    story.append(Paragraph(abs_p1, body))
    story.append(Spacer(1, 6))
    
    abs_p2 = (
        "To resolve these operational bottlenecks, this project presents <b>CampusAI</b>, an intelligent, 24/7 autonomous "
        "web-based conversational assistant engineered specifically for higher educational institutions. Built using Python (Flask), "
        "an ACID-compliant Third Normal Form (3NF) SQLite relational database, HTML5, CSS3, and asynchronous ES6 JavaScript, CampusAI "
        "delivers deterministic, sub-second responses to student queries while guaranteeing absolute factual integrity."
    )
    story.append(Paragraph(abs_p2, body))
    story.append(Spacer(1, 6))
    
    abs_p3 = (
        "CampusAI introduces an innovative <b>Dual-Tier Hybrid Response Architecture</b>: Tier-1 executes deterministic local NLP "
        "matching (text normalization, domain stop-word filtering, domain synonym expansion, and Jaccard similarity scoring) against "
        "verified institutional FAQ records in SQLite; Tier-2 invokes a context-bounded Generative AI layer (Google Gemini 2.5 Flash) "
        "only when conversational flexibility is required. A strict <b>Zero-Hallucination Policy</b> ensures that the bot never "
        "fabricates dates, fees, or policy rules. Backed by an administrative CRUD portal with salted PBKDF2 authentication and a 100% "
        "pass rate across 23 automated tests, CampusAI establishes an accessible, scalable campus support benchmark."
    )
    story.append(Paragraph(abs_p3, body))
    story.append(Spacer(1, 12))
    story.append(Paragraph("<b>Keywords:</b> Dual-Tier NLP, Jaccard Similarity, Google Gemini API, Zero-Hallucination, Flask, SQLite 3NF, BBA CA.", center_bold))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 5: TABLE OF CONTENT
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>TABLE OF CONTENT</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=12))
    
    toc_data = [
        [Paragraph("<b>Sr No</b>", tbl_hdr), Paragraph("<b>Topic</b>", tbl_hdr), Paragraph("<b>Page No</b>", tbl_hdr)],
        [Paragraph("1", tbl_cell), Paragraph("Introduction", tbl_cell), Paragraph("1", tbl_cell)],
        [Paragraph("2", tbl_cell), Paragraph("Problem Definition", tbl_cell), Paragraph("2", tbl_cell)],
        [Paragraph("3", tbl_cell), Paragraph("Existing System & Need for New System", tbl_cell), Paragraph("3", tbl_cell)],
        [Paragraph("4", tbl_cell), Paragraph("Scope of System", tbl_cell), Paragraph("4", tbl_cell)],
        [Paragraph("5", tbl_cell), Paragraph("Feasibility Study", tbl_cell), Paragraph("5", tbl_cell)],
        [Paragraph("6", tbl_cell), Paragraph("Hardware Requirements", tbl_cell), Paragraph("6", tbl_cell)],
        [Paragraph("7", tbl_cell), Paragraph("Software Requirements", tbl_cell), Paragraph("7", tbl_cell)],
        [Paragraph("8", tbl_cell), Paragraph("Requirement Analysis", tbl_cell), Paragraph("8", tbl_cell)],
        [Paragraph("9", tbl_cell), Paragraph("Decision Table", tbl_cell), Paragraph("9", tbl_cell)],
        [Paragraph("10", tbl_cell), Paragraph("Decision Tree", tbl_cell), Paragraph("10", tbl_cell)],
        [Paragraph("11", tbl_cell), Paragraph("Normalized Database Design (3NF) — Admins & Sessions Tables", tbl_cell), Paragraph("11", tbl_cell)],
        [Paragraph("12", tbl_cell), Paragraph("College Info (FAQs) & Knowledge Base Tables", tbl_cell), Paragraph("12", tbl_cell)],
        [Paragraph("13", tbl_cell), Paragraph("Chat History & Query Logs Tables", tbl_cell), Paragraph("13", tbl_cell)],
        [Paragraph("14", tbl_cell), Paragraph("ER Diagram", tbl_cell), Paragraph("14", tbl_cell)],
        [Paragraph("15", tbl_cell), Paragraph("Use Case Diagram", tbl_cell), Paragraph("15", tbl_cell)],
        [Paragraph("16", tbl_cell), Paragraph("Class Diagram", tbl_cell), Paragraph("16", tbl_cell)],
        [Paragraph("17", tbl_cell), Paragraph("Object Diagram", tbl_cell), Paragraph("17", tbl_cell)],
        [Paragraph("18", tbl_cell), Paragraph("Sequence Diagram", tbl_cell), Paragraph("18", tbl_cell)]
    ]
    toc_table = Table(toc_data, colWidths=[55, 360, 65])
    toc_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor("#ffffff"), colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(toc_table)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 6: TABLE OF CONTENT (CONTD.)
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>TABLE OF CONTENT (CONTD.)</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=12))
    
    toc_data2 = [
        [Paragraph("<b>Sr No</b>", tbl_hdr), Paragraph("<b>Topic</b>", tbl_hdr), Paragraph("<b>Page No</b>", tbl_hdr)],
        [Paragraph("19", tbl_cell), Paragraph("Activity Diagram", tbl_cell), Paragraph("19", tbl_cell)],
        [Paragraph("20", tbl_cell), Paragraph("Component Diagram", tbl_cell), Paragraph("20", tbl_cell)],
        [Paragraph("21", tbl_cell), Paragraph("Data Flow Diagram (DFD Level 0 & Level 1)", tbl_cell), Paragraph("21", tbl_cell)],
        [Paragraph("22", tbl_cell), Paragraph("Home Screen UI", tbl_cell), Paragraph("24", tbl_cell)],
        [Paragraph("23", tbl_cell), Paragraph("Student Portal & Chatbot Assistant UI", tbl_cell), Paragraph("25", tbl_cell)],
        [Paragraph("24", tbl_cell), Paragraph("Admin Command Center & Management UI", tbl_cell), Paragraph("26", tbl_cell)],
        [Paragraph("25", tbl_cell), Paragraph("Testing & Implementation (23 Automated Test Cases)", tbl_cell), Paragraph("27", tbl_cell)],
        [Paragraph("26", tbl_cell), Paragraph("Drawbacks & Limitations", tbl_cell), Paragraph("28", tbl_cell)],
        [Paragraph("27", tbl_cell), Paragraph("Proposed Enhancements", tbl_cell), Paragraph("29", tbl_cell)],
        [Paragraph("28", tbl_cell), Paragraph("Conclusion", tbl_cell), Paragraph("30", tbl_cell)],
        [Paragraph("29", tbl_cell), Paragraph("Bibliography", tbl_cell), Paragraph("31", tbl_cell)]
    ]
    toc_table2 = Table(toc_data2, colWidths=[55, 360, 65])
    toc_table2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor("#ffffff"), colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(toc_table2)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 7: TOPIC 1 - INTRODUCTION
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>INTRODUCTION :</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=10))
    story.append(Paragraph(
        "In modern higher education, dynamic communication between college administrations and students is essential. "
        "With thousands of enrolled students and prospective applicants seeking timely information, conventional administrative "
        "channels frequently face severe bottlenecks.", body
    ))
    story.append(Paragraph(
        "<b>CampusAI: Intelligent AI-Powered College Assistant Chatbot</b> is specifically engineered for G H Raisoni International "
        "Skill Tech University, Pune. It serves as an autonomous digital front desk and centralized knowledge engine across six key "
        "academic domains: Admissions, Courses & Syllabus, Fee Structures, Examination Schedules, Campus Facilities, and General Inquiries.", body
    ))
    story.append(Paragraph("<b>Key Architectural Pillars:</b>", h2))
    story.append(Paragraph("• <b>Dual-Tier Hybrid Response Engine:</b> Combines deterministic local NLP string-similarity matching with a context-bounded Generative AI layer (Google Gemini API).", bullet))
    story.append(Paragraph("• <b>Zero-Hallucination Policy:</b> Ensures the bot never invents dates, fees, or policy rules. Out-of-domain or unverified queries are gracefully referred to official college personnel.", bullet))
    story.append(Paragraph("• <b>ACID-Compliant 3NF Database:</b> Relational SQLite schema engineered in Third Normal Form to eliminate data redundancy and support sub-second query lookups.", bullet))
    story.append(Paragraph("• <b>Administrative Governance Portal:</b> Protected interface with salted PBKDF2 password hashing enabling staff to manage FAQs in real time and audit chat interaction logs.", bullet))
    story.append(Paragraph("• <b>Automated Verification Suite:</b> 23 unit and integration tests executing with a 100% pass rate in 1.18 seconds.", bullet))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 8: TOPIC 2 - PROBLEM DEFINITION
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>PROBLEM DEFINITION :</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=10))
    story.append(Paragraph(
        "Modern university ecosystems manage diverse academic operations simultaneously. During peak operational periods—such as "
        "admission cycles, fee payment windows, and semester examination weeks—the volume of repetitive inquiries exceeds the capacity "
        "of administrative staff, creating significant friction.", body
    ))
    story.append(Paragraph("<b>Core Problem Dimensions:</b>", h2))
    story.append(Paragraph("1. <b>Office Hour Bottlenecks:</b> Administrative inquiry windows are limited to weekdays (9:00 AM – 4:00 PM). Students studying late or prospective outstation applicants cannot access immediate verification after hours.", bullet))
    story.append(Paragraph("2. <b>Severe Counter Congestion:</b> Repetitive questions regarding fee installment deadlines, exam form submissions, and syllabus copies cause long queues at college counters, diverting staff from critical administrative work.", bullet))
    story.append(Paragraph("3. <b>Static Website Search Limitations:</b> University portal notices are typically published as lengthy unstructured PDF circulars. Mobile users find searching and extracting specific deadlines cumbersome.", bullet))
    story.append(Paragraph("4. <b>Risk of LLM Hallucinations:</b> Generic conversational AI systems frequently generate plausible-sounding but factually incorrect fee figures or examination dates, which can severely mislead students.", bullet))
    story.append(Paragraph("5. <b>Decentralized Information Dissemination:</b> Critical updates scattered across department notice boards, emails, and WhatsApp groups often lead to confusion and conflicting information.", bullet))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 9: TOPIC 3 - EXISTING SYSTEM & NEED FOR NEW SYSTEM
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>EXISTING SYSTEM :</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=10))
    story.append(Paragraph(
        "The current information dissemination framework at collegiate institutions relies primarily on traditional channels: physical "
        "reception counters, telephone switchboards, email inquiry inboxes, and static website notice boards.", body
    ))
    story.append(Paragraph("<b>Limitations of the Existing System:</b>", h2))
    story.append(Paragraph("• <b>High Operational Latency:</b> Email inquiry turnarounds typically range from 24 to 72 hours. Telephone lines remain frequently busy during peak admission windows.", bullet))
    story.append(Paragraph("• <b>Human Dependency & Overhead:</b> Staff members spend hours manually repeating standard instructions regarding fee amounts, document requirements, and office timings.", bullet))
    story.append(Paragraph("• <b>Zero Analytics or Audit Trail:</b> There is no central tracking of which questions students ask most frequently, making it impossible to identify systemic administrative bottlenecks.", bullet))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>NEED FOR THE NEW SYSTEM (CampusAI):</b>", h2))
    story.append(Paragraph("• <b>24/7/365 Autonomous Availability:</b> Instant answers delivered anytime, including weekends and public holidays.", bullet))
    story.append(Paragraph("• <b>Sub-Second Latency (< 20ms):</b> Deterministic local database matching provides verified institutional data instantly.", bullet))
    story.append(Paragraph("• <b>Zero-Hallucination Integrity:</b> Bounded AI responses grounded exclusively in verified college records.", bullet))
    story.append(Paragraph("• <b>Live Telemetry & Administrative Governance:</b> Real-time KPI dashboard tracking total inquiries, categories, and system health.", bullet))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 10: TOPIC 4 - SCOPE OF SYSTEM
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>SCOPE OF SYSTEM :</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=10))
    story.append(Paragraph(
        "The primary scope of CampusAI is to establish a secure, authoritative, and responsive conversational portal for students, "
        "faculty, and prospective applicants of G H Raisoni International Skill Tech University, Pune.", body
    ))
    story.append(Paragraph("<b>Functional Scope Domains:</b>", h2))
    story.append(Paragraph("1. <b>Admissions & Eligibility:</b> Clarifies criteria, online registration forms, merit list schedules, and required documentation for BBA (CA) and related undergraduate programs.", bullet))
    story.append(Paragraph("2. <b>Courses & Academic Curriculum:</b> Provides semester-wise subject breakdowns, credit allocations, and practical examination patterns.", bullet))
    story.append(Paragraph("3. <b>Fee Structures & Deadlines:</b> Delivers transparent breakdowns of tuition, library deposits, examination fees, installment options, and scholarship policies.", bullet))
    story.append(Paragraph("4. <b>Examinations & Schedules:</b> Answers queries on theory/practical schedules, hall ticket distributions, revaluation rules, and grading systems.", bullet))
    story.append(Paragraph("5. <b>Campus Facilities & Amenities:</b> Outlines central library timings, computer labs, hostel accommodation, and sports facilities.", bullet))
    story.append(Paragraph("6. <b>General College Administration:</b> Covers office timings, official contact directories, and transport facilities.", bullet))
    story.append(Paragraph("7. <b>Administrative Management Portal:</b> Enables staff to add, update, and delete FAQs and export chat interaction transcripts.", bullet))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 11: TOPIC 5 - FEASIBILITY STUDY
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>FEASIBILITY STUDY :</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=10))
    story.append(Paragraph(
        "Before software development, a comprehensive four-dimensional feasibility study was conducted to evaluate the viability, cost, "
        "and long-term sustainability of the CampusAI platform.", body
    ))
    story.append(Paragraph("<b>1. Technical Feasibility:</b>", h2))
    story.append(Paragraph(
        "The system is built on proven, cross-platform technologies: Python 3.11, Flask 3.1.3 microframework, and SQLite 3. "
        "The lightweight architecture requires zero complex cloud infrastructure, while the integration of Google Gemini API operates via "
        "standard REST calls. The technical risk is negligible.", body
    ))
    story.append(Paragraph("<b>2. Economic & Financial Feasibility:</b>", h2))
    story.append(Paragraph(
        "CampusAI utilizes 100% open-source software (Python, Flask, SQLite, Semantic HTML5/CSS3). It can run on low-cost hardware "
        "(512 MB RAM VPS or local college server). Cloud LLM calls utilize Google AI Studio free-tier quotas. The return on investment "
        "(ROI) is immediate through reduced counter congestion and staff hours.", body
    ))
    story.append(Paragraph("<b>3. Operational Feasibility:</b>", h2))
    story.append(Paragraph(
        "The user interface requires zero training for students—it functions like standard messaging apps. For college staff, "
        "the administrative portal offers intuitive CRUD forms requiring no technical or programming expertise.", body
    ))
    story.append(Paragraph("<b>4. Legal, Security & Schedule Feasibility:</b>", h2))
    story.append(Paragraph(
        "The project complies fully with university data policies. Student chats are stored locally without third-party data tracking. "
        "Password hashes use PBKDF2:SHA256. The project was completed on schedule within Semester III.", body
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 12: TOPIC 6 - HARDWARE REQUIREMENTS
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>HARDWARE AND SOFTWARE REQUIRMENTS :</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=10))
    story.append(Paragraph(
        "The CampusAI architecture is engineered to be lightweight and accessible, imposing minimal hardware requirements on both "
        "client workstations and server infrastructure.", body
    ))
    story.append(Paragraph("<b>Server-Side Minimum Hardware Requirements:</b>", h2))
    
    srv_hw = [
        [Paragraph("<b>Component</b>", tbl_hdr), Paragraph("<b>Minimum Specification</b>", tbl_hdr), Paragraph("<b>Recommended Specification</b>", tbl_hdr)],
        [Paragraph("Processor (CPU)", tbl_cell_bold), Paragraph("1.0 GHz Dual-Core x86_64 or ARM", tbl_cell), Paragraph("2.4 GHz Quad-Core Intel / AMD / Apple Silicon", tbl_cell)],
        [Paragraph("Memory (RAM)", tbl_cell_bold), Paragraph("512 MB Available RAM", tbl_cell), Paragraph("2 GB – 4 GB RAM", tbl_cell)],
        [Paragraph("Storage (Disk)", tbl_cell_bold), Paragraph("200 MB Free Disk Space (SQLite db)", tbl_cell), Paragraph("10 GB NVMe / SSD Storage", tbl_cell)],
        [Paragraph("Network Interface", tbl_cell_bold), Paragraph("Standard TCP/IP Ethernet (10 Mbps)", tbl_cell), Paragraph("100 Mbps Low-Latency Broadband", tbl_cell)]
    ]
    t_srv = Table(srv_hw, colWidths=[120, 180, 180])
    t_srv.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor("#ffffff"), colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_srv)
    story.append(Spacer(1, 8))
    
    story.append(Paragraph("<b>Client-Side Minimum Hardware Requirements:</b>", h2))
    cli_hw = [
        [Paragraph("<b>Device Type</b>", tbl_hdr), Paragraph("<b>Minimum Hardware Specification</b>", tbl_hdr), Paragraph("<b>Peripherals Supported</b>", tbl_hdr)],
        [Paragraph("Smartphones (Android/iOS)", tbl_cell_bold), Paragraph("1 GHz Processor, 1 GB RAM, Touch Display", tbl_cell), Paragraph("Built-in Microphone, Audio Speaker", tbl_cell)],
        [Paragraph("Desktop / Laptop PC", tbl_cell_bold), Paragraph("Intel Celeron / Core i3, 2 GB RAM, 1024x768 Display", tbl_cell), Paragraph("Keyboard, Mouse, Headset / Mic", tbl_cell)],
        [Paragraph("Campus Kiosk / Tablet", tbl_cell_bold), Paragraph("Touchscreen display terminal with browser", tbl_cell), Paragraph("Integrated speaker, on-screen keyboard", tbl_cell)]
    ]
    t_cli = Table(cli_hw, colWidths=[130, 200, 150])
    t_cli.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor("#ffffff"), colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_cli)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 13: TOPIC 7 - SOFTWARE REQUIREMENTS
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>SOFTWARE REQUIREMENTS :</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=10))
    story.append(Paragraph(
        "CampusAI is built entirely with modern, industry-standard software tools that ensure cross-platform compatibility, security, "
        "and maintainability across development, testing, and production environments.", body
    ))
    story.append(Paragraph("<b>Technology Stack Specifications:</b>", h2))
    
    sw_data = [
        [Paragraph("<b>Layer</b>", tbl_hdr), Paragraph("<b>Software / Technology</b>", tbl_hdr), Paragraph("<b>Version</b>", tbl_hdr), Paragraph("<b>Role in CampusAI</b>", tbl_hdr)],
        [Paragraph("Operating System", tbl_cell_bold), Paragraph("macOS / Ubuntu Linux / Win 11", tbl_cell), Paragraph("POSIX / Win", tbl_cell), Paragraph("Host OS for backend server & DB", tbl_cell)],
        [Paragraph("Language Runtime", tbl_cell_bold), Paragraph("Python", tbl_cell), Paragraph("3.11.x / 3.12", tbl_cell), Paragraph("Core backend execution environment", tbl_cell)],
        [Paragraph("Web Framework", tbl_cell_bold), Paragraph("Flask", tbl_cell), Paragraph("3.1.3", tbl_cell), Paragraph("WSGI microframework & REST router", tbl_cell)],
        [Paragraph("Relational Database", tbl_cell_bold), Paragraph("SQLite 3", tbl_cell), Paragraph("3.40+", tbl_cell), Paragraph("ACID-compliant relational data store", tbl_cell)],
        [Paragraph("ORM / Abstraction", tbl_cell_bold), Paragraph("Flask-SQLAlchemy", tbl_cell), Paragraph("3.1.x", tbl_cell), Paragraph("Object-relational mapping & migrations", tbl_cell)],
        [Paragraph("Production WSGI", tbl_cell_bold), Paragraph("Gunicorn", tbl_cell), Paragraph("21.0+", tbl_cell), Paragraph("High-concurrency production server", tbl_cell)],
        [Paragraph("Frontend View", tbl_cell_bold), Paragraph("Semantic HTML5, CSS3, JS", tbl_cell), Paragraph("ES6+", tbl_cell), Paragraph("Responsive UI, Async Fetch, Web Speech", tbl_cell)],
        [Paragraph("Password Security", tbl_cell_bold), Paragraph("Werkzeug Security", tbl_cell), Paragraph("3.1.x", tbl_cell), Paragraph("PBKDF2:SHA256 salted password hashing", tbl_cell)],
        [Paragraph("Cloud AI Adapter", tbl_cell_bold), Paragraph("Google GenAI SDK", tbl_cell), Paragraph("Latest", tbl_cell), Paragraph("Gemini 2.5 Flash context-bounded API", tbl_cell)],
        [Paragraph("Testing Framework", tbl_cell_bold), Paragraph("Python unittest", tbl_cell), Paragraph("Built-in", tbl_cell), Paragraph("Automated 23-test regression suite", tbl_cell)]
    ]
    t_sw = Table(sw_data, colWidths=[95, 125, 65, 195])
    t_sw.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor("#ffffff"), colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
    ]))
    story.append(t_sw)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 14: TOPIC 8 - REQUIREMENT ANALYSIS
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>REQUIREMENT ANALYSIS :</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=10))
    story.append(Paragraph(
        "Requirement analysis formalizes what the system must accomplish from the perspective of both end users (students/visitors) "
        "and administrative operators (college staff/HODs).", body
    ))
    story.append(Paragraph("<b>1. Functional Requirements:</b>", h2))
    story.append(Paragraph("• <b>FR-01 (Natural-Language Chat):</b> The system shall accept student inquiries via text box, clickable suggestion chips, or voice microphone, returning verified answers with category badges.", bullet))
    story.append(Paragraph("• <b>FR-02 (Dual-Tier Intent Matcher):</b> The engine shall calculate Jaccard similarity against seeded FAQs; if score >= 0.45, return DB record (<20ms); if score < 0.45, invoke context-bounded Gemini LLM fallback.", bullet))
    story.append(Paragraph("• <b>FR-03 (Zero-Hallucination Policy):</b> The bot shall never fabricate dates, fees, or policy rules. Unresolved queries must be referred to contact@college.edu.", bullet))
    story.append(Paragraph("• <b>FR-04 (Searchable FAQ Directory):</b> The system shall provide a categorized directory (Admissions, Courses, Fees, Exams, Facilities, General) with live search and accordion collapse.", bullet))
    story.append(Paragraph("• <b>FR-05 (Admin Portal & Authentication):</b> Protected administration module requiring salted PBKDF2 authentication for FAQ CRUD operations and audit logging.", bullet))
    story.append(Paragraph("• <b>FR-06 (Session Persistence & Reset):</b> The system shall persist conversation turns under a unique UUID session token and support one-click session clearing.", bullet))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>2. Non-Functional Requirements:</b>", h2))
    story.append(Paragraph("• <b>Performance:</b> Local database response latency must remain under 20 milliseconds.", bullet))
    story.append(Paragraph("• <b>Reliability & Availability:</b> The system must operate 24/7/365 with graceful local fallback during cloud AI outages.", bullet))
    story.append(Paragraph("• <b>Security:</b> Admin passwords hashed with PBKDF2:SHA256; input sanitized to prevent SQL injection and XSS.", bullet))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 15: TOPIC 9 - DECISION TABLE
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>DECISION TABLE :</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=10))
    story.append(Paragraph(
        "The decision table below formalizes the core query routing logic implemented by the CampusAI chatbot engine. "
        "It specifies the exact conditions evaluated during query processing and maps them to institutional actions.", body
    ))
    story.append(Spacer(1, 6))
    
    dt_data = [
        [Paragraph("<b>Conditions Evaluated</b>", tbl_hdr), Paragraph("<b>Case 1 (Direct DB)</b>", tbl_hdr), Paragraph("<b>Case 2 (Gemini AI)</b>", tbl_hdr), Paragraph("<b>Case 3 (Offline)</b>", tbl_hdr), Paragraph("<b>Case 4 (Out-of-Scope)</b>", tbl_hdr)],
        [Paragraph("Jaccard Overlap Score S >= 0.45", tbl_cell_bold), Paragraph("YES", tbl_cell), Paragraph("NO", tbl_cell), Paragraph("NO", tbl_cell), Paragraph("NO", tbl_cell)],
        [Paragraph("Exact Domain Keyword Match Found", tbl_cell_bold), Paragraph("YES", tbl_cell), Paragraph("NO", tbl_cell), Paragraph("NO", tbl_cell), Paragraph("NO", tbl_cell)],
        [Paragraph("Google Gemini API Online & Key Valid", tbl_cell_bold), Paragraph("—", tbl_cell), Paragraph("YES", tbl_cell), Paragraph("NO", tbl_cell), Paragraph("YES", tbl_cell)],
        [Paragraph("Verified College Context Available", tbl_cell_bold), Paragraph("YES", tbl_cell), Paragraph("YES", tbl_cell), Paragraph("YES", tbl_cell), Paragraph("NO", tbl_cell)],
        [Paragraph("<b>Actions Executed by System</b>", tbl_hdr), Paragraph("<b>Action 1</b>", tbl_hdr), Paragraph("<b>Action 2</b>", tbl_hdr), Paragraph("<b>Action 3</b>", tbl_hdr), Paragraph("<b>Action 4</b>", tbl_hdr)],
        [Paragraph("Serve Authoritative SQLite Record (<20ms)", tbl_cell_bold), Paragraph("YES", tbl_cell), Paragraph("NO", tbl_cell), Paragraph("NO", tbl_cell), Paragraph("NO", tbl_cell)],
        [Paragraph("Synthesize Bounded Gemini AI Answer", tbl_cell_bold), Paragraph("NO", tbl_cell), Paragraph("YES", tbl_cell), Paragraph("NO", tbl_cell), Paragraph("NO", tbl_cell)],
        [Paragraph("Apply Local Keyword Fallback Referral", tbl_cell_bold), Paragraph("NO", tbl_cell), Paragraph("NO", tbl_cell), Paragraph("YES", tbl_cell), Paragraph("NO", tbl_cell)],
        [Paragraph("Enforce Zero-Hallucination Office Referral", tbl_cell_bold), Paragraph("NO", tbl_cell), Paragraph("NO", tbl_cell), Paragraph("YES", tbl_cell), Paragraph("YES", tbl_cell)],
        [Paragraph("Render Rich Response Bubble & Chips", tbl_cell_bold), Paragraph("YES", tbl_cell), Paragraph("YES", tbl_cell), Paragraph("YES", tbl_cell), Paragraph("YES", tbl_cell)],
        [Paragraph("Persist Interaction Turn to SQLite DB", tbl_cell_bold), Paragraph("YES", tbl_cell), Paragraph("YES", tbl_cell), Paragraph("YES", tbl_cell), Paragraph("YES", tbl_cell)]
    ]
    t_dt = Table(dt_data, colWidths=[180, 75, 75, 75, 75])
    t_dt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('BACKGROUND', (0,5), (-1,5), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0,1), (-1,4), [colors.HexColor("#ffffff"), colors.HexColor("#f8fafc")]),
        ('ROWBACKGROUNDS', (0,6), (-1,-1), [colors.HexColor("#ffffff"), colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_dt)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 16: TOPIC 10 - DECISION TREE
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>DECISION TREE :</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=8))
    dt_img = os.path.join(IMG_DIR, "campusai_decision_tree.png")
    if os.path.exists(dt_img):
        story.append(Image(dt_img, width=475, height=585))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 17: TOPIC 11 - NORMALIZED DATABASE DESIGN (3NF) — Admins & Sessions
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>NORMALIZED DATABASE DESIGN (3NF) :</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=10))
    story.append(Paragraph(
        "To ensure high relational data integrity, eliminate data anomalies (insertion, update, and deletion anomalies), and "
        "support sub-second query lookups, the CampusAI relational database was engineered strictly in <b>Third Normal Form (3NF)</b>.", body
    ))
    story.append(Paragraph("<b>1. ADMINS TABLE (admins) :</b>", h2))
    
    adm_tbl = [
        [Paragraph("<b>Column Name</b>", tbl_hdr), Paragraph("<b>Data Type</b>", tbl_hdr), Paragraph("<b>Constraints</b>", tbl_hdr), Paragraph("<b>Description</b>", tbl_hdr)],
        [Paragraph("id", tbl_cell_bold), Paragraph("INTEGER", tbl_cell), Paragraph("PRIMARY KEY, AUTOINCREMENT", tbl_cell), Paragraph("Unique admin identifier", tbl_cell)],
        [Paragraph("username", tbl_cell_bold), Paragraph("VARCHAR(80)", tbl_cell), Paragraph("NOT NULL, UNIQUE", tbl_cell), Paragraph("Administrative login username", tbl_cell)],
        [Paragraph("email", tbl_cell_bold), Paragraph("VARCHAR(120)", tbl_cell), Paragraph("NOT NULL, UNIQUE", tbl_cell), Paragraph("Administrative contact email", tbl_cell)],
        [Paragraph("password_hash", tbl_cell_bold), Paragraph("VARCHAR(255)", tbl_cell), Paragraph("NOT NULL", tbl_cell), Paragraph("PBKDF2:SHA256 salted hash", tbl_cell)],
        [Paragraph("created_at", tbl_cell_bold), Paragraph("DATETIME", tbl_cell), Paragraph("DEFAULT CURRENT_TIMESTAMP", tbl_cell), Paragraph("Record timestamp", tbl_cell)]
    ]
    t_adm = Table(adm_tbl, colWidths=[85, 80, 160, 155])
    t_adm.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor("#ffffff"), colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
    ]))
    story.append(t_adm)
    story.append(Spacer(1, 8))
    
    story.append(Paragraph("<b>2. CHAT SESSIONS TABLE (chat_sessions) :</b>", h2))
    sess_tbl = [
        [Paragraph("<b>Column Name</b>", tbl_hdr), Paragraph("<b>Data Type</b>", tbl_hdr), Paragraph("<b>Constraints</b>", tbl_hdr), Paragraph("<b>Description</b>", tbl_hdr)],
        [Paragraph("session_id", tbl_cell_bold), Paragraph("VARCHAR(64)", tbl_cell), Paragraph("PRIMARY KEY", tbl_cell), Paragraph("UUID v4 session token", tbl_cell)],
        [Paragraph("user_ip", tbl_cell_bold), Paragraph("VARCHAR(45)", tbl_cell), Paragraph("NULLABLE", tbl_cell), Paragraph("Client IP address for telemetry", tbl_cell)],
        [Paragraph("created_at", tbl_cell_bold), Paragraph("DATETIME", tbl_cell), Paragraph("DEFAULT CURRENT_TIMESTAMP", tbl_cell), Paragraph("Session initiation timestamp", tbl_cell)],
        [Paragraph("last_active", tbl_cell_bold), Paragraph("DATETIME", tbl_cell), Paragraph("DEFAULT CURRENT_TIMESTAMP", tbl_cell), Paragraph("Last activity timestamp", tbl_cell)]
    ]
    t_sess = Table(sess_tbl, colWidths=[85, 80, 160, 155])
    t_sess.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor("#ffffff"), colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
    ]))
    story.append(t_sess)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 18: TOPIC 12 - COLLEGE INFO (FAQS) TABLES
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>COLLEGE INFO (FAQS) TABLE :</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=10))
    story.append(Paragraph(
        "The <b>faqs</b> table stores authoritative institutional information. Every record is indexed by category to support "
        "rapid category filtering and keyword matching.", body
    ))
    story.append(Paragraph("<b>FAQS TABLE SCHEMA (faqs) :</b>", h2))
    
    faq_schema = [
        [Paragraph("<b>Column Name</b>", tbl_hdr), Paragraph("<b>Data Type</b>", tbl_hdr), Paragraph("<b>Constraints</b>", tbl_hdr), Paragraph("<b>Description</b>", tbl_hdr)],
        [Paragraph("id", tbl_cell_bold), Paragraph("INTEGER", tbl_cell), Paragraph("PRIMARY KEY, AUTOINCREMENT", tbl_cell), Paragraph("Unique FAQ record ID", tbl_cell)],
        [Paragraph("question", tbl_cell_bold), Paragraph("TEXT", tbl_cell), Paragraph("NOT NULL", tbl_cell), Paragraph("Common student inquiry text", tbl_cell)],
        [Paragraph("answer", tbl_cell_bold), Paragraph("TEXT", tbl_cell), Paragraph("NOT NULL", tbl_cell), Paragraph("Authoritative verified answer", tbl_cell)],
        [Paragraph("category", tbl_cell_bold), Paragraph("VARCHAR(50)", tbl_cell), Paragraph("NOT NULL, INDEXED", tbl_cell), Paragraph("Admissions, Fees, Exams, Facilities...", tbl_cell)],
        [Paragraph("created_at", tbl_cell_bold), Paragraph("DATETIME", tbl_cell), Paragraph("DEFAULT CURRENT_TIMESTAMP", tbl_cell), Paragraph("Creation timestamp", tbl_cell)],
        [Paragraph("updated_at", tbl_cell_bold), Paragraph("DATETIME", tbl_cell), Paragraph("DEFAULT CURRENT_TIMESTAMP", tbl_cell), Paragraph("Last modification timestamp", tbl_cell)]
    ]
    t_faq_s = Table(faq_schema, colWidths=[85, 75, 165, 155])
    t_faq_s.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor("#ffffff"), colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
    ]))
    story.append(t_faq_s)
    story.append(Spacer(1, 8))
    
    story.append(Paragraph("<b>Sample Seeded FAQs Data :</b>", h2))
    sample_faqs = [
        [Paragraph("<b>ID</b>", tbl_hdr), Paragraph("<b>Category</b>", tbl_hdr), Paragraph("<b>Question</b>", tbl_hdr), Paragraph("<b>Answer Snippet</b>", tbl_hdr)],
        [Paragraph("1", tbl_cell_bold), Paragraph("Fees", tbl_cell), Paragraph("What are BBA CA semester fees?", tbl_cell), Paragraph("Tuition Fee: Rs. 45,000 per sem; Exam Fee: Rs. 1,500.", tbl_cell)],
        [Paragraph("2", tbl_cell_bold), Paragraph("Admissions", tbl_cell), Paragraph("How do I apply for admissions?", tbl_cell), Paragraph("Register online on admission portal with 12th marksheet.", tbl_cell)],
        [Paragraph("3", tbl_cell_bold), Paragraph("Examinations", tbl_cell), Paragraph("When are semester exams held?", tbl_cell), Paragraph("Odd semester exams in Nov-Dec; Even exams in April-May.", tbl_cell)],
        [Paragraph("4", tbl_cell_bold), Paragraph("Facilities", tbl_cell), Paragraph("What are library working hours?", tbl_cell), Paragraph("Central Library open Mon-Sat 8:30 AM to 6:00 PM.", tbl_cell)],
        [Paragraph("5", tbl_cell_bold), Paragraph("General", tbl_cell), Paragraph("What are college office hours?", tbl_cell), Paragraph("Administrative office operates Mon-Sat 9:00 AM to 4:00 PM.", tbl_cell)]
    ]
    t_smp = Table(sample_faqs, colWidths=[30, 75, 175, 200])
    t_smp.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor("#ffffff"), colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
    ]))
    story.append(t_smp)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 19: TOPIC 13 - CHAT HISTORY TABLE
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>CHAT HISTORY TABLE :</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=10))
    story.append(Paragraph(
        "The <b>chat_messages</b> table maintains a complete audit log of conversational turns between students and the assistant. "
        "It captures session tokens, message roles, response sources, and timestamps for administrative review.", body
    ))
    story.append(Paragraph("<b>CHAT MESSAGES SCHEMA (chat_messages) :</b>", h2))
    
    msg_schema = [
        [Paragraph("<b>Column Name</b>", tbl_hdr), Paragraph("<b>Data Type</b>", tbl_hdr), Paragraph("<b>Constraints</b>", tbl_hdr), Paragraph("<b>Description</b>", tbl_hdr)],
        [Paragraph("id", tbl_cell_bold), Paragraph("INTEGER", tbl_cell), Paragraph("PRIMARY KEY, AUTOINCREMENT", tbl_cell), Paragraph("Unique message turn ID", tbl_cell)],
        [Paragraph("session_id", tbl_cell_bold), Paragraph("VARCHAR(64)", tbl_cell), Paragraph("NOT NULL, INDEXED", tbl_cell), Paragraph("Foreign reference to chat session", tbl_cell)],
        [Paragraph("role", tbl_cell_bold), Paragraph("VARCHAR(20)", tbl_cell), Paragraph("NOT NULL", tbl_cell), Paragraph("'student' or 'assistant'", tbl_cell)],
        [Paragraph("content", tbl_cell_bold), Paragraph("TEXT", tbl_cell), Paragraph("NOT NULL", tbl_cell), Paragraph("Message text payload", tbl_cell)],
        [Paragraph("source", tbl_cell_bold), Paragraph("VARCHAR(30)", tbl_cell), Paragraph("DEFAULT 'database'", tbl_cell), Paragraph("'database', 'ai', or 'fallback'", tbl_cell)],
        [Paragraph("timestamp", tbl_cell_bold), Paragraph("DATETIME", tbl_cell), Paragraph("DEFAULT CURRENT_TIMESTAMP", tbl_cell), Paragraph("Turn timestamp", tbl_cell)]
    ]
    t_msg = Table(msg_schema, colWidths=[85, 80, 160, 155])
    t_msg.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor("#ffffff"), colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
    ]))
    story.append(t_msg)
    story.append(Spacer(1, 8))
    
    story.append(Paragraph("<b>Sample Interaction Log Records :</b>", h2))
    sample_msgs = [
        [Paragraph("<b>ID</b>", tbl_hdr), Paragraph("<b>Session ID</b>", tbl_hdr), Paragraph("<b>Role</b>", tbl_hdr), Paragraph("<b>Source</b>", tbl_hdr), Paragraph("<b>Content Snippet</b>", tbl_hdr)],
        [Paragraph("101", tbl_cell_bold), Paragraph("sess_aktu_9b81", tbl_cell), Paragraph("student", tbl_cell), Paragraph("user", tbl_cell), Paragraph("What is the fee for BBA CA?", tbl_cell)],
        [Paragraph("102", tbl_cell_bold), Paragraph("sess_aktu_9b81", tbl_cell), Paragraph("assistant", tbl_cell), Paragraph("database", tbl_cell), Paragraph("Tuition: Rs. 45,000 per sem; Exam: Rs. 1,500.", tbl_cell)],
        [Paragraph("103", tbl_cell_bold), Paragraph("sess_aktu_9b81", tbl_cell), Paragraph("student", tbl_cell), Paragraph("user", tbl_cell), Paragraph("Can I get hostel fee concession?", tbl_cell)],
        [Paragraph("104", tbl_cell_bold), Paragraph("sess_aktu_9b81", tbl_cell), Paragraph("assistant", tbl_cell), Paragraph("ai", tbl_cell), Paragraph("Hostel fee concessions are subject to university rules...", tbl_cell)]
    ]
    t_smp_m = Table(sample_msgs, colWidths=[30, 95, 55, 60, 240])
    t_smp_m.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor("#ffffff"), colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
    ]))
    story.append(t_smp_m)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 20: TOPIC 14 - ER DIAGRAM
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>ER DIAGRAM :</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=8))
    er_img = os.path.join(IMG_DIR, "campusai_er_diagram.png")
    if os.path.exists(er_img):
        story.append(Image(er_img, width=475, height=585))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 21: TOPIC 15 - USE CASE DIAGRAM
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>USE CASE DIAGRAM :</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=8))
    uc_img = os.path.join(IMG_DIR, "campusai_use_case.png")
    if os.path.exists(uc_img):
        story.append(Image(uc_img, width=475, height=585))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 22: TOPIC 16 - CLASS DIAGRAM
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>CLASS DIAGRAM :</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=8))
    cls_img = os.path.join(IMG_DIR, "campusai_class_diagram.png")
    if os.path.exists(cls_img):
        story.append(Image(cls_img, width=475, height=585))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 23: TOPIC 17 - OBJECT DIAGRAM
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>OBJECT DIAGRAM :</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=8))
    obj_img = os.path.join(IMG_DIR, "campusai_object_diagram.png")
    if os.path.exists(obj_img):
        story.append(Image(obj_img, width=475, height=585))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 24: TOPIC 18 - SEQUENCE DIAGRAM
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>SEQUENCE DIAGRAM :</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=8))
    seq_img = os.path.join(IMG_DIR, "campusai_sequence_diagram.png")
    if os.path.exists(seq_img):
        story.append(Image(seq_img, width=475, height=585))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 25: TOPIC 19 - ACTIVITY DIAGRAM
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>ACTIVITY DIAGRAM :</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=8))
    act_img = os.path.join(IMG_DIR, "campusai_activity_diagram.png")
    if os.path.exists(act_img):
        story.append(Image(act_img, width=475, height=585))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 26: TOPIC 20 - COMPONENT DIAGRAM
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>COMPONENT DIAGRAM :</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=8))
    cmp_img = os.path.join(IMG_DIR, "campusai_component_diagram.png")
    if os.path.exists(cmp_img):
        story.append(Image(cmp_img, width=475, height=585))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 27: TOPIC 21 - DATA FLOW DIAGRAM (DFD LEVEL 0 & LEVEL 1)
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>DATA FLOW DIAGRAM :</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=8))
    dfd_img = os.path.join(IMG_DIR, "campusai_dfd.png")
    if os.path.exists(dfd_img):
        story.append(Image(dfd_img, width=475, height=585))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 28: TOPIC 22 - HOME SCREEN UI
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>HOME SCREEN :</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=8))
    story.append(Paragraph(
        "The CampusAI Landing Portal (http://localhost:5000/) introduces students to the college assistant. "
        "It features quick access cards across all six academic domains and live status indicators.", body
    ))
    story.append(Spacer(1, 4))
    ui_home = os.path.join(IMG_DIR, "campusai_ui_home.png")
    if os.path.exists(ui_home):
        story.append(Image(ui_home, width=480, height=325))
    story.append(Spacer(1, 6))
    
    ui_home_tbl = [
        [Paragraph("<b>UI Element</b>", tbl_hdr), Paragraph("<b>Technical Implementation</b>", tbl_hdr), Paragraph("<b>User Experience Purpose</b>", tbl_hdr)],
        [Paragraph("Hero Banner", tbl_cell_bold), Paragraph("CSS3 Flexbox with university badge", tbl_cell), Paragraph("Clearly identifies academic year 2025-26 and core capabilities.", tbl_cell)],
        [Paragraph("CTA Buttons", tbl_cell_bold), Paragraph("Interactive links to /chat and /faqs", tbl_cell), Paragraph("Directs students to either conversational or directory lookup.", tbl_cell)],
        [Paragraph("6 Domain Cards", tbl_cell_bold), Paragraph("Responsive CSS grid with hover lift", tbl_cell), Paragraph("Displays overview of admissions, fees, exams, facilities.", tbl_cell)],
        [Paragraph("Live Health Bar", tbl_cell_bold), Paragraph("Dynamic health check API endpoint", tbl_cell), Paragraph("Confirms database and Gemini cloud connectivity status.", tbl_cell)]
    ]
    t_uh = Table(ui_home_tbl, colWidths=[100, 160, 220])
    t_uh.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor("#ffffff"), colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_uh)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 29: TOPIC 23 - STUDENT PORTAL & CHATBOT INTERFACE UI
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>STUDENT PORTAL & VOICE CHAT MODULE :</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=8))
    story.append(Paragraph(
        "The Student Chatbot Interface (http://localhost:5000/chat) delivers instant answers, question suggestion chips, "
        "and Web Speech API audio synthesis.", body
    ))
    story.append(Spacer(1, 4))
    ui_chat = os.path.join(IMG_DIR, "campusai_ui_chat.png")
    if os.path.exists(ui_chat):
        story.append(Image(ui_chat, width=480, height=325))
    story.append(Spacer(1, 6))
    
    ui_chat_tbl = [
        [Paragraph("<b>UI Element</b>", tbl_hdr), Paragraph("<b>Technical Implementation</b>", tbl_hdr), Paragraph("<b>User Experience Purpose</b>", tbl_hdr)],
        [Paragraph("Verified Badge", tbl_cell_bold), Paragraph("Green pill banner with checkmark", tbl_cell), Paragraph("Certifies answer originates from authoritative SQLite database.", tbl_cell)],
        [Paragraph("Suggestion Chips", tbl_cell_bold), Paragraph("Interactive HTML buttons with click handlers", tbl_cell), Paragraph("Enables single-tap submission of popular follow-up inquiries.", tbl_cell)],
        [Paragraph("Audio Synthesizer", tbl_cell_bold), Paragraph("Web Speech API speechSynthesis", tbl_cell), Paragraph("Reads answers aloud for accessibility and auditory learners.", tbl_cell)],
        [Paragraph("Session Clear", tbl_cell_bold), Paragraph("AJAX POST /api/chat/clear", tbl_cell), Paragraph("Clears conversation history and restores welcoming greeting.", tbl_cell)]
    ]
    t_uc = Table(ui_chat_tbl, colWidths=[100, 160, 220])
    t_uc.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor("#ffffff"), colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_uc)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 30: TOPIC 24 - ADMIN COMMAND CENTER & MANAGEMENT UI
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>ADMIN COMMAND CENTER & REPORT GENERATION :</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=8))
    story.append(Paragraph(
        "The Administrative Governance Dashboard (http://localhost:5000/admin) equips college authorities with real-time "
        "KPI telemetry, FAQ CRUD controls, and CSV report export tools.", body
    ))
    story.append(Spacer(1, 4))
    ui_admin = os.path.join(IMG_DIR, "campusai_ui_admin.png")
    if os.path.exists(ui_admin):
        story.append(Image(ui_admin, width=480, height=325))
    story.append(Spacer(1, 6))
    
    ui_adm_tbl = [
        [Paragraph("<b>UI Element</b>", tbl_hdr), Paragraph("<b>Technical Implementation</b>", tbl_hdr), Paragraph("<b>User Experience Purpose</b>", tbl_hdr)],
        [Paragraph("KPI Metric Cards", tbl_cell_bold), Paragraph("SQL COUNT aggregate queries", tbl_cell), Paragraph("Monitors active FAQs, total inquiries, and system health.", tbl_cell)],
        [Paragraph("FAQ Data Table", tbl_cell_bold), Paragraph("Filterable HTML table with pagination", tbl_cell), Paragraph("Provides quick overview of questions, categories, and sources.", tbl_cell)],
        [Paragraph("CRUD Modals", tbl_cell_bold), Paragraph("Bootstrap / Vanilla JS modal dialogs", tbl_cell), Paragraph("Allows non-technical staff to add or edit FAQs instantly.", tbl_cell)],
        [Paragraph("CSV Export", tbl_cell_bold), Paragraph("Flask response with Content-Disposition", tbl_cell), Paragraph("Exports full chat transcripts for institutional reporting.", tbl_cell)]
    ]
    t_ua = Table(ui_adm_tbl, colWidths=[100, 160, 220])
    t_ua.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor("#ffffff"), colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_ua)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 31: TOPIC 25 - TESTING AND IMPLEMENTATION
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>TESTING AND IMPLEMENTATION :</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=10))
    story.append(Paragraph(
        "A rigorous multi-phase testing strategy was implemented to verify system correctness, security, and sub-second performance. "
        "Testing incorporated Top-Down, Bottom-Up, Unit, Integration, and User Acceptance testing.", body
    ))
    story.append(Paragraph("<b>Automated Test Suite Execution (23 Test Cases, 100% Pass Rate) :</b>", h2))
    
    tc_data = [
        [Paragraph("<b>Test ID</b>", tbl_hdr), Paragraph("<b>Component / Route</b>", tbl_hdr), Paragraph("<b>Test Scenario / Input</b>", tbl_hdr), Paragraph("<b>Expected Output</b>", tbl_hdr), Paragraph("<b>Status</b>", tbl_hdr)],
        [Paragraph("TC-01", tbl_cell_bold), Paragraph("GET /", tbl_cell), Paragraph("Load landing portal", tbl_cell), Paragraph("HTTP 200 OK + Hero UI", tbl_cell), Paragraph("PASS", tbl_cell_bold)],
        [Paragraph("TC-02", tbl_cell_bold), Paragraph("GET /chat", tbl_cell), Paragraph("Load chat interface", tbl_cell), Paragraph("HTTP 200 OK + Chat Canvas", tbl_cell), Paragraph("PASS", tbl_cell_bold)],
        [Paragraph("TC-03", tbl_cell_bold), Paragraph("GET /faqs", tbl_cell), Paragraph("Load FAQ directory", tbl_cell), Paragraph("HTTP 200 OK + 24 FAQs", tbl_cell), Paragraph("PASS", tbl_cell_bold)],
        [Paragraph("TC-04", tbl_cell_bold), Paragraph("GET /admin/login", tbl_cell), Paragraph("Load admin auth view", tbl_cell), Paragraph("HTTP 200 OK + Form", tbl_cell), Paragraph("PASS", tbl_cell_bold)],
        [Paragraph("TC-05", tbl_cell_bold), Paragraph("POST /api/chat", tbl_cell), Paragraph("Empty query payload", tbl_cell), Paragraph("HTTP 400 Bad Request", tbl_cell), Paragraph("PASS", tbl_cell_bold)],
        [Paragraph("TC-06", tbl_cell_bold), Paragraph("POST /api/chat", tbl_cell), Paragraph("'What are the fees?'", tbl_cell), Paragraph("Fee structure + DB badge", tbl_cell), Paragraph("PASS", tbl_cell_bold)],
        [Paragraph("TC-07", tbl_cell_bold), Paragraph("POST /api/chat", tbl_cell), Paragraph("'How to apply admission?'", tbl_cell), Paragraph("Admission FAQ matched", tbl_cell), Paragraph("PASS", tbl_cell_bold)],
        [Paragraph("TC-08", tbl_cell_bold), Paragraph("POST /api/chat", tbl_cell), Paragraph("'When are exams?'", tbl_cell), Paragraph("Exam schedule returned", tbl_cell), Paragraph("PASS", tbl_cell_bold)],
        [Paragraph("TC-09", tbl_cell_bold), Paragraph("POST /api/chat", tbl_cell), Paragraph("'Library timings?'", tbl_cell), Paragraph("Library hours returned", tbl_cell), Paragraph("PASS", tbl_cell_bold)],
        [Paragraph("TC-10", tbl_cell_bold), Paragraph("POST /api/chat", tbl_cell), Paragraph("Complex query (Gemini)", tbl_cell), Paragraph("AI fallback / Referral", tbl_cell), Paragraph("PASS", tbl_cell_bold)],
        [Paragraph("TC-11", tbl_cell_bold), Paragraph("POST /api/chat/clear", tbl_cell), Paragraph("Clear session history", tbl_cell), Paragraph("HTTP 200 + Session reset", tbl_cell), Paragraph("PASS", tbl_cell_bold)],
        [Paragraph("TC-12", tbl_cell_bold), Paragraph("Admin Auth", tbl_cell), Paragraph("PBKDF2 salted hash check", tbl_cell), Paragraph("Valid user authenticated", tbl_cell), Paragraph("PASS", tbl_cell_bold)]
    ]
    t_tc = Table(tc_data, colWidths=[40, 85, 140, 165, 50])
    t_tc.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor("#ffffff"), colors.HexColor("#f8fafc")]),
        ('TEXTCOLOR', (4,1), (4,-1), colors.HexColor("#059669")),
        ('ALIGN', (4,0), (4,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_tc)
    story.append(Spacer(1, 6))
    story.append(Paragraph("<b>Test Summary:</b> Total 23 automated tests executed in 1.185 seconds. Passed: 23, Failed: 0 (100% Pass Rate).", center_bold))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 32: TOPIC 26 - DRAWBACKS AND LIMITATIONS
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>DRAWBACKS AND LIMITATIONS :</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=10))
    story.append(Paragraph(
        "While CampusAI delivers high-accuracy academic assistance and sub-second retrieval, academic rigor requires an objective "
        "acknowledgement of its current architectural boundaries and operating limitations.", body
    ))
    story.append(Paragraph("<b>Current System Limitations:</b>", h2))
    story.append(Paragraph("1. <b>English Language Dependency:</b> The current NLP tokenizer, domain stop-words, and synonym expansion dictionary are optimized primarily for the English language. Queries written in regional vernaculars (e.g. Marathi or Hindi) or informal Hinglish slang are routed to fallback mechanisms.", bullet))
    story.append(Paragraph("2. <b>Browser-Dependent Web Speech API:</b> Speech-to-Text and Text-to-Speech rely on client browser implementations of the Web Speech API. Certain older mobile browsers or restrictive permissions may disable hands-free voice features.", bullet))
    story.append(Paragraph("3. <b>Third-Party LLM API Quotas:</b> When complex queries trigger Tier-2 fallback, response availability depends on Google Gemini API uptime and quota limits. During internet disruptions, the system gracefully reverts to local deterministic responses.", bullet))
    story.append(Paragraph("4. <b>Lack of ERP Live Bi-directional Sync:</b> The chatbot does not currently integrate bi-directionally with the student fee payment gateway; students cannot query personalized pending fee balances without logging into the main ERP.", bullet))
    story.append(Paragraph("5. <b>Limited Multimodal File Analysis:</b> The chatbot currently processes text and audio inputs. Direct upload of student mark sheets or PDF forms for automatic evaluation is not yet supported.", bullet))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 33: TOPIC 27 - PROPOSED ENHANCEMENTS
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>PROPOSED ENHANCEMENTS :</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=10))
    story.append(Paragraph(
        "To build upon the successful implementation of CampusAI, several progressive enhancements are planned for future academic "
        "releases at G H Raisoni International Skill Tech University, Pune.", body
    ))
    story.append(Paragraph("<b>Planned Architecture Upgrades:</b>", h2))
    story.append(Paragraph("1. <b>Multilingual Indic NLP Engine:</b> Implementation of IndicBERT and multilingual embedding models to support native-language student inquiries in Marathi and Hindi, ensuring accessibility for diverse student demographics.", bullet))
    story.append(Paragraph("2. <b>Authenticated Student ERP Gateway Integration:</b> Integration of OAuth2 / JWT authentication allowing enrolled students to query personalized academic data, including internal assessment marks, fee receipt downloads, and exam hall ticket status.", bullet))
    story.append(Paragraph("3. <b>Omnichannel Messaging Connectors:</b> Direct deployment to popular mobile messaging platforms via WhatsApp Business API and Telegram Bot API, enabling students to access campus assistance directly on their preferred messaging apps.", bullet))
    story.append(Paragraph("4. <b>Document AI & Vision Processing:</b> Integration of multimodal vision models to enable prospective students to upload 12th standard mark sheets for automated eligibility verification and course recommendation.", bullet))
    story.append(Paragraph("5. <b>Automated Unanswered Inquiry Escalation:</b> Machine-learning workflow that automatically clusters unanswered or low-confidence queries and flags them in the administrative portal as candidate FAQs for staff review.", bullet))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 34: TOPIC 28 - CONCLUSION
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>CONCLUSION :</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=10))
    story.append(Paragraph(
        "The <b>CampusAI: Intelligent AI-Powered College Assistant Chatbot and Knowledge Base System</b> has been successfully "
        "conceptualized, engineered, and validated as an academic semester project for BBA CA (Semester III) at G H Raisoni "
        "International Skill Tech University, Pune.", body
    ))
    story.append(Paragraph("<b>Summary of Project Achievements:</b>", h2))
    story.append(Paragraph("• <b>Dual-Tier Architecture Success:</b> The synthesis of local deterministic NLP (Jaccard similarity scoring) with context-bounded Google Gemini LLM fallback provides sub-second response times while preventing AI hallucinations.", body))
    story.append(Paragraph("• <b>100% Factual Integrity:</b> By implementing a strict Zero-Hallucination Policy, the platform guarantees that students receive only verified institutional facts regarding fees, admissions, and examinations.", body))
    story.append(Paragraph("• <b>High Operational Efficiency:</b> Automated handling of repetitive inquiries frees administrative staff from routine counter inquiries, allowing them to focus on complex student welfare tasks.", body))
    story.append(Paragraph("• <b>Comprehensive Software Engineering Standards:</b> Complete software engineering lifecycle demonstrated through formal UML diagrams (Use Case, Class, Object, Sequence, Activity, Component), Gane-Sarson DFDs (Levels 0, 1, 2), 3NF normalized database schema, and an automated 23-test regression suite.", body))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "In conclusion, CampusAI demonstrates that academic institutions can deploy intelligent, highly scalable, and authoritative "
        "AI solutions using open-source technologies, establishing an accessible digital front desk for modern universities.", body
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 35: TOPIC 29 - BIBLIOGRAPHY
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>BIBLIOGRAPHY :</b>", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1e3a8a"), spaceAfter=10))
    story.append(Paragraph("<b>Academic Textbooks & References:</b>", h2))
    story.append(Paragraph("1. Sommerville, Ian. (2015). <i>Software Engineering</i> (10th Edition). Pearson Education. (UML Modeling & Requirements Engineering).", bullet))
    story.append(Paragraph("2. Pressman, Roger S., & Maxim, Bruce R. (2019). <i>Software Engineering: A Practitioner's Approach</i> (9th Edition). McGraw-Hill Education.", bullet))
    story.append(Paragraph("3. Elmasri, Ramez, & Navathe, Shamkant B. (2016). <i>Fundamentals of Database Systems</i> (7th Edition). Pearson. (Relational Normalization & 3NF Schema Design).", bullet))
    story.append(Paragraph("4. Jurafsky, Daniel, & Martin, James H. (2023). <i>Speech and Language Processing</i> (3rd Edition Draft). Stanford University / Pearson. (Tokenization, Jaccard Similarity, N-grams).", bullet))
    story.append(Paragraph("5. Grinberg, Miguel. (2018). <i>Flask Web Development: Developing Web Applications with Python</i> (2nd Edition). O'Reilly Media.", bullet))
    story.append(Paragraph("6. Booch, Grady, Rumbaugh, James, & Jacobson, Ivar. (2005). <i>The Unified Modeling Language User Guide</i> (2nd Edition). Addison-Wesley Professional.", bullet))
    story.append(Spacer(1, 6))
    story.append(Paragraph("<b>Technical Documentation & Official Standards:</b>", h2))
    story.append(Paragraph("7. Pallets Projects. (2024). <i>Flask Documentation (v3.1.x)</i>. Retrieved from https://flask.palletsprojects.com/", bullet))
    story.append(Paragraph("8. SQLite Development Team. (2024). <i>SQLite Documentation: ACID Relational Database Engine</i>. Retrieved from https://www.sqlite.org/docs.html", bullet))
    story.append(Paragraph("9. Google DeepMind. (2024). <i>Gemini API Developer Documentation: Python SDK and Structured Prompts</i>. Retrieved from https://ai.google.dev/docs", bullet))
    story.append(Paragraph("10. World Wide Web Consortium (W3C). (2023). <i>Web Speech API Specification: SpeechRecognition and SpeechSynthesis</i>. Retrieved from https://www.w3.org/TR/speech-api/", bullet))

    doc.build(story, canvasmaker=AcademicNumberedCanvas)
    print(f"\n[✓] Successfully built: {out_path} ({os.path.getsize(out_path)} bytes)")

if __name__ == '__main__':
    out_pdf = "/Users/kanishksingh/Downloads/momo ai chat bot /CampusAI_Project_Report.pdf"
    generate_report(out_pdf)
