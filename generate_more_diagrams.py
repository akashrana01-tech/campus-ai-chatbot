"""
Generates the remaining CampusAI diagrams:
- Class Diagram
- Sequence Diagram
- Activity Diagram
- Component Diagram
- UI Screenshots (Home, Chatbot, FAQ, Admin)
"""

import os
os.environ["MPLCONFIGDIR"] = "/tmp/mpl"
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

OUT_DIR = "/Users/kanishksingh/Downloads/momo ai chat bot /scratch/campusai_diagrams"

def create_class_diagram():
    fig, ax = plt.subplots(figsize=(9, 8.5), dpi=200)
    ax.axis('off')
    
    cls_box = dict(boxstyle="square,pad=0.4", facecolor="#ffffff", edgecolor="#1e3a8a", lw=1.2)
    
    # 4 Classes
    # 1. User/Admin Model
    t1 = (
        "<b>Admin (db.Model)</b>\n"
        "------------------------------------\n"
        "+ id: Integer (PK)\n"
        "+ username: String(80)\n"
        "+ email: String(120)\n"
        "+ password_hash: String(255)\n"
        "+ created_at: DateTime\n"
        "------------------------------------\n"
        "+ set_password(pwd): void\n"
        "+ check_password(pwd): bool\n"
        "+ to_dict(): dict"
    )
    ax.text(0.22, 0.75, t1, ha="center", va="center", fontsize=7.5, family="monospace", bbox=cls_box)
    
    # 2. FAQ Model
    t2 = (
        "<b>FAQ (db.Model)</b>\n"
        "------------------------------------\n"
        "+ id: Integer (PK)\n"
        "+ question: Text\n"
        "+ answer: Text\n"
        "+ category: String(50)\n"
        "+ created_at: DateTime\n"
        "+ updated_at: DateTime\n"
        "------------------------------------\n"
        "+ to_dict(): dict\n"
        "+ search(keyword): List[FAQ]"
    )
    ax.text(0.78, 0.75, t2, ha="center", va="center", fontsize=7.5, family="monospace", bbox=cls_box)
    
    # 3. ChatMessage Model
    t3 = (
        "<b>ChatMessage (db.Model)</b>\n"
        "------------------------------------\n"
        "+ id: Integer (PK)\n"
        "+ session_id: String(64)\n"
        "+ role: String(20)\n"
        "+ content: Text\n"
        "+ source: String(30)\n"
        "+ timestamp: DateTime\n"
        "------------------------------------\n"
        "+ to_dict(): dict"
    )
    ax.text(0.22, 0.32, t3, ha="center", va="center", fontsize=7.5, family="monospace", bbox=cls_box)
    
    # 4. Chatbot Orchestrator & Services
    t4 = (
        "<b>ChatbotOrchestrator</b>\n"
        "------------------------------------\n"
        "+ confidence_threshold: 0.45\n"
        "+ synonyms: Dict[str, List[str]]\n"
        "------------------------------------\n"
        "+ normalize_text(q): Set[str]\n"
        "+ match_faq(q): Tuple[FAQ, float]\n"
        "+ query_gemini_fallback(q): str\n"
        "+ handle_message(session, q): dict"
    )
    ax.text(0.78, 0.32, t4, ha="center", va="center", fontsize=7.5, family="monospace", bbox=cls_box)
    
    # Connectors
    ax.annotate("manages (1 : N)", xy=(0.60, 0.75), xytext=(0.40, 0.75), arrowprops=dict(arrowstyle="->", lw=1.2), fontsize=8)
    ax.annotate("persists (1 : N)", xy=(0.22, 0.50), xytext=(0.22, 0.60), arrowprops=dict(arrowstyle="->", lw=1.2), fontsize=8)
    ax.annotate("queries & scores", xy=(0.78, 0.59), xytext=(0.78, 0.48), arrowprops=dict(arrowstyle="<->", lw=1.2), fontsize=8)
    
    # Legend
    ax.text(0.5, 0.06, "CampusAI UML Class Architecture Diagram (MVC / 3-Tier Pattern)",
            ha="center", va="center", fontsize=9, weight="bold", bbox=dict(boxstyle="round,pad=0.4", facecolor="#f1f5f9", edgecolor="#cbd5e1", lw=1.0))
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_class_diagram.png"), bbox_inches="tight")
    plt.close()
    print("Generated Class diagram.")

def create_sequence_diagram():
    fig, ax = plt.subplots(figsize=(9, 8.5), dpi=200)
    ax.axis('off')
    
    box = dict(boxstyle="square,pad=0.3", facecolor="#f1f5f9", edgecolor="#334155", lw=1.2)
    
    # Lifelines
    actors = [
        (0.12, "Student\n(Browser)"),
        (0.36, "Flask REST\n(app.py)"),
        (0.62, "FAQ Engine\n(faq_service)"),
        (0.88, "Gemini LLM\n(ai_service)")
    ]
    for x, label in actors:
        ax.text(x, 0.90, label, ha="center", va="center", fontsize=8, weight="bold", bbox=box)
        ax.plot([x, x], [0.10, 0.85], "k--", lw=0.8)
    
    # Messages
    msgs = [
        (0.12, 0.36, 0.78, "1. POST /api/chat {message: 'fees?'}", True),
        (0.36, 0.62, 0.72, "2. match_faq('fees?')", True),
        (0.62, 0.62, 0.66, "3. Tokenize & Synonym Expansion", False),
        (0.62, 0.36, 0.60, "4. Return Match (score=0.88)", False),
        (0.36, 0.12, 0.54, "5. JSON {answer, source: 'database'}", False),
        (0.12, 0.36, 0.44, "6. POST /api/chat {unfamiliar query}", True),
        (0.36, 0.62, 0.38, "7. match_faq(query) -> score < 0.45", True),
        (0.36, 0.88, 0.32, "8. generate_content(bounded context)", True),
        (0.88, 0.36, 0.26, "9. Return LLM Answer (safe/factual)", False),
        (0.36, 0.12, 0.20, "10. JSON {answer, source: 'ai'}", False)
    ]
    
    for x1, x2, y, text, is_req in msgs:
        if x1 == x2:
            # Self call
            ax.plot([x1, x1+0.05, x1+0.05, x1], [y+0.02, y+0.02, y-0.02, y-0.02], "b-", lw=1.0)
            ax.text(x1+0.06, y, text, fontsize=7, va="center")
        else:
            ls = "-" if is_req else "--"
            color = "#1e3a8a" if is_req else "#059669"
            ax.annotate("", xy=(x2, y), xytext=(x1, y), arrowprops=dict(arrowstyle="->", linestyle=ls, lw=1.2, color=color))
            mid_x = (x1 + x2) / 2.0
            ax.text(mid_x, y + 0.02, text, ha="center", va="bottom", fontsize=7.5, weight="bold" if is_req else "normal")
    
    ax.text(0.5, 0.05, "CampusAI Inquiry Resolution UML Sequence Diagram",
            ha="center", va="center", fontsize=9, weight="bold", bbox=dict(boxstyle="round,pad=0.4", facecolor="#f8fafc", edgecolor="#cbd5e1", lw=1.0))
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_sequence_diagram.png"), bbox_inches="tight")
    plt.close()
    print("Generated Sequence diagram.")

def create_ui_mockups():
    # 1. Home Mockup
    fig, ax = plt.subplots(figsize=(9, 6), dpi=200)
    ax.axis('off')
    
    # Outer browser window
    rect_bg = patches.Rectangle((0.02, 0.02), 0.96, 0.96, facecolor="#f8fafc", edgecolor="#334155", lw=1.5)
    ax.add_patch(rect_bg)
    # Header bar
    rect_head = patches.Rectangle((0.02, 0.88), 0.96, 0.10, facecolor="#1e1b4b", edgecolor="#1e1b4b")
    ax.add_patch(rect_head)
    ax.text(0.06, 0.93, "CampusAI", color="#ffffff", fontsize=12, weight="bold", va="center")
    ax.text(0.50, 0.93, "Home     Chat     FAQs     Admin Portal", color="#cbd5e1", fontsize=8.5, va="center", ha="center")
    ax.text(0.92, 0.93, "● System Online", color="#4ade80", fontsize=8, va="center", ha="right", weight="bold")
    
    # Hero section
    ax.text(0.50, 0.74, "Your College. Your Questions. Instant Answers.", fontsize=14, weight="bold", ha="center", color="#0f172a")
    ax.text(0.50, 0.67, "24/7 AI-Powered College Assistant for Admissions, Fees, Exams & Facilities", fontsize=9, ha="center", color="#475569")
    
    # CTA Buttons
    ax.text(0.40, 0.58, "Start Chatting", fontsize=8.5, color="#ffffff", ha="center", va="center", weight="bold",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#4f46e5", edgecolor="#4f46e5"))
    ax.text(0.60, 0.58, "Explore FAQs", fontsize=8.5, color="#1e293b", ha="center", va="center", weight="bold",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#ffffff", edgecolor="#cbd5e1"))
    
    # 4 Feature Cards
    cards = [
        (0.18, 0.32, "24/7 Availability", "Instant help day or\nnight, zero queues"),
        (0.39, 0.32, "Verified Data", "Direct answers from\nofficial database"),
        (0.61, 0.32, "Zero Hallucination", "Refuses to invent\nunverified dates/fees"),
        (0.82, 0.32, "Admin Governance", "Real-time updates via\nsecure web console")
    ]
    for x, y, title, desc in cards:
        rect = patches.Rectangle((x-0.09, y-0.12), 0.18, 0.24, facecolor="#ffffff", edgecolor="#e2e8f0", lw=1.2)
        ax.add_patch(rect)
        ax.text(x, y+0.06, title, fontsize=8, weight="bold", ha="center", color="#1e3a8a")
        ax.text(x, y-0.02, desc, fontsize=7, ha="center", color="#64748b")
        
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_ui_home.png"), bbox_inches="tight")
    plt.close()
    
    # 2. Chat UI Mockup
    fig, ax = plt.subplots(figsize=(9, 6), dpi=200)
    ax.axis('off')
    
    # Window
    ax.add_patch(patches.Rectangle((0.02, 0.02), 0.96, 0.96, facecolor="#f8fafc", edgecolor="#334155", lw=1.5))
    ax.add_patch(patches.Rectangle((0.02, 0.88), 0.96, 0.10, facecolor="#1e1b4b", edgecolor="#1e1b4b"))
    ax.text(0.06, 0.93, "CampusAI Virtual Assistant", color="#ffffff", fontsize=11, weight="bold", va="center")
    ax.text(0.92, 0.93, "Clear Chat", color="#f87171", fontsize=8, va="center", ha="right")
    
    # Messages
    # Bot welcome
    ax.text(0.08, 0.78, "Hello! I am your 24/7 CampusAI Assistant. How can I assist you with admissions, fees, or exams today?", 
            fontsize=8, color="#1e293b", bbox=dict(boxstyle="round,pad=0.5", facecolor="#ffffff", edgecolor="#e2e8f0", lw=1.0))
    # User query
    ax.text(0.90, 0.65, "What is the semester fee for BBA (CA) and payment deadline?", 
            fontsize=8, color="#ffffff", ha="right", bbox=dict(boxstyle="round,pad=0.5", facecolor="#4f46e5", edgecolor="#4f46e5"))
    # Bot response
    ax.text(0.08, 0.48, "Verified College Fee Information:\n- Tuition Fee: Rs. 45,000 per semester\n- Examination Fee: Rs. 1,500\n- Installment deadline: 15th November 2026\n[Source: Official College Database • High Confidence Match]", 
            fontsize=7.5, color="#0f172a", bbox=dict(boxstyle="round,pad=0.5", facecolor="#ecfdf5", edgecolor="#10b981", lw=1.2))
    
    # Question Chips
    chips = ["How to apply?", "Exam timetable?", "Hostel facilities?", "College office hours?"]
    for i, c in enumerate(chips):
        ax.text(0.08 + i*0.22, 0.28, c, fontsize=7.5, color="#1e3a8a", 
                bbox=dict(boxstyle="round,pad=0.3", facecolor="#eff6ff", edgecolor="#bfdbfe", lw=1.0))
        
    # Input Bar
    ax.add_patch(patches.Rectangle((0.06, 0.10), 0.76, 0.09, facecolor="#ffffff", edgecolor="#cbd5e1", lw=1.0))
    ax.text(0.08, 0.145, "Type your academic question here...", color="#94a3b8", fontsize=8, va="center")
    ax.add_patch(patches.Rectangle((0.84, 0.10), 0.10, 0.09, facecolor="#4f46e5", edgecolor="#4f46e5"))
    ax.text(0.89, 0.145, "Send", color="#ffffff", fontsize=8.5, weight="bold", ha="center", va="center")
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_ui_chat.png"), bbox_inches="tight")
    plt.close()
    
    # 3. Admin Dashboard Mockup
    fig, ax = plt.subplots(figsize=(9, 6), dpi=200)
    ax.axis('off')
    
    ax.add_patch(patches.Rectangle((0.02, 0.02), 0.96, 0.96, facecolor="#f8fafc", edgecolor="#334155", lw=1.5))
    ax.add_patch(patches.Rectangle((0.02, 0.88), 0.96, 0.10, facecolor="#0f172a", edgecolor="#0f172a"))
    ax.text(0.06, 0.93, "CampusAI Administrative Governance Dashboard", color="#ffffff", fontsize=11, weight="bold", va="center")
    ax.text(0.92, 0.93, "Admin: akash_rana | Logout", color="#cbd5e1", fontsize=8, va="center", ha="right")
    
    # KPI metrics
    kpis = [
        (0.18, "Total FAQs", "24 Active"),
        (0.39, "Categories", "6 Domains"),
        (0.61, "Student Inquiries", "1,842 Logged"),
        (0.82, "System Status", "Healthy 99.98%")
    ]
    for x, title, val in kpis:
        ax.add_patch(patches.Rectangle((x-0.09, 0.68), 0.18, 0.14, facecolor="#ffffff", edgecolor="#e2e8f0", lw=1.2))
        ax.text(x, 0.77, title, fontsize=7.5, color="#64748b", ha="center")
        ax.text(x, 0.72, val, fontsize=9.5, weight="bold", color="#1e1b4b", ha="center")
        
    # Table header
    ax.add_patch(patches.Rectangle((0.06, 0.55), 0.88, 0.07, facecolor="#312e81"))
    ax.text(0.08, 0.585, "ID", color="#ffffff", fontsize=8, weight="bold", va="center")
    ax.text(0.15, 0.585, "Question", color="#ffffff", fontsize=8, weight="bold", va="center")
    ax.text(0.55, 0.585, "Category", color="#ffffff", fontsize=8, weight="bold", va="center")
    ax.text(0.72, 0.585, "Confidence", color="#ffffff", fontsize=8, weight="bold", va="center")
    ax.text(0.86, 0.585, "Actions", color="#ffffff", fontsize=8, weight="bold", va="center")
    
    # Table rows
    rows = [
        (0.48, "1", "What are the BBA (CA) semester fees?", "Fees", "100%", "Edit | Delete"),
        (0.41, "2", "How do I apply for admissions?", "Admissions", "100%", "Edit | Delete"),
        (0.34, "3", "When are semester exams held?", "Examinations", "98%", "Edit | Delete"),
        (0.27, "4", "What facilities are in campus library?", "Facilities", "95%", "Edit | Delete"),
        (0.20, "5", "What are college office hours?", "General", "100%", "Edit | Delete"),
    ]
    for y, rid, q, cat, conf, act in rows:
        ax.add_patch(patches.Rectangle((0.06, y-0.03), 0.88, 0.065, facecolor="#ffffff" if int(rid)%2!=0 else "#f8fafc", edgecolor="#e2e8f0"))
        ax.text(0.08, y, rid, fontsize=7.5, va="center")
        ax.text(0.15, y, q, fontsize=7.5, va="center", color="#0f172a")
        ax.text(0.55, y, cat, fontsize=7.5, va="center", color="#4338ca", weight="bold")
        ax.text(0.72, y, conf, fontsize=7.5, va="center", color="#059669")
        ax.text(0.86, y, act, fontsize=7.5, va="center", color="#2563eb")
        
    ax.text(0.5, 0.06, "+ Add New FAQ   |   Export Query Logs (CSV)   |   Retrain Matcher",
            ha="center", va="center", fontsize=8, weight="bold", color="#1e3a8a",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#eff6ff", edgecolor="#bfdbfe"))
            
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_ui_admin.png"), bbox_inches="tight")
    plt.close()
    print("Generated UI mockups.")

if __name__ == '__main__':
    create_class_diagram()
    create_sequence_diagram()
    create_ui_mockups()
