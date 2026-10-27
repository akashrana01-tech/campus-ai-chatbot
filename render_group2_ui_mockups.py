"""
CampusAI (Group 2) - Modern UI Screenshots Generator (Emerald & Amber Theme)
Generates high-resolution UI screenshots matching the real CampusAI web application:
1. campusai_ui_home.png: Landing portal with 8 academic domain cards, live health telemetry, and hero showcase.
2. campusai_ui_chat.png: Interactive student chat interface with category quick filter pills, amber user bubble, emerald assistant card with verified badge, mic button, and audio listen.
3. campusai_ui_admin.png: Admin command center with 26 seeded FAQs across 8 categories, KPI metric cards, and CSV export.
"""

import os
os.environ["MPLCONFIGDIR"] = "/tmp/mpl"
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle

OUT_DIR = "/Users/kanishksingh/Downloads/momo ai chat bot /scratch/campusai_diagrams"
os.makedirs(OUT_DIR, exist_ok=True)

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

CLR_BLUE = "#1d4ed8"
CLR_WHITE = "#ffffff"


# ==============================================================================
# 1. UI MOCKUP: HOME SCREEN (Emerald & Amber Portal)
# ==============================================================================
def render_ui_home():
    fig, ax = plt.subplots(figsize=(10.0, 6.8), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Browser Outer Frame
    frame = FancyBboxPatch((0.02, 0.02), 0.96, 0.96, boxstyle="round,pad=0.01,rounding_size=0.015",
                           facecolor=CLR_WHITE, edgecolor=CLR_SLATE, lw=1.5, zorder=1)
    ax.add_patch(frame)

    # Browser Title Bar (macOS style)
    tbar = Rectangle((0.02, 0.91), 0.96, 0.07, facecolor=CLR_SLATE_DARK, edgecolor=CLR_SLATE_DARK, zorder=2)
    ax.add_patch(tbar)
    ax.add_patch(Circle((0.050, 0.945), 0.010, facecolor="#ef4444", edgecolor="#b91c1c", lw=0.5, zorder=3))
    ax.add_patch(Circle((0.075, 0.945), 0.010, facecolor="#f59e0b", edgecolor="#d97706", lw=0.5, zorder=3))
    ax.add_patch(Circle((0.100, 0.945), 0.010, facecolor="#10b981", edgecolor="#059669", lw=0.5, zorder=3))

    # URL address bar
    url_box = FancyBboxPatch((0.16, 0.925), 0.68, 0.040, boxstyle="round,pad=0.008,rounding_size=0.01",
                             facecolor="#1e293b", edgecolor="#475569", lw=0.8, zorder=3)
    ax.add_patch(url_box)
    ax.text(0.18, 0.945, "[SECURE]  http://localhost:5000/  •  CampusAI | G H Raisoni International Skill Tech University",
            va="center", fontsize=7.2, color="#cbd5e1", zorder=4)
    ax.text(0.93, 0.945, "v2.5 (Emerald)", ha="right", va="center", fontsize=7.0, weight="bold", color=CLR_EMERALD_BORDER, zorder=4)

    # Navigation Bar
    ax.add_patch(Rectangle((0.02, 0.83), 0.96, 0.08, facecolor=CLR_WHITE, edgecolor="#e2e8f0", lw=1.0, zorder=2))
    ax.text(0.06, 0.87, "CampusAI Assistant", fontsize=10.5, weight="bold", color=CLR_EMERALD_DARK, va="center", zorder=3)
    ax.text(0.94, 0.87, "Home    |    AI Chatbot    |    FAQs Directory    |    Admin Portal",
            ha="right", va="center", fontsize=7.5, weight="bold", color=CLR_SLATE, zorder=3)

    # Hero Banner
    hero_bg = Rectangle((0.02, 0.50), 0.96, 0.33, facecolor="#f0fdf4", edgecolor="#bbf7d0", lw=0.8, zorder=2)
    ax.add_patch(hero_bg)

    badge = FancyBboxPatch((0.06, 0.77), 0.38, 0.035, boxstyle="round,pad=0.006,rounding_size=0.008",
                           facecolor=CLR_AMBER_LIGHT, edgecolor=CLR_AMBER_BORDER, lw=1.0, zorder=3)
    ax.add_patch(badge)
    ax.text(0.08, 0.787, "• BBA CA Academic Year 2025-26 • 24/7 AI-Powered Concierge",
            fontsize=7.0, weight="bold", color=CLR_AMBER_DARK, va="center", zorder=4)

    ax.text(0.06, 0.71, "Your College. Your Questions. Instant Answers.", fontsize=14.5, weight="bold", color=CLR_EMERALD_DARK, va="center", zorder=3)
    ax.text(0.06, 0.65, "Instant, authoritative academic information across 8 college domains: Admissions, Fees, Courses, Exams,\nPlacements, Scholarships, Hostels & Helpdesk. Powered by local Jaccard NLP & Google Gemini 2.5 Flash.",
            fontsize=7.8, color=CLR_SLATE, va="center", zorder=3)

    # CTA Buttons (Emerald & Amber)
    btn1 = FancyBboxPatch((0.06, 0.54), 0.22, 0.055, boxstyle="round,pad=0.008,rounding_size=0.01",
                          facecolor=CLR_EMERALD_DARK, edgecolor=CLR_EMERALD, lw=1.0, zorder=3)
    ax.add_patch(btn1)
    ax.text(0.17, 0.567, "Start AI Chatbot", ha="center", va="center", fontsize=8.0, weight="bold", color=CLR_WHITE, zorder=4)

    btn2 = FancyBboxPatch((0.30, 0.54), 0.22, 0.055, boxstyle="round,pad=0.008,rounding_size=0.01",
                          facecolor=CLR_WHITE, edgecolor=CLR_AMBER, lw=1.2, zorder=3)
    ax.add_patch(btn2)
    ax.text(0.41, 0.567, "Explore 26 Verified FAQs", ha="center", va="center", fontsize=8.0, weight="bold", color=CLR_AMBER_DARK, zorder=4)

    # 8 Academic Domain Cards Grid (4 columns x 2 rows)
    ax.text(0.06, 0.46, "Explore Campus Knowledge Domains (8 Official Academic Desks)", fontsize=9.5, weight="bold", color=CLR_SLATE_DARK, va="center", zorder=3)

    domain_cards = [
        ("1. Admissions Desk", "Eligibility, deadlines, merit criteria & documents", 0.06, 0.32),
        ("2. Courses & Syllabus", "BBA CA, BCA, subjects, practicals & credit hours", 0.29, 0.32),
        ("3. Fee Structure", "Tuition fees, installment dates & refund policies", 0.52, 0.32),
        ("4. Examination Cell", "Timetables, hall tickets, revaluation & rules", 0.75, 0.32),
        ("5. Placements Desk", "Recruiters, packages, training & aptitude drives", 0.06, 0.17),
        ("6. Scholarships Desk", "Merit freeships, EBC & reserved fee concessions", 0.29, 0.17),
        ("7. Campus Hostels", "Hostel rooms, mess fees, Wi-Fi & security rules", 0.52, 0.17),
        ("8. Student Helpdesk", "Office timings, certificates & student grievance", 0.75, 0.17),
    ]

    for title, desc, cx, cy in domain_cards:
        card_box = FancyBboxPatch((cx, cy), 0.21, 0.125, boxstyle="round,pad=0.006,rounding_size=0.008",
                                  facecolor=CLR_WHITE, edgecolor=CLR_EMERALD_BORDER, lw=1.0, zorder=3)
        ax.add_patch(card_box)
        # Top banner of card
        hdr_bar = Rectangle((cx, cy + 0.095), 0.21, 0.030, facecolor=CLR_EMERALD_LIGHT, edgecolor="none", zorder=3)
        ax.add_patch(hdr_bar)
        ax.text(cx + 0.010, cy + 0.110, title, fontsize=7.2, weight="bold", color=CLR_EMERALD_DARK, zorder=4)
        ax.text(cx + 0.010, cy + 0.050, desc, fontsize=6.2, color="#64748b", zorder=4)

    # Live Health Telemetry Footer inside app
    ax.add_patch(Rectangle((0.02, 0.03), 0.96, 0.05, facecolor="#f1f5f9", edgecolor="#e2e8f0", lw=0.8, zorder=2))
    ax.text(0.06, 0.055, "● System Status: Online (SQLite 3.x • Gemini 2.5 Flash Connected • 26 Seeded FAQs • 8 Domains)",
            fontsize=6.8, weight="bold", color=CLR_EMERALD_DARK, va="center", zorder=3)
    ax.text(0.94, 0.055, "Department of Computer Applications • Academic Year 2025-26",
            ha="right", va="center", fontsize=6.8, color="#64748b", zorder=3)

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_ui_home.png"), bbox_inches="tight")
    plt.close()
    print("[1/3] Generated campusai_ui_home.png (8 Domain Cards, Emerald/Amber)")

render_ui_home()


# ==============================================================================
# 2. UI MOCKUP: CHAT INTERFACE (Category Filter Pills, Mic, Amber Bubble)
# ==============================================================================
def render_ui_chat():
    fig, ax = plt.subplots(figsize=(10.0, 7.2), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Browser Outer Frame
    frame = FancyBboxPatch((0.02, 0.02), 0.96, 0.96, boxstyle="round,pad=0.01,rounding_size=0.015",
                           facecolor=CLR_WHITE, edgecolor=CLR_SLATE, lw=1.5, zorder=1)
    ax.add_patch(frame)

    # Browser Title Bar
    tbar = Rectangle((0.02, 0.91), 0.96, 0.07, facecolor=CLR_SLATE_DARK, edgecolor=CLR_SLATE_DARK, zorder=2)
    ax.add_patch(tbar)
    ax.add_patch(Circle((0.050, 0.945), 0.010, facecolor="#ef4444", edgecolor="#b91c1c", lw=0.5, zorder=3))
    ax.add_patch(Circle((0.075, 0.945), 0.010, facecolor="#f59e0b", edgecolor="#d97706", lw=0.5, zorder=3))
    ax.add_patch(Circle((0.100, 0.945), 0.010, facecolor="#10b981", edgecolor="#059669", lw=0.5, zorder=3))

    url_box = FancyBboxPatch((0.16, 0.925), 0.68, 0.040, boxstyle="round,pad=0.008,rounding_size=0.01",
                             facecolor="#1e293b", edgecolor="#475569", lw=0.8, zorder=3)
    ax.add_patch(url_box)
    ax.text(0.18, 0.945, "[SECURE]  http://localhost:5000/chat  •  CampusAI Virtual Chatbot Assistant",
            va="center", fontsize=7.2, color="#cbd5e1", zorder=4)

    # Chat Header Bar
    ax.add_patch(Rectangle((0.02, 0.83), 0.96, 0.08, facecolor=CLR_WHITE, edgecolor="#e2e8f0", lw=1.0, zorder=2))
    ax.text(0.06, 0.88, "CampusAI Student Assistant", fontsize=10.5, weight="bold", color=CLR_EMERALD_DARK, va="center", zorder=3)
    ax.text(0.06, 0.85, "● Active Session (ID: sess_istu_9b81) • Dual-Tier Hybrid Engine (<15ms)", fontsize=6.8, color=CLR_EMERALD, va="center", zorder=3)

    btn_clear = FancyBboxPatch((0.84, 0.845), 0.12, 0.042, boxstyle="round,pad=0.006,rounding_size=0.008",
                               facecolor="#fef2f2", edgecolor="#fca5a5", lw=1.0, zorder=3)
    ax.add_patch(btn_clear)
    ax.text(0.90, 0.866, "Clear Chat", ha="center", va="center", fontsize=7.0, weight="bold", color="#dc2626", zorder=4)

    # CATEGORY QUICK-FILTER PILLS BAR
    ax.add_patch(Rectangle((0.02, 0.77), 0.96, 0.06, facecolor="#f8fafc", edgecolor="#e2e8f0", lw=0.8, zorder=2))
    ax.text(0.04, 0.80, "Quick Filter:", fontsize=6.8, weight="bold", color=CLR_SLATE, va="center", zorder=3)

    pills = ["All", "Admissions", "Fees", "Courses", "Exams", "Placements", "Scholarships", "Hostels", "Helpdesk"]
    for idx, p in enumerate(pills):
        px = 0.13 + idx * 0.095
        is_active = (p == "Fees")
        p_bg = CLR_EMERALD_DARK if is_active else CLR_WHITE
        p_fg = CLR_WHITE if is_active else CLR_SLATE_DARK
        p_border = CLR_EMERALD if is_active else CLR_SLATE_BORDER
        p_box = FancyBboxPatch((px, 0.78), 0.088, 0.038, boxstyle="round,pad=0.004,rounding_size=0.008",
                               facecolor=p_bg, edgecolor=p_border, lw=0.9, zorder=3)
        ax.add_patch(p_box)
        ax.text(px + 0.044, 0.799, p, ha="center", va="center", fontsize=6.2, weight="bold" if is_active else "normal", color=p_fg, zorder=4)

    # Chat Messages Canvas
    chat_bg = Rectangle((0.02, 0.18), 0.96, 0.59, facecolor="#fafafa", edgecolor="#e2e8f0", lw=0.8, zorder=2)
    ax.add_patch(chat_bg)

    # Message 1: Student Question (Right aligned, Amber bubble)
    student_bubble = FancyBboxPatch((0.44, 0.66), 0.50, 0.08, boxstyle="round,pad=0.01,rounding_size=0.015",
                                    facecolor=CLR_AMBER, edgecolor=CLR_AMBER_DARK, lw=1.0, zorder=3)
    ax.add_patch(student_bubble)
    ax.text(0.92, 0.715, "Student (Akash Rana • BBA CA)", ha="right", va="center", fontsize=6.5, weight="bold", color=CLR_AMBER_LIGHT, zorder=4)
    ax.text(0.92, 0.685, "What is the fee structure for BBA (CA) and payment deadline?",
            ha="right", va="center", fontsize=7.8, color=CLR_WHITE, zorder=4)

    # Message 2: CampusAI Assistant Response (Left aligned, White card with Emerald Top Banner)
    bot_card = FancyBboxPatch((0.06, 0.32), 0.66, 0.30, boxstyle="round,pad=0.01,rounding_size=0.015",
                              facecolor=CLR_WHITE, edgecolor=CLR_EMERALD_BORDER, lw=1.2, zorder=3)
    ax.add_patch(bot_card)

    # Top border strip on card
    ax.add_patch(Rectangle((0.06, 0.605), 0.66, 0.015, facecolor=CLR_EMERALD, edgecolor="none", zorder=4))

    # Verified Badge & Confidence Telemetry
    v_badge = FancyBboxPatch((0.08, 0.565), 0.40, 0.032, boxstyle="round,pad=0.005,rounding_size=0.006",
                             facecolor=CLR_EMERALD_LIGHT, edgecolor=CLR_EMERALD_BORDER, lw=1.0, zorder=4)
    ax.add_patch(v_badge)
    ax.text(0.09, 0.581, "[✓ VERIFIED FAQ MATCH] • Domain: Fees • Score: 92% • Latency: 11ms",
            fontsize=6.5, weight="bold", color=CLR_EMERALD_DARK, va="center", zorder=5)

    bot_text = (
        "Here is the authoritative fee structure for Bachelor of Business Administration\n"
        "(Computer Applications) — BBA (CA) for Academic Year 2025-26:\n\n"
        "• Tuition Fee: Rs. 45,000 per semester (Rs. 90,000 annually)\n"
        "• Examination Fee: Rs. 1,500 per semester\n"
        "• Library & Computing Laboratory Deposit: Rs. 5,000 (Refundable)\n"
        "• First Installment Deadline: 15th November 2026\n\n"
        "Payments can be completed via student ERP online gateway or college accounts counter."
    )
    ax.text(0.08, 0.46, bot_text, fontsize=6.8, color=CLR_SLATE_DARK, va="center", zorder=4)

    # Audio Listen Button & Feedback Buttons
    aud_btn = FancyBboxPatch((0.08, 0.34), 0.14, 0.028, boxstyle="round,pad=0.004,rounding_size=0.006",
                             facecolor=CLR_EMERALD_LIGHT, edgecolor=CLR_EMERALD, lw=0.9, zorder=4)
    ax.add_patch(aud_btn)
    ax.text(0.15, 0.354, "[LISTEN] Audio TTS", ha="center", va="center", fontsize=6.2, weight="bold", color=CLR_EMERALD_DARK, zorder=5)

    copy_btn = FancyBboxPatch((0.24, 0.34), 0.11, 0.028, boxstyle="round,pad=0.004,rounding_size=0.006",
                              facecolor=CLR_SLATE_LIGHT, edgecolor=CLR_SLATE_BORDER, lw=0.9, zorder=4)
    ax.add_patch(copy_btn)
    ax.text(0.295, 0.354, "[COPY] Answer", ha="center", va="center", fontsize=6.2, color=CLR_SLATE_DARK, zorder=5)

    fb_up = FancyBboxPatch((0.37, 0.34), 0.08, 0.028, boxstyle="round,pad=0.004,rounding_size=0.006",
                           facecolor="#ecfdf5", edgecolor="#a7f3d0", lw=0.8, zorder=4)
    ax.add_patch(fb_up)
    ax.text(0.41, 0.354, "[+1] Helpful", ha="center", va="center", fontsize=6.0, weight="bold", color="#065f46", zorder=5)

    # Suggestion Chips Row
    ax.text(0.06, 0.26, "Suggested Follow-Up Inquiries:", fontsize=6.8, weight="bold", color="#64748b", zorder=3)
    chips = [
        "How do I apply for admissions?",
        "What companies visit for placements?",
        "Are merit scholarships available?",
        "Hostel fee & room options?"
    ]
    for idx, c in enumerate(chips):
        cx = 0.06 + idx * 0.225
        chip_box = FancyBboxPatch((cx, 0.205), 0.215, 0.038, boxstyle="round,pad=0.005,rounding_size=0.008",
                                  facecolor=CLR_EMERALD_LIGHT, edgecolor=CLR_EMERALD_BORDER, lw=0.9, zorder=3)
        ax.add_patch(chip_box)
        ax.text(cx + 0.107, 0.224, c, ha="center", va="center", fontsize=6.2, color=CLR_EMERALD_DARK, zorder=4)

    # Floating Input Bar with Pulsing Mic Button
    in_box = FancyBboxPatch((0.06, 0.05), 0.76, 0.09, boxstyle="round,pad=0.008,rounding_size=0.015",
                            facecolor=CLR_WHITE, edgecolor=CLR_EMERALD, lw=1.3, zorder=3)
    ax.add_patch(in_box)
    ax.text(0.09, 0.095, "Type your academic question here (e.g. syllabus, exams, fees, placements, scholarships)...",
            fontsize=7.2, color="#94a3b8", va="center", zorder=4)

    # Mic Button (Pulsing Amber)
    mic_btn = Circle((0.78, 0.095), 0.024, facecolor=CLR_AMBER_LIGHT, edgecolor=CLR_AMBER, lw=1.2, zorder=4)
    ax.add_patch(mic_btn)
    ax.text(0.78, 0.095, "[MIC]", ha="center", va="center", fontsize=6.5, weight="bold", color=CLR_AMBER_DARK, zorder=5)

    # Send Button (Emerald)
    send_btn = FancyBboxPatch((0.84, 0.05), 0.10, 0.09, boxstyle="round,pad=0.008,rounding_size=0.015",
                              facecolor=CLR_EMERALD_DARK, edgecolor=CLR_EMERALD, lw=1.0, zorder=3)
    ax.add_patch(send_btn)
    ax.text(0.89, 0.095, "Send", ha="center", va="center", fontsize=7.8, weight="bold", color=CLR_WHITE, zorder=4)

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_ui_chat.png"), bbox_inches="tight")
    plt.close()
    print("[2/3] Generated campusai_ui_chat.png (Category Pills, Mic, Amber Bubble)")

render_ui_chat()


# ==============================================================================
# 3. UI MOCKUP: ADMIN DASHBOARD (26 FAQs across 8 Categories)
# ==============================================================================
def render_ui_admin():
    fig, ax = plt.subplots(figsize=(10.0, 7.2), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Browser Outer Frame
    frame = FancyBboxPatch((0.02, 0.02), 0.96, 0.96, boxstyle="round,pad=0.01,rounding_size=0.015",
                           facecolor=CLR_WHITE, edgecolor=CLR_SLATE, lw=1.5, zorder=1)
    ax.add_patch(frame)

    # Browser Title Bar
    tbar = Rectangle((0.02, 0.91), 0.96, 0.07, facecolor=CLR_SLATE_DARK, edgecolor=CLR_SLATE_DARK, zorder=2)
    ax.add_patch(tbar)
    ax.add_patch(Circle((0.050, 0.945), 0.010, facecolor="#ef4444", edgecolor="#b91c1c", lw=0.5, zorder=3))
    ax.add_patch(Circle((0.075, 0.945), 0.010, facecolor="#f59e0b", edgecolor="#d97706", lw=0.5, zorder=3))
    ax.add_patch(Circle((0.100, 0.945), 0.010, facecolor="#10b981", edgecolor="#059669", lw=0.5, zorder=3))

    url_box = FancyBboxPatch((0.16, 0.925), 0.68, 0.040, boxstyle="round,pad=0.008,rounding_size=0.01",
                             facecolor="#1e293b", edgecolor="#475569", lw=0.8, zorder=3)
    ax.add_patch(url_box)
    ax.text(0.18, 0.945, "[SECURE]  http://localhost:5000/admin  •  CampusAI Administrative Governance Portal",
            va="center", fontsize=7.2, color="#cbd5e1", zorder=4)

    # Admin Navbar
    ax.add_patch(Rectangle((0.02, 0.83), 0.96, 0.08, facecolor=CLR_EMERALD_DARK, edgecolor=CLR_EMERALD_DARK, lw=1.0, zorder=2))
    ax.text(0.06, 0.87, "CampusAI Command Center", fontsize=11.0, weight="bold", color=CLR_WHITE, va="center", zorder=3)
    ax.text(0.94, 0.87, "Super Admin: akash_admin (ID: 1)  |  [ Logout ]",
            ha="right", va="center", fontsize=7.5, color=CLR_AMBER_LIGHT, zorder=3)

    # 4 KPI METRIC CARDS
    kpi_cards = [
        ("TOTAL ACTIVE FAQS", "26", "100% Corpus Verified", 0.06),
        ("KNOWLEDGE DOMAINS", "8", "Admissions, Fees, Placements...", 0.29),
        ("STUDENT INQUIRIES", "1,842", "98.8% Sub-second Speed", 0.52),
        ("SYSTEM HEALTH", "HEALTHY", "Gemini 2.5 API Connected", 0.75),
    ]

    for title, val, sub, cx in kpi_cards:
        k_box = FancyBboxPatch((cx, 0.69), 0.21, 0.11, boxstyle="round,pad=0.006,rounding_size=0.008",
                               facecolor=CLR_WHITE, edgecolor=CLR_SLATE_BORDER, lw=1.0, zorder=3)
        ax.add_patch(k_box)
        ax.text(cx + 0.015, 0.775, title, fontsize=6.5, weight="bold", color="#64748b", zorder=4)
        ax.text(cx + 0.015, 0.740, val, fontsize=13.0, weight="bold", color=CLR_EMERALD_DARK if val != "HEALTHY" else "#059669", zorder=4)
        ax.text(cx + 0.015, 0.708, sub, fontsize=6.0, color="#64748b", zorder=4)

    # Table Controls Header
    ax.text(0.06, 0.645, "Manage Academic FAQ Knowledge Base (CRUD Operations)", fontsize=9.5, weight="bold", color=CLR_SLATE_DARK, va="center", zorder=3)

    btn_add = FancyBboxPatch((0.68, 0.630), 0.12, 0.038, boxstyle="round,pad=0.005,rounding_size=0.006",
                             facecolor=CLR_EMERALD_DARK, edgecolor=CLR_EMERALD, lw=1.0, zorder=3)
    ax.add_patch(btn_add)
    ax.text(0.74, 0.649, "+ Add New FAQ", ha="center", va="center", fontsize=6.8, weight="bold", color=CLR_WHITE, zorder=4)

    btn_csv = FancyBboxPatch((0.82, 0.630), 0.12, 0.038, boxstyle="round,pad=0.005,rounding_size=0.006",
                             facecolor=CLR_WHITE, edgecolor=CLR_SLATE_BORDER, lw=1.0, zorder=3)
    ax.add_patch(btn_csv)
    ax.text(0.88, 0.649, "Export CSV", ha="center", va="center", fontsize=6.8, weight="bold", color=CLR_SLATE_DARK, zorder=4)

    # FAQ DATA TABLE (8 Sample Rows across Categories)
    tbl_top = 0.61
    row_h = 0.045
    col_w = [0.05, 0.42, 0.15, 0.14, 0.16]

    headers = ["ID", "Question / Inquiry Prompt", "Category", "Source", "Actions"]
    curr_x = 0.05
    for c_idx, h in enumerate(headers):
        w = col_w[c_idx]
        ax.add_patch(Rectangle((curr_x, tbl_top - row_h), w, row_h, facecolor=CLR_EMERALD_DARK, edgecolor=CLR_SLATE_BORDER, lw=0.5, zorder=3))
        ax.text(curr_x + w/2, tbl_top - row_h/2, h, ha="center", va="center", fontsize=6.8, weight="bold", color=CLR_WHITE, zorder=4)
        curr_x += w

    table_rows = [
        ("1", "What are the BBA (CA) semester fees?", "Fees", "● Database", "Edit  |  Delete"),
        ("2", "How do I apply for admissions to BCA / BBA CA?", "Admissions", "● Database", "Edit  |  Delete"),
        ("3", "When are semester III theory examinations scheduled?", "Examinations", "● Database", "Edit  |  Delete"),
        ("4", "What companies visit campus for placements?", "Placements", "● Database", "Edit  |  Delete"),
        ("5", "What are the eligibility criteria for government scholarships?", "Scholarships", "● Database", "Edit  |  Delete"),
        ("6", "What are the hostel room sharing and mess charges?", "Hostels", "● Database", "Edit  |  Delete"),
        ("7", "What are the central library working hours and rules?", "Facilities", "● Database", "Edit  |  Delete"),
        ("8", "Whom should I contact for student fee concession help?", "Helpdesk", "● Database", "Edit  |  Delete"),
    ]

    for r_idx, row in enumerate(table_rows):
        curr_x = 0.05
        y_pos = tbl_top - (r_idx + 2) * row_h
        bg = CLR_WHITE if r_idx % 2 == 0 else "#f8fafc"
        for c_idx, cell in enumerate(row):
            w = col_w[c_idx]
            ax.add_patch(Rectangle((curr_x, y_pos), w, row_h, facecolor=bg, edgecolor="#e2e8f0", lw=0.5, zorder=3))
            is_action = (c_idx == 4)
            fg = CLR_EMERALD if cell.startswith("●") else (CLR_BLUE if is_action else CLR_SLATE_DARK)
            ax.text(curr_x + (0.010 if c_idx == 1 else w/2), y_pos + row_h/2, cell,
                    ha="left" if c_idx == 1 else "center", va="center",
                    fontsize=6.5, weight="bold" if is_action or c_idx == 0 else "normal", color=fg, zorder=4)
            curr_x += w

    # Pagination Footer
    ax.text(0.06, 0.16, "Showing 1 to 8 of 26 Seeded FAQs • Database: SQLite 3.x (instance/campusai.db)", fontsize=6.5, color="#64748b", zorder=3)
    ax.text(0.94, 0.16, "« Previous   [1]   2   3   Next »", ha="right", fontsize=6.8, weight="bold", color=CLR_EMERALD_DARK, zorder=3)

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_ui_admin.png"), bbox_inches="tight")
    plt.close()
    print("[3/3] Generated campusai_ui_admin.png (26 FAQs across 8 Categories, Emerald/Amber)")

render_ui_admin()
print("[✓] ALL 3 UI MOCKUPS RENDERED PERFECTLY!")
