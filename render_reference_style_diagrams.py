"""
CampusAI (Group 2) - Reference-Style Architectural Diagrams Generator
Faithfully implements the EXACT diagram structures, visual layouts, and styling
demonstrated in the University-approved reference project report:
1. ER Diagram (Page 22 in ref): Tables with PK/FK headers, relationship diamonds (Creates, Manages, Contains, Matches, Receives), dashed legend box, and Description.
2. Use Case Diagram (Page 24 in ref): System boundary box, User & Admin stick figures on left, SQLite DB & Gemini AI on right, stacked oval use cases, and Description.
3. Class Diagram (Page 25 in ref): 3-compartment UML boxes with pastel headers (Admin, ChatbotEngine, GeminiService, FAQ, ChatSession, ChatMessage), multiplicity labels, and Description.
4. Object Diagram (Page 26 in ref): Concrete instance boxes with underlined titles (admin1, session1, msg1, faq1, reply1), links with action labels, and Description.
5. Sequence Diagram (Page 27 in ref): 6 Lifelines with dashed lines, numbered call/return arrows, and Description.
6. Activity Diagram (Page 28 in ref): 3 formal swimlanes (Student, Chatbot System, Administrator) with Start nodes, action rounded rectangles, decision diamonds, and End bullseyes.
7. Component Diagram (Page 29 in ref): Left Frontend box, Middle Backend Server box with matching modules, Right SQLite DB cylinder and Gemini AI box with interface lines.
8. Data Flow Diagram (Page 30 in ref): Level 0 Context Diagram at top, Level 1 DFD with vertical numbered process ovals (1 to 6) and open-ended data stores (D1 to D5).
9. Decision Tree (Page 19 in ref): Decision flowchart with Start, validation diamond, Jaccard calculation, routing branches, persistence, and Description.
"""

import os
os.environ["MPLCONFIGDIR"] = "/tmp/mpl"
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Polygon, Rectangle, Ellipse

OUT_DIR = "/Users/kanishksingh/Downloads/momo ai chat bot /scratch/campusai_diagrams"
os.makedirs(OUT_DIR, exist_ok=True)

# Reference PDF Pastel Palette
CLR_BG_PURPLE = "#f3e8ff"
CLR_BG_BLUE = "#dbeafe"
CLR_BG_GREEN = "#dcfce7"
CLR_BG_YELLOW = "#fef9c3"
CLR_BG_PINK = "#fce7f3"
CLR_BG_ORANGE = "#ffedd5"
CLR_BG_GRAY = "#f1f5f9"

CLR_BORDER = "#1e293b"
CLR_TEXT = "#0f172a"
CLR_TEXT_MUTED = "#475569"
CLR_WHITE = "#ffffff"


# ==============================================================================
# 1. ER DIAGRAM (Exact structure of Reference PDF Page 22)
# ==============================================================================
def create_reference_er_diagram():
    fig, ax = plt.subplots(figsize=(8.5, 8.5), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    def draw_entity_box(x, y, w, title, fields, hdr_bg=CLR_BG_BLUE):
        line_h = 0.024
        h_title = 0.038
        total_h = h_title + len(fields) * line_h + 0.010
        top_y = y

        # Outer box
        rect = patches.Rectangle((x, top_y - total_h), w, total_h, facecolor=CLR_WHITE, edgecolor=CLR_BORDER, lw=1.2, zorder=3)
        ax.add_patch(rect)
        # Header box
        hdr = patches.Rectangle((x, top_y - h_title), w, h_title, facecolor=hdr_bg, edgecolor=CLR_BORDER, lw=1.0, zorder=4)
        ax.add_patch(hdr)
        ax.text(x + w/2, top_y - h_title/2, title, ha="center", va="center", fontsize=8.2, weight="bold", color=CLR_TEXT, zorder=5)

        # Fields
        curr_y = top_y - h_title - 0.012
        for f in fields:
            ax.text(x + 0.012, curr_y, f, fontsize=7.0, color=CLR_TEXT, zorder=5)
            curr_y -= line_h

        return top_y - total_h

    def draw_diamond(cx, cy, w, h, text, bg=CLR_BG_YELLOW):
        pts = [[cx, cy + h/2], [cx + w/2, cy], [cx, cy - h/2], [cx - w/2, cy]]
        poly = Polygon(pts, closed=True, facecolor=bg, edgecolor=CLR_BORDER, lw=1.0, zorder=4)
        ax.add_patch(poly)
        ax.text(cx, cy, text, ha="center", va="center", fontsize=6.8, weight="bold", color=CLR_TEXT, zorder=5)

    # 1. USER / STUDENT Box (Top Left)
    draw_entity_box(0.08, 0.95, 0.22, "ADMIN_USER", [
        "Admin_ID (PK)",
        "Username",
        "Email",
        "Password_Hash",
        "Role",
        "Created_At"
    ], hdr_bg=CLR_BG_BLUE)

    # 2. CHAT_SESSION Box (Top Center)
    draw_entity_box(0.39, 0.95, 0.22, "CHAT_SESSION", [
        "Session_ID (PK)",
        "Client_IP",
        "Created_At",
        "Last_Active",
        "Total_Queries"
    ], hdr_bg=CLR_BG_GREEN)

    # 3. FEEDBACK_LOG Box (Top Right)
    draw_entity_box(0.70, 0.95, 0.22, "FEEDBACK_LOG", [
        "Feedback_ID (PK)",
        "Message_ID (FK)",
        "Rating_Value",
        "Client_Note",
        "Logged_At"
    ], hdr_bg=CLR_BG_PURPLE)

    # 4. CHAT_MESSAGE Box (Bottom Left)
    draw_entity_box(0.08, 0.52, 0.22, "CHAT_MESSAGE", [
        "Message_ID (PK)",
        "Session_ID (FK)",
        "Role (user/bot)",
        "Content",
        "Source_Tier",
        "Timestamp"
    ], hdr_bg=CLR_BG_PINK)

    # 5. FAQ_KNOWLEDGE_BASE Box (Bottom Center)
    draw_entity_box(0.39, 0.58, 0.22, "FAQ_KNOWLEDGE_BASE", [
        "FAQ_ID (PK)",
        "Category_ID (FK)",
        "Question",
        "Answer",
        "Keywords",
        "Updated_At"
    ], hdr_bg=CLR_BG_YELLOW)

    # 6. ACADEMIC_CATEGORY Box (Bottom Right)
    draw_entity_box(0.70, 0.52, 0.22, "ACADEMIC_CATEGORY", [
        "Category_ID (PK)",
        "Category_Name",
        "Display_Order",
        "Is_Active"
    ], hdr_bg=CLR_BG_ORANGE)

    # Relationships & Connecting Lines (with exact diamonds like Ref PDF)
    # Line 1: ADMIN_USER to FAQ (Manages 1 : M)
    ax.plot([0.19, 0.19, 0.39], [0.77, 0.65, 0.65], color=CLR_BORDER, lw=1.1, zorder=2)
    draw_diamond(0.29, 0.65, 0.08, 0.045, "Manages")
    ax.text(0.20, 0.74, "1", fontsize=7.5, weight="bold")
    ax.text(0.37, 0.66, "M", fontsize=7.5, weight="bold")

    # Line 2: CHAT_SESSION to CHAT_MESSAGE (Generates 1 : M)
    ax.plot([0.50, 0.50, 0.19], [0.80, 0.62, 0.62], color=CLR_BORDER, lw=1.1, zorder=2)
    ax.plot([0.19, 0.19], [0.62, 0.52], color=CLR_BORDER, lw=1.1, zorder=2)
    draw_diamond(0.34, 0.62, 0.09, 0.045, "Generates")
    ax.text(0.48, 0.78, "1", fontsize=7.5, weight="bold")
    ax.text(0.20, 0.54, "M", fontsize=7.5, weight="bold")

    # Line 3: CHAT_MESSAGE to FAQ (Matches M : 1)
    ax.plot([0.30, 0.39], [0.38, 0.38], color=CLR_BORDER, lw=1.1, zorder=2)
    draw_diamond(0.345, 0.38, 0.08, 0.045, "Matches")
    ax.text(0.31, 0.40, "M", fontsize=7.5, weight="bold")
    ax.text(0.37, 0.40, "1", fontsize=7.5, weight="bold")

    # Line 4: CHAT_MESSAGE to FEEDBACK_LOG (Receives 1 : 1)
    ax.plot([0.30, 0.30, 0.81, 0.81], [0.45, 0.72, 0.72, 0.80], color=CLR_BORDER, lw=1.1, zorder=2)
    draw_diamond(0.55, 0.72, 0.08, 0.045, "Receives")
    ax.text(0.31, 0.48, "1", fontsize=7.5, weight="bold")
    ax.text(0.79, 0.78, "1", fontsize=7.5, weight="bold")

    # Line 5: FAQ to CATEGORY (Belongs to M : 1)
    ax.plot([0.61, 0.70], [0.38, 0.38], color=CLR_BORDER, lw=1.1, zorder=2)
    draw_diamond(0.655, 0.38, 0.08, 0.045, "Belongs to")
    ax.text(0.62, 0.40, "M", fontsize=7.5, weight="bold")
    ax.text(0.68, 0.40, "1", fontsize=7.5, weight="bold")

    # Dashed LEGEND box on the bottom right (Exact as Page 22)
    leg = patches.Rectangle((0.68, 0.08), 0.24, 0.18, facecolor=CLR_WHITE, edgecolor=CLR_BORDER, linestyle="--", lw=1.0, zorder=3)
    ax.add_patch(leg)
    ax.text(0.80, 0.23, "LEGEND", ha="center", fontsize=7.5, weight="bold", color=CLR_TEXT)
    ax.text(0.71, 0.19, "PK  -  Primary Key", fontsize=6.8, color=CLR_TEXT)
    ax.text(0.71, 0.16, "FK  -  Foreign Key", fontsize=6.8, color=CLR_TEXT)
    ax.text(0.71, 0.13, "1    -  One", fontsize=6.8, color=CLR_TEXT)
    ax.text(0.71, 0.10, "M   -  Many", fontsize=6.8, color=CLR_TEXT)

    # Caption (Italic)
    ax.text(0.50, 0.02, "Fig: Entity Relationship Diagram", ha="center", fontsize=8.5, style="italic", color=CLR_TEXT)

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_er_diagram.png"), bbox_inches="tight")
    plt.close()
    print("[1/9] Generated Reference-Style ER Diagram: campusai_er_diagram.png")

create_reference_er_diagram()


# ==============================================================================
# 2. USE CASE DIAGRAM (Exact structure of Reference PDF Page 24)
# ==============================================================================
def create_reference_use_case_diagram():
    fig, ax = plt.subplots(figsize=(8.5, 9.2), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Boundary Box
    bound = patches.Rectangle((0.26, 0.08), 0.48, 0.88, facecolor=CLR_WHITE, edgecolor=CLR_BORDER, lw=1.2, zorder=1)
    ax.add_patch(bound)
    # Title box at top of boundary
    t_box = patches.Rectangle((0.26, 0.92), 0.48, 0.04, facecolor=CLR_BG_GRAY, edgecolor=CLR_BORDER, lw=1.0, zorder=2)
    ax.add_patch(t_box)
    ax.text(0.50, 0.94, "CampusAI College Assistant Chatbot", ha="center", va="center", fontsize=8.0, weight="bold", color=CLR_TEXT, zorder=3)

    def draw_actor(x, y, label):
        h = Circle((x, y + 0.038), 0.016, facecolor=CLR_WHITE, edgecolor=CLR_BORDER, lw=1.3, zorder=5)
        ax.add_patch(h)
        ax.plot([x, x], [y + 0.022, y - 0.018], color=CLR_BORDER, lw=1.3, zorder=5)
        ax.plot([x - 0.020, x + 0.020], [y + 0.008, y + 0.008], color=CLR_BORDER, lw=1.3, zorder=5)
        ax.plot([x, x - 0.016], [y - 0.018, y - 0.050], color=CLR_BORDER, lw=1.3, zorder=5)
        ax.plot([x, x + 0.016], [y - 0.018, y - 0.050], color=CLR_BORDER, lw=1.3, zorder=5)
        ax.text(x, y - 0.068, label, ha="center", va="top", fontsize=8.0, weight="bold", color=CLR_TEXT, zorder=6)

    # Actor 1: Student (Left)
    draw_actor(0.12, 0.72, "Student")

    # Actor 2: Admin (Left)
    draw_actor(0.12, 0.28, "Admin")

    # Database Cylinder (Right)
    # Top ellipse
    top_e = Ellipse((0.86, 0.60), 0.16, 0.05, facecolor=CLR_BG_BLUE, edgecolor=CLR_BORDER, lw=1.2, zorder=4)
    # Body
    body_r = patches.Rectangle((0.78, 0.46), 0.16, 0.14, facecolor=CLR_BG_BLUE, edgecolor="none", zorder=2)
    ax.add_patch(body_r)
    ax.plot([0.78, 0.78], [0.46, 0.60], color=CLR_BORDER, lw=1.2, zorder=3)
    ax.plot([0.94, 0.94], [0.46, 0.60], color=CLR_BORDER, lw=1.2, zorder=3)
    # Bottom ellipse
    bot_e = Ellipse((0.86, 0.46), 0.16, 0.05, facecolor=CLR_BG_BLUE, edgecolor=CLR_BORDER, lw=1.2, zorder=3)
    ax.add_patch(bot_e)
    ax.add_patch(top_e)
    ax.text(0.86, 0.53, "SQLite 3 DB\n& Gemini AI", ha="center", va="center", fontsize=7.2, weight="bold", color=CLR_TEXT, zorder=5)

    # Use Cases (Stacked ovals inside boundary)
    user_ucs = [
        "Ask Academic Query",
        "Search Knowledge Base",
        "Filter by 8 Domains",
        "Use Voice Input & TTS",
        "Click Suggestion Chips",
        "Submit Answer Feedback",
        "Clear Chat Session"
    ]

    admin_ucs = [
        "Admin Login (PBKDF2)",
        "Manage FAQs (CRUD)",
        "View System Telemetry",
        "Export Chat Logs (CSV)"
    ]

    all_ucs = user_ucs + admin_ucs
    start_y = 0.88
    step_y = 0.075

    for idx, uc_text in enumerate(all_ucs):
        cy = start_y - idx * step_y
        e = Ellipse((0.50, cy), 0.38, 0.048, facecolor=CLR_WHITE, edgecolor=CLR_BORDER, lw=1.1, zorder=3)
        ax.add_patch(e)
        ax.text(0.50, cy, uc_text, ha="center", va="center", fontsize=6.8, color=CLR_TEXT, zorder=4)

        # Connect to Database on right
        ax.plot([0.69, 0.78], [cy, 0.53], color=CLR_BORDER, lw=0.9, zorder=2)

        # Connect from User (first 7) or Admin (last 4)
        if idx < len(user_ucs):
            ax.plot([0.16, 0.31], [0.72, cy], color=CLR_BORDER, lw=0.9, zorder=2)
        else:
            ax.plot([0.16, 0.31], [0.28, cy], color=CLR_BORDER, lw=0.9, zorder=2)

    ax.text(0.50, 0.02, "Fig: Use Case Diagram", ha="center", fontsize=8.5, style="italic", color=CLR_TEXT)

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_use_case.png"), bbox_inches="tight")
    plt.close()
    print("[2/9] Generated Reference-Style Use Case Diagram: campusai_use_case.png")

create_reference_use_case_diagram()


# ==============================================================================
# 3. CLASS DIAGRAM (Exact structure of Reference PDF Page 25)
# ==============================================================================
def create_reference_class_diagram():
    fig, ax = plt.subplots(figsize=(8.5, 9.2), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    def draw_class(x, y, w, title, attrs, methods, hdr_bg=CLR_BG_BLUE):
        line_h = 0.022
        h_title = 0.034
        h_attrs = len(attrs) * line_h + 0.008
        h_meths = len(methods) * line_h + 0.008
        total_h = h_title + h_attrs + h_meths
        top_y = y

        # Box
        rect = patches.Rectangle((x, top_y - total_h), w, total_h, facecolor=CLR_WHITE, edgecolor=CLR_BORDER, lw=1.2, zorder=3)
        ax.add_patch(rect)
        # Header
        hdr = patches.Rectangle((x, top_y - h_title), w, h_title, facecolor=hdr_bg, edgecolor=CLR_BORDER, lw=1.0, zorder=4)
        ax.add_patch(hdr)
        ax.text(x + w/2, top_y - h_title/2, title, ha="center", va="center", fontsize=8.0, weight="bold", color=CLR_TEXT, zorder=5)

        # Attrs
        curr_y = top_y - h_title - 0.010
        for a in attrs:
            ax.text(x + 0.010, curr_y, a, fontsize=6.8, color=CLR_TEXT, zorder=5)
            curr_y -= line_h

        # Divider line
        div_y = top_y - h_title - h_attrs
        ax.plot([x, x + w], [div_y, div_y], color=CLR_BORDER, lw=0.9, zorder=4)

        # Methods
        curr_y = div_y - 0.010
        for m in methods:
            ax.text(x + 0.010, curr_y, m, fontsize=6.8, color=CLR_TEXT, zorder=5)
            curr_y -= line_h

        return top_y - total_h

    # 1. Admin Class (Top Left)
    draw_class(0.12, 0.95, 0.32, "Admin", [
        "admin_id : int",
        "username : string",
        "email : string",
        "password_hash : string"
    ], [
        "login()",
        "manageFAQs()",
        "exportCSV()"
    ], hdr_bg=CLR_BG_PURPLE)

    # 2. GeminiService Class (Top Right)
    draw_class(0.56, 0.95, 0.32, "GeminiService", [
        "model_name : string",
        "api_key : string",
        "system_prompt : string"
    ], [
        "generateFallback()",
        "enforceZeroHallucination()",
        "checkHealth()"
    ], hdr_bg=CLR_BG_PURPLE)

    # 3. StudentUser Class (Middle Left)
    draw_class(0.12, 0.65, 0.32, "StudentUser", [
        "session_id : string",
        "client_ip : string",
        "selected_domain : string"
    ], [
        "submitQuery()",
        "filterCategory()",
        "clearChat()"
    ], hdr_bg=CLR_BG_BLUE)

    # 4. ChatbotEngine Class (Middle Right)
    draw_class(0.56, 0.65, 0.32, "ChatbotEngine", [
        "threshold : float = 0.45",
        "stop_words : list",
        "domain_synonyms : dict"
    ], [
        "tokenize()",
        "jaccardSimilarity()",
        "processMessage()"
    ], hdr_bg=CLR_BG_GREEN)

    # 5. ChatMessage Class (Bottom Left)
    draw_class(0.12, 0.35, 0.32, "ChatMessage", [
        "message_id : int",
        "session_id : string",
        "role : string",
        "content : string",
        "source : string"
    ], [
        "saveMessage()",
        "logFeedback()"
    ], hdr_bg=CLR_BG_PINK)

    # 6. FAQ KnowledgeBase Class (Bottom Right)
    draw_class(0.56, 0.35, 0.32, "FAQ", [
        "faq_id : int",
        "category : string",
        "question : string",
        "answer : string",
        "keywords : string"
    ], [
        "search()",
        "filterCategory()"
    ], hdr_bg=CLR_BG_YELLOW)

    # Relationship Connectors (Multiplicity & Actions like Ref PDF)
    # Admin to FAQ (manages 1 to M)
    ax.plot([0.28, 0.28, 0.72, 0.72], [0.73, 0.70, 0.70, 0.35], color=CLR_BORDER, lw=1.1, zorder=2)
    ax.text(0.30, 0.72, "1", fontsize=7.2, weight="bold")
    ax.text(0.74, 0.37, "M", fontsize=7.2, weight="bold")
    ax.text(0.48, 0.71, "manages", ha="center", fontsize=7.0, style="italic")

    # Student to ChatMessage (creates 1 to M)
    ax.plot([0.28, 0.28], [0.46, 0.35], color=CLR_BORDER, lw=1.1, zorder=2)
    ax.text(0.30, 0.44, "1", fontsize=7.2, weight="bold")
    ax.text(0.30, 0.37, "M", fontsize=7.2, weight="bold")
    ax.text(0.24, 0.40, "creates", ha="right", fontsize=7.0, style="italic")

    # ChatbotEngine to GeminiService (invokes 1 to 1)
    ax.plot([0.72, 0.72], [0.65, 0.74], color=CLR_BORDER, lw=1.1, zorder=2)
    ax.text(0.74, 0.67, "1", fontsize=7.2, weight="bold")
    ax.text(0.74, 0.72, "1", fontsize=7.2, weight="bold")
    ax.text(0.74, 0.70, "invokes", fontsize=7.0, style="italic")

    # ChatMessage to FAQ (refers to M to 1)
    ax.plot([0.44, 0.56], [0.22, 0.22], color=CLR_BORDER, lw=1.1, zorder=2)
    ax.text(0.45, 0.24, "M", fontsize=7.2, weight="bold")
    ax.text(0.54, 0.24, "1", fontsize=7.2, weight="bold")
    ax.text(0.50, 0.24, "refers to", ha="center", fontsize=7.0, style="italic")

    ax.text(0.50, 0.02, "Fig: Class Diagram", ha="center", fontsize=8.5, style="italic", color=CLR_TEXT)

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_class_diagram.png"), bbox_inches="tight")
    plt.close()
    print("[3/9] Generated Reference-Style Class Diagram: campusai_class_diagram.png")

create_reference_class_diagram()


# ==============================================================================
# 4. OBJECT DIAGRAM (Exact structure of Reference PDF Page 26)
# ==============================================================================
def create_reference_object_diagram():
    fig, ax = plt.subplots(figsize=(8.5, 9.2), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    def draw_object(x, y, w, inst_title, slots, hdr_bg=CLR_BG_BLUE):
        line_h = 0.024
        h_title = 0.034
        total_h = h_title + len(slots) * line_h + 0.010
        top_y = y

        rect = patches.Rectangle((x, top_y - total_h), w, total_h, facecolor=CLR_WHITE, edgecolor=CLR_BORDER, lw=1.2, zorder=3)
        ax.add_patch(rect)
        hdr = patches.Rectangle((x, top_y - h_title), w, h_title, facecolor=hdr_bg, edgecolor=CLR_BORDER, lw=1.0, zorder=4)
        ax.add_patch(hdr)
        ax.text(x + w/2, top_y - h_title/2, inst_title, ha="center", va="center", fontsize=7.8, weight="bold", color=CLR_TEXT, zorder=5)

        curr_y = top_y - h_title - 0.012
        for s in slots:
            ax.text(x + 0.010, curr_y, s, fontsize=7.0, color=CLR_TEXT, zorder=5)
            curr_y -= line_h

        return top_y - total_h

    # Object 1: user1 : Student (Top Center)
    draw_object(0.35, 0.95, 0.30, "user1 : Student", [
        "roll_no = \"ISTU25010120004\"",
        "name = \"Akash Rana\"",
        "course = \"BBA CA (Sem III)\"",
        "session_id = \"sess_astu_9b81\""
    ], hdr_bg=CLR_BG_BLUE)

    # Object 2: session1 : ChatSession (Middle Left)
    draw_object(0.08, 0.68, 0.32, "session1 : ChatSession", [
        "session_id = \"sess_astu_9b81\"",
        "client_ip = \"192.168.1.45\"",
        "started_at = \"10:14:02\"",
        "total_messages = 2"
    ], hdr_bg=CLR_BG_GREEN)

    # Object 3: fav1 : FeedbackLog (Middle Right)
    draw_object(0.60, 0.68, 0.32, "feedback1 : FeedbackLog", [
        "feedback_id = 501",
        "message_id = 102",
        "rating = \"thumbs_up (+1)\"",
        "comment = \"Helpful answer\""
    ], hdr_bg=CLR_BG_PINK)

    # Object 4: msg1 : ChatMessage (Bottom Left)
    draw_object(0.08, 0.38, 0.32, "msg1 : ChatMessage", [
        "message_id = 101",
        "role = \"student\"",
        "content = \"What are the fees?\"",
        "timestamp = \"10:14:05\""
    ], hdr_bg=CLR_BG_PURPLE)

    # Object 5: faq1 : FAQ (Bottom Right)
    draw_object(0.60, 0.38, 0.32, "faq1 : FAQ", [
        "faq_id = 4",
        "category = \"Fees\"",
        "question = \"Semester fee structure?\"",
        "answer = \"Rs 45,000 per sem\""
    ], hdr_bg=CLR_BG_YELLOW)

    # Connectors with labels (Exact like Ref PDF Page 26)
    # user1 to session1 (creates)
    ax.plot([0.42, 0.24], [0.77, 0.68], color=CLR_BORDER, lw=1.1, zorder=2)
    ax.text(0.30, 0.74, "creates", ha="center", fontsize=7.2, style="italic")

    # user1 to feedback1 (saves)
    ax.plot([0.58, 0.76], [0.77, 0.68], color=CLR_BORDER, lw=1.1, zorder=2)
    ax.text(0.70, 0.74, "submits", ha="center", fontsize=7.2, style="italic")

    # session1 to msg1 (contains)
    ax.plot([0.24, 0.24], [0.49, 0.38], color=CLR_BORDER, lw=1.1, zorder=2)
    ax.text(0.26, 0.44, "contains", fontsize=7.2, style="italic")

    # feedback1 to faq1 (refers to)
    ax.plot([0.76, 0.76], [0.49, 0.38], color=CLR_BORDER, lw=1.1, zorder=2)
    ax.text(0.78, 0.44, "refers to", fontsize=7.2, style="italic")

    # msg1 to faq1 (matches)
    ax.plot([0.40, 0.60], [0.26, 0.26], color=CLR_BORDER, lw=1.1, zorder=2)
    ax.text(0.50, 0.28, "matches", ha="center", fontsize=7.2, style="italic")

    ax.text(0.50, 0.02, "Fig: Object Diagram", ha="center", fontsize=8.5, style="italic", color=CLR_TEXT)

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_object_diagram.png"), bbox_inches="tight")
    plt.close()
    print("[4/9] Generated Reference-Style Object Diagram: campusai_object_diagram.png")

create_reference_object_diagram()


# ==============================================================================
# 5. SEQUENCE DIAGRAM (Exact structure of Reference PDF Page 27)
# ==============================================================================
def create_reference_sequence_diagram():
    fig, ax = plt.subplots(figsize=(8.5, 9.2), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # 6 Lifeline headers
    lifelines = [
        (0.10, "Student"),
        (0.26, "Web App\n(HTML5/JS)"),
        (0.44, "API Server\n(Flask app)"),
        (0.62, "NLP Engine\n(Jaccard)"),
        (0.78, "SQLite DB\n(campusai.db)"),
        (0.92, "Gemini AI\n(Cloud API)")
    ]

    for x, label in lifelines:
        box = patches.Rectangle((x - 0.07, 0.90), 0.14, 0.045, facecolor=CLR_BG_GRAY, edgecolor=CLR_BORDER, lw=1.1, zorder=3)
        ax.add_patch(box)
        ax.text(x, 0.922, label, ha="center", va="center", fontsize=6.8, weight="bold", color=CLR_TEXT, zorder=4)
        ax.plot([x, x], [0.08, 0.90], color="#94a3b8", linestyle="--", lw=0.9, zorder=1)

    steps = [
        (0.10, 0.26, "1. Open chat page", "-", False, 0.86),
        (0.10, 0.26, "2. Type query / Voice input", "-", False, 0.81),
        (0.26, 0.44, "3. POST /api/chat {query}", "-", False, 0.76),
        (0.44, 0.62, "4. Tokenize & clean text", "-", False, 0.71),
        (0.62, 0.78, "5. Query FAQ corpus", "-", False, 0.66),
        (0.78, 0.62, "6. Return FAQ tokens", "--", False, 0.61),
        (0.62, 0.44, "7. Best score S = 0.88", "--", False, 0.56),
        (0.44, 0.78, "8. Fetch verified answer", "-", False, 0.51),
        (0.78, 0.44, "9. Return answer text", "--", False, 0.46),
        (0.44, 0.92, "10. [If low score] Gemini fallback", "-", False, 0.41),
        (0.92, 0.44, "11. Bounded answer return", "--", False, 0.36),
        (0.44, 0.78, "12. Save turn to chat_messages", "-", False, 0.31),
        (0.44, 0.26, "13. Return JSON response", "--", False, 0.26),
        (0.26, 0.10, "14. Render answer & TTS audio", "--", False, 0.21),
        (0.10, 0.26, "15. Click feedback (+1 / -1)", "-", False, 0.16),
        (0.26, 0.78, "16. Save feedback to database", "-", False, 0.11),
    ]

    for x1, x2, msg, style, is_ret, y in steps:
        ls = "--" if style == "--" else "-"
        ax.annotate(msg, xy=(x2, y), xytext=(x1, y),
                    arrowprops=dict(arrowstyle="->", linestyle=ls, lw=1.0, color=CLR_BORDER),
                    fontsize=6.5, color=CLR_TEXT, zorder=3)

    ax.text(0.50, 0.02, "Fig: Sequence Diagram – Query Ingestion, NLP Matching, Fallback and Feedback Flow", ha="center", fontsize=8.0, style="italic", color=CLR_TEXT)

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_sequence_diagram.png"), bbox_inches="tight")
    plt.close()
    print("[5/9] Generated Reference-Style Sequence Diagram: campusai_sequence_diagram.png")

create_reference_sequence_diagram()


# ==============================================================================
# 6. ACTIVITY DIAGRAM (Exact structure of Reference PDF Page 28: 3 Swimlanes!)
# ==============================================================================
def create_reference_activity_diagram():
    fig, ax = plt.subplots(figsize=(8.5, 9.2), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # 3 Swimlanes Outer Box
    ax.add_patch(patches.Rectangle((0.08, 0.08), 0.84, 0.88, facecolor=CLR_WHITE, edgecolor=CLR_BORDER, lw=1.2, zorder=1))

    # Column dividers
    ax.plot([0.36, 0.36], [0.08, 0.96], color=CLR_BORDER, lw=1.1, zorder=2)
    ax.plot([0.64, 0.64], [0.08, 0.96], color=CLR_BORDER, lw=1.1, zorder=2)

    # Swimlane Header row
    ax.add_patch(patches.Rectangle((0.08, 0.91), 0.84, 0.05, facecolor=CLR_BG_PURPLE, edgecolor=CLR_BORDER, lw=1.1, zorder=2))
    ax.text(0.22, 0.935, "Student", ha="center", va="center", fontsize=8.0, weight="bold", color=CLR_TEXT, zorder=3)
    ax.text(0.50, 0.935, "Chatbot System (Engine)", ha="center", va="center", fontsize=8.0, weight="bold", color=CLR_TEXT, zorder=3)
    ax.text(0.78, 0.935, "Administrator", ha="center", va="center", fontsize=8.0, weight="bold", color=CLR_TEXT, zorder=3)

    def draw_act(cx, cy, w, h, text):
        b = patches.FancyBboxPatch((cx - w/2, cy - h/2), w, h, boxstyle="round,pad=0.008,rounding_size=0.012",
                                   facecolor=CLR_BG_GRAY, edgecolor=CLR_BORDER, lw=1.0, zorder=3)
        ax.add_patch(b)
        ax.text(cx, cy, text, ha="center", va="center", fontsize=6.8, color=CLR_TEXT, zorder=4)

    def draw_diamond(cx, cy, w, h, text):
        pts = [[cx, cy + h/2], [cx + w/2, cy], [cx, cy - h/2], [cx - w/2, cy]]
        poly = Polygon(pts, closed=True, facecolor=CLR_WHITE, edgecolor=CLR_BORDER, lw=1.0, zorder=3)
        ax.add_patch(poly)
        ax.text(cx, cy, text, ha="center", va="center", fontsize=6.5, color=CLR_TEXT, zorder=4)

    # Lane 1 (Student):
    start1 = Circle((0.22, 0.87), 0.014, facecolor=CLR_BORDER, edgecolor=CLR_BORDER, zorder=4)
    ax.add_patch(start1)

    ax.annotate("", xy=(0.22, 0.81), xytext=(0.22, 0.85), arrowprops=dict(arrowstyle="->", lw=1.0))
    draw_act(0.22, 0.78, 0.22, 0.042, "Open Chatbot Page")

    ax.annotate("", xy=(0.22, 0.71), xytext=(0.22, 0.76), arrowprops=dict(arrowstyle="->", lw=1.0))
    draw_act(0.22, 0.68, 0.22, 0.042, "Enter Academic Query\n(Text or Mic)")

    ax.annotate("", xy=(0.22, 0.52), xytext=(0.22, 0.66), arrowprops=dict(arrowstyle="->", lw=1.0))
    draw_act(0.22, 0.49, 0.22, 0.042, "View Answer Bubble\n& Category Badge")

    ax.annotate("", xy=(0.22, 0.41), xytext=(0.22, 0.47), arrowprops=dict(arrowstyle="->", lw=1.0))
    draw_act(0.22, 0.38, 0.22, 0.042, "Listen Audio TTS\nor Copy Answer")

    ax.annotate("", xy=(0.22, 0.30), xytext=(0.22, 0.36), arrowprops=dict(arrowstyle="->", lw=1.0))
    draw_act(0.22, 0.27, 0.22, 0.042, "Submit Feedback\n(Thumbs Up / Down)")

    ax.annotate("", xy=(0.22, 0.19), xytext=(0.22, 0.25), arrowprops=dict(arrowstyle="->", lw=1.0))
    draw_act(0.22, 0.16, 0.22, 0.042, "Clear Session")

    ax.annotate("", xy=(0.22, 0.11), xytext=(0.22, 0.14), arrowprops=dict(arrowstyle="->", lw=1.0))
    end1_out = Circle((0.22, 0.10), 0.012, facecolor=CLR_WHITE, edgecolor=CLR_BORDER, lw=1.2, zorder=4)
    end1_in = Circle((0.22, 0.10), 0.007, facecolor=CLR_BORDER, edgecolor=CLR_BORDER, zorder=5)
    ax.add_patch(end1_out)
    ax.add_patch(end1_in)

    # Lane 2 (System):
    ax.annotate("", xy=(0.39, 0.68), xytext=(0.33, 0.68), arrowprops=dict(arrowstyle="->", lw=1.0))
    draw_act(0.50, 0.68, 0.22, 0.042, "NLP Tokenization\n& Jaccard Matching")

    ax.annotate("", xy=(0.50, 0.61), xytext=(0.50, 0.66), arrowprops=dict(arrowstyle="->", lw=1.0))
    draw_diamond(0.50, 0.58, 0.12, 0.045, "Score >= 0.45?")

    # Yes branch -> DB match
    ax.annotate("Yes", xy=(0.50, 0.51), xytext=(0.50, 0.555), arrowprops=dict(arrowstyle="->", lw=1.0), fontsize=6.5)
    draw_act(0.50, 0.48, 0.22, 0.042, "Fetch Verified FAQ\nfrom SQLite Database")

    # No branch -> Gemini fallback
    ax.annotate("No", xy=(0.42, 0.58), xytext=(0.44, 0.58), fontsize=6.5)
    ax.plot([0.44, 0.38, 0.38, 0.39], [0.58, 0.58, 0.42, 0.42], color=CLR_BORDER, lw=0.9)
    draw_act(0.50, 0.42, 0.22, 0.038, "Invoke Gemini AI Fallback\n(Bounded Context)")

    ax.annotate("", xy=(0.50, 0.33), xytext=(0.50, 0.46), arrowprops=dict(arrowstyle="->", lw=1.0))
    draw_act(0.50, 0.30, 0.22, 0.042, "Save Conversation Turn\nto chat_messages")

    # Return to student
    ax.plot([0.39, 0.33], [0.49, 0.49], color=CLR_BORDER, lw=1.0)
    ax.annotate("", xy=(0.33, 0.49), xytext=(0.39, 0.49), arrowprops=dict(arrowstyle="->", lw=1.0))

    # Lane 3 (Administrator):
    start3 = Circle((0.78, 0.87), 0.014, facecolor=CLR_BORDER, edgecolor=CLR_BORDER, zorder=4)
    ax.add_patch(start3)

    ax.annotate("", xy=(0.78, 0.81), xytext=(0.78, 0.85), arrowprops=dict(arrowstyle="->", lw=1.0))
    draw_act(0.78, 0.78, 0.22, 0.042, "Admin Login\n(PBKDF2 Password)")

    ax.annotate("", xy=(0.78, 0.70), xytext=(0.78, 0.76), arrowprops=dict(arrowstyle="->", lw=1.0))
    draw_act(0.78, 0.67, 0.22, 0.042, "Manage FAQs\n(Add / Edit / Delete)")

    ax.annotate("", xy=(0.78, 0.59), xytext=(0.78, 0.65), arrowprops=dict(arrowstyle="->", lw=1.0))
    draw_act(0.78, 0.56, 0.22, 0.042, "Filter by 8 Domains\n& View Telemetry")

    ax.annotate("", xy=(0.78, 0.48), xytext=(0.78, 0.54), arrowprops=dict(arrowstyle="->", lw=1.0))
    draw_act(0.78, 0.45, 0.22, 0.042, "Export Chat History\nto CSV File")

    ax.annotate("", xy=(0.78, 0.37), xytext=(0.78, 0.43), arrowprops=dict(arrowstyle="->", lw=1.0))
    draw_act(0.78, 0.34, 0.22, 0.042, "View Live System Health\n& Model Latency")

    ax.annotate("", xy=(0.78, 0.28), xytext=(0.78, 0.32), arrowprops=dict(arrowstyle="->", lw=1.0))
    end3_out = Circle((0.78, 0.26), 0.012, facecolor=CLR_WHITE, edgecolor=CLR_BORDER, lw=1.2, zorder=4)
    end3_in = Circle((0.78, 0.26), 0.007, facecolor=CLR_BORDER, edgecolor=CLR_BORDER, zorder=5)
    ax.add_patch(end3_out)
    ax.add_patch(end3_in)

    ax.text(0.50, 0.02, "Fig: Activity Diagram", ha="center", fontsize=8.5, style="italic", color=CLR_TEXT)

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_activity_diagram.png"), bbox_inches="tight")
    plt.close()
    print("[6/9] Generated Reference-Style Activity Diagram: campusai_activity_diagram.png")

create_reference_activity_diagram()


# ==============================================================================
# 7. COMPONENT DIAGRAM (Exact structure of Reference PDF Page 29)
# ==============================================================================
def create_reference_component_diagram():
    fig, ax = plt.subplots(figsize=(8.5, 9.2), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # 1. Frontend Outer Box (Left)
    ax.add_patch(patches.Rectangle((0.08, 0.08), 0.32, 0.88, facecolor=CLR_WHITE, edgecolor=CLR_BORDER, lw=1.2, zorder=1))
    ax.add_patch(patches.Rectangle((0.08, 0.92), 0.32, 0.04, facecolor=CLR_BG_GRAY, edgecolor=CLR_BORDER, lw=1.0, zorder=2))
    ax.text(0.24, 0.94, "Frontend (HTML5 / JS / CSS3)", ha="center", va="center", fontsize=7.8, weight="bold", color=CLR_TEXT, zorder=3)

    # 2. Backend Server Outer Box (Center)
    ax.add_patch(patches.Rectangle((0.44, 0.08), 0.32, 0.88, facecolor=CLR_WHITE, edgecolor=CLR_BORDER, lw=1.2, zorder=1))
    ax.add_patch(patches.Rectangle((0.44, 0.92), 0.32, 0.04, facecolor=CLR_BG_GRAY, edgecolor=CLR_BORDER, lw=1.0, zorder=2))
    ax.text(0.60, 0.94, "Backend Server (Python + Flask)", ha="center", va="center", fontsize=7.8, weight="bold", color=CLR_TEXT, zorder=3)

    def draw_module_box(x, y, w, h, text):
        b = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.005,rounding_size=0.008",
                                   facecolor=CLR_BG_BLUE, edgecolor=CLR_BORDER, lw=0.9, zorder=3)
        ax.add_patch(b)
        ax.text(x + w/2, y + h/2, text, ha="center", va="center", fontsize=6.8, color=CLR_TEXT, zorder=4)

    modules = [
        ("Login / Register UI", "Authentication Module"),
        ("Query Input & Chat UI", "NLP Routing Module"),
        ("Voice Speech (STT) UI", "Speech Transcription Engine"),
        ("Category Filter Bar UI", "Domain Classification Module"),
        ("Audio Synthesis (TTS) UI", "Audio Streaming Module"),
        ("Admin Dashboard UI", "Telemetry & Analytics Module"),
        ("FAQ Management UI", "Knowledge Base CRUD Module")
    ]

    start_y = 0.84
    step_y = 0.11

    for idx, (fe_text, be_text) in enumerate(modules):
        my = start_y - idx * step_y
        draw_module_box(0.10, my, 0.28, 0.065, fe_text)
        draw_module_box(0.46, my, 0.28, 0.065, be_text)

        # Horizontal connecting line between Frontend and Backend
        ax.plot([0.38, 0.46], [my + 0.032, my + 0.032], color=CLR_BORDER, lw=1.0, zorder=2)

        # Connecting line from Backend to Database Cylinder
        ax.plot([0.74, 0.82], [my + 0.032, 0.50], color=CLR_BORDER, lw=0.9, zorder=2)

    # Database Cylinder (Right Center)
    top_e = Ellipse((0.89, 0.55), 0.14, 0.05, facecolor=CLR_BG_BLUE, edgecolor=CLR_BORDER, lw=1.2, zorder=4)
    body_r = patches.Rectangle((0.82, 0.42), 0.14, 0.13, facecolor=CLR_BG_BLUE, edgecolor="none", zorder=2)
    ax.add_patch(body_r)
    ax.plot([0.82, 0.82], [0.42, 0.55], color=CLR_BORDER, lw=1.2, zorder=3)
    ax.plot([0.96, 0.96], [0.42, 0.55], color=CLR_BORDER, lw=1.2, zorder=3)
    bot_e = Ellipse((0.89, 0.42), 0.14, 0.05, facecolor=CLR_BG_BLUE, edgecolor=CLR_BORDER, lw=1.2, zorder=3)
    ax.add_patch(bot_e)
    ax.add_patch(top_e)
    ax.text(0.89, 0.48, "SQLite 3\nDatabase\n(campusai.db)", ha="center", va="center", fontsize=6.8, weight="bold", color=CLR_TEXT, zorder=5)

    # External Service Box: Google Gemini API (Top Right, yellow box like Ref PDF)
    gem_box = patches.FancyBboxPatch((0.82, 0.75), 0.14, 0.08, boxstyle="round,pad=0.005,rounding_size=0.008",
                                     facecolor=CLR_BG_YELLOW, edgecolor=CLR_BORDER, lw=1.0, zorder=3)
    ax.add_patch(gem_box)
    ax.text(0.89, 0.79, "Google Gemini\n2.5 Flash API", ha="center", va="center", fontsize=6.8, weight="bold", color=CLR_TEXT, zorder=4)
    ax.plot([0.74, 0.82], [0.73, 0.79], color=CLR_BORDER, linestyle="--", lw=1.0, zorder=2)

    # External Service Box: Web Speech API (Bottom Right, yellow box like Ref PDF)
    stt_box = patches.FancyBboxPatch((0.82, 0.18), 0.14, 0.08, boxstyle="round,pad=0.005,rounding_size=0.008",
                                     facecolor=CLR_BG_YELLOW, edgecolor=CLR_BORDER, lw=1.0, zorder=3)
    ax.add_patch(stt_box)
    ax.text(0.89, 0.22, "W3C Web Speech\nAPI Engine", ha="center", va="center", fontsize=6.8, weight="bold", color=CLR_TEXT, zorder=4)
    ax.plot([0.74, 0.82], [0.29, 0.22], color=CLR_BORDER, linestyle="--", lw=1.0, zorder=2)

    ax.text(0.50, 0.02, "Fig: Component Diagram", ha="center", fontsize=8.5, style="italic", color=CLR_TEXT)

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_component_diagram.png"), bbox_inches="tight")
    plt.close()
    print("[7/9] Generated Reference-Style Component Diagram: campusai_component_diagram.png")

create_reference_component_diagram()


# ==============================================================================
# 8. DATA FLOW DIAGRAM (Exact structure of Reference PDF Page 30)
# ==============================================================================
def create_reference_dfd():
    fig, ax = plt.subplots(figsize=(8.5, 9.8), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # PART 1: LEVEL 0 CONTEXT DIAGRAM
    ax.text(0.08, 0.97, "Level 0 (Context Diagram)", fontsize=8.5, weight="bold", color=CLR_TEXT)

    # Entities
    def draw_entity(cx, cy, w, h, text):
        r = patches.Rectangle((cx - w/2, cy - h/2), w, h, facecolor=CLR_BG_GRAY, edgecolor=CLR_BORDER, lw=1.1, zorder=3)
        ax.add_patch(r)
        ax.text(cx, cy, text, ha="center", va="center", fontsize=7.5, weight="bold", color=CLR_TEXT, zorder=4)

    draw_entity(0.18, 0.88, 0.14, 0.05, "Student")
    draw_entity(0.82, 0.88, 0.14, 0.05, "Admin")

    # Center Process Circle
    p0 = Circle((0.50, 0.88), 0.065, facecolor=CLR_BG_PURPLE, edgecolor=CLR_BORDER, lw=1.2, zorder=3)
    ax.add_patch(p0)
    ax.text(0.50, 0.90, "0", ha="center", fontsize=7.5, weight="bold", color=CLR_TEXT, zorder=4)
    ax.text(0.50, 0.87, "CampusAI College\nAssistant Chatbot\nSystem", ha="center", va="center", fontsize=6.2, color=CLR_TEXT, zorder=4)

    # Database Cylinder (Bottom of Level 0)
    top_e = Ellipse((0.50, 0.77), 0.16, 0.035, facecolor=CLR_BG_BLUE, edgecolor=CLR_BORDER, lw=1.1, zorder=4)
    body_r = patches.Rectangle((0.42, 0.72), 0.16, 0.05, facecolor=CLR_BG_BLUE, edgecolor="none", zorder=2)
    ax.add_patch(body_r)
    ax.plot([0.42, 0.42], [0.72, 0.77], color=CLR_BORDER, lw=1.1, zorder=3)
    ax.plot([0.58, 0.58], [0.72, 0.77], color=CLR_BORDER, lw=1.1, zorder=3)
    bot_e = Ellipse((0.50, 0.72), 0.16, 0.035, facecolor=CLR_BG_BLUE, edgecolor=CLR_BORDER, lw=1.1, zorder=3)
    ax.add_patch(bot_e)
    ax.add_patch(top_e)
    ax.text(0.50, 0.74, "Database", ha="center", va="center", fontsize=7.0, color=CLR_TEXT, zorder=5)

    # Flows for Level 0
    ax.annotate("query, speech input", xy=(0.435, 0.89), xytext=(0.25, 0.89), arrowprops=dict(arrowstyle="->", lw=1.0), fontsize=6.2)
    ax.annotate("verified answers, audio", xy=(0.25, 0.86), xytext=(0.435, 0.86), arrowprops=dict(arrowstyle="->", lw=1.0), fontsize=6.2)
    ax.annotate("manage faqs, credentials", xy=(0.565, 0.89), xytext=(0.75, 0.89), arrowprops=dict(arrowstyle="->", lw=1.0), fontsize=6.2)
    ax.annotate("analytics reports, logs", xy=(0.75, 0.86), xytext=(0.565, 0.86), arrowprops=dict(arrowstyle="->", lw=1.0), fontsize=6.2)
    ax.annotate("", xy=(0.50, 0.785), xytext=(0.50, 0.815), arrowprops=dict(arrowstyle="<->", lw=1.0))

    ax.text(0.50, 0.68, "Fig: DFD Level 0", ha="center", fontsize=7.8, style="italic", color=CLR_TEXT)
    ax.plot([0.08, 0.92], [0.66, 0.66], color=CLR_BORDER, lw=0.8, linestyle="--")

    # PART 2: LEVEL 1 DFD
    ax.text(0.08, 0.64, "Level 1 DFD", fontsize=8.5, weight="bold", color=CLR_TEXT)

    # Student on left
    draw_entity(0.14, 0.35, 0.12, 0.06, "Student")

    # Process Ovals (1 to 6)
    procs = [
        "1. Ingest Query",
        "2. NLP Tokenize",
        "3. Jaccard Match",
        "4. Gemini Fallback",
        "5. Format Response",
        "6. Admin CRUD"
    ]
    start_y = 0.58
    step_y = 0.085

    for idx, p_name in enumerate(procs):
        py = start_y - idx * step_y
        e = Ellipse((0.44, py), 0.22, 0.045, facecolor=CLR_BG_GRAY, edgecolor=CLR_BORDER, lw=1.1, zorder=3)
        ax.add_patch(e)
        ax.text(0.44, py, p_name, ha="center", va="center", fontsize=6.8, color=CLR_TEXT, zorder=4)

        # Arrow from Student to Process
        ax.plot([0.20, 0.33], [0.35, py], color=CLR_BORDER, lw=0.9, zorder=2)

    # Data Stores on right (open on right like Ref PDF)
    stores = [
        "D1 User Sessions",
        "D2 FAQ Knowledge Base",
        "Google Gemini API",
        "D3 Chat History",
        "D4 Feedback Logs",
        "D5 Admin Accounts"
    ]

    for idx, s_name in enumerate(stores):
        sy = start_y - idx * step_y
        is_service = ("Gemini" in s_name)
        bg = CLR_BG_YELLOW if is_service else CLR_BG_GRAY
        r = patches.Rectangle((0.68, sy - 0.022), 0.24, 0.044, facecolor=bg, edgecolor=CLR_BORDER, lw=1.0, zorder=3)
        ax.add_patch(r)
        ax.text(0.80, sy, s_name, ha="center", va="center", fontsize=6.8, color=CLR_TEXT, zorder=4)

        # Arrow from Process to Store
        ax.plot([0.55, 0.68], [sy, sy], color=CLR_BORDER, lw=0.9, zorder=2)

    ax.text(0.50, 0.02, "Fig: DFD Level 1", ha="center", fontsize=7.8, style="italic", color=CLR_TEXT)

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_dfd.png"), bbox_inches="tight")
    plt.close()
    print("[8/9] Generated Reference-Style DFD Diagram: campusai_dfd.png")

create_reference_dfd()


# ==============================================================================
# 9. DECISION TREE (Exact structure of Reference PDF Page 19)
# ==============================================================================
def create_reference_decision_tree():
    fig, ax = plt.subplots(figsize=(8.5, 9.2), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    def draw_box(cx, cy, w, h, text, bg=CLR_BG_GRAY):
        r = patches.FancyBboxPatch((cx - w/2, cy - h/2), w, h, boxstyle="round,pad=0.006,rounding_size=0.010",
                                   facecolor=bg, edgecolor=CLR_BORDER, lw=1.0, zorder=3)
        ax.add_patch(r)
        ax.text(cx, cy, text, ha="center", va="center", fontsize=6.8, color=CLR_TEXT, zorder=4)

    def draw_diamond(cx, cy, w, h, text, bg=CLR_BG_YELLOW):
        pts = [[cx, cy + h/2], [cx + w/2, cy], [cx, cy - h/2], [cx - w/2, cy]]
        poly = Polygon(pts, closed=True, facecolor=bg, edgecolor=CLR_BORDER, lw=1.0, zorder=3)
        ax.add_patch(poly)
        ax.text(cx, cy, text, ha="center", va="center", fontsize=6.8, color=CLR_TEXT, zorder=4)

    # Start Node (Oval)
    st = Ellipse((0.50, 0.94), 0.14, 0.045, facecolor=CLR_BG_BLUE, edgecolor=CLR_BORDER, lw=1.1, zorder=3)
    ax.add_patch(st)
    ax.text(0.50, 0.94, "Start", ha="center", va="center", fontsize=7.5, weight="bold", color=CLR_TEXT, zorder=4)

    ax.annotate("", xy=(0.50, 0.88), xytext=(0.50, 0.915), arrowprops=dict(arrowstyle="->", lw=1.0))
    draw_box(0.50, 0.85, 0.26, 0.045, "Open Chatbot / Enter Query")

    ax.annotate("", xy=(0.50, 0.77), xytext=(0.50, 0.825), arrowprops=dict(arrowstyle="->", lw=1.0))
    draw_diamond(0.50, 0.74, 0.18, 0.055, "Valid Input?")

    # No branch
    ax.annotate("No", xy=(0.74, 0.74), xytext=(0.59, 0.74), arrowprops=dict(arrowstyle="->", lw=1.0), fontsize=6.8)
    draw_box(0.82, 0.74, 0.16, 0.045, "Show Error\nMessage", bg=CLR_BG_PINK)
    ax.plot([0.82, 0.82, 0.63], [0.715, 0.85, 0.85], color=CLR_BORDER, lw=0.9)

    # Yes branch
    ax.annotate("Yes", xy=(0.50, 0.65), xytext=(0.50, 0.71), arrowprops=dict(arrowstyle="->", lw=1.0), fontsize=6.8)
    draw_box(0.50, 0.62, 0.32, 0.045, "Preprocess Text (Tokenize & Synonyms)")

    ax.annotate("", xy=(0.50, 0.55), xytext=(0.50, 0.595), arrowprops=dict(arrowstyle="->", lw=1.0))
    draw_box(0.50, 0.52, 0.32, 0.045, "Compute Jaccard Similarity (S)")

    # Choose Action Diamond
    ax.annotate("", xy=(0.50, 0.44), xytext=(0.50, 0.495), arrowprops=dict(arrowstyle="->", lw=1.0))
    draw_diamond(0.50, 0.41, 0.22, 0.060, "Evaluate Score S")

    # 4 Branch boxes (Horizontal spread)
    branches = [
        ("Tier 1: Direct FAQ\n(S >= 0.45)", 0.15),
        ("Tier 2: Gemini AI\n(S < 0.45)", 0.38),
        ("Tier 3: Helpdesk\n(Office Referral)", 0.62),
        ("Audio Read-Aloud\n(TTS Engine)", 0.85)
    ]

    for b_text, bx in branches:
        ax.plot([0.50, bx, bx], [0.38, 0.38, 0.33], color=CLR_BORDER, lw=0.9)
        ax.annotate("", xy=(bx, 0.30), xytext=(bx, 0.33), arrowprops=dict(arrowstyle="->", lw=1.0))
        draw_box(bx, 0.27, 0.20, 0.055, b_text, bg=CLR_BG_BLUE if "Tier 1" in b_text else CLR_BG_GRAY)

        # Connect down to Process Request
        ax.plot([bx, bx, 0.50], [0.24, 0.20, 0.20], color=CLR_BORDER, lw=0.9)

    # Convergence Box
    ax.annotate("", xy=(0.50, 0.16), xytext=(0.50, 0.20), arrowprops=dict(arrowstyle="->", lw=1.0))
    draw_box(0.50, 0.13, 0.46, 0.045, "Persist turn to chat_messages & Format JSON response")

    ax.annotate("", xy=(0.50, 0.075), xytext=(0.50, 0.105), arrowprops=dict(arrowstyle="->", lw=1.0))
    draw_box(0.50, 0.055, 0.46, 0.040, "Render Chat Bubble, Suggestions & Await Feedback")

    ax.text(0.50, 0.01, "Fig: Decision Tree of CampusAI Query Routing Engine", ha="center", fontsize=8.0, style="italic", color=CLR_TEXT)

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_decision_tree.png"), bbox_inches="tight")
    plt.close()
    print("[9/9] Generated Reference-Style Decision Tree: campusai_decision_tree.png")

create_reference_decision_tree()
print("[✓] ALL 9 CAMPUSAI REFERENCE-STYLE DIAGRAMS SUCCESSFULLY GENERATED!")
