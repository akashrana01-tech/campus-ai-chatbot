"""
Updates the official 35-page College AI Chatbot Project Report PDF:
Replaces student names and roll numbers with:
- Akash rana (ISTU25010120004)
- Shreyash katke (ISTU25010120003)

Ensures exact layout, fonts, double borders, and data preservation across all 35 pages.
"""

import io
import os
import pypdf
from reportlab.pdfgen import canvas
from reportlab.lib.colors import white, black, HexColor
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT, TA_CENTER, TA_LEFT

SRC_PDF = "/Users/kanishksingh/.gemini/antigravity/brain/60288257-9f14-453a-bf1a-fc74825b030f/.user_uploaded/media_1793003039133_537ddeaa.pdf"
PAGE_W, PAGE_H = 594.96, 841.92

def generate_page1_overlay():
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(PAGE_W, PAGE_H))
    can.setFillColor(white)
    can.setStrokeColor(white)
    # Cover old student names on cover page
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
    # Cover old certificate body text
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
    # Cover old student signatures on acknowledgement page
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
    # x=368, y=637, width=95, height=14
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
    # http://localhost:5000/chat • Student Active Session (Roll No: ISTU25010120001)
    can.setFillColor(HexColor("#f8fafc"))
    can.setStrokeColor(HexColor("#f8fafc"))
    # The header box in UI
    can.rect(370, 750, 95, 15, fill=1, stroke=0)
    can.setFillColor(HexColor("#475569"))
    can.setFont('Courier', 7.5)
    can.drawString(372, 754, "ISTU25010120004")
    
    # 2. Student chat bubble query
    # What is my attendance status for Roll No ISTU25010120001?
    can.setFillColor(HexColor("#1e40af")) # Blue chat bubble
    can.setStrokeColor(HexColor("#1e40af"))
    can.rect(485, 348, 85, 15, fill=1, stroke=0)
    can.setFillColor(white)
    can.setFont('Times-Roman', 9)
    can.drawString(487, 352, "ISTU25010120004?")
    
    # 3. Attendance Record Name
    # Name: Kanishk Singh • Course: BBA-CA
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
    
    # In table: row 1 roll number
    can.setFillColor(white)
    can.setStrokeColor(white)
    can.rect(72, 620, 75, 12, fill=1, stroke=0)
    can.setFillColor(black)
    can.setFont('Times-Roman', 8)
    can.drawString(73.5, 623, "ISTU25010120004")
    
    # Row 2 roll number
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
    
    # TC_01 table row
    # Test Input: Roll No: ISTU25010120001
    can.setFillColor(white)
    can.setStrokeColor(white)
    can.rect(264, 408, 90, 15, fill=1, stroke=0)
    can.setFillColor(black)
    can.setFont('Times-Roman', 9)
    can.drawString(266, 412, "ISTU25010120004")
    
    # Expected Output: Profile Loaded (KanishkSingh)
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

def update_entire_pdf():
    reader = pypdf.PdfReader(SRC_PDF)
    writer = pypdf.PdfWriter()
    
    print(f"Loaded source PDF with {len(reader.pages)} pages.")
    
    overlays = {
        1: generate_page1_overlay(),
        2: generate_page2_overlay(),
        3: generate_page3_overlay(),
        14: generate_page14_overlay(),
        29: generate_page29_overlay(),
        30: generate_page30_overlay(),
        31: generate_page31_overlay(),
    }
    
    for idx, page in enumerate(reader.pages):
        page_num = idx + 1
        if page_num in overlays:
            page.merge_page(overlays[page_num])
            print(f"Applied name update overlay on Page {page_num}.")
        writer.add_page(page)
    
    destinations = [
        "/Users/kanishksingh/Downloads/momo ai chat bot /CampusAI_Project_Report.pdf",
        "/Users/kanishksingh/Downloads/momo ai chat bot /momo ki topri/CampusAI_Project_Report.pdf",
        "/Users/kanishksingh/Desktop/momo ki topri/CampusAI_Project_Report.pdf",
        "/Users/kanishksingh/Downloads/momo ai chat bot /momo ki topri/College_AI_Chatbot_Official_Report_Akash_Shreyash.pdf",
        "/Users/kanishksingh/Desktop/momo ki topri/College_AI_Chatbot_Official_Report_Akash_Shreyash.pdf"
    ]
    
    for dst in destinations:
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, 'wb') as f:
            writer.write(f)
        print(f"[✓] Saved updated 35-page report to: {dst} ({os.path.getsize(dst)} bytes)")

if __name__ == '__main__':
    update_entire_pdf()
