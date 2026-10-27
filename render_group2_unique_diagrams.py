"""
CampusAI (Group 2) - Unique UML & Architectural Diagrams Generator
Designs 100% DISTINCT, PUBLICATION-GRADE diagrams for CampusAI:
- Completely different visual style, layout, and notation from Group 1's diagrams.
- Uses Modern Crow's Foot ERD, Subsystem Package Use Case, Enterprise Clean Architecture Class Diagram,
  Combined Fragment Sequence Diagram, Horizontal Pipeline Activity Diagram with Fork/Join,
  Hexagonal Component Diagram with Ports/Adapters, and Multi-Level DFD.
- Academic Year: 2025-2026 | SY BBA CA | G H Raisoni International Skill Tech University, Pune
- Students: Akash Rana (ISTU25010120004) & Shreyash Katke (ISTU25010120003) | Guide: Prof. Sheela Satav
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

# CampusAI Brand Palette: Forest Emerald & Amber Gold with Modern Slate Accents
CLR_EMERALD_DARK = "#064e3b"
CLR_EMERALD = "#059669"
CLR_EMERALD_LIGHT = "#ecfdf5"
CLR_EMERALD_BORDER = "#10b981"

CLR_AMBER_DARK = "#78350f"
CLR_AMBER = "#d97706"
CLR_AMBER_LIGHT = "#fef3c7"
CLR_AMBER_BORDER = "#f59e0b"

CLR_SLATE_DARK = "#0f172a"
CLR_SLATE = "#334155"
CLR_SLATE_LIGHT = "#f8fafc"
CLR_SLATE_BORDER = "#cbd5e1"

CLR_PURPLE = "#7e22ce"
CLR_PURPLE_LIGHT = "#f3e8ff"
CLR_BLUE = "#1d4ed8"
CLR_BLUE_LIGHT = "#eff6ff"

CLR_WHITE = "#ffffff"
CLR_BLACK = "#000000"


# ==============================================================================
# 1. MODERN CROW'S FOOT RELATIONAL SCHEMA ER DIAGRAM
# (Completely distinct from Chen notation ovals!)
# ==============================================================================
def create_crows_foot_er_diagram():
    fig, ax = plt.subplots(figsize=(10.5, 10.5), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Title Banner
    ax.text(0.5, 0.975, "CampusAI Relational Database Architecture: Crow's Foot Schema (3NF)",
            ha="center", va="center", fontsize=11.5, weight="bold", color=CLR_EMERALD_DARK)
    ax.text(0.5, 0.952, "Strict Third Normal Form (3NF) • Entities with Explicit Keys, Data Types, and Relational Cardinality",
            ha="center", va="center", fontsize=8.0, color=CLR_SLATE)

    def draw_entity_table(x, y, w, title, pk_list, fk_list, attr_list, header_color=CLR_EMERALD_DARK):
        line_h = 0.020
        h_title = 0.034
        n_rows = len(pk_list) + len(fk_list) + len(attr_list)
        total_h = h_title + n_rows * line_h + 0.010
        top_y = y

        # Background Card
        card = patches.FancyBboxPatch((x, top_y - total_h), w, total_h,
                                     boxstyle="round,pad=0.005,rounding_size=0.010",
                                     facecolor=CLR_WHITE, edgecolor=header_color, lw=1.3, zorder=3)
        ax.add_patch(card)

        # Header Box
        header_poly = patches.FancyBboxPatch((x, top_y - h_title), w, h_title,
                                             boxstyle="round,pad=0.005,rounding_size=0.010",
                                             facecolor=header_color, edgecolor=header_color, lw=1.0, zorder=4)
        ax.add_patch(header_poly)
        ax.text(x + w/2, top_y - h_title/2, title, ha="center", va="center",
                fontsize=8.5, weight="bold", color=CLR_WHITE, zorder=5)

        curr_y = top_y - h_title - 0.012

        # Draw Primary Keys
        for key_name, dtype in pk_list:
            ax.text(x + 0.012, curr_y, "PK", fontsize=6.8, weight="bold", color=CLR_AMBER_DARK, family="monospace", zorder=5)
            ax.text(x + 0.045, curr_y, key_name, fontsize=7.2, weight="bold", color=CLR_SLATE_DARK, family="monospace", zorder=5)
            ax.text(x + w - 0.012, curr_y, dtype, fontsize=6.8, color="#64748b", family="monospace", ha="right", zorder=5)
            curr_y -= line_h

        # Draw Foreign Keys
        for key_name, dtype in fk_list:
            ax.text(x + 0.012, curr_y, "FK", fontsize=6.8, weight="bold", color=CLR_BLUE, family="monospace", zorder=5)
            ax.text(x + 0.045, curr_y, key_name, fontsize=7.2, color=CLR_SLATE_DARK, family="monospace", zorder=5)
            ax.text(x + w - 0.012, curr_y, dtype, fontsize=6.8, color="#64748b", family="monospace", ha="right", zorder=5)
            curr_y -= line_h

        # Divider line
        if (pk_list or fk_list) and attr_list:
            ax.plot([x + 0.010, x + w - 0.010], [curr_y + 0.005, curr_y + 0.005], color=CLR_SLATE_BORDER, lw=0.8, zorder=4)
            curr_y -= 0.005

        # Draw Normal Attributes
        for attr_name, dtype in attr_list:
            ax.text(x + 0.012, curr_y, "•", fontsize=7.5, color=CLR_SLATE, zorder=5)
            ax.text(x + 0.045, curr_y, attr_name, fontsize=7.0, color=CLR_SLATE_DARK, family="monospace", zorder=5)
            ax.text(x + w - 0.012, curr_y, dtype, fontsize=6.8, color="#64748b", family="monospace", ha="right", zorder=5)
            curr_y -= line_h

        return top_y - total_h

    # Table 1: ADMINISTRATORS (Top Left)
    draw_entity_table(0.05, 0.91, 0.28, "ADMINISTRATORS (admins)",
                      [("admin_id", "INT AUTO_INC")],
                      [],
                      [("username", "VARCHAR(80)"),
                       ("email", "VARCHAR(120)"),
                       ("password_hash", "VARCHAR(255)"),
                       ("role", "VARCHAR(30)"),
                       ("created_at", "DATETIME")],
                      header_color=CLR_EMERALD_DARK)

    # Table 2: ACADEMIC_CATEGORIES (Top Right)
    draw_entity_table(0.67, 0.91, 0.28, "ACADEMIC_CATEGORIES (categories)",
                      [("category_id", "INT AUTO_INC")],
                      [],
                      [("category_name", "VARCHAR(60)"),
                       ("slug", "VARCHAR(50)"),
                       ("icon_code", "VARCHAR(30)"),
                       ("display_order", "INT"),
                       ("is_active", "BOOLEAN")],
                      header_color="#1e3a8a")

    # Table 3: FAQ_KNOWLEDGE_BASE (Center Right)
    draw_entity_table(0.67, 0.68, 0.28, "FAQ_KNOWLEDGE_BASE (faqs)",
                      [("faq_id", "INT AUTO_INC")],
                      [("category_id", "INT [FK]")],
                      [("question", "TEXT NOT NULL"),
                       ("answer", "TEXT NOT NULL"),
                       ("keywords", "VARCHAR(255)"),
                       ("view_count", "INT DEFAULT 0"),
                       ("updated_at", "DATETIME")],
                      header_color=CLR_EMERALD_DARK)

    # Table 4: CHAT_SESSIONS (Center Left)
    draw_entity_table(0.05, 0.65, 0.28, "CHAT_SESSIONS (chat_sessions)",
                      [("session_id", "VARCHAR(64)")],
                      [],
                      [("client_ip", "VARCHAR(45)"),
                       ("created_at", "DATETIME"),
                       ("last_active", "DATETIME"),
                       ("total_turns", "INT DEFAULT 1")],
                      header_color="#0f766e")

    # Table 5: CHAT_MESSAGES (Bottom Left)
    draw_entity_table(0.05, 0.40, 0.38, "CHAT_MESSAGES (chat_messages)",
                      [("message_id", "INT AUTO_INC")],
                      [("session_id", "VARCHAR(64) [FK]")],
                      [("role", "VARCHAR(20) [user/bot]"),
                       ("content", "TEXT NOT NULL"),
                       ("source_tier", "VARCHAR(30) [db/ai/fb]"),
                       ("similarity_score", "FLOAT"),
                       ("timestamp", "DATETIME DEFAULT NOW")],
                      header_color=CLR_EMERALD_DARK)

    # Table 6: USER_FEEDBACK_LOGS (Bottom Right)
    draw_entity_table(0.57, 0.38, 0.38, "USER_FEEDBACK_LOGS (feedback_logs)",
                      [("feedback_id", "INT AUTO_INC")],
                      [("message_id", "INT [FK]")],
                      [("rating_value", "INT [+1 / -1]"),
                       ("feedback_tag", "VARCHAR(50)"),
                       ("client_note", "TEXT NULLABLE"),
                       ("created_at", "DATETIME DEFAULT NOW")],
                      header_color=CLR_AMBER_DARK)

    # Crow's Foot Connector Lines with formal Cardinality Markers
    # 1. CATEGORIES to FAQS (1 to Many: || to }o)
    ax.plot([0.81, 0.81], [0.73, 0.68], color=CLR_SLATE_DARK, lw=1.3, zorder=2)
    # 1 marker at Categories
    ax.plot([0.795, 0.825], [0.725, 0.725], color=CLR_SLATE_DARK, lw=1.3, zorder=2)
    ax.plot([0.795, 0.825], [0.720, 0.720], color=CLR_SLATE_DARK, lw=1.3, zorder=2)
    # Crow foot marker at FAQS
    ax.plot([0.81, 0.795], [0.68, 0.695], color=CLR_SLATE_DARK, lw=1.3, zorder=2)
    ax.plot([0.81, 0.825], [0.68, 0.695], color=CLR_SLATE_DARK, lw=1.3, zorder=2)
    ax.text(0.82, 0.705, "1 : N (Classified In)", fontsize=7.2, color=CLR_SLATE_DARK, weight="bold")

    # 2. CHAT_SESSIONS to CHAT_MESSAGES (1 to Many: || to }o)
    ax.plot([0.19, 0.19], [0.49, 0.40], color=CLR_SLATE_DARK, lw=1.3, zorder=2)
    ax.plot([0.175, 0.205], [0.485, 0.485], color=CLR_SLATE_DARK, lw=1.3, zorder=2)
    ax.plot([0.175, 0.205], [0.480, 0.480], color=CLR_SLATE_DARK, lw=1.3, zorder=2)
    ax.plot([0.19, 0.175], [0.40, 0.415], color=CLR_SLATE_DARK, lw=1.3, zorder=2)
    ax.plot([0.19, 0.205], [0.40, 0.415], color=CLR_SLATE_DARK, lw=1.3, zorder=2)
    ax.text(0.20, 0.445, "1 : N (Generates)", fontsize=7.2, color=CLR_SLATE_DARK, weight="bold")

    # 3. CHAT_MESSAGES to USER_FEEDBACK_LOGS (1 to Zero-or-One: || to |o)
    ax.plot([0.43, 0.57], [0.26, 0.26], color=CLR_SLATE_DARK, lw=1.3, zorder=2)
    ax.plot([0.445, 0.445], [0.25, 0.27], color=CLR_SLATE_DARK, lw=1.3, zorder=2)
    ax.plot([0.455, 0.455], [0.25, 0.27], color=CLR_SLATE_DARK, lw=1.3, zorder=2)
    # Circle + Line at Feedback
    circ = Circle((0.550, 0.26), 0.007, facecolor=CLR_WHITE, edgecolor=CLR_SLATE_DARK, lw=1.2, zorder=3)
    ax.add_patch(circ)
    ax.plot([0.562, 0.562], [0.25, 0.27], color=CLR_SLATE_DARK, lw=1.3, zorder=2)
    ax.text(0.50, 0.28, "1 : 0..1 (Audits)", ha="center", fontsize=7.2, color=CLR_SLATE_DARK, weight="bold")

    # 4. ADMIN to FAQS (1 to Many: || to }o)
    ax.plot([0.33, 0.67], [0.82, 0.82], color=CLR_EMERALD, lw=1.3, linestyle="--", zorder=2)
    ax.text(0.50, 0.835, "1 : N (Governs & Maintains)", ha="center", fontsize=7.2, color=CLR_EMERALD, weight="bold")

    # Crow's Foot Notation Key Card at Bottom
    leg_box = patches.FancyBboxPatch((0.05, 0.03), 0.90, 0.09,
                                     boxstyle="round,pad=0.005,rounding_size=0.010",
                                     facecolor="#f1f5f9", edgecolor=CLR_SLATE_BORDER, lw=1.0, zorder=2)
    ax.add_patch(leg_box)
    ax.text(0.07, 0.095, "CROW'S FOOT NOTATION CONVENTIONS & 3NF INTEGRITY SPECIFICATION:", fontsize=7.5, weight="bold", color=CLR_SLATE_DARK)
    ax.text(0.07, 0.072, "• Exact Cardinality: || = Exactly One (Mandatory)  |o = Zero or One (Optional)  }o = Zero or Many  }| = One or Many", fontsize=7.0, color=CLR_SLATE)
    ax.text(0.07, 0.052, "• Normalization: Zero transitive dependencies, functional determinism on primary keys, strict referential FK constraints.", fontsize=7.0, color=CLR_SLATE)
    ax.text(0.07, 0.035, "• Database Engine: ACID-Compliant Embedded SQLite 3 with WAL (Write-Ahead Logging) and sub-millisecond B-Tree indexing.", fontsize=7.0, color=CLR_SLATE)

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_er_diagram.png"), bbox_inches="tight")
    plt.close()
    print("[1/8] Generated Unique Crow's Foot ER Diagram: campusai_er_diagram.png")

create_crows_foot_er_diagram()


# ==============================================================================
# 2. SUBSYSTEM-PACKAGED UML 2.5 USE CASE DIAGRAM
# (Grouped into functional packages with distinct visual architecture!)
# ==============================================================================
def create_packaged_use_case_diagram():
    fig, ax = plt.subplots(figsize=(10.5, 11.0), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.text(0.5, 0.980, "UML 2.5 Use Case Architecture: CampusAI Academic Assistant System",
            ha="center", va="center", fontsize=11.5, weight="bold", color=CLR_EMERALD_DARK)
    ax.text(0.5, 0.960, "Functional Subsystem Decomposition • 4 Dedicated Actors, Boundary Packages, and Dependency Stereotypes",
            ha="center", va="center", fontsize=8.0, color=CLR_SLATE)

    def draw_actor(x, y, label, sublabel, color="#0f172a"):
        # Head
        h = Circle((x, y + 0.038), 0.016, facecolor=CLR_WHITE, edgecolor=color, lw=1.5, zorder=5)
        ax.add_patch(h)
        # Body
        ax.plot([x, x], [y + 0.022, y - 0.018], color=color, lw=1.5, zorder=5)
        # Arms
        ax.plot([x - 0.020, x + 0.020], [y + 0.008, y + 0.008], color=color, lw=1.5, zorder=5)
        # Legs
        ax.plot([x, x - 0.016], [y - 0.018, y - 0.050], color=color, lw=1.5, zorder=5)
        ax.plot([x, x + 0.016], [y - 0.018, y - 0.050], color=color, lw=1.5, zorder=5)
        # Labels
        ax.text(x, y - 0.065, label, ha="center", va="top", fontsize=8.0, weight="bold", color=color, zorder=6)
        ax.text(x, y - 0.085, sublabel, ha="center", va="top", fontsize=6.8, color="#64748b", zorder=6)

    def draw_package(x, y, w, h, title, border_clr="#0284c7", bg_clr="#f0f9ff"):
        # Tab
        tab_w = w * 0.45
        tab_h = 0.028
        tab = patches.Rectangle((x, y + h), tab_w, tab_h, facecolor=border_clr, edgecolor=border_clr, lw=1.0, zorder=2)
        ax.add_patch(tab)
        ax.text(x + tab_w/2, y + h + tab_h/2, f"«subsystem» {title}", ha="center", va="center", fontsize=7.2, weight="bold", color=CLR_WHITE, zorder=3)
        # Body
        body = patches.Rectangle((x, y), w, h, facecolor=bg_clr, edgecolor=border_clr, lw=1.3, zorder=1)
        ax.add_patch(body)

    def draw_uc(cx, cy, label, w=0.24, h=0.040, bg="#ffffff", border="#0284c7"):
        e = Ellipse((cx, cy), w, h, facecolor=bg, edgecolor=border, lw=1.2, zorder=4)
        ax.add_patch(e)
        ax.text(cx, cy, label, ha="center", va="center", fontsize=6.8, weight="bold", color=CLR_SLATE_DARK, zorder=5)

    # ACTOR 1: Student / Visitor (Left)
    draw_actor(0.08, 0.70, "Student / Visitor", "«Primary Actor»", color=CLR_EMERALD_DARK)

    # ACTOR 2: Chief Administrator (Right)
    draw_actor(0.92, 0.70, "College Administrator", "«Primary Actor»", color="#1e3a8a")

    # ACTOR 3: SQLite Storage System (Bottom Left)
    draw_actor(0.08, 0.22, "SQLite3 Database", "«Data Store»", color="#0f766e")

    # ACTOR 4: Gemini Cloud Service (Bottom Right)
    draw_actor(0.92, 0.22, "Google Gemini AI", "«Cloud Intelligence»", color=CLR_PURPLE)

    # SUBSYSTEM 1: CONVERSATIONAL QUERY SERVICES (Top Half)
    draw_package(0.20, 0.60, 0.60, 0.33, "Conversational Query Subsystem", border_clr=CLR_EMERALD, bg_clr=CLR_EMERALD_LIGHT)
    draw_uc(0.35, 0.88, "UC1: Natural Language Query", 0.24, 0.040, border=CLR_EMERALD)
    draw_uc(0.35, 0.81, "UC2: Voice Input (Web Speech STT)", 0.24, 0.040, border=CLR_EMERALD)
    draw_uc(0.35, 0.74, "UC3: Filter Inquiries by 8 Domains", 0.24, 0.040, border=CLR_EMERALD)
    draw_uc(0.35, 0.67, "UC4: Audio Read-Aloud (TTS)", 0.24, 0.040, border=CLR_EMERALD)
    draw_uc(0.65, 0.88, "UC5: Click Quick Suggestion Chips", 0.24, 0.040, border=CLR_EMERALD)
    draw_uc(0.65, 0.81, "UC6: Copy Response to Clipboard", 0.24, 0.040, border=CLR_EMERALD)
    draw_uc(0.65, 0.74, "UC7: Submit Answer Feedback (+1 / -1)", 0.24, 0.040, border=CLR_EMERALD)
    draw_uc(0.65, 0.67, "UC8: Clear Chat Session & Reset", 0.24, 0.040, border=CLR_EMERALD)

    # SUBSYSTEM 2: INTELLIGENT AI & RETRIEVAL ENGINE (Middle)
    draw_package(0.20, 0.34, 0.60, 0.23, "Hybrid Dual-Tier AI Subsystem", border_clr="#6366f1", bg_clr="#eef2ff")
    draw_uc(0.35, 0.50, "UC9: Local Jaccard NLP Matching", 0.24, 0.040, border="#6366f1")
    draw_uc(0.65, 0.50, "UC10: Gemini 2.5 Flash Fallback", 0.24, 0.040, border=CLR_PURPLE, bg="#faf5ff")
    draw_uc(0.50, 0.39, "UC11: Enforce Zero-Hallucination Policy", 0.28, 0.040, border="#dc2626", bg="#fef2f2")

    # SUBSYSTEM 3: ADMINISTRATIVE GOVERNANCE & TELEMETRY (Bottom)
    draw_package(0.20, 0.08, 0.60, 0.23, "Administrative Governance Subsystem", border_clr="#1e3a8a", bg_clr="#eff6ff")
    draw_uc(0.35, 0.25, "UC12: Salted PBKDF2 Authentication", 0.24, 0.040, border="#1e3a8a")
    draw_uc(0.65, 0.25, "UC13: FAQ Knowledge Base CRUD", 0.24, 0.040, border="#1e3a8a")
    draw_uc(0.35, 0.14, "UC14: Live Health & Telemetry KPI", 0.24, 0.040, border="#1e3a8a")
    draw_uc(0.65, 0.14, "UC15: Audit Transcripts & CSV Export", 0.24, 0.040, border="#1e3a8a")

    # Connect Student Actor to UC1..UC4
    for y_pos in [0.88, 0.81, 0.74, 0.67]:
        ax.plot([0.11, 0.23], [0.70, y_pos], color=CLR_EMERALD_DARK, lw=1.1, zorder=3)

    # Connect Administrator Actor to UC12..UC15
    for y_pos in [0.25, 0.14]:
        ax.plot([0.89, 0.77], [0.70, y_pos], color="#1e3a8a", lw=1.1, zorder=3)
    ax.plot([0.89, 0.47], [0.70, 0.25], color="#1e3a8a", lw=1.1, zorder=3)
    ax.plot([0.89, 0.47], [0.70, 0.14], color="#1e3a8a", lw=1.1, zorder=3)

    # Stereotypes <<extend>> and <<include>>
    ax.annotate("«extend»", xy=(0.65, 0.52), xytext=(0.47, 0.88),
                arrowprops=dict(arrowstyle="->", linestyle="--", color=CLR_PURPLE, lw=1.1),
                fontsize=6.8, weight="bold", color=CLR_PURPLE)

    ax.annotate("«include»", xy=(0.50, 0.41), xytext=(0.65, 0.48),
                arrowprops=dict(arrowstyle="->", linestyle="--", color="#dc2626", lw=1.1),
                fontsize=6.8, weight="bold", color="#dc2626")

    # Connect Gemini Actor to UC10
    ax.plot([0.89, 0.77], [0.22, 0.50], color=CLR_PURPLE, lw=1.2, linestyle="-", zorder=3)

    # Connect SQLite Actor to UC9 & UC15
    ax.plot([0.11, 0.23], [0.22, 0.50], color="#0f766e", lw=1.2, linestyle="-", zorder=3)
    ax.plot([0.11, 0.23], [0.22, 0.14], color="#0f766e", lw=1.2, linestyle="-", zorder=3)

    # Legend / Specification Box
    ax.text(0.50, 0.03, "UML 2.5 Package Conventions: Solid Lines = Actor Association Links • Dashed Arrows = Stereotyped Dependencies («include», «extend»)",
            ha="center", va="center", fontsize=7.2, color=CLR_SLATE)

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_use_case.png"), bbox_inches="tight")
    plt.close()
    print("[2/8] Generated Unique Package-Based Use Case Diagram: campusai_use_case.png")

create_packaged_use_case_diagram()


# ==============================================================================
# 3. ENTERPRISE LAYERED ARCHITECTURE CLASS DIAGRAM
# (Clean 4-tier layer structure: Controller, Service, Domain, Repository)
# ==============================================================================
def create_layered_class_diagram():
    fig, ax = plt.subplots(figsize=(10.5, 11.5), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.text(0.5, 0.985, "CampusAI Enterprise Layered Class Architecture (MVC & Service Layer)",
            ha="center", va="center", fontsize=11.5, weight="bold", color=CLR_EMERALD_DARK)
    ax.text(0.5, 0.965, "Object-Oriented Design • Controller Layer, Service Engine, Domain Models, and Persistence Adapters",
            ha="center", va="center", fontsize=8.0, color=CLR_SLATE)

    def draw_class(x, y, w, title, stereotype, attributes, methods, border_clr=CLR_EMERALD_DARK, hdr_clr=CLR_EMERALD_LIGHT):
        line_h = 0.015
        h_title = 0.034
        h_attr = max(0.025, len(attributes) * line_h + 0.010)
        h_meth = max(0.025, len(methods) * line_h + 0.010)
        total_h = h_title + h_attr + h_meth

        # Outer Box
        card = patches.Rectangle((x, y - total_h), w, total_h, facecolor=CLR_WHITE, edgecolor=border_clr, lw=1.2, zorder=3)
        ax.add_patch(card)

        # Header Box
        hdr = patches.Rectangle((x, y - h_title), w, h_title, facecolor=hdr_clr, edgecolor=border_clr, lw=1.0, zorder=4)
        ax.add_patch(hdr)
        if stereotype:
            ax.text(x + w/2, y - 0.011, f"«{stereotype}»", ha="center", va="center", fontsize=6.2, color="#475569", zorder=5)
            ax.text(x + w/2, y - 0.024, title, ha="center", va="center", fontsize=7.8, weight="bold", color=CLR_SLATE_DARK, zorder=5)
        else:
            ax.text(x + w/2, y - h_title/2, title, ha="center", va="center", fontsize=8.0, weight="bold", color=CLR_SLATE_DARK, zorder=5)

        # Attributes
        curr_y = y - h_title - 0.010
        for a in attributes:
            ax.text(x + 0.008, curr_y, a, fontsize=6.5, family="monospace", color=CLR_SLATE_DARK, zorder=5)
            curr_y -= line_h

        # Method Divider
        div_y = y - h_title - h_attr
        ax.plot([x, x + w], [div_y, div_y], color=border_clr, lw=0.9, zorder=4)

        # Methods
        curr_y = div_y - 0.010
        for m in methods:
            ax.text(x + 0.008, curr_y, m, fontsize=6.5, family="monospace", color=CLR_SLATE_DARK, zorder=5)
            curr_y -= line_h

        return total_h

    # LAYER 1: CONTROLLER LAYER (Top)
    ax.text(0.04, 0.940, "LAYER 1: CONTROLLERS & REST APIS", fontsize=7.5, weight="bold", color=CLR_EMERALD_DARK)
    draw_class(0.04, 0.925, 0.44, "ChatbotAPIController", "Flask REST Endpoint",
               ["- route : str = '/api/chat'", "- session_cookie : str"],
               ["+ post_message(query: str) : JSON", "+ clear_conversation() : JSON", "+ get_health_status() : JSON"],
               border_clr=CLR_EMERALD_DARK, hdr_clr=CLR_EMERALD_LIGHT)

    draw_class(0.52, 0.925, 0.44, "AdminPortalController", "Flask Security Blueprint",
               ["- route_prefix : str = '/admin'", "- auth_required : bool = True"],
               ["+ authenticate(user, pwd) : bool", "+ manage_faqs(crud_action) : void", "+ export_telemetry_csv() : File"],
               border_clr="#1e3a8a", hdr_clr="#eff6ff")

    # LAYER 2: SERVICE & AI ENGINE LAYER (Middle)
    ax.text(0.04, 0.720, "LAYER 2: BUSINESS LOGIC & AI SERVICES", fontsize=7.5, weight="bold", color=CLR_EMERALD_DARK)
    draw_class(0.04, 0.705, 0.44, "DualTierNLPEngine", "Service Facade",
               ["- similarity_threshold : float = 0.45", "- stop_words : Set[str]", "- domain_synonyms : Dict[str, list]"],
               ["+ tokenize_and_clean(q: str) : Set[str]", "+ compute_jaccard(s1, s2) : float", "+ match_verified_faq(q) : FAQMatchResult"],
               border_clr="#0f766e", hdr_clr="#ccfbf1")

    draw_class(0.52, 0.705, 0.44, "GeminiGenAIService", "Cloud LLM Adapter",
               ["- model_name : str = 'gemini-2.5-flash'", "- api_key_secure : str", "- grounding_context : str"],
               ["+ synthesize_bounded_reply(q, ctx) : str", "+ enforce_zero_hallucination() : bool", "+ ping_service_health() : bool"],
               border_clr=CLR_PURPLE, hdr_clr=CLR_PURPLE_LIGHT)

    # LAYER 3: DOMAIN ENTITIES & MODELS (Lower Middle)
    ax.text(0.04, 0.460, "LAYER 3: RELATIONAL DOMAIN ENTITIES (ORM)", fontsize=7.5, weight="bold", color=CLR_EMERALD_DARK)
    draw_class(0.04, 0.445, 0.28, "FAQKnowledgeBase", "SQLAlchemy Model",
               ["- id : Integer [PK]", "- category_id : Integer [FK]", "- question : Text", "- answer : Text", "- keywords : String"],
               ["+ to_json_dict() : dict", "+ update_timestamp() : void"],
               border_clr=CLR_SLATE, hdr_clr=CLR_SLATE_LIGHT)

    draw_class(0.36, 0.445, 0.28, "ChatMessageRecord", "SQLAlchemy Model",
               ["- id : Integer [PK]", "- session_id : String(64) [FK]", "- role : String(20)", "- content : Text", "- source : String(30)"],
               ["+ to_audit_row() : list", "+ get_turn_latency() : float"],
               border_clr=CLR_SLATE, hdr_clr=CLR_SLATE_LIGHT)

    draw_class(0.68, 0.445, 0.28, "AdminAccount", "SQLAlchemy Model",
               ["- id : Integer [PK]", "- username : String(80)", "- password_hash : String", "- role : String(30)"],
               ["+ verify_hash(pwd: str) : bool", "+ hash_pbkdf2(pwd: str) : void"],
               border_clr=CLR_SLATE, hdr_clr=CLR_SLATE_LIGHT)

    # LAYER 4: DATA ACCESS & INFRASTRUCTURE (Bottom)
    ax.text(0.04, 0.210, "LAYER 4: REPOSITORY & INFRASTRUCTURE LAYER", fontsize=7.5, weight="bold", color=CLR_EMERALD_DARK)
    draw_class(0.04, 0.195, 0.44, "SQLiteRepositoryManager", "Data Access Object",
               ["- db_uri : str = 'sqlite:///campusai.db'", "- engine : SQLAlchemyEngine", "- connection_pool : Pool"],
               ["+ execute_query(sql, params) : Result", "+ commit_transaction() : void", "+ rollback_on_error() : void"],
               border_clr="#0f172a", hdr_clr="#f1f5f9")

    draw_class(0.52, 0.195, 0.44, "WebSpeechAudioAdapter", "Client Accessibility Bridge",
               ["- stt_engine : WebSpeechRecognition", "- tts_synthesizer : SpeechSynthesis", "- voice_lang : str = 'en-IN'"],
               ["+ start_mic_stream() : void", "+ read_aloud(text: str) : void", "+ toggle_listening_indicator() : void"],
               border_clr=CLR_AMBER_DARK, hdr_clr=CLR_AMBER_LIGHT)

    # Architectural Dependency Links
    ax.annotate("delegates", xy=(0.26, 0.705), xytext=(0.26, 0.78),
                arrowprops=dict(arrowstyle="->", lw=1.2, color=CLR_EMERALD_DARK), fontsize=6.8, color=CLR_EMERALD_DARK)
    ax.annotate("delegates", xy=(0.74, 0.705), xytext=(0.74, 0.78),
                arrowprops=dict(arrowstyle="->", lw=1.2, color="#1e3a8a"), fontsize=6.8, color="#1e3a8a")

    ax.annotate("queries / updates", xy=(0.18, 0.445), xytext=(0.18, 0.53),
                arrowprops=dict(arrowstyle="->", lw=1.2, color="#0f766e"), fontsize=6.8, color="#0f766e")
    ax.annotate("persists", xy=(0.50, 0.445), xytext=(0.30, 0.53),
                arrowprops=dict(arrowstyle="->", lw=1.2, color="#0f766e"), fontsize=6.8, color="#0f766e")

    # Legend at bottom
    ax.text(0.50, 0.02, "Architectural Pattern: Enterprise Domain-Driven Design (DDD) with Strict Clean Layer Separation & Facade Pattern",
            ha="center", va="center", fontsize=7.2, color=CLR_SLATE)

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_class_diagram.png"), bbox_inches="tight")
    plt.close()
    print("[3/8] Generated Unique Enterprise Layered Class Diagram: campusai_class_diagram.png")

create_layered_class_diagram()


# ==============================================================================
# 4. RUNTIME MEMORY HEAP SNAPSHOT OBJECT DIAGRAM
# (Complete with real runtime values, pointers, confidence vectors!)
# ==============================================================================
def create_heap_snapshot_object_diagram():
    fig, ax = plt.subplots(figsize=(10.5, 11.0), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.text(0.5, 0.980, "CampusAI Runtime Memory Heap Object Diagram",
            ha="center", va="center", fontsize=11.5, weight="bold", color=CLR_EMERALD_DARK)
    ax.text(0.5, 0.958, "Concrete Runtime State during an Active Multi-Turn Student Academic Inquiry Session",
            ha="center", va="center", fontsize=8.0, color=CLR_SLATE)

    def draw_object(x, y, w, inst_name, class_name, slot_dict, border_clr=CLR_EMERALD_DARK, bg_clr="#f0fdf4"):
        line_h = 0.016
        h_title = 0.034
        total_h = h_title + len(slot_dict) * line_h + 0.012

        card = patches.Rectangle((x, y - total_h), w, total_h, facecolor=CLR_WHITE, edgecolor=border_clr, lw=1.2, zorder=3)
        ax.add_patch(card)

        hdr = patches.Rectangle((x, y - h_title), w, h_title, facecolor=bg_clr, edgecolor=border_clr, lw=1.0, zorder=4)
        ax.add_patch(hdr)

        full_title = f"{inst_name} : {class_name}"
        ax.text(x + w/2, y - h_title/2, full_title, ha="center", va="center", fontsize=7.5, weight="bold", color=CLR_SLATE_DARK, zorder=5)
        # Underline
        t_w = len(full_title) * 0.0042
        ax.plot([x + w/2 - t_w, x + w/2 + t_w], [y - h_title*0.75, y - h_title*0.75], color=CLR_SLATE_DARK, lw=1.0, zorder=5)

        curr_y = y - h_title - 0.010
        for slot, val in slot_dict.items():
            ax.text(x + 0.010, curr_y, f"{slot} = {val}", fontsize=6.8, family="monospace", color=CLR_SLATE_DARK, zorder=5)
            curr_y -= line_h

        return total_h

    # Object 1: currentStudentSession
    draw_object(0.04, 0.92, 0.44, "currentSession", "ChatSession", {
        "session_uuid": "\"sess_istu_2026_9b81f4a\"",
        "client_ip": "\"192.168.1.104\"",
        "started_at": "\"2026-10-27 10:14:02 IST\"",
        "total_queries_in_session": "4",
        "current_state": "\"ACTIVE_CONVERSATION\""
    }, border_clr=CLR_EMERALD_DARK, bg_clr=CLR_EMERALD_LIGHT)

    # Object 2: currentAdminSession
    draw_object(0.52, 0.92, 0.44, "activeAdmin", "AdminAccount", {
        "admin_id": "1",
        "username": "\"akash_admin\"",
        "email": "\"akash.rana@istu.ac.in\"",
        "role": "\"Chief Knowledge Administrator\"",
        "auth_token": "\"jwt_sha256_9182ab3c4...\""
    }, border_clr="#1e3a8a", bg_clr="#eff6ff")

    # Object 3: rawInquiryMessage
    draw_object(0.04, 0.68, 0.44, "inquiryMsg", "ChatMessageRecord", {
        "message_id": "101",
        "session_id": "\"sess_istu_2026_9b81f4a\"",
        "role": "\"student\"",
        "content": "\"What are the BBA CA admission eligibility criteria?\"",
        "input_modality": "\"VOICE_STT_MICROPHONE\"",
        "received_timestamp": "\"2026-10-27 10:14:05.120\""
    }, border_clr="#0f766e", bg_clr="#ccfbf1")

    # Object 4: activeNLPTokenizer
    draw_object(0.52, 0.68, 0.44, "nlpTokenizer", "DualTierNLPEngine", {
        "raw_tokens": "['what', 'are', 'bba', 'ca', 'eligibility']",
        "pruned_tokens": "['bba', 'ca', 'eligibility', 'admission']",
        "synonym_expanded": "['criteria', 'qualification', '12th', 'hsc']",
        "target_category": "\"Admissions\""
    }, border_clr=CLR_AMBER_DARK, bg_clr=CLR_AMBER_LIGHT)

    # Object 5: matchedFAQEntity
    draw_object(0.04, 0.44, 0.44, "matchedFaq", "FAQKnowledgeBase", {
        "faq_id": "2",
        "category": "\"Admissions\"",
        "question": "\"How do I apply for admissions to BBA CA?\"",
        "answer": "\"HSC 12th pass with minimum 45% aggregate...\"",
        "verified_by_guide": "\"Prof. Sheela Satav\""
    }, border_clr=CLR_EMERALD_DARK, bg_clr=CLR_EMERALD_LIGHT)

    # Object 6: assistantResponseTurn
    draw_object(0.52, 0.44, 0.44, "assistantReply", "ChatMessageRecord", {
        "message_id": "102",
        "session_id": "\"sess_istu_2026_9b81f4a\"",
        "role": "\"assistant\"",
        "source_tier": "\"TIER_1_SQLITE_VERIFIED\"",
        "similarity_score": "0.885",
        "latency_ms": "11.4 ms",
        "student_feedback": "\"THUMBS_UP (+1)\""
    }, border_clr="#0284c7", bg_clr="#e0f2fe")

    # Object 7: systemHealthTelemetry
    draw_object(0.04, 0.20, 0.92, "liveTelemetryMonitor", "TelemetryDiagnostics", {
        "database_status": "\"HEALTHY (sqlite3 - instance/campusai.db)\"",
        "active_faqs_count": "26",
        "knowledge_domains": "8 (Admissions, Fees, Exams, Courses, Placements, Scholarships, Hostels, Helpdesk)",
        "gemini_api_connection": "\"ONLINE (Google AI Studio gemini-2.5-flash)\"",
        "zero_hallucination_guard": "\"ACTIVE (Strict Grounding Context Enabled)\""
    }, border_clr="#4338ca", bg_clr="#eef2ff")

    # Object Link Connectors
    ax.annotate("«originates_from»", xy=(0.26, 0.68), xytext=(0.26, 0.74),
                arrowprops=dict(arrowstyle="->", lw=1.2, color=CLR_EMERALD_DARK), fontsize=6.8, color=CLR_EMERALD_DARK)
    ax.annotate("«tokenized_by»", xy=(0.52, 0.58), xytext=(0.48, 0.58),
                arrowprops=dict(arrowstyle="->", lw=1.2, color=CLR_AMBER_DARK), fontsize=6.8, color=CLR_AMBER_DARK)
    ax.annotate("«retrieved_from»", xy=(0.48, 0.35), xytext=(0.52, 0.35),
                arrowprops=dict(arrowstyle="->", lw=1.2, color=CLR_EMERALD_DARK), fontsize=6.8, color=CLR_EMERALD_DARK)

    # Bottom Note
    ax.text(0.50, 0.02, "Runtime Semantics: Underlined titles designate concrete instances • Arrows indicate pointer references in execution heap",
            ha="center", va="center", fontsize=7.2, color=CLR_SLATE)

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_object_diagram.png"), bbox_inches="tight")
    plt.close()
    print("[4/8] Generated Unique Runtime Heap Snapshot Object Diagram: campusai_object_diagram.png")

create_heap_snapshot_object_diagram()


# ==============================================================================
# 5. ADVANCED COMBINED FRAGMENT UML 2.5 SEQUENCE DIAGRAM
# (Features alt [Tier 1 vs Tier 2], opt [Speech], and loop frames!)
# ==============================================================================
def create_combined_fragment_sequence_diagram():
    fig, ax = plt.subplots(figsize=(10.5, 11.5), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.text(0.5, 0.985, "UML 2.5 Sequence Diagram: Dual-Tier Query Routing with Combined Fragments",
            ha="center", va="center", fontsize=11.5, weight="bold", color=CLR_EMERALD_DARK)
    ax.text(0.5, 0.965, "Execution Lifelines, Asynchronous Signals, and UML 2.5 Combined Fragment Frames (alt, opt)",
            ha="center", va="center", fontsize=8.0, color=CLR_SLATE)

    # 5 Lifelines
    lifelines = [
        (0.10, "Student (UI)\n«Client View»", CLR_EMERALD_LIGHT, CLR_EMERALD_DARK),
        (0.32, "Flask Router\n«Controller»", "#f1f5f9", CLR_SLATE_DARK),
        (0.54, "NLP Matcher\n«Local Engine»", CLR_AMBER_LIGHT, CLR_AMBER_DARK),
        (0.74, "SQLite DB\n«3NF Store»", "#eff6ff", "#1e3a8a"),
        (0.92, "Gemini Cloud\n«GenAI API»", CLR_PURPLE_LIGHT, CLR_PURPLE)
    ]

    for x, label, bg, border in lifelines:
        rect = patches.Rectangle((x - 0.07, 0.90), 0.14, 0.045, facecolor=bg, edgecolor=border, lw=1.2, zorder=3)
        ax.add_patch(rect)
        ax.text(x, 0.922, label, ha="center", va="center", fontsize=7.0, weight="bold", color=CLR_SLATE_DARK, zorder=4)
        # Vertical dashed lifeline
        ax.plot([x, x], [0.08, 0.90], color="#94a3b8", linestyle="--", lw=1.0, zorder=1)

    def draw_activation(x, y_top, y_bot, color="#cbd5e1"):
        rect = patches.Rectangle((x - 0.009, y_bot), 0.018, y_top - y_bot, facecolor=color, edgecolor="#475569", lw=0.9, zorder=2)
        ax.add_patch(rect)

    draw_activation(0.10, 0.88, 0.10, color=CLR_EMERALD_LIGHT)
    draw_activation(0.32, 0.86, 0.14, color="#e2e8f0")
    draw_activation(0.54, 0.84, 0.60, color=CLR_AMBER_LIGHT)
    draw_activation(0.74, 0.82, 0.40, color="#bfdbfe")
    draw_activation(0.92, 0.50, 0.35, color=CLR_PURPLE_LIGHT)

    # Initial Message
    ax.annotate("1. Type Query / Voice STT", xy=(0.32, 0.86), xytext=(0.10, 0.86),
                arrowprops=dict(arrowstyle="->", lw=1.2, color=CLR_SLATE_DARK), fontsize=6.8, weight="bold")
    ax.annotate("2. Delegate NLP Tokenization", xy=(0.54, 0.83), xytext=(0.32, 0.83),
                arrowprops=dict(arrowstyle="->", lw=1.1, color=CLR_SLATE_DARK), fontsize=6.5)
    ax.annotate("3. Fetch 26 Seeded FAQs Corpus", xy=(0.74, 0.80), xytext=(0.54, 0.80),
                arrowprops=dict(arrowstyle="->", lw=1.1, color=CLR_BLUE), fontsize=6.5, color=CLR_BLUE)
    ax.annotate("4. Return FAQs Token Stream", xy=(0.54, 0.77), xytext=(0.74, 0.77),
                arrowprops=dict(arrowstyle="->", linestyle="--", lw=1.1, color=CLR_BLUE), fontsize=6.5, color=CLR_BLUE)
    ax.annotate("5. Calculate Jaccard Similarity Score (S)", xy=(0.54, 0.74), xytext=(0.54, 0.74),
                ha="center", fontsize=6.5, color=CLR_AMBER_DARK, weight="bold")

    # COMBINED FRAGMENT 1: alt (Alternative Evaluation)
    alt_rect = patches.Rectangle((0.04, 0.30), 0.92, 0.42, facecolor="#fafafa", edgecolor="#0284c7", lw=1.4, zorder=1)
    ax.add_patch(alt_rect)
    # Tag
    tag_tab = patches.Rectangle((0.04, 0.69), 0.08, 0.03, facecolor="#0284c7", edgecolor="#0284c7", lw=1.0, zorder=2)
    ax.add_patch(tag_tab)
    ax.text(0.08, 0.705, "alt", ha="center", va="center", fontsize=7.5, weight="bold", color=CLR_WHITE, zorder=3)

    # Frame 1: [Score S >= 0.45: Tier 1 Direct SQLite Match]
    ax.text(0.14, 0.695, "[Score S >= 0.45 : Tier-1 Deterministic SQLite Match (<15ms)]", fontsize=7.2, weight="bold", color=CLR_EMERALD_DARK)
    ax.annotate("6. Return Verified FAQ Record (Score = 0.88)", xy=(0.32, 0.66), xytext=(0.54, 0.66),
                arrowprops=dict(arrowstyle="->", linestyle="--", lw=1.2, color=CLR_EMERALD_DARK), fontsize=6.8, color=CLR_EMERALD_DARK, weight="bold")
    ax.annotate("7. Render Verified Bubble + Category Badge", xy=(0.10, 0.63), xytext=(0.32, 0.63),
                arrowprops=dict(arrowstyle="->", linestyle="--", lw=1.2, color=CLR_EMERALD_DARK), fontsize=6.8, color=CLR_EMERALD_DARK, weight="bold")

    # Divider line
    ax.plot([0.04, 0.96], [0.58, 0.58], color="#0284c7", linestyle="-.", lw=1.2, zorder=2)

    # Frame 2: [Score S < 0.45: Tier 2 Gemini Cloud Fallback]
    ax.text(0.14, 0.555, "[Score S < 0.45 : Tier-2 Context-Bounded Gemini 2.5 Flash GenAI]", fontsize=7.2, weight="bold", color=CLR_PURPLE)
    ax.annotate("8. Invoke Gemini API (Strict Grounded Context)", xy=(0.92, 0.50), xytext=(0.32, 0.50),
                arrowprops=dict(arrowstyle="->", lw=1.2, color=CLR_PURPLE), fontsize=6.8, color=CLR_PURPLE, weight="bold")
    ax.annotate("9. Return Zero-Hallucination Synthesized Answer", xy=(0.32, 0.45), xytext=(0.92, 0.45),
                arrowprops=dict(arrowstyle="->", linestyle="--", lw=1.2, color=CLR_PURPLE), fontsize=6.8, color=CLR_PURPLE, weight="bold")
    ax.annotate("10. Render AI Response + Confidence Telemetry", xy=(0.10, 0.41), xytext=(0.32, 0.41),
                arrowprops=dict(arrowstyle="->", linestyle="--", lw=1.2, color=CLR_PURPLE), fontsize=6.8, color=CLR_PURPLE, weight="bold")

    # Divider line 2
    ax.plot([0.04, 0.96], [0.37, 0.37], color="#0284c7", linestyle="-.", lw=1.2, zorder=2)

    # Frame 3: [API Disconnected / Fallback]
    ax.text(0.14, 0.345, "[Offline / Disconnected : Tier-3 Institutional Helpdesk Referral]", fontsize=7.2, weight="bold", color="#b91c1c")
    ax.annotate("11. Return Office Directory (contact@college.edu)", xy=(0.10, 0.31), xytext=(0.32, 0.31),
                arrowprops=dict(arrowstyle="->", linestyle="--", lw=1.2, color="#b91c1c"), fontsize=6.8, color="#b91c1c")

    # COMBINED FRAGMENT 2: opt (Speech Output)
    opt_rect = patches.Rectangle((0.04, 0.17), 0.92, 0.10, facecolor="#fefce8", edgecolor=CLR_AMBER, lw=1.2, zorder=1)
    ax.add_patch(opt_rect)
    opt_tab = patches.Rectangle((0.04, 0.24), 0.08, 0.03, facecolor=CLR_AMBER, edgecolor=CLR_AMBER, lw=1.0, zorder=2)
    ax.add_patch(opt_tab)
    ax.text(0.08, 0.255, "opt", ha="center", va="center", fontsize=7.5, weight="bold", color=CLR_WHITE, zorder=3)
    ax.text(0.14, 0.245, "[Student Clicks 'Listen' (Audio TTS Requested)]", fontsize=7.2, weight="bold", color=CLR_AMBER_DARK)
    ax.annotate("12. Trigger Web Speech API SpeechSynthesis", xy=(0.10, 0.20), xytext=(0.10, 0.20),
                ha="left", fontsize=6.8, color=CLR_AMBER_DARK, weight="bold")

    # Final Turn Persistence
    ax.annotate("13. Persist Turn to chat_messages", xy=(0.74, 0.13), xytext=(0.32, 0.13),
                arrowprops=dict(arrowstyle="->", lw=1.2, color=CLR_SLATE_DARK), fontsize=6.8, weight="bold")
    ax.annotate("14. Student Submits Feedback (+1 / -1)", xy=(0.32, 0.09), xytext=(0.10, 0.09),
                arrowprops=dict(arrowstyle="->", lw=1.2, color=CLR_EMERALD_DARK), fontsize=6.8, color=CLR_EMERALD_DARK, weight="bold")

    ax.text(0.50, 0.02, "UML 2.5 Sequence Combined Fragment Notation: alt = Mutually Exclusive Alternative Execution Paths • opt = Optional Interaction",
            ha="center", va="center", fontsize=7.2, color=CLR_SLATE)

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_sequence_diagram.png"), bbox_inches="tight")
    plt.close()
    print("[5/8] Generated Unique Combined Fragment Sequence Diagram: campusai_sequence_diagram.png")

create_combined_fragment_sequence_diagram()


# ==============================================================================
# 6. HORIZONTAL PIPELINE ACTIVITY DIAGRAM WITH FORK & JOIN BARS
# (Completely distinct layout from 3 vertical columns!)
# ==============================================================================
def create_pipeline_activity_diagram():
    fig, ax = plt.subplots(figsize=(10.5, 11.5), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.text(0.5, 0.985, "CampusAI Multi-Stage Activity Pipeline with Fork / Join Concurrency",
            ha="center", va="center", fontsize=11.5, weight="bold", color=CLR_EMERALD_DARK)
    ax.text(0.5, 0.965, "UML 2.5 Activity Specification • Parallel Preprocessing, Decision Guards, and Exception Handlers",
            ha="center", va="center", fontsize=8.0, color=CLR_SLATE)

    def draw_activity_box(cx, cy, w, h, text, bg=CLR_WHITE, border=CLR_EMERALD):
        box = patches.FancyBboxPatch((cx - w/2, cy - h/2), w, h,
                                     boxstyle="round,pad=0.015,rounding_size=0.015",
                                     facecolor=bg, edgecolor=border, lw=1.2, zorder=3)
        ax.add_patch(box)
        ax.text(cx, cy, text, ha="center", va="center", fontsize=7.0, color=CLR_SLATE_DARK, zorder=4)

    # 4 STAGE BANNERS (Vertical Columns)
    stages = [
        (0.04, 0.21, "STAGE 1: INGESTION", CLR_EMERALD_LIGHT, CLR_EMERALD),
        (0.27, 0.22, "STAGE 2: NLP PARALLEL FORK", CLR_AMBER_LIGHT, CLR_AMBER),
        (0.51, 0.25, "STAGE 3: DUAL-TIER ROUTING", "#eef2ff", "#6366f1"),
        (0.78, 0.18, "STAGE 4: PRESENTATION", CLR_BLUE_LIGHT, CLR_BLUE)
    ]
    for x, w, label, bg, border in stages:
        rect = patches.Rectangle((x, 0.06), w, 0.88, facecolor=bg, edgecolor=border, lw=1.1, zorder=1)
        ax.add_patch(rect)
        hdr = patches.Rectangle((x, 0.91), w, 0.03, facecolor=border, edgecolor=border, lw=1.0, zorder=2)
        ax.add_patch(hdr)
        ax.text(x + w/2, 0.925, label, ha="center", va="center", fontsize=7.2, weight="bold", color=CLR_WHITE, zorder=3)

    # Stage 1: Ingestion
    start = Circle((0.145, 0.86), 0.014, facecolor=CLR_BLACK, edgecolor=CLR_BLACK, zorder=4)
    ax.add_patch(start)
    ax.text(0.145, 0.88, "Start", ha="center", fontsize=6.8, color="#64748b")

    ax.annotate("", xy=(0.145, 0.80), xytext=(0.145, 0.84), arrowprops=dict(arrowstyle="->", lw=1.2))
    draw_activity_box(0.145, 0.77, 0.18, 0.045, "Student Submits Query\n(Text Box / Mic Button)", border=CLR_EMERALD)

    ax.annotate("", xy=(0.145, 0.69), xytext=(0.145, 0.74), arrowprops=dict(arrowstyle="->", lw=1.2))
    draw_activity_box(0.145, 0.66, 0.18, 0.045, "Validate Input & Extract\nSession UUID Cookie", border=CLR_EMERALD)

    # Transition to Stage 2: FORK BAR (Heavy black bar)
    ax.annotate("", xy=(0.29, 0.66), xytext=(0.235, 0.66), arrowprops=dict(arrowstyle="->", lw=1.2))
    fork_bar = patches.Rectangle((0.29, 0.50), 0.012, 0.32, facecolor=CLR_BLACK, edgecolor=CLR_BLACK, zorder=5)
    ax.add_patch(fork_bar)
    ax.text(0.296, 0.83, "FORK", ha="center", fontsize=6.5, weight="bold", color=CLR_SLATE)

    # Parallel Branch 1: Normalization
    ax.annotate("", xy=(0.33, 0.76), xytext=(0.302, 0.76), arrowprops=dict(arrowstyle="->", lw=1.2))
    draw_activity_box(0.38, 0.76, 0.14, 0.045, "Tokenize & Strip\nDomain Stopwords", border=CLR_AMBER)

    # Parallel Branch 2: Synonym Expansion
    ax.annotate("", xy=(0.33, 0.56), xytext=(0.302, 0.56), arrowprops=dict(arrowstyle="->", lw=1.2))
    draw_activity_box(0.38, 0.56, 0.14, 0.045, "Expand Academic\nDomain Synonyms", border=CLR_AMBER)

    # JOIN BAR (Heavy black bar)
    join_bar = patches.Rectangle((0.465, 0.50), 0.012, 0.32, facecolor=CLR_BLACK, edgecolor=CLR_BLACK, zorder=5)
    ax.add_patch(join_bar)
    ax.annotate("", xy=(0.465, 0.76), xytext=(0.45, 0.76), arrowprops=dict(arrowstyle="->", lw=1.2))
    ax.annotate("", xy=(0.465, 0.56), xytext=(0.45, 0.56), arrowprops=dict(arrowstyle="->", lw=1.2))
    ax.text(0.471, 0.83, "JOIN", ha="center", fontsize=6.5, weight="bold", color=CLR_SLATE)

    # Transition to Stage 3: Jaccard Calculation
    ax.annotate("", xy=(0.53, 0.66), xytext=(0.477, 0.66), arrowprops=dict(arrowstyle="->", lw=1.2))
    draw_activity_box(0.635, 0.66, 0.20, 0.045, "Compute Jaccard Score\nAgainst 26 SQLite FAQs", border="#6366f1")

    # Decision Diamond: S >= 0.45?
    ax.annotate("", xy=(0.635, 0.57), xytext=(0.635, 0.635), arrowprops=dict(arrowstyle="->", lw=1.2))
    dia1 = Polygon([[0.635, 0.55], [0.70, 0.52], [0.635, 0.49], [0.57, 0.52]], closed=True,
                   facecolor=CLR_AMBER_LIGHT, edgecolor=CLR_AMBER, lw=1.2, zorder=4)
    ax.add_patch(dia1)
    ax.text(0.635, 0.52, "Score\nS >= 0.45 ?", ha="center", va="center", fontsize=6.8, weight="bold")

    # Branch YES: Fetch DB Answer
    ax.annotate("[YES]", xy=(0.80, 0.52), xytext=(0.70, 0.52),
                arrowprops=dict(arrowstyle="->", lw=1.2, color=CLR_EMERALD), fontsize=6.8, weight="bold", color=CLR_EMERALD)

    # Branch NO: Gemini API Check
    ax.annotate("[NO]", xy=(0.635, 0.42), xytext=(0.635, 0.49),
                arrowprops=dict(arrowstyle="->", lw=1.2, color="#dc2626"), fontsize=6.8, weight="bold", color="#dc2626")

    draw_activity_box(0.635, 0.38, 0.20, 0.045, "Invoke Gemini 2.5 Flash\n(Strict Grounded Prompt)", border=CLR_PURPLE, bg=CLR_PURPLE_LIGHT)

    # Merge Diamond in Stage 3
    dia2 = Polygon([[0.635, 0.26], [0.68, 0.23], [0.635, 0.20], [0.59, 0.23]], closed=True,
                   facecolor="#cbd5e1", edgecolor=CLR_SLATE, lw=1.1, zorder=4)
    ax.add_patch(dia2)
    ax.annotate("", xy=(0.635, 0.26), xytext=(0.635, 0.355), arrowprops=dict(arrowstyle="->", lw=1.2))

    # Stage 4: Presentation
    draw_activity_box(0.87, 0.52, 0.15, 0.045, "Format Response Bubble\nwith Category Badge", border=CLR_BLUE)
    ax.plot([0.68, 0.74, 0.74, 0.87], [0.23, 0.23, 0.45, 0.495], color=CLR_SLATE_DARK, lw=1.1)

    ax.annotate("", xy=(0.87, 0.43), xytext=(0.87, 0.495), arrowprops=dict(arrowstyle="->", lw=1.2))
    draw_activity_box(0.87, 0.40, 0.15, 0.045, "Persist Conversation\nto SQLite chat_messages", border=CLR_BLUE)

    ax.annotate("", xy=(0.87, 0.31), xytext=(0.87, 0.375), arrowprops=dict(arrowstyle="->", lw=1.2))
    draw_activity_box(0.87, 0.28, 0.15, 0.045, "Synthesize Web Speech\nAudio (If Requested)", border=CLR_AMBER)

    ax.annotate("", xy=(0.87, 0.19), xytext=(0.87, 0.255), arrowprops=dict(arrowstyle="->", lw=1.2))
    draw_activity_box(0.87, 0.16, 0.15, 0.045, "Await User Feedback\n(Thumbs Up / Down)", border=CLR_EMERALD)

    # Bullseye End Node
    ax.annotate("", xy=(0.87, 0.10), xytext=(0.87, 0.135), arrowprops=dict(arrowstyle="->", lw=1.2))
    end_outer = Circle((0.87, 0.085), 0.015, facecolor=CLR_WHITE, edgecolor=CLR_BLACK, lw=1.5, zorder=5)
    end_inner = Circle((0.87, 0.085), 0.009, facecolor=CLR_BLACK, edgecolor=CLR_BLACK, zorder=6)
    ax.add_patch(end_outer)
    ax.add_patch(end_inner)
    ax.text(0.87, 0.065, "End", ha="center", fontsize=6.8, color="#64748b")

    ax.text(0.50, 0.02, "UML 2.5 Activity Notation: FORK / JOIN Bars represent concurrent task execution • Decision Diamonds evaluate runtime guards",
            ha="center", va="center", fontsize=7.2, color=CLR_SLATE)

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_activity_diagram.png"), bbox_inches="tight")
    plt.close()
    print("[6/8] Generated Unique Fork/Join Pipeline Activity Diagram: campusai_activity_diagram.png")

create_pipeline_activity_diagram()


# ==============================================================================
# 7. HEXAGONAL / CLEAN ARCHITECTURE COMPONENT DIAGRAM
# (With formal Ports & Interfaces: Lollipop and Socket Notation!)
# ==============================================================================
def create_hexagonal_component_diagram():
    fig, ax = plt.subplots(figsize=(10.5, 11.5), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.text(0.5, 0.985, "CampusAI Component Architecture: Hexagonal Modular Topology",
            ha="center", va="center", fontsize=11.5, weight="bold", color=CLR_EMERALD_DARK)
    ax.text(0.5, 0.965, "UML 2.5 Component Specification • Subsystem Boundaries, Ports, Provided (Lollipop) and Required (Socket) Interfaces",
            ha="center", va="center", fontsize=8.0, color=CLR_SLATE)

    def draw_component(x, y, w, h, name, tech, border_clr=CLR_EMERALD_DARK, bg_clr=CLR_WHITE):
        card = patches.Rectangle((x, y), w, h, facecolor=bg_clr, edgecolor=border_clr, lw=1.3, zorder=2)
        ax.add_patch(card)
        # Component icon tabs
        t1 = patches.Rectangle((x - 0.012, y + h - 0.022), 0.018, 0.012, facecolor="#e0e7ff", edgecolor=border_clr, lw=1.0, zorder=3)
        t2 = patches.Rectangle((x - 0.012, y + 0.010), 0.018, 0.012, facecolor="#e0e7ff", edgecolor=border_clr, lw=1.0, zorder=3)
        ax.add_patch(t1)
        ax.add_patch(t2)
        ax.text(x + w/2, y + h/2 + 0.010, f"«component»\n{name}", ha="center", va="center", fontsize=7.5, weight="bold", color=CLR_SLATE_DARK, zorder=4)
        ax.text(x + w/2, y + h/2 - 0.016, tech, ha="center", va="center", fontsize=6.5, color="#64748b", zorder=4)

    # SUBSYSTEM 1: CLIENT PRESENTATION SUBSYSTEM (Top)
    p1 = patches.Rectangle((0.05, 0.70), 0.90, 0.23, facecolor=CLR_EMERALD_LIGHT, edgecolor=CLR_EMERALD, lw=1.2, zorder=1)
    ax.add_patch(p1)
    ax.text(0.07, 0.905, "CLIENT PRESENTATION TIER (Responsive Web Application)", fontsize=8.0, weight="bold", color=CLR_EMERALD_DARK)

    draw_component(0.08, 0.73, 0.25, 0.14, "StudentChatView", "HTML5 / CSS3 / ES6 Fetch", border_clr=CLR_EMERALD)
    draw_component(0.38, 0.73, 0.25, 0.14, "SpeechAudioEngine", "W3C Web Speech API (STT/TTS)", border_clr=CLR_EMERALD)
    draw_component(0.68, 0.73, 0.24, 0.14, "AdminConsoleView", "Bootstrap 5 / Vanilla JS", border_clr=CLR_EMERALD)

    # SUBSYSTEM 2: FLASK CORE WSGI BACKEND (Center)
    p2 = patches.Rectangle((0.05, 0.38), 0.90, 0.27, facecolor="#eff6ff", edgecolor="#1e3a8a", lw=1.2, zorder=1)
    ax.add_patch(p2)
    ax.text(0.07, 0.625, "APPLICATION CORE TIER (Python 3.11 / Flask WSGI Microframework)", fontsize=8.0, weight="bold", color="#1e3a8a")

    draw_component(0.08, 0.42, 0.25, 0.17, "RestApiController\n(app.py)", "Flask Route Blueprints & CSRF", border_clr="#1e3a8a")
    draw_component(0.38, 0.42, 0.25, 0.17, "DualTierEngine\n(chatbot.py)", "Jaccard Tokenizer & Synonyms", border_clr="#1e3a8a")
    draw_component(0.68, 0.42, 0.24, 0.17, "AuthGovernance\n(admin.py)", "PBKDF2 Hashing & CSV Export", border_clr="#1e3a8a")

    # SUBSYSTEM 3: INTELLIGENCE & PERSISTENCE TIER (Bottom)
    p3 = patches.Rectangle((0.05, 0.08), 0.90, 0.25, facecolor="#faf5ff", edgecolor=CLR_PURPLE, lw=1.2, zorder=1)
    ax.add_patch(p3)
    ax.text(0.07, 0.305, "INTELLIGENCE & STORAGE TIER (Embedded Database & Cloud LLM)", fontsize=8.0, weight="bold", color=CLR_PURPLE)

    draw_component(0.08, 0.12, 0.38, 0.15, "SQLite3 Relational Engine", "instance/campusai.db (3NF 26 FAQs)", border_clr="#0f766e")
    draw_component(0.54, 0.12, 0.38, 0.15, "Google Gemini 2.5 Flash", "Google GenAI SDK (Zero-Hallucination)", border_clr=CLR_PURPLE)

    # Ports & Lollipop Interfaces (Client to Server)
    ax.plot([0.20, 0.20], [0.73, 0.59], color=CLR_EMERALD, lw=1.4, zorder=3)
    ax.plot([0.20], [0.65], marker='o', markersize=6, color=CLR_EMERALD, zorder=4)
    ax.text(0.21, 0.65, "HTTP REST API (/api/chat)", fontsize=6.8, color=CLR_EMERALD_DARK, weight="bold")

    ax.plot([0.80, 0.80], [0.73, 0.59], color="#1e3a8a", lw=1.4, zorder=3)
    ax.plot([0.80], [0.65], marker='o', markersize=6, color="#1e3a8a", zorder=4)
    ax.text(0.81, 0.65, "Admin Session (/admin)", fontsize=6.8, color="#1e3a8a", weight="bold")

    # Core to Storage
    ax.plot([0.27, 0.27], [0.42, 0.27], color="#0f766e", lw=1.4, zorder=3)
    ax.plot([0.27], [0.34], marker='o', markersize=6, color="#0f766e", zorder=4)
    ax.text(0.28, 0.34, "SQLAlchemy ORM (models.py)", fontsize=6.8, color="#0f766e", weight="bold")

    # Core to Gemini API
    ax.plot([0.73, 0.73], [0.42, 0.27], color=CLR_PURPLE, lw=1.4, linestyle="--", zorder=3)
    ax.plot([0.73], [0.34], marker='o', markersize=6, color=CLR_PURPLE, zorder=4)
    ax.text(0.74, 0.34, "HTTPS REST (Google AI Studio)", fontsize=6.8, color=CLR_PURPLE, weight="bold")

    ax.text(0.50, 0.02, "UML 2.5 Component Conventions: Lollipop Circles (-O) = Provided Interfaces • Dotted Connectors = External Cloud Integration",
            ha="center", va="center", fontsize=7.2, color=CLR_SLATE)

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_component_diagram.png"), bbox_inches="tight")
    plt.close()
    print("[7/8] Generated Unique Modular Component Architecture Diagram: campusai_component_diagram.png")

create_hexagonal_component_diagram()


# ==============================================================================
# 8. MULTI-LEVEL DATA FLOW DIAGRAM (LEVEL 0 & LEVEL 1)
# (Gane-Sarson standards, clear functional processes, distinct styling)
# ==============================================================================
def create_multilevel_dfd():
    fig, ax = plt.subplots(figsize=(10.5, 12.0), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.text(0.5, 0.985, "CampusAI Data Flow Architecture (Gane-Sarson & DeMarco Conventions)",
            ha="center", va="center", fontsize=11.5, weight="bold", color=CLR_EMERALD_DARK)
    ax.text(0.5, 0.968, "Hierarchical Information Engineering • DFD Level 0 (System Context) & DFD Level 1 (Functional Decomposition)",
            ha="center", va="center", fontsize=8.0, color=CLR_SLATE)

    def draw_dfd_entity(cx, cy, w, h, name, sub=""):
        rect = patches.Rectangle((cx - w/2, cy - h/2), w, h, facecolor="#f1f5f9", edgecolor=CLR_SLATE_DARK, lw=1.3, zorder=3)
        ax.add_patch(rect)
        ax.text(cx, cy + (0.010 if sub else 0), name, ha="center", va="center", fontsize=7.5, weight="bold", color=CLR_SLATE_DARK, zorder=4)
        if sub:
            ax.text(cx, cy - 0.012, f"[{sub}]", ha="center", va="center", fontsize=6.2, color="#64748b", zorder=4)

    def draw_dfd_process(cx, cy, r, pid, name, bg="#ecfdf5", border=CLR_EMERALD):
        circ = Circle((cx, cy), r, facecolor=bg, edgecolor=border, lw=1.3, zorder=3)
        ax.add_patch(circ)
        id_y = cy + r * 0.35
        ax.plot([cx - r * 0.88, cx + r * 0.88], [id_y, id_y], color=border, lw=0.9, zorder=4)
        ax.text(cx, cy + r * 0.62, pid, ha="center", va="center", fontsize=7.2, weight="bold", color=border, zorder=5)
        ax.text(cx, cy - r * 0.18, name, ha="center", va="center", fontsize=6.5, color=CLR_SLATE_DARK, zorder=5)

    def draw_dfd_store(x, y, w, h, sid, name):
        ax.plot([x, x + w], [y + h, y + h], color=CLR_SLATE_DARK, lw=1.3, zorder=3)
        ax.plot([x, x + w], [y, y], color=CLR_SLATE_DARK, lw=1.3, zorder=3)
        ax.plot([x, x], [y, y + h], color=CLR_SLATE_DARK, lw=1.3, zorder=3)
        div_x = x + 0.045
        ax.plot([div_x, div_x], [y, y + h], color=CLR_SLATE_DARK, lw=1.0, zorder=3)
        rect = patches.Rectangle((x, y), w, h, facecolor=CLR_SLATE_LIGHT, edgecolor="none", zorder=2)
        ax.add_patch(rect)
        ax.text(x + 0.022, y + h/2, sid, ha="center", va="center", fontsize=7.2, weight="bold", color=CLR_EMERALD_DARK, zorder=4)
        ax.text(div_x + 0.010, y + h/2, name, ha="left", va="center", fontsize=7.0, color=CLR_SLATE_DARK, zorder=4)

    # --------------------------------------------------------------------------
    # PART A: LEVEL 0 CONTEXT DIAGRAM
    # --------------------------------------------------------------------------
    ax.text(0.04, 0.940, "DFD LEVEL 0: CONTEXT-LEVEL DATA FLOW DIAGRAM", fontsize=8.5, weight="bold", color=CLR_EMERALD_DARK)

    draw_dfd_entity(0.12, 0.87, 0.16, 0.065, "STUDENT", "External Entity")
    draw_dfd_entity(0.88, 0.87, 0.16, 0.065, "ADMINISTRATOR", "External Entity")
    draw_dfd_process(0.50, 0.87, 0.052, "0.0", "CampusAI College\nAssistant Chatbot\nSystem", bg=CLR_EMERALD_LIGHT, border=CLR_EMERALD)

    ax.annotate("Natural-Language Queries & Voice STT Input", xy=(0.448, 0.89), xytext=(0.20, 0.89),
                arrowprops=dict(arrowstyle="->", lw=1.1, color=CLR_EMERALD_DARK), fontsize=6.5, color=CLR_EMERALD_DARK)
    ax.annotate("Verified Answers, Suggestion Chips & Speech Audio", xy=(0.20, 0.85), xytext=(0.448, 0.85),
                arrowprops=dict(arrowstyle="->", lw=1.1, color=CLR_EMERALD_DARK), fontsize=6.5, color=CLR_EMERALD_DARK)

    ax.annotate("Admin Credentials & Knowledge Base CRUD", xy=(0.552, 0.89), xytext=(0.80, 0.89),
                arrowprops=dict(arrowstyle="->", lw=1.1, color="#1e3a8a"), fontsize=6.5, color="#1e3a8a")
    ax.annotate("Telemetry Reports, Analytics & CSV Logs", xy=(0.80, 0.85), xytext=(0.552, 0.85),
                arrowprops=dict(arrowstyle="->", lw=1.1, color="#1e3a8a"), fontsize=6.5, color="#1e3a8a")

    ax.plot([0.04, 0.96], [0.79, 0.79], color=CLR_SLATE_BORDER, linestyle="--", lw=1.0)

    # --------------------------------------------------------------------------
    # PART B: LEVEL 1 FUNCTIONAL DECOMPOSITION
    # --------------------------------------------------------------------------
    ax.text(0.04, 0.765, "DFD LEVEL 1: DETAILED FUNCTIONAL PROCESS DECOMPOSITION", fontsize=8.5, weight="bold", color=CLR_EMERALD_DARK)

    # 5 Key Processes
    draw_dfd_process(0.12, 0.68, 0.042, "1.0", "Ingest & Validate\nInquiry Query", bg=CLR_EMERALD_LIGHT, border=CLR_EMERALD)
    draw_dfd_process(0.36, 0.68, 0.042, "2.0", "NLP Tokenize\n& Jaccard Match", bg=CLR_AMBER_LIGHT, border=CLR_AMBER)
    draw_dfd_process(0.62, 0.68, 0.042, "3.0", "Context-Bounded\nGemini Fallback", bg=CLR_PURPLE_LIGHT, border=CLR_PURPLE)
    draw_dfd_process(0.88, 0.68, 0.042, "4.0", "Format Response\n& Render Audio", bg=CLR_BLUE_LIGHT, border=CLR_BLUE)
    draw_dfd_process(0.50, 0.48, 0.042, "5.0", "Admin Telemetry\n& CRUD Governance", bg="#f1f5f9", border="#1e3a8a")

    # 4 Gane-Sarson Open Data Stores
    draw_dfd_store(0.04, 0.54, 0.22, 0.038, "D1", "Administrators (admins)")
    draw_dfd_store(0.30, 0.54, 0.24, 0.038, "D2", "FAQ Knowledge Base (faqs)")
    draw_dfd_store(0.70, 0.54, 0.26, 0.038, "D3", "Chat History (chat_messages)")
    draw_dfd_store(0.35, 0.36, 0.30, 0.038, "D4", "Feedback Telemetry (feedback_logs)")

    # Data Flow Connections
    ax.annotate("query text", xy=(0.078, 0.68), xytext=(0.02, 0.68), arrowprops=dict(arrowstyle="->", lw=1.1), fontsize=6.2)
    ax.annotate("normalized tokens", xy=(0.318, 0.68), xytext=(0.162, 0.68), arrowprops=dict(arrowstyle="->", lw=1.1), fontsize=6.2)
    ax.annotate("score < 0.45", xy=(0.578, 0.68), xytext=(0.402, 0.68), arrowprops=dict(arrowstyle="->", lw=1.1, color="#b91c1c"), fontsize=6.2, color="#b91c1c")
    ax.annotate("score >= 0.45 (direct answer)", xy=(0.838, 0.70), xytext=(0.402, 0.70), arrowprops=dict(arrowstyle="->", lw=1.1, color=CLR_EMERALD), fontsize=6.2, color=CLR_EMERALD)
    ax.annotate("synthesized reply", xy=(0.838, 0.66), xytext=(0.662, 0.66), arrowprops=dict(arrowstyle="->", lw=1.1, color=CLR_PURPLE), fontsize=6.2, color=CLR_PURPLE)

    # Store Read / Write Connections
    ax.annotate("query FAQs", xy=(0.36, 0.638), xytext=(0.36, 0.578), arrowprops=dict(arrowstyle="<-", lw=1.1, color=CLR_AMBER), fontsize=6.2)
    ax.annotate("log conversation turn", xy=(0.80, 0.578), xytext=(0.88, 0.638), arrowprops=dict(arrowstyle="->", lw=1.1, color=CLR_BLUE), fontsize=6.2)
    ax.annotate("record feedback", xy=(0.50, 0.398), xytext=(0.50, 0.438), arrowprops=dict(arrowstyle="->", lw=1.1, color=CLR_SLATE), fontsize=6.2)

    # DFD Conventions Legend Table
    conventions = [
        ["Symbol", "DFD Element", "Standard Gane-Sarson Definition", "Implementation in CampusAI"],
        ["Square", "External Entity", "Origin / destination of data outside system boundary", "Student / Visitor & College Administrator"],
        ["Circle", "Process Bubble", "Transforms inputs into outputs (Numbered ID + Verb phrase)", "1.0 Ingest, 2.0 NLP Match, 3.0 Gemini Fallback, 4.0 Format, 5.0 Admin"],
        ["Open Box", "Data Store", "Repository of data at rest (Right side MUST be open)", "D1 Admins, D2 FAQs, D3 Chat Messages, D4 Feedback Logs"],
        ["Solid Arrow", "Data Flow", "Carries data packets with explicit noun-phrase labels", "query tokens, verified FAQ answer, synthesized AI reply, CSV report"]
    ]
    t_y = 0.28
    r_h = 0.040
    c_w = [0.12, 0.20, 0.36, 0.28]
    for r_idx, row in enumerate(conventions):
        c_x = 0.04
        for c_idx, cell in enumerate(row):
            bg = CLR_EMERALD_DARK if r_idx == 0 else (CLR_SLATE_LIGHT if r_idx % 2 == 1 else CLR_WHITE)
            fg = CLR_WHITE if r_idx == 0 else CLR_SLATE_DARK
            rect = patches.Rectangle((c_x, t_y - (r_idx + 1) * r_h), c_w[c_idx], r_h, facecolor=bg, edgecolor=CLR_SLATE_BORDER, lw=0.8)
            ax.add_patch(rect)
            ax.text(c_x + 0.008, t_y - (r_idx + 0.5) * r_h, cell, ha="left", va="center", fontsize=6.5, weight="bold" if r_idx == 0 else "normal", color=fg)
            c_x += c_w[c_idx]

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_dfd.png"), bbox_inches="tight")
    plt.close()
    print("[8/8] Generated Unique Multi-Level DFD Diagram: campusai_dfd.png")

create_multilevel_dfd()
print("[✓] ALL 8 CAMPUSAI UNIQUE DIAGRAMS SUCCESSFULLY GENERATED!")
