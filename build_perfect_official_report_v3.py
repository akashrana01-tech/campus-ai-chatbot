"""
CampusAI / College AI Chatbot Official 35-Page Project Report Generator
Fulfilling all teacher requirements:
1. Diagram structures match approved departmental reference (Images 1-4)
2. All topic headings from Page 7 to Page 35 are CENTERED
3. Database design (Topics 11, 12, 13) matches ERD and Class Diagram
4. ERD and Use Case diagrams match approved reference format
5. Conclusion and Bibliography match approved academic references
6. Student names:
   - Akash rana (ISTU25010120004)
   - Shreyash katke (ISTU25010120003)
   Guide: Prof. Sheela Satav
   Degree: BBA CA (Semester III, 2025-26)
   Institution: G H Raisoni International Skill Tech University, Pune-412207
"""

import io
import os
import pypdf
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.colors import white, black, HexColor
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT, TA_CENTER

SRC_PDF = "/Users/kanishksingh/.gemini/antigravity/brain/60288257-9f14-453a-bf1a-fc74825b030f/.user_uploaded/media_1793003039133_537ddeaa.pdf"
PAGE_W, PAGE_H = 594.96, 841.92

HEADINGS = {
    7: "INTRODUCTION :",
    8: "PROBLEM DEFINITION :",
    9: "EXISTING SYSTEM :",
    10: "SCOPE OF SYSTEM :",
    11: "FEASIBILITY STUDY",
    12: "HARDWARE AND SOFTWARE REQUIRMENTS :",
    13: "SOFTWARE REQUIREMENTS :",
    14: "REQUIREMENT ANALYSIS",
    15: "DECISION TABLE :",
    16: "DECISION TREE :",
    17: "NORMALIZED DATABASE DESIGN (3NF):",
    18: "COLLEGE INFO (FAQS) TABLE :",
    19: "CHAT HISTORY TABLE :",
    20: "ER DIAGRAM:",
    21: "USE CASE DIAGRAM:",
    22: "CLASS DIAGRAM",
    23: "OBJECT DIAGRAM :",
    24: "SEQUENCE DIAGRAM :",
    25: "ACTIVITY DIAGRAM :",
    26: "COMPONENT DIAGRAM :",
    27: "DATA FLOW DIAGRAM :",
    28: "HOME SCREEN :",
    29: "STUDENT PORTAL & VOICE CHAT MODULE :",
    30: "ADMIN COMMAND CENTER & REPORT GENERATION :",
    31: "TESTING AND IMPLEMENTATION :",
    32: "DRAWBACKS AND LIMITATIONS :",
    33: "PROPOSED ENHANCEMENTS :",
    34: "CONCLUSION :",
    35: "BIBLIOGRAPHY"
}

def generate_page1_overlay():
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(PAGE_W, PAGE_H))
    can.setFillColor(white)
    can.setStrokeColor(white)
    can.rect(120, 220, 360, 65, fill=1, stroke=0)
    
    can.setFillColor(black)
    can.setFont('Times-Bold', 14.25)
    can.drawCentredString(PAGE_W / 2.0, 258, "Akash rana (ISTU25010120004)")
    can.drawCentredString(PAGE_W / 2.0, 236, "Shreyash katke (ISTU25010120003)")
    can.save()
    packet.seek(0)
    return pypdf.PdfReader(packet).pages[0]

def generate_page2_overlay():
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(PAGE_W, PAGE_H))
    can.setFillColor(white)
    can.setStrokeColor(white)
    can.rect(70, 510, 455, 125, fill=1, stroke=0)
    
    style = ParagraphStyle(
        'CertBody',
        fontName='Times-Roman',
        fontSize=12,
        leading=23.25,
        alignment=TA_JUSTIFY,
        textColor=black
    )
    text = (
        "This is to certify that <b>Mr. Akash rana (Roll No: ISTU25010120004)</b> and "
        "<b>Mr. Shreyash katke (Roll No: ISTU25010120003)</b>, students of <b>SY BBA CA</b>, "
        "have satisfactorily completed their Project entitled <b>“College AI Chatbot”</b> "
        "and submitted this project report in partial fulfillment of the requirements for "
        "the award of the degree of <b>BBA CA</b> for the academic Year <b>2025-26</b>."
    )
    p = Paragraph(text, style)
    w, h = p.wrap(440, 150)
    p.drawOn(can, 77.5, 635 - h)
    can.save()
    packet.seek(0)
    return pypdf.PdfReader(packet).pages[0]

def generate_page3_overlay():
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(PAGE_W, PAGE_H))
    can.setFillColor(white)
    can.setStrokeColor(white)
    can.rect(360, 340, 170, 48, fill=1, stroke=0)
    
    can.setFillColor(black)
    can.setFont('Times-Bold', 10.125)
    can.drawRightString(515, 372, "Akash rana (ISTU25010120004)")
    can.drawRightString(515, 354, "Shreyash katke (ISTU25010120003)")
    can.save()
    packet.seek(0)
    return pypdf.PdfReader(packet).pages[0]

def generate_page14_overlay():
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(PAGE_W, PAGE_H))
    can.setFillColor(white)
    can.setStrokeColor(white)
    can.rect(368, 638, 95, 14, fill=1, stroke=0)
    
    can.setFillColor(black)
    can.setFont('Times-Roman', 11)
    can.drawString(369.8, 640.5, "ISTU25010120004")
    can.save()
    packet.seek(0)
    return pypdf.PdfReader(packet).pages[0]

def generate_page29_overlay():
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(PAGE_W, PAGE_H))
    
    # 1. Header bar roll number
    can.setFillColor(HexColor("#f8fafc"))
    can.setStrokeColor(HexColor("#f8fafc"))
    can.rect(370, 750, 95, 15, fill=1, stroke=0)
    can.setFillColor(HexColor("#475569"))
    can.setFont('Courier', 7.5)
    can.drawString(372, 754, "ISTU25010120004")
    
    # 2. Student chat bubble query
    can.setFillColor(HexColor("#1e40af"))
    can.setStrokeColor(HexColor("#1e40af"))
    can.rect(485, 348, 85, 15, fill=1, stroke=0)
    can.setFillColor(white)
    can.setFont('Times-Roman', 9)
    can.drawString(487, 352, "ISTU25010120004?")
    
    # 3. Attendance Record Name
    can.setFillColor(white)
    can.setStrokeColor(white)
    can.rect(125, 311, 80, 14, fill=1, stroke=0)
    can.setFillColor(black)
    can.setFont('Times-Roman', 9)
    can.drawString(127, 315, "Akash rana •")
    
    can.save()
    packet.seek(0)
    return pypdf.PdfReader(packet).pages[0]

def generate_page30_overlay():
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(PAGE_W, PAGE_H))
    
    can.setFillColor(white)
    can.setStrokeColor(white)
    can.rect(72, 620, 75, 12, fill=1, stroke=0)
    can.setFillColor(black)
    can.setFont('Times-Roman', 8)
    can.drawString(73.5, 623, "ISTU25010120004")
    
    can.setFillColor(white)
    can.setStrokeColor(white)
    can.rect(72, 603, 75, 12, fill=1, stroke=0)
    can.setFillColor(black)
    can.setFont('Times-Roman', 8)
    can.drawString(73.5, 606.5, "ISTU25010120003")
    
    can.save()
    packet.seek(0)
    return pypdf.PdfReader(packet).pages[0]

def generate_page31_overlay():
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(PAGE_W, PAGE_H))
    
    can.setFillColor(white)
    can.setStrokeColor(white)
    can.rect(264, 408, 90, 15, fill=1, stroke=0)
    can.setFillColor(black)
    can.setFont('Times-Roman', 9)
    can.drawString(266, 412, "ISTU25010120004")
    
    can.setFillColor(white)
    can.setStrokeColor(white)
    can.rect(350, 404, 130, 22, fill=1, stroke=0)
    can.setFillColor(black)
    can.setFont('Times-Roman', 8.5)
    can.drawString(353, 415, "Profile Loaded (Akash")
    can.drawString(353, 405, "rana)")
    
    can.save()
    packet.seek(0)
    return pypdf.PdfReader(packet).pages[0]

def generate_centered_heading_overlay(page_num, heading_text):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(PAGE_W, PAGE_H))
    
    # White out old left-aligned heading
    can.setFillColor(white)
    can.setStrokeColor(white)
    can.rect(42, 770, 510, 42, fill=1, stroke=0)
    
    # Determine y-position based on page type
    is_diagram_page = page_num in [16, 20, 21, 22, 23, 24, 25, 26, 27]
    y_pos = 787.9 if is_diagram_page else 781.9
    
    # Draw bold centered heading
    can.setFillColor(black)
    can.setFont('Times-Bold', 15.5)
    can.drawCentredString(PAGE_W / 2.0, y_pos, heading_text)
    
    can.save()
    packet.seek(0)
    return pypdf.PdfReader(packet).pages[0]

def prepare_object_diagram_images():
    # 1. stu_akash (replacing X157)
    im1 = Image.open('scratch/pdf2_images/page_23_0_X157.png').convert('RGBA')
    draw1 = ImageDraw.Draw(im1)
    draw1.rectangle([8, 8, 704, 88], fill=(217, 232, 251, 255))
    draw1.rectangle([8, 94, 704, 524], fill=(255, 255, 255, 255))
    
    font_bold = ImageFont.truetype('/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf', 32)
    font_slot = ImageFont.truetype('/System/Library/Fonts/Supplemental/Times New Roman.ttf', 27)
    
    h_text = 'stu_akash : Student'
    bbox = draw1.textbbox((0, 0), h_text, font=font_bold)
    w_t = bbox[2] - bbox[0]
    draw1.text(((712 - w_t)/2, 28), h_text, fill=(15, 23, 42, 255), font=font_bold)
    draw1.line([(712 - w_t)/2, 66, (712 + w_t)/2, 66], fill=(15, 23, 42, 255), width=2)
    
    slots1 = [
        'roll_no = \"ISTU25010120004\"',
        'name = \"Akash Rana\"',
        'course = \"BBA-CA\"',
        'semester = \"Semester III\"',
        'cgpa = 9.40',
        'attendance = 88.50 %',
        'fees_due = 0.00',
        'mentor = \"Prof. Sheela Satav\"',
        'exam_date = \"2026-10-15\"'
    ]
    y_s = 110
    for s in slots1:
        draw1.text((28, y_s), s, fill=(30, 41, 59, 255), font=font_slot)
        y_s += 44
    im1.save('scratch/updated_stu_akash.png')

    # 2. msg_42 (replacing X163)
    im2 = Image.open('scratch/pdf2_images/page_23_2_X163.png').convert('RGBA')
    draw2 = ImageDraw.Draw(im2)
    draw2.rectangle([8, 8, 704, 88], fill=(217, 232, 251, 255))
    draw2.rectangle([8, 92, 704, 395], fill=(255, 255, 255, 255))
    
    h_text2 = 'msg_42 : ChatHistory'
    bbox2 = draw2.textbbox((0, 0), h_text2, font=font_bold)
    w_t2 = bbox2[2] - bbox2[0]
    draw2.text(((712 - w_t2)/2, 28), h_text2, fill=(15, 23, 42, 255), font=font_bold)
    draw2.line([(712 - w_t2)/2, 66, (712 + w_t2)/2, 66], fill=(15, 23, 42, 255), width=2)
    
    slots2 = [
        'id = 42',
        'roll_no = \"ISTU25010120004\"',
        'user_query = \"When are internal exams?\"',
        'bot_response = \"Exams start Oct 15, 2026\"',
        'timestamp = \"2026-09-29 14:22:10\"',
        'feedback = \"thumbs up (+1)\"'
    ]
    y_s2 = 110
    for s in slots2:
        draw2.text((28, y_s2), s, fill=(30, 41, 59, 255), font=font_slot)
        y_s2 += 44
    im2.save('scratch/updated_msg_42.png')

def build_full_report():
    print("Preparing high-resolution object diagram assets...")
    prepare_object_diagram_images()
    
    im_akash = Image.open('scratch/updated_stu_akash.png')
    im_msg = Image.open('scratch/updated_msg_42.png')

    reader = pypdf.PdfReader(SRC_PDF)
    writer = pypdf.PdfWriter()

    print(f"Source PDF has {len(reader.pages)} pages.")

    content_overlays = {
        1: generate_page1_overlay(),
        2: generate_page2_overlay(),
        3: generate_page3_overlay(),
        14: generate_page14_overlay(),
        29: generate_page29_overlay(),
        30: generate_page30_overlay(),
        31: generate_page31_overlay()
    }

    for idx, page in enumerate(reader.pages):
        page_num = idx + 1
        
        # 1. Apply specific content replacements
        if page_num in content_overlays:
            page.merge_page(content_overlays[page_num])
            print(f"Applied student data overlay on Page {page_num}.")
            
        # 2. Apply centered heading overlay for pages 7 to 35
        if page_num in HEADINGS:
            heading_overlay = generate_centered_heading_overlay(page_num, HEADINGS[page_num])
            page.merge_page(heading_overlay)
            print(f"Centered heading on Page {page_num}: {HEADINGS[page_num]}")
            
        # 3. Add to writer
        writer.add_page(page)

    # 4. Replace Object Diagram images on Page 23
    writer.pages[22].images['/X157'].replace(im_akash)
    writer.pages[22].images['/X163'].replace(im_msg)
    print("Replaced Object Diagram images with Akash Rana's credentials on Page 23.")

    destinations = [
        "/Users/kanishksingh/Downloads/momo ai chat bot /CampusAI_Project_Report.pdf",
        "/Users/kanishksingh/Downloads/momo ai chat bot /momo ki topri/CampusAI_Project_Report.pdf",
        "/Users/kanishksingh/Downloads/momo ai chat bot /momo ki topri/CampusAI_Official_Report_Akash_Shreyash.pdf"
    ]

    for dst in destinations:
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, 'wb') as f:
            writer.write(f)
        print(f"[✓] Saved updated 35-page report to: {dst} ({os.path.getsize(dst)} bytes)")

if __name__ == '__main__':
    build_full_report()
