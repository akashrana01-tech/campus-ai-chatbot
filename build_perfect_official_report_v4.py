"""
CampusAI Official 35-Page Project Report Generator (v4)
Strictly adheres to:
1. ZERO modification to project table data:
   - Decision Table (Page 15): Jaccard NLP & Google Gemini AI fallback logic
   - Database Tables (Pages 17, 18, 19): admins, faqs, chat_messages schemas & sample data
   - Requirements Tables (Pages 12, 13): Hardware & Software specifications
   - Testing Table (Page 31): TC-01 to TC-23 automated test suite
2. Teacher-mandated STRUCTURE corrections:
   - Centered Headings: All headings from Page 7 to Page 35 are centered (TA_CENTER)
   - 8 UML/DFD Diagrams (Pages 20-27): Exact vector structures matching teacher's approved departmental reference
   - Object Diagram (Page 23): Akash Rana's credentials (Roll No: ISTU25010120004, Prof. Sheela Satav)
   - Academic Conclusion (Page 34) & Bibliography (Page 35)
3. Student details:
   - Akash rana (ISTU25010120004)
   - Shreyash katke (ISTU25010120003)
   Course: BBA CA (Semester III, 2025-26)
   Guide: Prof. Sheela Satav
   Institution: G H Raisoni International Skill Tech University, Pune-412207
"""

import io
import os
import pypdf
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.colors import white, black

BASE_DIR = "/Users/kanishksingh/Downloads/momo ai chat bot "
SRC_PDF = "/Users/kanishksingh/.gemini/antigravity/brain/60288257-9f14-453a-bf1a-fc74825b030f/.user_uploaded/media_1793003039133_537ddeaa.pdf"
PAGE_W, PAGE_H = 594.96, 841.92

DIAGRAM_HEADINGS = {
    20: "ER DIAGRAM:",
    21: "USE CASE DIAGRAM:",
    22: "CLASS DIAGRAM",
    23: "OBJECT DIAGRAM :",
    24: "SEQUENCE DIAGRAM :",
    25: "ACTIVITY DIAGRAM :",
    26: "COMPONENT DIAGRAM :",
    27: "DATA FLOW DIAGRAM :"
}

def make_centered_heading_overlay(h_text):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(PAGE_W, PAGE_H))
    # Cover old left-aligned heading cleanly
    can.setFillColor(white)
    can.setStrokeColor(white)
    can.rect(42, 770, 510, 42, fill=1, stroke=0)
    # Draw centered heading
    can.setFillColor(black)
    can.setFont("Times-Bold", 14.25)
    can.drawCentredString(PAGE_W / 2.0, 795.6, h_text)
    can.save()
    packet.seek(0)
    return pypdf.PdfReader(packet).pages[0]

def prepare_object_diagram_assets():
    os.makedirs(os.path.join(BASE_DIR, "scratch"), exist_ok=True)
    
    # 1. stu_akash (replacing X157)
    im1 = Image.open(os.path.join(BASE_DIR, "scratch/pdf2_images/page_23_0_X157.png")).convert("RGBA")
    draw1 = ImageDraw.Draw(im1)
    draw1.rectangle([8, 8, 704, 88], fill=(217, 232, 251, 255))
    draw1.rectangle([8, 94, 704, 524], fill=(255, 255, 255, 255))
    
    font_bold = ImageFont.truetype("/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf", 32)
    font_slot = ImageFont.truetype("/System/Library/Fonts/Supplemental/Times New Roman.ttf", 27)
    
    h_text = "stu_akash : Student"
    bbox = draw1.textbbox((0, 0), h_text, font=font_bold)
    w_t = bbox[2] - bbox[0]
    draw1.text(((712 - w_t)/2, 28), h_text, fill=(15, 23, 42, 255), font=font_bold)
    draw1.line([(712 - w_t)/2, 66, (712 + w_t)/2, 66], fill=(15, 23, 42, 255), width=2)
    
    slots1 = [
        'roll_no = "ISTU25010120004"',
        'name = "Akash Rana"',
        'course = "BBA-CA"',
        'semester = "Semester III"',
        'cgpa = 9.40',
        'attendance = 88.50 %',
        'fees_due = 0.00',
        'mentor = "Prof. Sheela Satav"',
        'exam_date = "2026-10-15"'
    ]
    y_s = 110
    for s in slots1:
        draw1.text((28, y_s), s, fill=(30, 41, 59, 255), font=font_slot)
        y_s += 44
    im1.save(os.path.join(BASE_DIR, "scratch/updated_stu_akash.png"))

    # 2. msg_42 (replacing X163)
    im2 = Image.open(os.path.join(BASE_DIR, "scratch/pdf2_images/page_23_2_X163.png")).convert("RGBA")
    draw2 = ImageDraw.Draw(im2)
    draw2.rectangle([8, 8, 704, 88], fill=(217, 232, 251, 255))
    draw2.rectangle([8, 92, 704, 395], fill=(255, 255, 255, 255))
    
    h_text2 = "msg_42 : ChatHistory"
    bbox2 = draw2.textbbox((0, 0), h_text2, font=font_bold)
    w_t2 = bbox2[2] - bbox2[0]
    draw2.text(((712 - w_t2)/2, 28), h_text2, fill=(15, 23, 42, 255), font=font_bold)
    draw2.line([(712 - w_t2)/2, 66, (712 + w_t2)/2, 66], fill=(15, 23, 42, 255), width=2)
    
    slots2 = [
        'id = 42',
        'roll_no = "ISTU25010120004"',
        'user_query = "When are internal exams?"',
        'bot_response = "Exams start Oct 15, 2026"',
        'timestamp = "2026-09-29 14:22:10"',
        'feedback = "thumbs up (+1)"'
    ]
    y_s2 = 110
    for s in slots2:
        draw2.text((28, y_s2), s, fill=(30, 41, 59, 255), font=font_slot)
        y_s2 += 44
    im2.save(os.path.join(BASE_DIR, "scratch/updated_msg_42.png"))

def build_v4_report():
    print("Step 1: Compiling centered pure CampusAI reportlab pages...")
    import sys
    sys.path.insert(0, os.path.join(BASE_DIR, "scratch"))
    import build_perfect_35page_report_centered as b_centered
    
    temp_rl_path = os.path.join(BASE_DIR, "scratch/temp_campusai_reportlab_centered.pdf")
    b_centered.generate_report(temp_rl_path)
    
    print("Step 2: Preparing Object Diagram image replacements...")
    prepare_object_diagram_assets()
    im_akash = Image.open(os.path.join(BASE_DIR, "scratch/updated_stu_akash.png"))
    im_msg = Image.open(os.path.join(BASE_DIR, "scratch/updated_msg_42.png"))

    rl_reader = pypdf.PdfReader(temp_rl_path)
    ref_reader = pypdf.PdfReader(SRC_PDF)
    writer = pypdf.PdfWriter()

    print("Step 3: Assembling document...")
    # A. Pages 1 to 19 from ReportLab (pure CampusAI tables, centered headings, Akash/Shreyash)
    for i in range(19):
        writer.add_page(rl_reader.pages[i])
    print("  -> Added Pages 1-19 (Front matter, Introduction, pure CampusAI Decision & DB Tables)")

    # B. Pages 20 to 27 from Teacher-Approved Vector Reference (with centered headings)
    for p_num in range(20, 28):
        p = ref_reader.pages[p_num - 1]
        overlay = make_centered_heading_overlay(DIAGRAM_HEADINGS[p_num])
        p.merge_page(overlay)
        writer.add_page(p)
    print("  -> Added Pages 20-27 (Teacher's approved 8 UML/DFD diagram structures)")

    # Replace Object Diagram images on Page 23 (writer.pages[22])
    writer.pages[22].images['/X157'].replace(im_akash)
    writer.pages[22].images['/X163'].replace(im_msg)
    print("  -> Updated Page 23 Object Diagram with Akash Rana's credentials")

    # C. Pages 28 to 35 from ReportLab (pure CampusAI UI, 23 Test Cases Table, Conclusion, Bibliography)
    for i in range(27, 35):
        writer.add_page(rl_reader.pages[i])
    print("  -> Added Pages 28-35 (UI screens, 23 Automated Test Cases, Conclusion, Bibliography)")

    destinations = [
        os.path.join(BASE_DIR, "CampusAI_Project_Report.pdf"),
        os.path.join(BASE_DIR, "momo ki topri/CampusAI_Project_Report.pdf"),
        os.path.join(BASE_DIR, "momo ki topri/CampusAI_Official_Report_Akash_Shreyash.pdf")
    ]

    for dst in destinations:
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, "wb") as f:
            writer.write(f)
        print(f"[✓] Successfully wrote: {dst} ({os.path.getsize(dst)} bytes, {len(writer.pages)} pages)")

if __name__ == '__main__':
    build_v4_report()
