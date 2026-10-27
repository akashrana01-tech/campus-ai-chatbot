import os
os.environ["MPLCONFIGDIR"] = "/tmp/mpl"
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Polygon, Rectangle, Ellipse

OUT_DIR = "/Users/kanishksingh/Downloads/momo ai chat bot /scratch/campusai_diagrams"
os.makedirs(OUT_DIR, exist_ok=True)

# Common styling palette
C_NAVY = "#0f172a"
C_BLUE = "#1e3a8a"
C_BLUE_LIGHT = "#eff6ff"
C_BLUE_BORDER = "#3b82f6"
C_INDIGO = "#4338ca"
C_SLATE = "#334155"
C_GREEN = "#059669"
C_GREEN_LIGHT = "#ecfdf5"
C_GREEN_BORDER = "#10b981"
C_AMBER = "#b45309"
C_AMBER_LIGHT = "#fef3c7"
C_RED = "#dc2626"
C_RED_LIGHT = "#fef2f2"
C_WHITE = "#ffffff"

def draw_stick_figure(ax, x, y, scale=1.0, color="#1e293b", label="Actor", sublabel=""):
    """Draws a standard UML stick figure actor."""
    head_radius = 0.024 * scale
    # Head
    head = Circle((x, y + 0.058 * scale), head_radius, facecolor=C_WHITE, edgecolor=color, lw=1.6, zorder=5)
    ax.add_patch(head)
    # Body
    ax.plot([x, x], [y + 0.034 * scale, y - 0.025 * scale], color=color, lw=1.6, zorder=5)
    # Arms
    ax.plot([x - 0.028 * scale, x + 0.028 * scale], [y + 0.015 * scale, y + 0.015 * scale], color=color, lw=1.6, zorder=5)
    # Left Leg
    ax.plot([x, x - 0.022 * scale], [y - 0.025 * scale, y - 0.070 * scale], color=color, lw=1.6, zorder=5)
    # Right Leg
    ax.plot([x, x + 0.022 * scale], [y - 0.025 * scale, y - 0.070 * scale], color=color, lw=1.6, zorder=5)
    # Label
    ax.text(x, y - 0.092 * scale, label, ha="center", va="top", fontsize=8.5, weight="bold", color=color, zorder=6)
    if sublabel:
        ax.text(x, y - 0.125 * scale, sublabel, ha="center", va="top", fontsize=7.0, color="#64748b", zorder=6)

def draw_cylinder(ax, x, y, w, h, facecolor="#eff6ff", edgecolor="#2563eb", label="Database"):
    """Draws a standard UML/DFD database cylinder."""
    bot_ellipse = Ellipse((x + w/2, y + h*0.2), w, h*0.4, facecolor=facecolor, edgecolor=edgecolor, lw=1.2, zorder=3)
    body = Rectangle((x, y + h*0.2), w, h*0.6, facecolor=facecolor, edgecolor=facecolor, zorder=2)
    top_ellipse = Ellipse((x + w/2, y + h*0.8), w, h*0.4, facecolor=facecolor, edgecolor=edgecolor, lw=1.2, zorder=4)
    ax.plot([x, x], [y + h*0.2, y + h*0.8], color=edgecolor, lw=1.2, zorder=4)
    ax.plot([x + w, x + w], [y + h*0.2, y + h*0.8], color=edgecolor, lw=1.2, zorder=4)
    ax.add_patch(bot_ellipse)
    ax.add_patch(body)
    ax.add_patch(top_ellipse)
    ax.text(x + w/2, y + h*0.45, label, ha="center", va="center", fontsize=7.5, weight="bold", color="#1e3a8a", zorder=5)

def draw_diamond(ax, cx, cy, w, h, facecolor=C_AMBER_LIGHT, edgecolor=C_AMBER, lw=1.2, text="", fontsize=7.5, zorder=4):
    """Draws a sharp diamond for ER relationships or Decision trees."""
    pts = [[cx, cy + h/2], [cx + w/2, cy], [cx, cy - h/2], [cx - w/2, cy]]
    poly = Polygon(pts, closed=True, facecolor=facecolor, edgecolor=edgecolor, lw=lw, zorder=zorder)
    ax.add_patch(poly)
    if text:
        ax.text(cx, cy, text, ha="center", va="center", fontsize=fontsize, weight="bold", color="#78350f", zorder=zorder+1)

def draw_oval(ax, cx, cy, w, h, facecolor=C_WHITE, edgecolor="#64748b", text="", is_pk=False, fontsize=7.5, zorder=4):
    """Draws an oval/ellipse for ER attributes or Use Cases."""
    el = Ellipse((cx, cy), w, h, facecolor=facecolor, edgecolor=edgecolor, lw=1.1, zorder=zorder)
    ax.add_patch(el)
    if text:
        ax.text(cx, cy, text, ha="center", va="center", fontsize=fontsize, color="#0f172a", zorder=zorder+1)
        if is_pk:
            txt_len = len(text) * 0.0050
            ax.plot([cx - txt_len, cx + txt_len], [cy - h*0.22, cy - h*0.22], color="#0f172a", lw=1.0, zorder=zorder+2)

# ==============================================================================
# 1. DECISION TREE DIAGRAM
# ==============================================================================
def create_decision_tree():
    fig, ax = plt.subplots(figsize=(9.0, 10.0), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    
    # Title
    ax.text(0.5, 0.97, "CampusAI Hierarchical Decision Tree: Query Routing & Fallback Evaluation",
            ha="center", va="center", fontsize=11, weight="bold", color=C_NAVY)
    ax.text(0.5, 0.945, "Academic Year 2025-26 • Dual-Tier Hybrid NLP & Zero-Hallucination Pipeline",
            ha="center", va="center", fontsize=8.0, color="#64748b")
    
    # Root: Student Query Input
    root_box = dict(boxstyle="round,pad=0.5", facecolor=C_BLUE, edgecolor="#1e1b4b", lw=1.5)
    ax.text(0.5, 0.89, "Student Enters Natural-Language Query\n(Text Input / Clickable Suggestion Chip / Voice)", 
            ha="center", va="center", fontsize=8.5, weight="bold", color=C_WHITE, bbox=root_box)
    
    # Preprocessing
    ax.annotate("", xy=(0.5, 0.81), xytext=(0.5, 0.85), arrowprops=dict(arrowstyle="->", lw=1.5, color="#1e293b"))
    prep_box = dict(boxstyle="square,pad=0.4", facecolor=C_BLUE_LIGHT, edgecolor=C_BLUE_BORDER, lw=1.2)
    ax.text(0.5, 0.77, "Text Normalization & Stop-Word Stripping\nDomain Synonym Expansion (Admissions, Courses, Fees, Exams, Facilities)", 
            ha="center", va="center", fontsize=8.0, color=C_NAVY, bbox=prep_box)
    
    # Jaccard Scoring
    ax.annotate("", xy=(0.5, 0.69), xytext=(0.5, 0.73), arrowprops=dict(arrowstyle="->", lw=1.5, color="#1e293b"))
    ax.text(0.5, 0.655, "Compute Jaccard Similarity Score (S) Against 24 Seeded FAQs in SQLite DB\nS(Q, F) = |Tokens(Q) ∩ Tokens(F)| / |Tokens(Q) ∪ Tokens(F)|", 
            ha="center", va="center", fontsize=7.5, family="monospace", color=C_NAVY, bbox=prep_box)
    
    # Decision Diamond 1: S >= 0.45?
    ax.annotate("", xy=(0.5, 0.58), xytext=(0.5, 0.62), arrowprops=dict(arrowstyle="->", lw=1.5, color="#1e293b"))
    draw_diamond(ax, 0.5, 0.54, 0.26, 0.08, facecolor=C_AMBER_LIGHT, edgecolor=C_AMBER, text="Is Best Score\nS >= 0.45 ?", fontsize=8.5)
    
    # Branch YES: Tier-1 Direct SQLite Match
    ax.annotate("YES\n(High Confidence\nS >= 0.45)", xy=(0.20, 0.42), xytext=(0.37, 0.54),
                arrowprops=dict(arrowstyle="->", lw=1.5, color=C_GREEN), fontsize=8.0, weight="bold", color=C_GREEN)
    
    tier1_box = dict(boxstyle="round,pad=0.45", facecolor=C_GREEN_LIGHT, edgecolor=C_GREEN_BORDER, lw=1.4)
    ax.text(0.20, 0.38, "Tier 1: Deterministic SQLite FAQ Match\n• Immediate Local Lookup (< 15ms)\n• Source: Official College FAQ Corpus\n• Confidence: 100% Factual Integrity\n• Set response_source = 'database'",
            ha="center", va="center", fontsize=7.5, color="#064e3b", bbox=tier1_box)
    
    # Branch NO: Check LLM
    ax.annotate("NO\n(Score < 0.45)", xy=(0.80, 0.42), xytext=(0.63, 0.54),
                arrowprops=dict(arrowstyle="->", lw=1.5, color=C_RED), fontsize=8.0, weight="bold", color=C_RED)
    
    draw_diamond(ax, 0.80, 0.38, 0.26, 0.08, facecolor=C_AMBER_LIGHT, edgecolor=C_AMBER, text="Is Google Gemini\nAPI Online & Key\nConfigured?", fontsize=7.5)
    
    # Sub-branch Gemini YES
    ax.annotate("YES", xy=(0.67, 0.25), xytext=(0.74, 0.34), arrowprops=dict(arrowstyle="->", lw=1.3, color=C_GREEN), fontsize=7.5, weight="bold", color=C_GREEN)
    tier2_box = dict(boxstyle="square,pad=0.4", facecolor=C_BLUE_LIGHT, edgecolor="#6366f1", lw=1.2)
    ax.text(0.67, 0.21, "Tier 2: Context-Bounded LLM\n• Model: gemini-2.5-flash\n• Strict Zero-Hallucination Prompt\n• Grounded in College Context Only\n• Set response_source = 'ai'",
            ha="center", va="center", fontsize=7.2, color="#312e81", bbox=tier2_box)
    
    # Sub-branch Gemini NO / Outage
    ax.annotate("NO / Error", xy=(0.89, 0.25), xytext=(0.86, 0.34), arrowprops=dict(arrowstyle="->", lw=1.3, color=C_RED), fontsize=7.5, weight="bold", color=C_RED)
    tier3_box = dict(boxstyle="square,pad=0.4", facecolor=C_RED_LIGHT, edgecolor=C_RED, lw=1.2)
    ax.text(0.89, 0.21, "Tier 3: Graceful Fallback\n• Deterministic Office Referral\n• Avoids fabricated answers\n• Contact: contact@college.edu\n• Set response_source = 'fallback'",
            ha="center", va="center", fontsize=7.2, color="#7f1d1d", bbox=tier3_box)
    
    # Convergence to Final Output
    ax.annotate("", xy=(0.50, 0.11), xytext=(0.20, 0.30), arrowprops=dict(arrowstyle="->", lw=1.2, color="#475569"))
    ax.annotate("", xy=(0.50, 0.11), xytext=(0.67, 0.15), arrowprops=dict(arrowstyle="->", lw=1.2, color="#475569"))
    ax.annotate("", xy=(0.50, 0.11), xytext=(0.89, 0.15), arrowprops=dict(arrowstyle="->", lw=1.2, color="#475569"))
    
    final_box = dict(boxstyle="round,pad=0.5", facecolor=C_NAVY, edgecolor="#000000", lw=1.5)
    ax.text(0.50, 0.07, "Dispatch Dynamic JSON Response to Client Interface\nRender Formatted Chat Bubble • Refresh 4 Suggestion Chips • Persist Turn to chat_messages",
            ha="center", va="center", fontsize=8.0, weight="bold", color=C_WHITE, bbox=final_box)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_decision_tree.png"), bbox_inches="tight")
    plt.close()
    print("[1/12] Generated campusai_decision_tree.png")

create_decision_tree()

# ==============================================================================
# 2. CLASSIC CHEN ER DIAGRAM (3NF SCHEMA)
# ==============================================================================
def create_er_diagram():
    fig, ax = plt.subplots(figsize=(9.5, 9.5), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    
    # Title
    ax.text(0.5, 0.97, "ER Diagram (Classic Chen Notation): CampusAI Relational Database Architecture",
            ha="center", va="center", fontsize=11, weight="bold", color=C_NAVY)
    ax.text(0.5, 0.945, "Strict Third Normal Form (3NF) • Entities (Rectangles), Relationships (Diamonds), Attributes (Ovals)",
            ha="center", va="center", fontsize=8.0, color="#64748b")
    
    # ENTITIES (Sharp Rectangles)
    ent_style = dict(boxstyle="square,pad=0.5", facecolor="#e0e7ff", edgecolor="#3730a3", lw=1.5)
    
    # 1. ADMINS Entity (Top-Left)
    ax.text(0.25, 0.76, "ADMINS\n(admin_user)", ha="center", va="center", fontsize=9.0, weight="bold", color="#1e1b4b", bbox=ent_style)
    # Attributes for ADMINS
    draw_oval(ax, 0.10, 0.88, 0.14, 0.05, text="id (PK)", is_pk=True)
    draw_oval(ax, 0.10, 0.81, 0.14, 0.05, text="username")
    draw_oval(ax, 0.10, 0.74, 0.14, 0.05, text="email")
    draw_oval(ax, 0.10, 0.67, 0.15, 0.05, text="password_hash")
    draw_oval(ax, 0.25, 0.64, 0.14, 0.05, text="created_at")
    # Connect attributes to ADMINS
    ax.plot([0.16, 0.20], [0.86, 0.79], "k-", lw=0.9)
    ax.plot([0.17, 0.20], [0.80, 0.77], "k-", lw=0.9)
    ax.plot([0.17, 0.20], [0.74, 0.76], "k-", lw=0.9)
    ax.plot([0.17, 0.20], [0.69, 0.74], "k-", lw=0.9)
    ax.plot([0.25, 0.25], [0.665, 0.72], "k-", lw=0.9)
    
    # 2. FAQS Entity (Top-Right)
    ax.text(0.75, 0.76, "FAQS\n(knowledge_base)", ha="center", va="center", fontsize=9.0, weight="bold", color="#1e1b4b", bbox=ent_style)
    # Attributes for FAQS
    draw_oval(ax, 0.90, 0.88, 0.14, 0.05, text="id (PK)", is_pk=True)
    draw_oval(ax, 0.90, 0.81, 0.14, 0.05, text="question")
    draw_oval(ax, 0.90, 0.74, 0.14, 0.05, text="answer")
    draw_oval(ax, 0.90, 0.67, 0.15, 0.05, text="category (IDX)")
    draw_oval(ax, 0.75, 0.64, 0.14, 0.05, text="updated_at")
    # Connect attributes to FAQS
    ax.plot([0.84, 0.80], [0.86, 0.79], "k-", lw=0.9)
    ax.plot([0.83, 0.80], [0.80, 0.77], "k-", lw=0.9)
    ax.plot([0.83, 0.80], [0.74, 0.76], "k-", lw=0.9)
    ax.plot([0.83, 0.80], [0.69, 0.74], "k-", lw=0.9)
    ax.plot([0.75, 0.75], [0.665, 0.72], "k-", lw=0.9)
    
    # RELATIONSHIP 1: ADMINS MANAGES FAQS (Diamond)
    draw_diamond(ax, 0.50, 0.76, 0.18, 0.09, text="MANAGES\n(1 : N)", fontsize=8.0)
    ax.plot([0.31, 0.41], [0.76, 0.76], "k-", lw=1.3)
    ax.plot([0.59, 0.68], [0.76, 0.76], "k-", lw=1.3)
    ax.text(0.33, 0.78, "1", fontsize=8.5, weight="bold", color=C_NAVY)
    ax.text(0.66, 0.78, "N", fontsize=8.5, weight="bold", color=C_NAVY)
    
    # 3. CHAT_SESSIONS Entity (Bottom-Left)
    ax.text(0.25, 0.32, "CHAT_SESSIONS\n(student_sessions)", ha="center", va="center", fontsize=9.0, weight="bold", color="#1e1b4b", bbox=ent_style)
    # Attributes for CHAT_SESSIONS
    draw_oval(ax, 0.10, 0.44, 0.16, 0.05, text="session_id (PK)", is_pk=True)
    draw_oval(ax, 0.10, 0.37, 0.14, 0.05, text="created_at")
    draw_oval(ax, 0.10, 0.30, 0.14, 0.05, text="last_active")
    draw_oval(ax, 0.10, 0.23, 0.14, 0.05, text="user_ip")
    # Connect attributes
    ax.plot([0.17, 0.20], [0.42, 0.35], "k-", lw=0.9)
    ax.plot([0.17, 0.20], [0.36, 0.33], "k-", lw=0.9)
    ax.plot([0.17, 0.20], [0.30, 0.31], "k-", lw=0.9)
    ax.plot([0.17, 0.20], [0.25, 0.29], "k-", lw=0.9)
    
    # 4. CHAT_MESSAGES Entity (Bottom-Right)
    ax.text(0.75, 0.32, "CHAT_MESSAGES\n(conversation_turn)", ha="center", va="center", fontsize=9.0, weight="bold", color="#1e1b4b", bbox=ent_style)
    # Attributes for CHAT_MESSAGES
    draw_oval(ax, 0.90, 0.44, 0.14, 0.05, text="id (PK)", is_pk=True)
    draw_oval(ax, 0.90, 0.37, 0.15, 0.05, text="session_id (FK)")
    draw_oval(ax, 0.90, 0.30, 0.14, 0.05, text="role (user/bot)")
    draw_oval(ax, 0.90, 0.23, 0.14, 0.05, text="content")
    draw_oval(ax, 0.75, 0.18, 0.16, 0.05, text="source (db/ai)")
    draw_oval(ax, 0.90, 0.16, 0.14, 0.05, text="timestamp")
    # Connect attributes
    ax.plot([0.83, 0.80], [0.42, 0.35], "k-", lw=0.9)
    ax.plot([0.83, 0.80], [0.36, 0.33], "k-", lw=0.9)
    ax.plot([0.83, 0.80], [0.30, 0.31], "k-", lw=0.9)
    ax.plot([0.83, 0.80], [0.25, 0.29], "k-", lw=0.9)
    ax.plot([0.75, 0.75], [0.205, 0.28], "k-", lw=0.9)
    ax.plot([0.83, 0.79], [0.18, 0.27], "k-", lw=0.9)
    
    # RELATIONSHIP 2: SESSIONS CONTAINS MESSAGES (Diamond)
    draw_diamond(ax, 0.50, 0.32, 0.18, 0.09, text="CONTAINS\n(1 : N)", fontsize=8.0)
    ax.plot([0.33, 0.41], [0.32, 0.32], "k-", lw=1.3)
    ax.plot([0.59, 0.66], [0.32, 0.32], "k-", lw=1.3)
    ax.text(0.35, 0.34, "1", fontsize=8.5, weight="bold", color=C_NAVY)
    ax.text(0.64, 0.34, "N", fontsize=8.5, weight="bold", color=C_NAVY)
    
    # RELATIONSHIP 3: MESSAGES MATCHED IN FAQS (Vertical Diamond)
    draw_diamond(ax, 0.75, 0.54, 0.16, 0.09, text="MATCHED IN\n(N : 1)", fontsize=8.0)
    ax.plot([0.75, 0.75], [0.68, 0.585], "k-", lw=1.3)
    ax.plot([0.75, 0.75], [0.495, 0.37], "k-", lw=1.3)
    ax.text(0.77, 0.65, "1", fontsize=8.5, weight="bold", color=C_NAVY)
    ax.text(0.77, 0.40, "N", fontsize=8.5, weight="bold", color=C_NAVY)
    
    # RELATIONSHIP 4: ADMIN AUDITS MESSAGES (Diagonal dashed connection)
    draw_diamond(ax, 0.50, 0.54, 0.16, 0.09, text="AUDITS\n(1 : N)", fontsize=8.0, facecolor="#f3e8ff", edgecolor="#9333ea")
    ax.plot([0.30, 0.42], [0.72, 0.58], "k--", lw=1.1)
    ax.plot([0.58, 0.69], [0.50, 0.36], "k--", lw=1.1)
    ax.text(0.34, 0.67, "1", fontsize=8.0, weight="bold", color="#581c87")
    ax.text(0.66, 0.42, "N", fontsize=8.0, weight="bold", color="#581c87")
    
    # Schema legend at bottom
    leg_box = dict(boxstyle="round,pad=0.45", facecolor="#f8fafc", edgecolor="#cbd5e1", lw=1.0)
    legend_text = (
        "3NF Relational Integrity Invariants:\n"
        "• Primary Keys (Underlined): Unique row addressability with autoincrement integer or UUID\n"
        "• Foreign Keys (FK): Referential integrity between chat_messages.session_id and chat_sessions.session_id\n"
        "• Index Constraints (IDX): B-Tree indexes on faqs.category and chat_messages.session_id for sub-second scans"
    )
    ax.text(0.50, 0.06, legend_text, ha="center", va="center", fontsize=7.8, color="#334155", bbox=leg_box)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_er_diagram.png"), bbox_inches="tight")
    plt.close()
    print("[2/12] Generated campusai_er_diagram.png")

create_er_diagram()

# ==============================================================================
# 3. UML USE CASE DIAGRAM
# ==============================================================================
def create_use_case_diagram():
    fig, ax = plt.subplots(figsize=(10.0, 10.5), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    
    # Title
    ax.text(0.5, 0.975, "UML Use Case Diagram: CampusAI College Assistant Chatbot",
            ha="center", va="center", fontsize=11, weight="bold", color=C_NAVY)
    ax.text(0.5, 0.952, "Actors (Primary & Secondary), System Boundary, Functional Use Cases, and Dependency Relationships",
            ha="center", va="center", fontsize=8.0, color="#64748b")
    
    # SYSTEM BOUNDARY RECTANGLE
    boundary = patches.Rectangle((0.21, 0.05), 0.58, 0.87, linewidth=1.8, edgecolor="#2563eb", facecolor="#f8fafc", zorder=1)
    ax.add_patch(boundary)
    ax.text(0.50, 0.90, "System Boundary: CampusAI Application Engine", ha="center", va="center", fontsize=9.5, weight="bold", color="#1e3a8a", zorder=2)
    
    # 1. PRIMARY ACTOR: STUDENT / VISITOR (Left)
    draw_stick_figure(ax, 0.10, 0.65, scale=1.1, color="#1e293b", label="Student / Visitor", sublabel="<<primary actor>>")
    
    # 2. PRIMARY ACTOR: ADMINISTRATOR (Right)
    draw_stick_figure(ax, 0.90, 0.65, scale=1.1, color="#1e293b", label="Administrator", sublabel="<<primary actor>>")
    
    # 3. SECONDARY ACTOR: GEMINI AI CLOUD (Bottom Right)
    gem_box = dict(boxstyle="round,pad=0.4", facecolor="#f3e8ff", edgecolor="#9333ea", lw=1.2)
    ax.text(0.90, 0.22, "Google Gemini AI\nCloud Service\n<<secondary actor>>", ha="center", va="center", fontsize=7.5, weight="bold", color="#581c87", bbox=gem_box, zorder=5)
    
    # 4. SECONDARY ACTOR: SQLITE DATABASE (Bottom Left)
    draw_cylinder(ax, 0.04, 0.14, 0.12, 0.12, facecolor="#eff6ff", edgecolor="#2563eb", label="SQLite 3 DB\n<<data store>>")
    
    # USE CASES (Ellipses inside boundary)
    # Student Use Cases
    student_ucs = [
        (0.40, 0.83, "UC1: Browse Campus FAQs & Categories", 0.32, 0.052),
        (0.40, 0.74, "UC2: Ask Academic Query (Text / Voice)", 0.33, 0.052),
        (0.40, 0.65, "UC3: Use Clickable Suggestion Chips", 0.32, 0.052),
        (0.40, 0.56, "UC4: Search Knowledge Base by Keyword", 0.33, 0.052),
        (0.40, 0.47, "UC5: Clear / Reset Chat Session", 0.30, 0.052),
    ]
    
    # Admin Use Cases
    admin_ucs = [
        (0.60, 0.83, "UC6: Authenticate Admin Login (PBKDF2)", 0.33, 0.052),
        (0.60, 0.74, "UC7: Manage FAQs (Create, Read, Update, Delete)", 0.34, 0.052),
        (0.60, 0.65, "UC8: View Telemetry & System KPIs", 0.31, 0.052),
        (0.60, 0.56, "UC9: Inspect Interaction Transcripts", 0.31, 0.052),
        (0.60, 0.47, "UC10: Export Query Records to CSV", 0.30, 0.052),
    ]
    
    # Extended & Included Use Cases
    extended_ucs = [
        (0.50, 0.34, "UC11: Invoke Bounded Gemini Fallback", 0.33, 0.052),
        (0.50, 0.24, "UC12: Enforce Zero-Hallucination Guardrails", 0.35, 0.052),
        (0.35, 0.12, "UC13: Persist Interaction Turn to SQLite", 0.33, 0.052),
    ]
    
    # Draw all ellipses
    for cx, cy, label, w, h in student_ucs + admin_ucs:
        draw_oval(ax, cx, cy, w, h, facecolor=C_WHITE, edgecolor="#3b82f6", text=label, fontsize=7.2, zorder=3)
        
    for cx, cy, label, w, h in extended_ucs:
        draw_oval(ax, cx, cy, w, h, facecolor="#fefce8", edgecolor="#ca8a04", text=label, fontsize=7.2, zorder=3)
    
    # Connect Student Actor to UC1 - UC5
    for _, cy, _, _, _ in student_ucs:
        ax.plot([0.14, 0.24], [0.65, cy], color="#1e3a8a", lw=1.1, zorder=2)
        
    # Connect Admin Actor to UC6 - UC10
    for _, cy, _, _, _ in admin_ucs:
        ax.plot([0.86, 0.76], [0.65, cy], color="#047857", lw=1.1, zorder=2)
        
    # Stereotype connections:
    # UC2 --<<extend>>--> UC11
    ax.annotate("<<extend>>", xy=(0.50, 0.37), xytext=(0.40, 0.71),
                arrowprops=dict(arrowstyle="->", linestyle="--", color="#b45309", lw=1.2),
                fontsize=7.2, weight="bold", color="#b45309", zorder=4)
                
    # UC11 --<<include>>--> UC12
    ax.annotate("<<include>>", xy=(0.50, 0.27), xytext=(0.50, 0.31),
                arrowprops=dict(arrowstyle="->", linestyle="--", color="#0369a1", lw=1.2),
                fontsize=7.2, weight="bold", color="#0369a1", zorder=4)
                
    # UC2 --<<include>>--> UC13
    ax.annotate("<<include>>", xy=(0.35, 0.15), xytext=(0.35, 0.44),
                arrowprops=dict(arrowstyle="->", linestyle="--", color="#0369a1", lw=1.2),
                fontsize=7.2, weight="bold", color="#0369a1", zorder=4)
                
    # UC11 connected to Gemini AI Cloud
    ax.plot([0.67, 0.82], [0.34, 0.24], color="#9333ea", linestyle="-", lw=1.2, zorder=2)
    
    # UC13 connected to SQLite DB
    ax.plot([0.19, 0.16], [0.12, 0.18], color="#2563eb", linestyle="-", lw=1.2, zorder=2)
    
    # Legend
    leg_box = dict(boxstyle="round,pad=0.35", facecolor="#ffffff", edgecolor="#cbd5e1", lw=0.9)
    ax.text(0.50, 0.02, "Standard UML 2.5 Conventions: Solid lines = Actor Associations • Dashed arrows = Stereotyped Dependencies (<<include>>, <<extend>>)",
            ha="center", va="center", fontsize=7.2, color="#475569", bbox=leg_box)
            
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_use_case.png"), bbox_inches="tight")
    plt.close()
    print("[3/12] Generated campusai_use_case.png")

create_use_case_diagram()

# Helper function for UML Class Box
def draw_class_box(ax, x, y, w, title, attributes, methods, facecolor="#ffffff", edgecolor="#1e3a8a"):
    """Draws a formal 3-compartment UML Class box."""
    line_h = 0.016
    h_title = 0.038
    h_attr = max(0.04, len(attributes) * line_h + 0.015)
    h_meth = max(0.04, len(methods) * line_h + 0.015)
    total_h = h_title + h_attr + h_meth
    
    # Outer box
    rect = patches.Rectangle((x, y - total_h), w, total_h, facecolor=facecolor, edgecolor=edgecolor, lw=1.3, zorder=3)
    ax.add_patch(rect)
    
    # Title compartment background
    t_bg = patches.Rectangle((x, y - h_title), w, h_title, facecolor="#f1f5f9", edgecolor=edgecolor, lw=1.0, zorder=3)
    ax.add_patch(t_bg)
    ax.text(x + w/2, y - h_title/2, title, ha="center", va="center", fontsize=8.2, weight="bold", color="#0f172a", zorder=4)
    
    # Divider 1: between title and attributes
    ax.plot([x, x + w], [y - h_title, y - h_title], color=edgecolor, lw=1.1, zorder=4)
    
    # Attributes
    curr_y = y - h_title - 0.012
    for attr in attributes:
        ax.text(x + 0.010, curr_y, attr, ha="left", va="center", fontsize=6.8, family="monospace", color="#1e293b", zorder=4)
        curr_y -= line_h
        
    # Divider 2: between attributes and methods
    div2_y = y - h_title - h_attr
    ax.plot([x, x + w], [div2_y, div2_y], color=edgecolor, lw=1.1, zorder=4)
    
    # Methods
    curr_y = div2_y - 0.012
    for m in methods:
        ax.text(x + 0.010, curr_y, m, ha="left", va="center", fontsize=6.8, family="monospace", color="#1e293b", zorder=4)
        curr_y -= line_h
        
    return total_h

# ==============================================================================
# 4. UML CLASS DIAGRAM
# ==============================================================================
def create_class_diagram():
    fig, ax = plt.subplots(figsize=(10.0, 10.5), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    
    # Title
    ax.text(0.5, 0.975, "UML Class Diagram: CampusAI MVC & Service Layer Architecture",
            ha="center", va="center", fontsize=11, weight="bold", color=C_NAVY)
    ax.text(0.5, 0.952, "Object-Oriented Design • 3-Compartment Class Specifications, Attribute Types, Methods, and Associations",
            ha="center", va="center", fontsize=8.0, color="#64748b")
            
    # Class 1: Admin Model (Top Left)
    admin_attrs = [
        "- id : Integer [PK]",
        "- username : String(80) [UNIQUE]",
        "- email : String(120) [UNIQUE]",
        "- password_hash : String(255)",
        "- created_at : DateTime"
    ]
    admin_methods = [
        "+ set_password(pwd: str) : void",
        "+ check_password(pwd: str) : bool",
        "+ to_dict() : dict"
    ]
    h1 = draw_class_box(ax, 0.05, 0.90, 0.28, "Admin\n<<db.Model>>", admin_attrs, admin_methods)
    
    # Class 2: FAQ Model (Top Right)
    faq_attrs = [
        "- id : Integer [PK]",
        "- question : Text [NOT NULL]",
        "- answer : Text [NOT NULL]",
        "- category : String(50) [IDX]",
        "- created_at : DateTime",
        "- updated_at : DateTime"
    ]
    faq_methods = [
        "+ to_dict() : dict",
        "+ search(kw: str) : List[FAQ]",
        "+ filter_category(cat: str) : List[FAQ]"
    ]
    h2 = draw_class_box(ax, 0.67, 0.90, 0.28, "FAQ\n<<db.Model>>", faq_attrs, faq_methods)
    
    # Class 3: ChatMessage Model (Middle Left)
    msg_attrs = [
        "- id : Integer [PK]",
        "- session_id : String(64) [IDX]",
        "- role : String(20) [user/bot]",
        "- content : Text",
        "- source : String(30) [db/ai]",
        "- timestamp : DateTime"
    ]
    msg_methods = [
        "+ to_dict() : dict",
        "+ get_history(sid: str) : List[ChatMessage]"
    ]
    h3 = draw_class_box(ax, 0.05, 0.55, 0.28, "ChatMessage\n<<db.Model>>", msg_attrs, msg_methods)
    
    # Class 4: FAQService / NLP Engine (Middle Right)
    nlp_attrs = [
        "- confidence_threshold : float = 0.45",
        "- stopwords : Set[str]",
        "- synonyms : Dict[str, List[str]]"
    ]
    nlp_methods = [
        "+ normalize(text: str) : Set[str]",
        "+ expand_synonyms(tokens: set) : set",
        "+ jaccard_similarity(s1, s2) : float",
        "+ match_faq(query: str) : Tuple[FAQ, float]"
    ]
    h4 = draw_class_box(ax, 0.67, 0.55, 0.28, "FAQService\n<<nlp_engine>>", nlp_attrs, nlp_methods)
    
    # Class 5: AIService / Gemini Integration (Bottom Left)
    ai_attrs = [
        "- api_key : String",
        "- model_name : str = 'gemini-2.5-flash'",
        "- system_instruction : Text"
    ]
    ai_methods = [
        "+ is_available() : bool",
        "+ generate_response(prompt, ctx) : str",
        "+ enforce_zero_hallucination() : bool"
    ]
    h5 = draw_class_box(ax, 0.05, 0.25, 0.28, "AIService\n<<gemini_adapter>>", ai_attrs, ai_methods)
    
    # Class 6: ChatbotOrchestrator (Bottom Right / Center)
    orch_attrs = [
        "- faq_service : FAQService",
        "- ai_service : AIService",
        "- default_category : str = 'General'"
    ]
    orch_methods = [
        "+ handle_message(sid, q) : dict",
        "+ get_suggestion_chips() : List[str]",
        "+ clear_chat_session(sid) : bool"
    ]
    h6 = draw_class_box(ax, 0.67, 0.25, 0.28, "ChatbotOrchestrator\n<<controller>>", orch_attrs, orch_methods)
    
    # Associations & Multiplicity Connectors
    # 1. Admin manages FAQ (1 to 0..*)
    ax.annotate("", xy=(0.67, 0.82), xytext=(0.33, 0.82), arrowprops=dict(arrowstyle="->", lw=1.3, color="#1e3a8a"))
    ax.text(0.50, 0.84, "manages (CRUD)", ha="center", va="center", fontsize=7.5, weight="bold", color="#1e3a8a")
    ax.text(0.35, 0.80, "1", fontsize=8.0, weight="bold", color="#1e3a8a")
    ax.text(0.65, 0.80, "0..*", fontsize=8.0, weight="bold", color="#1e3a8a")
    
    # 2. ChatMessage matched_from FAQ (0..* to 1)
    ax.annotate("", xy=(0.67, 0.75), xytext=(0.33, 0.50), arrowprops=dict(arrowstyle="->", linestyle="--", lw=1.2, color="#059669"))
    ax.text(0.52, 0.64, "matched_from", ha="center", va="center", fontsize=7.2, weight="bold", color="#059669")
    
    # 3. FAQService indexes FAQ
    ax.annotate("", xy=(0.81, 0.66), xytext=(0.81, 0.55), arrowprops=dict(arrowstyle="->", linestyle="--", lw=1.2, color="#4338ca"))
    ax.text(0.85, 0.61, "indexes & scores", ha="left", va="center", fontsize=7.2, color="#4338ca")
    
    # 4. Orchestrator uses FAQService & AIService
    ax.annotate("", xy=(0.81, 0.35), xytext=(0.81, 0.25), arrowprops=dict(arrowstyle="->", lw=1.3, color="#0f172a"))
    ax.text(0.85, 0.30, "delegates NLP", ha="left", va="center", fontsize=7.2, color="#0f172a")
    
    ax.annotate("", xy=(0.33, 0.17), xytext=(0.67, 0.17), arrowprops=dict(arrowstyle="->", lw=1.3, color="#0f172a"))
    ax.text(0.50, 0.19, "invokes LLM fallback", ha="center", va="center", fontsize=7.2, color="#0f172a")
    
    # 5. Orchestrator persists ChatMessage
    ax.annotate("", xy=(0.20, 0.34), xytext=(0.67, 0.20), arrowprops=dict(arrowstyle="->", linestyle="--", lw=1.2, color="#0f172a"))
    ax.text(0.40, 0.28, "persists turn", ha="center", va="center", fontsize=7.2, color="#0f172a")
    
    # Legend
    leg_box = dict(boxstyle="round,pad=0.4", facecolor="#f8fafc", edgecolor="#cbd5e1", lw=0.9)
    ax.text(0.50, 0.04, "UML 2.5 Multiplicity: 1 = Exactly One • 0..* = Zero or Many • Visibility: + = Public, - = Private\nDesign Pattern: Model-View-Controller (MVC) with Service-Repository Separation",
            ha="center", va="center", fontsize=7.5, color="#334155", bbox=leg_box)
            
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_class_diagram.png"), bbox_inches="tight")
    plt.close()
    print("[4/12] Generated campusai_class_diagram.png")

create_class_diagram()

# ==============================================================================
# 5. UML OBJECT DIAGRAM (RUNTIME SNAPSHOT)
# ==============================================================================
def create_object_diagram():
    fig, ax = plt.subplots(figsize=(10.0, 10.5), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    
    # Title
    ax.text(0.5, 0.975, "UML Object Diagram: Runtime Instance Snapshot of CampusAI",
            ha="center", va="center", fontsize=11, weight="bold", color=C_NAVY)
    ax.text(0.5, 0.952, "Concrete System State during an Active Student Chat Interaction (Slot Values & Stereotyped Links)",
            ha="center", va="center", fontsize=8.0, color="#64748b")
            
    def draw_object_box(x, y, w, inst_title, slots, facecolor="#ffffff", edgecolor="#0f172a"):
        line_h = 0.018
        h_title = 0.038
        total_h = h_title + len(slots) * line_h + 0.015
        
        # Outer box
        rect = patches.Rectangle((x, y - total_h), w, total_h, facecolor=facecolor, edgecolor=edgecolor, lw=1.2, zorder=3)
        ax.add_patch(rect)
        # Header background
        h_bg = patches.Rectangle((x, y - h_title), w, h_title, facecolor="#f1f5f9", edgecolor=edgecolor, lw=1.0, zorder=3)
        ax.add_patch(h_bg)
        # Underlined instance title
        ax.text(x + w/2, y - h_title/2, inst_title, ha="center", va="center", fontsize=8.0, weight="bold", color="#0f172a", zorder=4)
        t_len = len(inst_title) * 0.0042
        ax.plot([x + w/2 - t_len, x + w/2 + t_len], [y - h_title*0.75, y - h_title*0.75], color="#0f172a", lw=1.0, zorder=4)
        # Slots
        curr_y = y - h_title - 0.012
        for s in slots:
            ax.text(x + 0.010, curr_y, s, ha="left", va="center", fontsize=6.8, family="monospace", color="#334155", zorder=4)
            curr_y -= line_h
        return total_h

    # Object 1: admin_session : Admin (Top Left)
    draw_object_box(0.06, 0.90, 0.38, "current_admin : Admin", [
        "id = 1",
        "username = \"akash_admin\"",
        "email = \"akash.admin@campusai.edu\"",
        "password_hash = \"pbkdf2:sha256:600000$8a...\"",
        "created_at = \"2026-08-15 09:00:00\""
    ])
    
    # Object 2: fee_faq : FAQ (Top Right)
    draw_object_box(0.56, 0.90, 0.38, "fee_faq_record : FAQ", [
        "id = 4",
        "category = \"Fees\"",
        "question = \"What are the semester fees?\"",
        "answer = \"Tuition: Rs 45,000; Exam: Rs 1,500\"",
        "created_at = \"2026-08-20 11:30:00\""
    ])
    
    # Object 3: active_session : ChatSession (Middle Left)
    draw_object_box(0.06, 0.65, 0.38, "active_session : ChatSession", [
        "session_id = \"sess_aktu_2026_9b81f4a\"",
        "ip_address = \"127.0.0.1\"",
        "total_messages = 2",
        "created_at = \"2026-10-27 10:14:02\""
    ])
    
    # Object 4: student_turn : ChatMessage (Middle Right)
    draw_object_box(0.56, 0.65, 0.38, "student_msg : ChatMessage", [
        "id = 201",
        "session_id = \"sess_aktu_2026_9b81f4a\"",
        "role = \"student\"",
        "content = \"What is the semester fee?\"",
        "timestamp = \"2026-10-27 10:14:05\""
    ])
    
    # Object 5: bot_turn : ChatMessage (Bottom Left)
    draw_object_box(0.06, 0.40, 0.38, "bot_reply : ChatMessage", [
        "id = 202",
        "session_id = \"sess_aktu_2026_9b81f4a\"",
        "role = \"assistant\"",
        "source = \"database\"",
        "content = \"Verified Fee Info: Rs 45,000...\"",
        "timestamp = \"2026-10-27 10:14:06\""
    ])
    
    # Object 6: active_matcher : FAQService (Bottom Right)
    draw_object_box(0.56, 0.40, 0.38, "nlp_engine : FAQService", [
        "confidence_threshold = 0.45",
        "indexed_faqs_count = 24",
        "calculated_jaccard = 0.88",
        "matched_faq_id = 4"
    ])
    
    # Links & Stereotypes between Objects
    # Link: Admin to FAQ (Aggregation)
    ax.plot([0.44, 0.56], [0.82, 0.82], "k-", lw=1.2)
    ax.text(0.50, 0.84, "<<aggregation>>\ncreated_by", ha="center", va="center", fontsize=6.8, weight="bold", color="#78350f")
    
    # Link: Session to Student Message (Composition)
    ax.plot([0.44, 0.56], [0.57, 0.57], "k-", lw=1.2)
    ax.text(0.50, 0.59, "<<composition>>\ncontains", ha="center", va="center", fontsize=6.8, weight="bold", color="#1e3a8a")
    
    # Link: Student Message to Bot Reply (Association)
    ax.plot([0.56, 0.44], [0.52, 0.35], "k-", lw=1.2)
    ax.text(0.50, 0.44, "<<association>>\nanswered_by", ha="center", va="center", fontsize=6.8, weight="bold", color="#059669")
    
    # Link: Bot Reply to FAQ (Dependency)
    ax.plot([0.44, 0.56], [0.32, 0.75], "k--", lw=1.1)
    ax.text(0.48, 0.68, "<<dependency>>\nretrieved_from", ha="center", va="center", fontsize=6.8, weight="bold", color="#4338ca")
    
    # Link: Matcher to FAQ (Dependency)
    ax.plot([0.75, 0.75], [0.40, 0.74], "k--", lw=1.1)
    ax.text(0.79, 0.47, "<<dependency>>\nscored_from", ha="left", va="center", fontsize=6.8, weight="bold", color="#4338ca")
    
    # NOTATION REFERENCE TABLE AT BOTTOM
    tbl_data = [
        ["Notation Element", "UML Semantic Meaning", "Implementation in CampusAI System"],
        ["Object Box", "Instance: Class with concrete slot values", "Active runtime entities (admin, session, message, FAQ)"],
        ["Composition (Solid Link)", "Part cannot exist without Whole (strong ownership)", "ChatMessage turn bound to parent ChatSession UUID"],
        ["Aggregation (Open Diamond)", "Part can exist independently of Whole", "FAQ entity created by Admin, persists after Admin logout"],
        ["Dependency (Dashed Line)", "One runtime object requires another to execute", "FAQService evaluates text against FAQ record to generate answer"]
    ]
    
    t_y = 0.22
    row_h = 0.032
    col_w = [0.24, 0.38, 0.32]
    for row_idx, row in enumerate(tbl_data):
        curr_x = 0.03
        for col_idx, cell in enumerate(row):
            bg = "#1e3a8a" if row_idx == 0 else ("#f8fafc" if row_idx % 2 == 1 else "#ffffff")
            fg = "#ffffff" if row_idx == 0 else "#0f172a"
            w = col_w[col_idx]
            rect = patches.Rectangle((curr_x, t_y - (row_idx + 1) * row_h), w, row_h, facecolor=bg, edgecolor="#cbd5e1", lw=0.8)
            ax.add_patch(rect)
            ax.text(curr_x + 0.010, t_y - (row_idx + 0.5) * row_h, cell, ha="left", va="center", fontsize=6.8, weight="bold" if row_idx == 0 else "normal", color=fg)
            curr_x += w
            
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_object_diagram.png"), bbox_inches="tight")
    plt.close()
    print("[5/12] Generated campusai_object_diagram.png")

create_object_diagram()

# ==============================================================================
# 6. UML SEQUENCE DIAGRAM
# ==============================================================================
def create_sequence_diagram():
    fig, ax = plt.subplots(figsize=(10.0, 11.0), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    
    # Title
    ax.text(0.5, 0.980, "UML Sequence Diagram: Student Query Processing & Fallback Flow",
            ha="center", va="center", fontsize=11, weight="bold", color=C_NAVY)
    ax.text(0.5, 0.958, "Asynchronous Execution Lifelines, Method Invocations, Activation Boxes, and Return Signals",
            ha="center", va="center", fontsize=8.0, color="#64748b")
            
    # 5 Lifelines
    lifelines = [
        (0.10, "Student\n(Browser UI)", "#e0f2fe", "#0284c7"),
        (0.30, "Flask Router\n(app.py)", "#f1f5f9", "#334155"),
        (0.52, "NLP Matcher\n(faq_service)", "#eff6ff", "#2563eb"),
        (0.74, "Database\n(SQLite 3)", "#ecfdf5", "#059669"),
        (0.92, "Gemini AI\n(Cloud API)", "#f3e8ff", "#9333ea")
    ]
    
    box_w, box_h = 0.14, 0.045
    for x, label, bg, border in lifelines:
        rect = patches.Rectangle((x - box_w/2, 0.90 - box_h/2), box_w, box_h, facecolor=bg, edgecolor=border, lw=1.2, zorder=3)
        ax.add_patch(rect)
        ax.text(x, 0.90, label, ha="center", va="center", fontsize=7.2, weight="bold", color="#0f172a", zorder=4)
        # Lifeline dashed vertical line
        ax.plot([x, x], [0.08, 0.875], color="#94a3b8", linestyle="--", lw=1.0, zorder=1)
        
    def draw_activation(x, y_start, y_end, color="#cbd5e1"):
        """Draws a standard UML activation bar."""
        act_w = 0.016
        rect = patches.Rectangle((x - act_w/2, y_end), act_w, y_start - y_end, facecolor=color, edgecolor="#475569", lw=0.9, zorder=2)
        ax.add_patch(rect)

    # Activations
    draw_activation(0.10, 0.85, 0.10, color="#bae6fd")
    draw_activation(0.30, 0.84, 0.12, color="#e2e8f0")
    draw_activation(0.52, 0.82, 0.48, color="#bfdbfe")
    draw_activation(0.74, 0.79, 0.52, color="#a7f3d0")
    draw_activation(0.92, 0.40, 0.30, color="#e9d5ff")
    draw_activation(0.74, 0.28, 0.16, color="#a7f3d0")

    # Messages (Calls & Returns)
    # 1. User sends message
    ax.annotate("1. Type 'fees' / Click Suggestion Chip", xy=(0.30, 0.84), xytext=(0.10, 0.84),
                arrowprops=dict(arrowstyle="->", lw=1.2, color="#1e3a8a"), fontsize=6.8, weight="bold", color="#1e3a8a", zorder=4)
                
    # 2. Flask dispatches to NLP
    ax.annotate("2. match_faq('fees')", xy=(0.52, 0.81), xytext=(0.30, 0.81),
                arrowprops=dict(arrowstyle="->", lw=1.2, color="#1e293b"), fontsize=6.8, color="#1e293b", zorder=4)
                
    # 3. Query SQLite for FAQs
    ax.annotate("3. SELECT id, question, answer FROM faqs", xy=(0.74, 0.77), xytext=(0.52, 0.77),
                arrowprops=dict(arrowstyle="->", lw=1.1, color="#059669"), fontsize=6.5, family="monospace", color="#059669", zorder=4)
                
    # 4. Return FAQ tuples
    ax.annotate("4. Return 24 Seeded FAQ Records", xy=(0.52, 0.73), xytext=(0.74, 0.73),
                arrowprops=dict(arrowstyle="->", linestyle="--", lw=1.1, color="#059669"), fontsize=6.5, color="#059669", zorder=4)
                
    # 5. Jaccard scoring self-call
    ax.plot([0.52, 0.56, 0.56, 0.52], [0.70, 0.70, 0.67, 0.67], color="#2563eb", lw=1.1, zorder=3)
    ax.text(0.57, 0.685, "5. Tokenize & Jaccard Score (S=0.88 >= 0.45)", fontsize=6.2, color="#1d4ed8")
    
    # 6. Return best FAQ to Flask
    ax.annotate("6. Return (FAQ #4, score=0.88, source='database')", xy=(0.30, 0.64), xytext=(0.52, 0.64),
                arrowprops=dict(arrowstyle="->", linestyle="--", lw=1.1, color="#1e3a8a"), fontsize=6.5, weight="bold", color="#1e3a8a", zorder=4)
                
    # 7. Persist turn to chat_messages
    ax.annotate("7. INSERT INTO chat_messages (user & bot turn)", xy=(0.74, 0.60), xytext=(0.30, 0.60),
                arrowprops=dict(arrowstyle="->", lw=1.1, color="#047857"), fontsize=6.5, color="#047857", zorder=4)
                
    # 8. DB returns 200 OK
    ax.annotate("8. 200 OK (rows_inserted=2)", xy=(0.30, 0.56), xytext=(0.74, 0.56),
                arrowprops=dict(arrowstyle="->", linestyle="--", lw=1.1, color="#047857"), fontsize=6.5, color="#047857", zorder=4)
                
    # 9. Return JSON to Client
    ax.annotate("9. JSON {answer, confidence: 0.88, source: 'database'}", xy=(0.10, 0.52), xytext=(0.30, 0.52),
                arrowprops=dict(arrowstyle="->", linestyle="--", lw=1.2, color="#1e3a8a"), fontsize=6.8, weight="bold", color="#1e3a8a", zorder=4)
                
    # Divider for Fallback Phase
    ax.plot([0.05, 0.95], [0.47, 0.47], color="#cbd5e1", linestyle=":", lw=1.2)
    ax.text(0.50, 0.47, " [ Scenario 2: Unmatched Complex Query & Bounded Gemini LLM Fallback ] ", 
            ha="center", va="center", fontsize=7.2, weight="bold", color="#475569", bbox=dict(boxstyle="round,pad=0.2", facecolor="#ffffff", edgecolor="#cbd5e1"))

    # 10. Student submits complex query
    ax.annotate("10. Submit Complex Query ('Hostel fee refund policy?')", xy=(0.30, 0.43), xytext=(0.10, 0.43),
                arrowprops=dict(arrowstyle="->", lw=1.2, color="#1e3a8a"), fontsize=6.8, color="#1e3a8a", zorder=4)
                
    # 11. Matcher reports score < 0.45
    ax.annotate("11. match_faq(query) -> score=0.15 < 0.45 (No Match)", xy=(0.30, 0.39), xytext=(0.52, 0.39),
                arrowprops=dict(arrowstyle="->", linestyle="--", lw=1.1, color="#dc2626"), fontsize=6.5, color="#dc2626", zorder=4)
                
    # 12. Invoke Gemini Cloud API
    ax.annotate("12. generate_response(query, college_context)", xy=(0.92, 0.35), xytext=(0.30, 0.35),
                arrowprops=dict(arrowstyle="->", lw=1.2, color="#9333ea"), fontsize=6.8, weight="bold", color="#9333ea", zorder=4)
                
    # 13. Gemini returns bounded response
    ax.annotate("13. Return Zero-Hallucination Verified Response / Referral", xy=(0.30, 0.30), xytext=(0.92, 0.30),
                arrowprops=dict(arrowstyle="->", linestyle="--", lw=1.2, color="#9333ea"), fontsize=6.8, color="#9333ea", zorder=4)
                
    # 14. Persist AI turn
    ax.annotate("14. INSERT INTO chat_messages (source='ai')", xy=(0.74, 0.25), xytext=(0.30, 0.25),
                arrowprops=dict(arrowstyle="->", lw=1.1, color="#047857"), fontsize=6.5, color="#047857", zorder=4)
                
    # 15. Return JSON to Client
    ax.annotate("15. JSON {answer: '...', source: 'ai'}", xy=(0.10, 0.21), xytext=(0.30, 0.21),
                arrowprops=dict(arrowstyle="->", linestyle="--", lw=1.2, color="#1e3a8a"), fontsize=6.8, weight="bold", color="#1e3a8a", zorder=4)
                
    # 16. Clear Chat Session
    ax.annotate("16. Click 'Clear Chat' -> POST /api/chat/clear", xy=(0.30, 0.16), xytext=(0.10, 0.16),
                arrowprops=dict(arrowstyle="->", lw=1.2, color="#b45309"), fontsize=6.8, color="#b45309", zorder=4)
    ax.annotate("17. DELETE FROM chat_messages WHERE session_id", xy=(0.74, 0.13), xytext=(0.30, 0.13),
                arrowprops=dict(arrowstyle="->", lw=1.1, color="#b45309"), fontsize=6.5, color="#b45309", zorder=4)
    ax.annotate("18. JSON {status: 'cleared'} & UI Reset", xy=(0.10, 0.10), xytext=(0.30, 0.10),
                arrowprops=dict(arrowstyle="->", linestyle="--", lw=1.2, color="#b45309"), fontsize=6.8, color="#b45309", zorder=4)

    # Legend at bottom
    leg_box = dict(boxstyle="round,pad=0.35", facecolor="#ffffff", edgecolor="#cbd5e1", lw=0.9)
    ax.text(0.50, 0.04, "UML 2.5 Sequence Notation: Solid Arrows (───>) = Synchronous Message Calls • Dashed Arrows (< - - -) = Reply Return Signals\nVertical Shaded Bars = Active Execution Focus of Control",
            ha="center", va="center", fontsize=7.2, color="#475569", bbox=leg_box)
            
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_sequence_diagram.png"), bbox_inches="tight")
    plt.close()
    print("[6/12] Generated campusai_sequence_diagram.png")

create_sequence_diagram()

# ==============================================================================
# 7. UML ACTIVITY DIAGRAM (WITH 3 FORMAL SWIMLANES)
# ==============================================================================
def create_activity_diagram():
    fig, ax = plt.subplots(figsize=(10.0, 11.0), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    
    # Title
    ax.text(0.5, 0.980, "UML Activity Diagram: Query Processing & Fallback Resolution Pipeline",
            ha="center", va="center", fontsize=11, weight="bold", color=C_NAVY)
    ax.text(0.5, 0.958, "Partitioned Swimlanes (Student, Flask Engine, SQLite & Gemini Cloud) with Decision Nodes & Guard Conditions",
            ha="center", va="center", fontsize=8.0, color="#64748b")
            
    # 3 SWIMLANES (Vertical Columns)
    lanes = [
        (0.04, 0.33, "Student (User Interface)", "#f8fafc", "#3b82f6"),
        (0.37, 0.30, "CampusAI Engine (Flask & NLP)", "#ffffff", "#1e3a8a"),
        (0.67, 0.29, "Persistence & Services (SQLite & Gemini)", "#f8fafc", "#059669")
    ]
    
    for x, w, label, bg, border in lanes:
        rect = patches.Rectangle((x, 0.06), w, 0.87, facecolor=bg, edgecolor=border, lw=1.3, zorder=1)
        ax.add_patch(rect)
        # Header box
        h_rect = patches.Rectangle((x, 0.89), w, 0.04, facecolor="#1e3a8a", edgecolor=border, lw=1.0, zorder=2)
        ax.add_patch(h_rect)
        ax.text(x + w/2, 0.91, label, ha="center", va="center", fontsize=8.0, weight="bold", color=C_WHITE, zorder=3)

    def draw_activity(cx, cy, w, h, text, facecolor="#eff6ff", edgecolor="#3b82f6"):
        """Draws an activity state (rounded rectangle)."""
        box = patches.FancyBboxPatch((cx - w/2, cy - h/2), w, h,
                                     boxstyle="round,pad=0.015,rounding_size=0.015",
                                     facecolor=facecolor, edgecolor=edgecolor, lw=1.2, zorder=3)
        ax.add_patch(box)
        ax.text(cx, cy, text, ha="center", va="center", fontsize=7.2, color="#0f172a", zorder=4)

    # 1. Start Node (Solid circle) in Lane 1
    start_circle = Circle((0.205, 0.85), 0.014, facecolor="#000000", edgecolor="#000000", zorder=4)
    ax.add_patch(start_circle)
    ax.text(0.205, 0.87, "Initial Node", ha="center", va="bottom", fontsize=7.0, color="#64748b")
    
    # 2. Activity: Enter Query in Lane 1
    ax.annotate("", xy=(0.205, 0.80), xytext=(0.205, 0.835), arrowprops=dict(arrowstyle="->", lw=1.2))
    draw_activity(0.205, 0.77, 0.26, 0.045, "Enters Academic Query\n(Text / Voice / Suggestion Chip)")
    
    # 3. Transition to Lane 2: Validate Input
    ax.annotate("", xy=(0.52, 0.77), xytext=(0.335, 0.77), arrowprops=dict(arrowstyle="->", lw=1.2))
    draw_activity(0.52, 0.77, 0.25, 0.045, "Receive POST /api/chat\nExtract Session & Validate Input")
    
    # 4. Activity: Normalize & Tokenize in Lane 2
    ax.annotate("", xy=(0.52, 0.70), xytext=(0.52, 0.745), arrowprops=dict(arrowstyle="->", lw=1.2))
    draw_activity(0.52, 0.67, 0.25, 0.045, "Normalize Text & Strip Stopwords\nExpand Domain Synonyms")
    
    # 5. Activity: Compute Jaccard Score in Lane 2
    ax.annotate("", xy=(0.52, 0.60), xytext=(0.52, 0.645), arrowprops=dict(arrowstyle="->", lw=1.2))
    draw_activity(0.52, 0.57, 0.25, 0.045, "Query FAQs Corpus & Compute\nJaccard Similarity Score (S)")
    
    # 6. Decision Diamond 1: S >= 0.45? in Lane 2
    ax.annotate("", xy=(0.52, 0.51), xytext=(0.52, 0.545), arrowprops=dict(arrowstyle="->", lw=1.2))
    draw_diamond(ax, 0.52, 0.48, 0.16, 0.05, text="S >= 0.45 ?", fontsize=7.5)
    
    # Branch YES: To Lane 3 (SQLite Match)
    ax.annotate("[Yes: High Confidence]", xy=(0.72, 0.48), xytext=(0.60, 0.48),
                arrowprops=dict(arrowstyle="->", lw=1.2, color=C_GREEN), fontsize=6.8, weight="bold", color=C_GREEN)
    draw_activity(0.81, 0.48, 0.24, 0.045, "Fetch Verified FAQ Answer\nSet source = 'database'", facecolor=C_GREEN_LIGHT, edgecolor=C_GREEN_BORDER)
    
    # Branch NO: Check Gemini LLM
    ax.annotate("[No: Score < 0.45]", xy=(0.52, 0.41), xytext=(0.52, 0.455),
                arrowprops=dict(arrowstyle="->", lw=1.2, color=C_RED), fontsize=6.8, weight="bold", color=C_RED)
    draw_diamond(ax, 0.52, 0.38, 0.18, 0.05, text="Gemini Online?", fontsize=7.5)
    
    # Gemini YES -> To Lane 3 (Gemini API)
    ax.annotate("[Yes: API Ready]", xy=(0.72, 0.38), xytext=(0.61, 0.38),
                arrowprops=dict(arrowstyle="->", lw=1.2, color="#9333ea"), fontsize=6.8, weight="bold", color="#9333ea")
    draw_activity(0.81, 0.38, 0.24, 0.045, "Invoke Gemini 2.5 Flash\nApply Zero-Hallucination Prompt", facecolor="#f3e8ff", edgecolor="#9333ea")
    
    # Gemini NO -> Construct Office Referral
    ax.annotate("[No / Outage]", xy=(0.52, 0.31), xytext=(0.52, 0.355),
                arrowprops=dict(arrowstyle="->", lw=1.2, color="#b45309"), fontsize=6.8, weight="bold", color="#b45309")
    draw_activity(0.52, 0.28, 0.25, 0.045, "Construct Office Referral\n(contact@college.edu)", facecolor=C_AMBER_LIGHT, edgecolor=C_AMBER)
    
    # Merge Diamond in Lane 2
    draw_diamond(ax, 0.52, 0.20, 0.14, 0.045, text="Merge", fontsize=7.2)
    # Connect from DB answer
    ax.plot([0.81, 0.81, 0.59], [0.455, 0.20, 0.20], color=C_GREEN, lw=1.1)
    # Connect from Gemini answer
    ax.plot([0.81, 0.81, 0.59], [0.355, 0.20, 0.20], color="#9333ea", lw=1.1)
    # Connect from referral
    ax.plot([0.52, 0.52], [0.255, 0.225], color="#b45309", lw=1.1)
    
    # Persist in SQLite (Lane 3)
    ax.annotate("", xy=(0.70, 0.20), xytext=(0.59, 0.20), arrowprops=dict(arrowstyle="->", lw=1.2))
    draw_activity(0.81, 0.20, 0.24, 0.045, "Persist Conversation Turn\nto chat_messages Table", facecolor="#eff6ff", edgecolor="#2563eb")
    
    # Transition to Lane 1: Render Response
    ax.plot([0.81, 0.81, 0.205], [0.175, 0.13, 0.13], color="#1e3a8a", lw=1.2)
    ax.annotate("", xy=(0.205, 0.18), xytext=(0.205, 0.13), arrowprops=dict(arrowstyle="->", lw=1.2))
    draw_activity(0.205, 0.205, 0.26, 0.045, "Render Formatted Chat Bubble\nRefresh Suggestion Chips & Audio")
    
    # Final Bullseye Node in Lane 1
    ax.annotate("", xy=(0.205, 0.11), xytext=(0.205, 0.18), arrowprops=dict(arrowstyle="->", lw=1.2))
    outer_end = Circle((0.205, 0.095), 0.015, facecolor="#ffffff", edgecolor="#000000", lw=1.5, zorder=4)
    inner_end = Circle((0.205, 0.095), 0.009, facecolor="#000000", edgecolor="#000000", zorder=5)
    ax.add_patch(outer_end)
    ax.add_patch(inner_end)
    ax.text(0.205, 0.075, "Activity Completed", ha="center", va="top", fontsize=6.8, color="#64748b")
    
    # Legend
    leg_box = dict(boxstyle="round,pad=0.35", facecolor="#ffffff", edgecolor="#cbd5e1", lw=0.9)
    ax.text(0.50, 0.03, "UML 2.5 Activity Semantics: Solid Circle = Initial Node • Rounded Boxes = Activity States • Diamonds = Decisions/Merges • Bullseye = Final Activity State",
            ha="center", va="center", fontsize=7.2, color="#475569", bbox=leg_box)
            
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_activity_diagram.png"), bbox_inches="tight")
    plt.close()
    print("[7/12] Generated campusai_activity_diagram.png")

create_activity_diagram()

# ==============================================================================
# 8. UML COMPONENT DIAGRAM (DEPLOYMENT ARCHITECTURE)
# ==============================================================================
def create_component_diagram():
    fig, ax = plt.subplots(figsize=(10.0, 10.5), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    
    # Title
    ax.text(0.5, 0.980, "UML Component Diagram: CampusAI Physical & Logical Architecture",
            ha="center", va="center", fontsize=11, weight="bold", color=C_NAVY)
    ax.text(0.5, 0.958, "3-Tier Deployment Topology • Hardware Execution Nodes, Modular Components, and Interface Stereotypes",
            ha="center", va="center", fontsize=8.0, color="#64748b")
            
    def draw_hardware_node(x, y, w, h, title, spec_text=""):
        """Draws a 3D-perspective hardware deployment node."""
        depth = 0.025
        # Front face
        front = patches.Rectangle((x, y), w, h, facecolor="#f8fafc", edgecolor="#475569", lw=1.3, zorder=2)
        ax.add_patch(front)
        # Top face
        top_pts = [[x, y + h], [x + depth, y + h + depth], [x + w + depth, y + h + depth], [x + w, y + h]]
        top_poly = Polygon(top_pts, closed=True, facecolor="#e2e8f0", edgecolor="#475569", lw=1.1, zorder=1)
        ax.add_patch(top_poly)
        # Right face
        rt_pts = [[x + w, y], [x + w + depth, y + depth], [x + w + depth, y + h + depth], [x + w, y + h]]
        rt_poly = Polygon(rt_pts, closed=True, facecolor="#cbd5e1", edgecolor="#475569", lw=1.1, zorder=1)
        ax.add_patch(rt_poly)
        # Header text
        ax.text(x + 0.015, y + h - 0.025, f"<<device>> {title}", fontsize=8.5, weight="bold", color="#0f172a", zorder=3)
        if spec_text:
            ax.text(x + 0.015, y + h - 0.048, spec_text, fontsize=6.8, color="#64748b", zorder=3)

    def draw_uml_component(x, y, w, h, name, tech=""):
        """Draws a UML component box with two protruding side tabs."""
        # Main box
        comp = patches.Rectangle((x, y), w, h, facecolor="#ffffff", edgecolor="#1e3a8a", lw=1.2, zorder=3)
        ax.add_patch(comp)
        # Tab 1
        t1 = patches.Rectangle((x - 0.012, y + h - 0.022), 0.020, 0.012, facecolor="#e0e7ff", edgecolor="#1e3a8a", lw=1.0, zorder=4)
        ax.add_patch(t1)
        # Tab 2
        t2 = patches.Rectangle((x - 0.012, y + 0.010), 0.020, 0.012, facecolor="#e0e7ff", edgecolor="#1e3a8a", lw=1.0, zorder=4)
        ax.add_patch(t2)
        # Text
        ax.text(x + w/2, y + h/2 + (0.008 if tech else 0), f"<<component>>\n{name}", ha="center", va="center", fontsize=7.2, weight="bold", color="#1e3a8a", zorder=5)
        if tech:
            ax.text(x + w/2, y + h/2 - 0.016, tech, ha="center", va="center", fontsize=6.2, color="#64748b", zorder=5)

    # 1. NODE 1: Client Workstation / Mobile Device (Left)
    draw_hardware_node(0.04, 0.50, 0.38, 0.42, "Client Workstation / Phone", "RAM: 2GB+ • Modern Web Browser • Audio Speaker")
    draw_uml_component(0.08, 0.74, 0.30, 0.08, "ChatbotUI", "HTML5 / CSS3 / ES6 Fetch API")
    draw_uml_component(0.08, 0.56, 0.30, 0.08, "AudioEngine", "Web Speech API (STT & TTS)")
    
    # 2. NODE 2: Application Server Host (Right Top)
    draw_hardware_node(0.50, 0.42, 0.46, 0.50, "App Server (macOS / Linux)", "Python 3.11+ • Flask 3.1.3 • Gunicorn WSGI")
    draw_uml_component(0.54, 0.77, 0.38, 0.075, "FlaskRouter (app.py)", "REST Controllers & Endpoints")
    draw_uml_component(0.54, 0.65, 0.38, 0.075, "NLPEngine (faq_service)", "Jaccard Tokenizer & Synonyms")
    draw_uml_component(0.54, 0.53, 0.38, 0.075, "AIService (ai_service)", "Google GenAI SDK Adapter")
    draw_uml_component(0.54, 0.44, 0.38, 0.065, "DataModel (models.py)", "Flask-SQLAlchemy ORM")
    
    # 3. NODE 3: Data & Cloud Infrastructure Layer (Bottom)
    draw_hardware_node(0.04, 0.08, 0.92, 0.30, "Persistence & External Cloud Services", "ACID Embedded Relational Database & High-Throughput Gemini Cloud API")
    draw_uml_component(0.08, 0.13, 0.38, 0.16, "SQLite3 Engine\n(college.db)", "3NF Normalized Tables:\nadmins, faqs, chat_messages, chat_sessions")
    draw_uml_component(0.54, 0.13, 0.38, 0.16, "Google Gemini Cloud\n(gemini-2.5-flash)", "Context-Bounded Large Language Model\nStrict Zero-Hallucination Guardrails")
    
    # Interface Connections
    # Client to Server REST
    ax.plot([0.38, 0.54], [0.78, 0.81], color="#2563eb", lw=1.5, zorder=5)
    # Lollipop on client side
    ax.plot([0.46], [0.795], marker='o', markersize=6, color="#2563eb", zorder=6)
    ax.text(0.46, 0.83, "HTTP POST\n/api/chat", ha="center", va="bottom", fontsize=6.8, weight="bold", color="#1e3a8a")
    
    # Server to SQLite
    ax.plot([0.73, 0.73, 0.27, 0.27], [0.44, 0.38, 0.38, 0.29], color="#059669", lw=1.3, zorder=5)
    ax.text(0.50, 0.36, "SQLAlchemy Engine (sqlite:///instance/college.db)", ha="center", va="center", fontsize=6.8, color="#059669")
    
    # Server to Gemini API
    ax.plot([0.73, 0.73], [0.53, 0.29], color="#9333ea", lw=1.3, linestyle="--", zorder=5)
    ax.text(0.75, 0.36, "HTTPS / gRPC (Google AI Studio API Key)", ha="left", va="center", fontsize=6.8, color="#9333ea")
    
    # Legend
    leg_box = dict(boxstyle="round,pad=0.35", facecolor="#ffffff", edgecolor="#cbd5e1", lw=0.9)
    ax.text(0.50, 0.03, "UML 2.5 Component Conventions: 3D Blocks = Hardware Nodes • Tabbed Rectangles = Modular Software Components • Lollipop Connectors = Provided REST Interfaces",
            ha="center", va="center", fontsize=7.2, color="#475569", bbox=leg_box)
            
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_component_diagram.png"), bbox_inches="tight")
    plt.close()
    print("[8/12] Generated campusai_component_diagram.png")

create_component_diagram()

# ==============================================================================
# 9. DATA FLOW DIAGRAMS (LEVEL 0, LEVEL 1, LEVEL 2 & SYMBOLS TABLE)
# ==============================================================================
def create_dfd_diagram():
    fig, ax = plt.subplots(figsize=(10.0, 14.5), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    
    # Main Header
    ax.text(0.5, 0.985, "CampusAI Data Flow Diagrams: Context, Decomposition & Symbol Standards",
            ha="center", va="center", fontsize=11, weight="bold", color=C_NAVY)
    ax.text(0.5, 0.970, "Gane-Sarson & DeMarco Conventions • Level 0 (Context), Level 1 (Functional), Level 2 (NLP Engine)",
            ha="center", va="center", fontsize=8.0, color="#64748b")
            
    def draw_dfd_store(x, y, w, h, store_id, name):
        """Draws a standard Gane-Sarson Data Store (Open on the right side)."""
        # Top line
        ax.plot([x, x + w], [y + h, y + h], color="#0f172a", lw=1.3, zorder=3)
        # Bottom line
        ax.plot([x, x + w], [y, y], color="#0f172a", lw=1.3, zorder=3)
        # Left closing vertical line
        ax.plot([x, x], [y, y + h], color="#0f172a", lw=1.3, zorder=3)
        # Store ID divider vertical line
        div_x = x + 0.045
        ax.plot([div_x, div_x], [y, y + h], color="#0f172a", lw=1.0, zorder=3)
        # Fill
        rect = patches.Rectangle((x, y), w, h, facecolor="#f8fafc", edgecolor="none", zorder=2)
        ax.add_patch(rect)
        # Text
        ax.text(x + 0.022, y + h/2, store_id, ha="center", va="center", fontsize=7.5, weight="bold", color="#1e3a8a", zorder=4)
        ax.text(div_x + 0.010, y + h/2, name, ha="left", va="center", fontsize=7.2, color="#0f172a", zorder=4)

    def draw_dfd_process(cx, cy, radius, proc_id, name, facecolor="#eff6ff", edgecolor="#2563eb"):
        """Draws a standard Gane-Sarson process circle with ID and name."""
        circle = Circle((cx, cy), radius, facecolor=facecolor, edgecolor=edgecolor, lw=1.3, zorder=3)
        ax.add_patch(circle)
        # ID line
        id_y = cy + radius * 0.35
        ax.plot([cx - radius*0.88, cx + radius*0.88], [id_y, id_y], color=edgecolor, lw=0.9, zorder=4)
        ax.text(cx, cy + radius * 0.62, proc_id, ha="center", va="center", fontsize=7.2, weight="bold", color="#1e3a8a", zorder=5)
        ax.text(cx, cy - radius * 0.18, name, ha="center", va="center", fontsize=6.5, color="#0f172a", zorder=5)

    def draw_dfd_entity(cx, cy, w, h, name, subname=""):
        """Draws an external entity sharp rectangle."""
        rect = patches.Rectangle((cx - w/2, cy - h/2), w, h, facecolor="#f1f5f9", edgecolor="#334155", lw=1.3, zorder=3)
        ax.add_patch(rect)
        ax.text(cx, cy + (0.010 if subname else 0), name, ha="center", va="center", fontsize=7.5, weight="bold", color="#0f172a", zorder=4)
        if subname:
            ax.text(cx, cy - 0.012, subname, ha="center", va="center", fontsize=6.2, color="#64748b", zorder=4)

    # --------------------------------------------------------------------------
    # SECTION 1: DFD LEVEL 0 (CONTEXT DIAGRAM)
    # --------------------------------------------------------------------------
    ax.text(0.04, 0.945, "DFD Level 0: Global Context Diagram (System Environment)", fontsize=8.8, weight="bold", color="#1e3a8a")
    
    # External Entities
    draw_dfd_entity(0.12, 0.88, 0.16, 0.065, "STUDENT", "External Entity")
    draw_dfd_entity(0.88, 0.88, 0.16, 0.065, "ADMINISTRATOR", "External Entity")
    
    # Central Process 0.0
    draw_dfd_process(0.50, 0.88, 0.052, "0.0", "CampusAI College\nAssistant Chatbot\nSystem")
    
    # Data Flows (Student to System)
    ax.annotate("Student Academic Queries & Session Tokens", xy=(0.448, 0.90), xytext=(0.20, 0.90),
                arrowprops=dict(arrowstyle="->", lw=1.2, color="#1e3a8a"), fontsize=6.8, color="#1e3a8a")
    ax.annotate("Verified Answers, Suggestion Chips & Speech Audio", xy=(0.20, 0.86), xytext=(0.448, 0.86),
                arrowprops=dict(arrowstyle="->", lw=1.2, color="#1e3a8a"), fontsize=6.8, color="#1e3a8a")
                
    # Data Flows (Admin to System)
    ax.annotate("Admin Credentials & FAQ Updates (CRUD)", xy=(0.552, 0.90), xytext=(0.80, 0.90),
                arrowprops=dict(arrowstyle="->", lw=1.2, color="#047857"), fontsize=6.8, color="#047857")
    ax.annotate("Telemetry KPIs, Chat Audit Transcripts & CSV Exports", xy=(0.80, 0.86), xytext=(0.552, 0.86),
                arrowprops=dict(arrowstyle="->", lw=1.2, color="#047857"), fontsize=6.8, color="#047857")
                
    ax.plot([0.04, 0.96], [0.81, 0.81], color="#cbd5e1", linestyle="--", lw=1.0)

    # --------------------------------------------------------------------------
    # SECTION 2: DFD LEVEL 1 (FUNCTIONAL DECOMPOSITION)
    # --------------------------------------------------------------------------
    ax.text(0.04, 0.790, "DFD Level 1: First-Level Process Decomposition & Data Stores", fontsize=8.8, weight="bold", color="#1e3a8a")
    
    # Processes
    draw_dfd_process(0.12, 0.71, 0.040, "1.0", "Receive &\nValidate Query")
    draw_dfd_process(0.36, 0.71, 0.040, "2.0", "NLP Tokenize\n& Jaccard Match")
    draw_dfd_process(0.62, 0.71, 0.040, "3.0", "Bounded LLM\nFallback")
    draw_dfd_process(0.88, 0.71, 0.040, "4.0", "Format Bubble\n& Log Message")
    
    draw_dfd_process(0.50, 0.58, 0.040, "5.0", "Admin Dashboard\n& KPI Telemetry")
    
    # Data Stores (Open-ended on right side)
    draw_dfd_store(0.04, 0.60, 0.22, 0.038, "D1", "Admins Store (auth_credentials)")
    draw_dfd_store(0.30, 0.60, 0.22, 0.038, "D2", "FAQs Store (official_corpus)")
    draw_dfd_store(0.70, 0.60, 0.25, 0.038, "D3", "Chat Messages Store (transcripts)")
    
    # Connections for Level 1
    ax.annotate("query", xy=(0.08, 0.71), xytext=(0.02, 0.71), arrowprops=dict(arrowstyle="->", lw=1.1), fontsize=6.5)
    ax.annotate("clean_text", xy=(0.32, 0.71), xytext=(0.16, 0.71), arrowprops=dict(arrowstyle="->", lw=1.1), fontsize=6.5)
    ax.annotate("score < 0.45", xy=(0.58, 0.71), xytext=(0.40, 0.71), arrowprops=dict(arrowstyle="->", lw=1.1, color=C_RED), fontsize=6.5, color=C_RED)
    ax.annotate("direct answer", xy=(0.84, 0.73), xytext=(0.40, 0.73), arrowprops=dict(arrowstyle="->", lw=1.1, color=C_GREEN), fontsize=6.5, color=C_GREEN)
    ax.annotate("ai response", xy=(0.84, 0.69), xytext=(0.66, 0.69), arrowprops=dict(arrowstyle="->", lw=1.1, color="#9333ea"), fontsize=6.5, color="#9333ea")
    
    # Store connects
    ax.plot([0.36, 0.36], [0.67, 0.638], color="#059669", lw=1.1)
    ax.text(0.37, 0.655, "read FAQs", fontsize=6.2, color="#059669")
    
    ax.plot([0.88, 0.88], [0.67, 0.638], color="#1e3a8a", lw=1.1)
    ax.text(0.89, 0.655, "save turns", fontsize=6.2, color="#1e3a8a")
    
    ax.plot([0.50, 0.26], [0.58, 0.60], color="#334155", lw=1.1)
    ax.plot([0.50, 0.70], [0.58, 0.60], color="#334155", lw=1.1)
    ax.text(0.50, 0.53, "Admin CRUD updates D2 & reads D3 logs for analytics", ha="center", fontsize=6.5, color="#475569")
    
    ax.plot([0.04, 0.96], [0.50, 0.50], color="#cbd5e1", linestyle="--", lw=1.0)

    # --------------------------------------------------------------------------
    # SECTION 3: DFD LEVEL 2 (NLP ENGINE DECOMPOSITION)
    # --------------------------------------------------------------------------
    ax.text(0.04, 0.478, "DFD Level 2: NLP Intent Matching Engine Functional Decomposition (Process 2.0)", fontsize=8.8, weight="bold", color="#1e3a8a")
    
    draw_dfd_process(0.12, 0.40, 0.038, "2.1", "Lowercase &\nPunctuation Strip")
    draw_dfd_process(0.36, 0.40, 0.038, "2.2", "Stop-Word\nRemoval")
    draw_dfd_process(0.60, 0.40, 0.038, "2.3", "Domain Synonym\nExpansion")
    draw_dfd_process(0.86, 0.40, 0.038, "2.4", "Jaccard Overlap\nScorer (>= 0.45)")
    
    ax.annotate("raw_query", xy=(0.082, 0.40), xytext=(0.02, 0.40), arrowprops=dict(arrowstyle="->", lw=1.1), fontsize=6.5)
    ax.annotate("normalized", xy=(0.322, 0.40), xytext=(0.158, 0.40), arrowprops=dict(arrowstyle="->", lw=1.1), fontsize=6.5)
    ax.annotate("filtered", xy=(0.562, 0.40), xytext=(0.398, 0.40), arrowprops=dict(arrowstyle="->", lw=1.1), fontsize=6.5)
    ax.annotate("expanded_set", xy=(0.822, 0.40), xytext=(0.638, 0.40), arrowprops=dict(arrowstyle="->", lw=1.1), fontsize=6.5)
    
    ax.text(0.86, 0.33, "Evaluates against 24 Seeded FAQ token sets;\nEmits best match if Score >= 0.45, else triggers 3.0",
            ha="center", fontsize=6.5, color="#1e3a8a")

    ax.plot([0.04, 0.96], [0.30, 0.30], color="#cbd5e1", linestyle="--", lw=1.0)

    # --------------------------------------------------------------------------
    # SECTION 4: STANDARD DFD NOTATION REFERENCE TABLE
    # --------------------------------------------------------------------------
    ax.text(0.04, 0.275, "Standard DFD Notation & Symbol Conventions (Gane-Sarson & DeMarco Standards)", fontsize=8.8, weight="bold", color=C_NAVY)
    
    dfd_table = [
        ["Symbol Shape", "DFD Element", "Standard Academic Definition", "Implementation in CampusAI"],
        ["Square Box", "External Entity", "Origin / destination of data outside the system boundary", "Student (User) and Administrator (Faculty / College Authority)"],
        ["Circle / Bubble", "Process", "Transforms incoming data flows into outgoing data packets", "1.0 Receive Query, 2.0 NLP Engine, 3.0 Gemini Fallback, 4.0 Render"],
        ["Open Rectangle", "Data Store", "Repository of data at rest; MANDATORY: Right side must be open", "D1 Admins Store, D2 College FAQs Store, D3 Chat Messages Store"],
        ["Directed Arrow", "Data Flow", "Path over which information travels with explicit noun payload", "user_query, session_id, matched_faq, confidence_score, audit_csv"]
    ]
    
    tbl_top = 0.250
    row_h = 0.042
    col_widths = [0.15, 0.16, 0.35, 0.30]
    
    for r_idx, row in enumerate(dfd_table):
        curr_x = 0.02
        y_pos = tbl_top - (r_idx + 1) * row_h
        for c_idx, cell in enumerate(row):
            w = col_widths[c_idx]
            bg = "#1e3a8a" if r_idx == 0 else ("#f8fafc" if r_idx % 2 == 1 else "#ffffff")
            fg = "#ffffff" if r_idx == 0 else "#0f172a"
            rect = patches.Rectangle((curr_x, y_pos), w, row_h, facecolor=bg, edgecolor="#cbd5e1", lw=0.8, zorder=2)
            ax.add_patch(rect)
            ax.text(curr_x + 0.008, y_pos + row_h/2, cell, ha="left", va="center", fontsize=6.8, weight="bold" if r_idx == 0 else "normal", color=fg, zorder=3)
            curr_x += w

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_dfd.png"), bbox_inches="tight")
    plt.close()
    print("[9/12] Generated campusai_dfd.png")

create_dfd_diagram()

# ==============================================================================
# 10. UI MOCKUP: HOME SCREEN
# ==============================================================================
def create_ui_home():
    fig, ax = plt.subplots(figsize=(10.0, 6.8), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    
    # Outer browser window frame
    frame = patches.FancyBboxPatch((0.02, 0.02), 0.96, 0.96, boxstyle="round,pad=0.01,rounding_size=0.02",
                                  facecolor="#ffffff", edgecolor="#334155", lw=1.5, zorder=1)
    ax.add_patch(frame)
    
    # Browser Title Bar (macOS style)
    tbar = patches.Rectangle((0.02, 0.91), 0.96, 0.07, facecolor="#0f172a", edgecolor="#0f172a", zorder=2)
    ax.add_patch(tbar)
    
    # Traffic light dots (Red, Yellow, Green)
    ax.add_patch(Circle((0.050, 0.945), 0.010, facecolor="#ef4444", edgecolor="#b91c1c", lw=0.5, zorder=3))
    ax.add_patch(Circle((0.075, 0.945), 0.010, facecolor="#f59e0b", edgecolor="#d97706", lw=0.5, zorder=3))
    ax.add_patch(Circle((0.100, 0.945), 0.010, facecolor="#10b981", edgecolor="#059669", lw=0.5, zorder=3))
    
    # URL address bar
    url_box = patches.FancyBboxPatch((0.16, 0.925), 0.68, 0.040, boxstyle="round,pad=0.008,rounding_size=0.01",
                                    facecolor="#1e293b", edgecolor="#475569", lw=0.8, zorder=3)
    ax.add_patch(url_box)
    ax.text(0.18, 0.945, "[SECURE]  http://localhost:5000/  •  CampusAI | G H Raisoni International Skill Tech University",
            va="center", fontsize=7.2, color="#cbd5e1", zorder=4)
    ax.text(0.93, 0.945, "v2.5", ha="right", va="center", fontsize=7.0, weight="bold", color="#94a3b8", zorder=4)
    
    # Navigation bar inside app
    ax.add_patch(patches.Rectangle((0.02, 0.83), 0.96, 0.08, facecolor="#ffffff", edgecolor="#e2e8f0", lw=1.0, zorder=2))
    ax.text(0.06, 0.87, " CampusAI Assistant", fontsize=10.0, weight="bold", color="#1e3a8a", va="center", zorder=3)
    ax.text(0.94, 0.87, "Home    |    Chat Assistant    |    FAQ Directory    |    Admin Portal", 
            ha="right", va="center", fontsize=7.5, weight="bold", color="#475569", zorder=3)
            
    # Hero Section
    hero_bg = patches.Rectangle((0.02, 0.48), 0.96, 0.35, facecolor="#f8fafc", edgecolor="#e2e8f0", lw=0.8, zorder=2)
    ax.add_patch(hero_bg)
    
    badge = patches.FancyBboxPatch((0.06, 0.77), 0.36, 0.035, boxstyle="round,pad=0.006,rounding_size=0.008",
                                   facecolor="#eff6ff", edgecolor="#bfdbfe", lw=1.0, zorder=3)
    ax.add_patch(badge)
    ax.text(0.08, 0.787, "• BBA CA Academic Year 2025-26 • 24/7 AI Concierge", fontsize=7.0, weight="bold", color="#1d4ed8", va="center", zorder=4)
    
    ax.text(0.06, 0.71, "Intelligent AI-Powered College Assistant", fontsize=15.0, weight="bold", color="#0f172a", va="center", zorder=3)
    ax.text(0.06, 0.65, "Instant, authoritative academic information across Admissions, Courses, Fees, Exams & Facilities.\nPowered by deterministic local NLP matching with context-bounded Gemini AI fallback.",
            fontsize=8.0, color="#475569", va="center", zorder=3)
            
    # CTA Buttons
    btn1 = patches.FancyBboxPatch((0.06, 0.53), 0.22, 0.055, boxstyle="round,pad=0.008,rounding_size=0.01",
                                  facecolor="#2563eb", edgecolor="#1d4ed8", lw=1.0, zorder=3)
    ax.add_patch(btn1)
    ax.text(0.17, 0.557, " Open Chat Assistant", ha="center", va="center", fontsize=8.0, weight="bold", color="#ffffff", zorder=4)
    
    btn2 = patches.FancyBboxPatch((0.30, 0.53), 0.22, 0.055, boxstyle="round,pad=0.008,rounding_size=0.01",
                                  facecolor="#ffffff", edgecolor="#cbd5e1", lw=1.0, zorder=3)
    ax.add_patch(btn2)
    ax.text(0.41, 0.557, " Browse FAQ Directory", ha="center", va="center", fontsize=8.0, weight="bold", color="#334155", zorder=4)
    
    # 6 Domain Cards Section
    ax.text(0.06, 0.44, "Explore Campus Knowledge Domains", fontsize=10.0, weight="bold", color="#0f172a", va="center", zorder=3)
    
    cards = [
        ("Admissions", "Eligibility, deadlines, merit criteria & documents", 0.06, 0.28),
        ("Courses & Syllabus", "BBA CA, BCA, subjects & credit hours", 0.36, 0.28),
        ("Fee Structure", "Tuition, installment dates & concessions", 0.66, 0.28),
        ("Examinations", "Timetables, hall tickets & exam rules", 0.06, 0.12),
        ("Campus Facilities", "Central library, computing labs & hostels", 0.36, 0.12),
        ("General Inquiry", "College office hours, address & phone", 0.66, 0.12),
    ]
    
    for title, desc, cx, cy in cards:
        card_box = patches.FancyBboxPatch((cx, cy), 0.28, 0.13, boxstyle="round,pad=0.008,rounding_size=0.01",
                                          facecolor="#ffffff", edgecolor="#e2e8f0", lw=1.0, zorder=3)
        ax.add_patch(card_box)
        ax.text(cx + 0.02, cy + 0.095, f"• {title}", fontsize=8.0, weight="bold", color="#1e3a8a", zorder=4)
        ax.text(cx + 0.02, cy + 0.045, desc, fontsize=6.8, color="#64748b", zorder=4)
        
    # Footer Status Bar
    ax.add_patch(patches.Rectangle((0.02, 0.02), 0.96, 0.045, facecolor="#f1f5f9", edgecolor="#e2e8f0", lw=0.8, zorder=2))
    ax.text(0.06, 0.042, "● System Status: Online (SQLite 3.x • Gemini 2.5 Flash API Connected • 24 Seeded FAQs)", 
            fontsize=6.8, color="#059669", weight="bold", va="center", zorder=3)
    ax.text(0.94, 0.042, "Department of Computer Applications • Academic Year 2025-26", 
            ha="right", fontsize=6.8, color="#64748b", va="center", zorder=3)
            
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_ui_home.png"), bbox_inches="tight")
    plt.close()
    print("[10/12] Generated campusai_ui_home.png")

create_ui_home()

# ==============================================================================
# 11. UI MOCKUP: CHATBOT INTERFACE
# ==============================================================================
def create_ui_chat():
    fig, ax = plt.subplots(figsize=(10.0, 7.2), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    
    # Outer browser window frame
    frame = patches.FancyBboxPatch((0.02, 0.02), 0.96, 0.96, boxstyle="round,pad=0.01,rounding_size=0.02",
                                  facecolor="#ffffff", edgecolor="#334155", lw=1.5, zorder=1)
    ax.add_patch(frame)
    
    # Browser Title Bar (macOS style)
    tbar = patches.Rectangle((0.02, 0.91), 0.96, 0.07, facecolor="#0f172a", edgecolor="#0f172a", zorder=2)
    ax.add_patch(tbar)
    
    # Traffic light dots
    ax.add_patch(Circle((0.050, 0.945), 0.010, facecolor="#ef4444", edgecolor="#b91c1c", lw=0.5, zorder=3))
    ax.add_patch(Circle((0.075, 0.945), 0.010, facecolor="#f59e0b", edgecolor="#d97706", lw=0.5, zorder=3))
    ax.add_patch(Circle((0.100, 0.945), 0.010, facecolor="#10b981", edgecolor="#059669", lw=0.5, zorder=3))
    
    # URL address bar
    url_box = patches.FancyBboxPatch((0.16, 0.925), 0.68, 0.040, boxstyle="round,pad=0.008,rounding_size=0.01",
                                    facecolor="#1e293b", edgecolor="#475569", lw=0.8, zorder=3)
    ax.add_patch(url_box)
    ax.text(0.18, 0.945, "[SECURE]  http://localhost:5000/chat  •  CampusAI Virtual Chatbot Session",
            va="center", fontsize=7.2, color="#cbd5e1", zorder=4)
            
    # Chat Window Header Bar
    ax.add_patch(patches.Rectangle((0.02, 0.82), 0.96, 0.09, facecolor="#ffffff", edgecolor="#e2e8f0", lw=1.0, zorder=2))
    ax.text(0.06, 0.87, " CampusAI Student Assistant", fontsize=10.0, weight="bold", color="#1e3a8a", va="center", zorder=3)
    ax.text(0.06, 0.84, "● Active Session (ID: sess_aktu_9b81) • Sub-second Retrieval (<20ms)", fontsize=6.8, color="#059669", va="center", zorder=3)
    
    btn_clear = patches.FancyBboxPatch((0.84, 0.835), 0.12, 0.045, boxstyle="round,pad=0.006,rounding_size=0.008",
                                       facecolor="#fef2f2", edgecolor="#fca5a5", lw=1.0, zorder=3)
    ax.add_patch(btn_clear)
    ax.text(0.90, 0.857, " Clear Chat", ha="center", va="center", fontsize=7.0, weight="bold", color="#dc2626", zorder=4)
    
    # CHAT MESSAGES CANVAS
    chat_bg = patches.Rectangle((0.02, 0.20), 0.96, 0.62, facecolor="#f8fafc", edgecolor="#e2e8f0", lw=0.8, zorder=2)
    ax.add_patch(chat_bg)
    
    # Message 1: Student Question (Right aligned, Blue bubble)
    student_bubble = patches.FancyBboxPatch((0.44, 0.70), 0.50, 0.08, boxstyle="round,pad=0.01,rounding_size=0.015",
                                            facecolor="#2563eb", edgecolor="#1d4ed8", lw=1.0, zorder=3)
    ax.add_patch(student_bubble)
    ax.text(0.92, 0.75, "Student", ha="right", va="center", fontsize=6.5, weight="bold", color="#bfdbfe", zorder=4)
    ax.text(0.92, 0.72, "What is the fee structure for BBA (CA) and payment deadline?", 
            ha="right", va="center", fontsize=7.8, color="#ffffff", zorder=4)
            
    # Message 2: CampusAI Response (Left aligned, White card with green verified badge)
    bot_card = patches.FancyBboxPatch((0.06, 0.38), 0.65, 0.28, boxstyle="round,pad=0.01,rounding_size=0.015",
                                      facecolor="#ffffff", edgecolor="#cbd5e1", lw=1.2, zorder=3)
    ax.add_patch(bot_card)
    
    # Verified Badge
    v_badge = patches.FancyBboxPatch((0.08, 0.60), 0.35, 0.035, boxstyle="round,pad=0.005,rounding_size=0.006",
                                     facecolor=C_GREEN_LIGHT, edgecolor=C_GREEN_BORDER, lw=1.0, zorder=4)
    ax.add_patch(v_badge)
    ax.text(0.09, 0.617, "✓ Verified Database Match (Score: 100% • Cat: Fees)", 
            fontsize=6.5, weight="bold", color="#065f46", va="center", zorder=5)
            
    # Bot Answer Content
    bot_text = (
        "Here is the authoritative fee structure for Bachelor of Business Administration\n"
        "(Computer Applications) — BBA (CA) for Academic Year 2025-26:\n\n"
        "• Tuition Fee: ₹45,000 per semester\n"
        "• Examination Fee: ₹1,500 per semester\n"
        "• Library & Computer Laboratory Caution Deposit: ₹5,000 (Refundable)\n"
        "• First Installment Deadline: 15th November 2026\n\n"
        "Payments can be completed via student ERP online gateway or college accounts counter."
    )
    ax.text(0.08, 0.49, bot_text, fontsize=7.0, color="#1e293b", va="center", zorder=4)
    
    # Audio Listen Button
    aud_btn = patches.FancyBboxPatch((0.56, 0.395), 0.13, 0.030, boxstyle="round,pad=0.004,rounding_size=0.006",
                                     facecolor="#eff6ff", edgecolor="#bfdbfe", lw=0.8, zorder=4)
    ax.add_patch(aud_btn)
    ax.text(0.625, 0.410, "[AUDIO] Read Aloud", ha="center", va="center", fontsize=6.2, weight="bold", color="#1d4ed8", zorder=5)
    
    # Suggestion Chips Row
    ax.text(0.06, 0.28, "Suggested Follow-Up Questions:", fontsize=7.0, weight="bold", color="#64748b", zorder=3)
    chips = [
        "How do I apply for admissions?",
        "When are semester exams held?",
        "Library operating hours?",
        "Hostel fee refund policy?"
    ]
    for idx, c in enumerate(chips):
        cx = 0.06 + idx * 0.225
        chip_box = patches.FancyBboxPatch((cx, 0.22), 0.215, 0.040, boxstyle="round,pad=0.006,rounding_size=0.008",
                                          facecolor="#eff6ff", edgecolor="#93c5fd", lw=0.9, zorder=3)
        ax.add_patch(chip_box)
        ax.text(cx + 0.107, 0.240, c, ha="center", va="center", fontsize=6.5, color="#1e3a8a", zorder=4)
        
    # Input Bar Section
    in_box = patches.FancyBboxPatch((0.06, 0.06), 0.76, 0.09, boxstyle="round,pad=0.008,rounding_size=0.01",
                                    facecolor="#ffffff", edgecolor="#94a3b8", lw=1.2, zorder=3)
    ax.add_patch(in_box)
    ax.text(0.09, 0.105, "Type your academic question here (e.g. syllabus, exams, fees, facilities)...", 
            fontsize=7.5, color="#94a3b8", va="center", zorder=4)
            
    mic_btn = patches.Circle((0.78, 0.105), 0.022, facecolor="#f1f5f9", edgecolor="#cbd5e1", lw=1.0, zorder=4)
    ax.add_patch(mic_btn)
    ax.text(0.78, 0.105, "[MIC]", ha="center", va="center", fontsize=8.5, zorder=5)
    
    send_btn = patches.FancyBboxPatch((0.84, 0.06), 0.10, 0.09, boxstyle="round,pad=0.008,rounding_size=0.01",
                                      facecolor="#2563eb", edgecolor="#1d4ed8", lw=1.0, zorder=3)
    ax.add_patch(send_btn)
    ax.text(0.89, 0.105, "Send ➤", ha="center", va="center", fontsize=8.0, weight="bold", color="#ffffff", zorder=4)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_ui_chat.png"), bbox_inches="tight")
    plt.close()
    print("[11/12] Generated campusai_ui_chat.png")

create_ui_chat()

# ==============================================================================
# 12. UI MOCKUP: ADMIN DASHBOARD
# ==============================================================================
def create_ui_admin():
    fig, ax = plt.subplots(figsize=(10.0, 7.2), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    
    # Outer browser window frame
    frame = patches.FancyBboxPatch((0.02, 0.02), 0.96, 0.96, boxstyle="round,pad=0.01,rounding_size=0.02",
                                  facecolor="#ffffff", edgecolor="#334155", lw=1.5, zorder=1)
    ax.add_patch(frame)
    
    # Browser Title Bar (macOS style)
    tbar = patches.Rectangle((0.02, 0.91), 0.96, 0.07, facecolor="#0f172a", edgecolor="#0f172a", zorder=2)
    ax.add_patch(tbar)
    
    # Traffic light dots
    ax.add_patch(Circle((0.050, 0.945), 0.010, facecolor="#ef4444", edgecolor="#b91c1c", lw=0.5, zorder=3))
    ax.add_patch(Circle((0.075, 0.945), 0.010, facecolor="#f59e0b", edgecolor="#d97706", lw=0.5, zorder=3))
    ax.add_patch(Circle((0.100, 0.945), 0.010, facecolor="#10b981", edgecolor="#059669", lw=0.5, zorder=3))
    
    # URL address bar
    url_box = patches.FancyBboxPatch((0.16, 0.925), 0.68, 0.040, boxstyle="round,pad=0.008,rounding_size=0.01",
                                    facecolor="#1e293b", edgecolor="#475569", lw=0.8, zorder=3)
    ax.add_patch(url_box)
    ax.text(0.18, 0.945, "[SECURE]  http://localhost:5000/admin  •  CampusAI Administrative Governance Portal",
            va="center", fontsize=7.2, color="#cbd5e1", zorder=4)
            
    # Admin Header Bar
    ax.add_patch(patches.Rectangle((0.02, 0.83), 0.96, 0.08, facecolor="#1e1b4b", edgecolor="#1e1b4b", zorder=2))
    ax.text(0.06, 0.87, " CampusAI Command Center", fontsize=10.0, weight="bold", color="#ffffff", va="center", zorder=3)
    ax.text(0.94, 0.87, "Super Admin: akash_admin (ID: 1)  |  [ Logout ]", 
            ha="right", va="center", fontsize=7.2, color="#cbd5e1", zorder=3)
            
    # 4 KPI METRIC CARDS
    kpis = [
        ("TOTAL ACTIVE FAQS", "24", "100% Corpus Verified", "#2563eb", 0.06),
        ("KNOWLEDGE DOMAINS", "6", "Admissions, Fees, Exams...", "#059669", 0.29),
        ("STUDENT INQUIRIES", "1,842", "99.8% Sub-second Speed", "#7c3aed", 0.52),
        ("SYSTEM HEALTH", "HEALTHY", "Gemini LLM API Connected", "#0d9488", 0.75)
    ]
    for title, val, sub, col, x in kpis:
        k_card = patches.FancyBboxPatch((x, 0.68), 0.20, 0.12, boxstyle="round,pad=0.008,rounding_size=0.01",
                                        facecolor="#ffffff", edgecolor="#e2e8f0", lw=1.2, zorder=3)
        ax.add_patch(k_card)
        ax.text(x + 0.015, 0.77, title, fontsize=6.5, weight="bold", color="#64748b", zorder=4)
        ax.text(x + 0.015, 0.73, val, fontsize=12.0, weight="bold", color=col, zorder=4)
        ax.text(x + 0.015, 0.695, sub, fontsize=5.8, color="#94a3b8", zorder=4)

    # TABLE TOOLBAR
    ax.text(0.06, 0.63, "Manage Academic FAQ Knowledge Base (CRUD)", fontsize=9.0, weight="bold", color="#0f172a", va="center", zorder=3)
    
    add_btn = patches.FancyBboxPatch((0.72, 0.61), 0.12, 0.045, boxstyle="round,pad=0.006,rounding_size=0.008",
                                     facecolor="#2563eb", edgecolor="#1d4ed8", lw=1.0, zorder=3)
    ax.add_patch(add_btn)
    ax.text(0.78, 0.632, "+ Add New FAQ", ha="center", va="center", fontsize=6.8, weight="bold", color="#ffffff", zorder=4)
    
    csv_btn = patches.FancyBboxPatch((0.85, 0.61), 0.11, 0.045, boxstyle="round,pad=0.006,rounding_size=0.008",
                                     facecolor="#ffffff", edgecolor="#cbd5e1", lw=1.0, zorder=3)
    ax.add_patch(csv_btn)
    ax.text(0.905, 0.632, " Export CSV", ha="center", va="center", fontsize=6.8, weight="bold", color="#334155", zorder=4)

    # TABLE HEADER
    th_bg = patches.Rectangle((0.06, 0.54), 0.88, 0.045, facecolor="#312e81", zorder=3)
    ax.add_patch(th_bg)
    ax.text(0.08, 0.562, "ID", fontsize=6.8, weight="bold", color="#ffffff", va="center", zorder=4)
    ax.text(0.13, 0.562, "Question / Inquiry Prompt", fontsize=6.8, weight="bold", color="#ffffff", va="center", zorder=4)
    ax.text(0.55, 0.562, "Category", fontsize=6.8, weight="bold", color="#ffffff", va="center", zorder=4)
    ax.text(0.70, 0.562, "Source", fontsize=6.8, weight="bold", color="#ffffff", va="center", zorder=4)
    ax.text(0.84, 0.562, "Actions", fontsize=6.8, weight="bold", color="#ffffff", va="center", zorder=4)

    # TABLE ROWS
    rows = [
        ("1", "What are the BBA (CA) semester fees?", "Fees", "Database", "Edit  |  Delete"),
        ("2", "How do I apply for admissions to BCA / BBA CA?", "Admissions", "Database", "Edit  |  Delete"),
        ("3", "When are semester III theory examinations scheduled?", "Examinations", "Database", "Edit  |  Delete"),
        ("4", "What are the central library working hours and rules?", "Facilities", "Database", "Edit  |  Delete"),
        ("5", "What is the college office inquiry timing?", "General", "Database", "Edit  |  Delete"),
        ("6", "What is the hostel accommodation fee and deposit?", "Facilities", "Database", "Edit  |  Delete"),
        ("7", "What are the eligibility criteria for BBA CA course?", "Admissions", "Database", "Edit  |  Delete"),
        ("8", "Are scholarships available for reserved category students?", "Fees", "Database", "Edit  |  Delete"),
    ]
    
    r_top = 0.54
    r_h = 0.045
    for idx, (rid, q, cat, src, act) in enumerate(rows):
        y_pos = r_top - (idx + 1) * r_h
        bg_col = "#ffffff" if idx % 2 == 0 else "#f8fafc"
        ax.add_patch(patches.Rectangle((0.06, y_pos), 0.88, r_h, facecolor=bg_col, edgecolor="#e2e8f0", lw=0.6, zorder=2))
        ax.text(0.08, y_pos + r_h/2, rid, fontsize=6.5, va="center", color="#0f172a", zorder=3)
        ax.text(0.13, y_pos + r_h/2, q, fontsize=6.5, va="center", color="#0f172a", zorder=3)
        
        # Category pill
        cat_pill = patches.FancyBboxPatch((0.545, y_pos + 0.008), 0.12, 0.028, boxstyle="round,pad=0.004,rounding_size=0.006",
                                          facecolor="#eff6ff", edgecolor="#bfdbfe", lw=0.6, zorder=3)
        ax.add_patch(cat_pill)
        ax.text(0.605, y_pos + r_h/2, cat, ha="center", va="center", fontsize=6.0, weight="bold", color="#1d4ed8", zorder=4)
        
        ax.text(0.70, y_pos + r_h/2, f"● {src}", fontsize=6.5, va="center", color="#059669", zorder=3)
        ax.text(0.84, y_pos + r_h/2, act, fontsize=6.5, va="center", color="#2563eb", weight="bold", zorder=3)
        
    # Table pagination footer
    ax.add_patch(patches.Rectangle((0.06, r_top - 9 * r_h), 0.88, 0.040, facecolor="#f1f5f9", edgecolor="#e2e8f0", lw=0.6, zorder=2))
    ax.text(0.08, r_top - 8.5 * r_h, "Showing 1 to 8 of 24 Seeded FAQs  •  Database: SQLite 3.x (instance/college.db)", 
            fontsize=6.2, color="#64748b", va="center", zorder=3)
    ax.text(0.92, r_top - 8.5 * r_h, "◄ Previous   [1]   2   3   Next ►", ha="right", fontsize=6.2, color="#334155", weight="bold", va="center", zorder=3)

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_ui_admin.png"), bbox_inches="tight")
    plt.close()
    print("[12/12] Generated campusai_ui_admin.png")

create_ui_admin()
print("\n[✓] ALL 12 DIAGRAMS RENDERED TO ABSOLUTE STRUCTURAL PERFECTION!")
