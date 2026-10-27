import os
os.environ["MPLCONFIGDIR"] = "/tmp/mpl"
"""
Generates clean, academic diagram assets for CampusAI project report:
1. Decision Tree Diagram
2. ER Diagram (3NF)
3. Use Case Diagram
4. Class Diagram
5. Sequence Diagram
6. Activity Diagram
7. Component Diagram
8. DFD Level 0 & Level 1 Diagram
9. Architecture Diagram
10. UI Mockups (Home, Chatbot, Admin)
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

OUT_DIR = "/Users/kanishksingh/Downloads/momo ai chat bot /scratch/campusai_diagrams"
os.makedirs(OUT_DIR, exist_ok=True)

def create_decision_tree():
    fig, ax = plt.subplots(figsize=(8.5, 9.5), dpi=200)
    ax.axis('off')
    
    # Styles
    box_blue = dict(boxstyle="round,pad=0.5", facecolor="#1e3a8a", edgecolor="#1e1b4b", lw=1.5)
    box_proc = dict(boxstyle="square,pad=0.4", facecolor="#eff6ff", edgecolor="#3b82f6", lw=1.2)
    box_cond = dict(boxstyle="round4,pad=0.4", facecolor="#fef3c7", edgecolor="#d97706", lw=1.2)
    box_green = dict(boxstyle="round,pad=0.4", facecolor="#ecfdf5", edgecolor="#059669", lw=1.2)
    box_red = dict(boxstyle="round,pad=0.4", facecolor="#fef2f2", edgecolor="#dc2626", lw=1.2)
    
    # Root
    ax.text(0.5, 0.94, "Student Enters Query\n(Text Input / Voice Microphone)", ha="center", va="center", color="white", fontsize=10, weight="bold", bbox=box_blue)
    
    # Step 1: Normalization
    ax.annotate("", xy=(0.5, 0.85), xytext=(0.5, 0.90), arrowprops=dict(arrowstyle="->", lw=1.5, color="#1e293b"))
    ax.text(0.5, 0.82, "Text Normalization & Stop-Word Removal\nDomain Synonym Expansion (Fees, Admissions, Exams, Facilities)", ha="center", va="center", fontsize=8.5, bbox=box_proc)
    
    # Step 2: Scoring
    ax.annotate("", xy=(0.5, 0.74), xytext=(0.5, 0.78), arrowprops=dict(arrowstyle="->", lw=1.5, color="#1e293b"))
    ax.text(0.5, 0.71, "Compute Jaccard Overlap Score (S)\nAgainst Indexed SQLite FAQs Corpus", ha="center", va="center", fontsize=8.5, bbox=box_proc)
    
    # Decision 1
    ax.annotate("", xy=(0.5, 0.62), xytext=(0.5, 0.67), arrowprops=dict(arrowstyle="->", lw=1.5, color="#1e293b"))
    ax.text(0.5, 0.59, "Is Max Score\nS >= 0.45 ?", ha="center", va="center", fontsize=9, weight="bold", bbox=box_cond)
    
    # Yes -> High Confidence Database Match
    ax.annotate("YES\n(High Confidence)", xy=(0.22, 0.46), xytext=(0.40, 0.59), arrowprops=dict(arrowstyle="->", lw=1.5, color="#059669"))
    ax.text(0.22, 0.43, "Tier 1: Deterministic DB Answer\nInstant Retrieval (<20ms)\nVerified Academic Data", ha="center", va="center", fontsize=8.5, bbox=box_green)
    
    # No -> Check LLM
    ax.annotate("NO\n(Score < 0.45)", xy=(0.78, 0.46), xytext=(0.60, 0.59), arrowprops=dict(arrowstyle="->", lw=1.5, color="#dc2626"))
    ax.text(0.78, 0.43, "Is Gemini AI API\nConfigured & Online?", ha="center", va="center", fontsize=8.5, weight="bold", bbox=box_cond)
    
    # AI Yes
    ax.annotate("YES", xy=(0.65, 0.30), xytext=(0.72, 0.38), arrowprops=dict(arrowstyle="->", lw=1.2, color="#059669"))
    ax.text(0.65, 0.27, "Tier 2: Context-Bounded LLM\nStrict Zero-Hallucination Prompt\nFactual Synthesis", ha="center", va="center", fontsize=8, bbox=box_proc)
    
    # AI No / Offline Fallback
    ax.annotate("NO / Outage", xy=(0.88, 0.30), xytext=(0.84, 0.38), arrowprops=dict(arrowstyle="->", lw=1.2, color="#dc2626"))
    ax.text(0.88, 0.27, "Offline Fallback\nLocal Keyword Matcher\nZero Downtime", ha="center", va="center", fontsize=8, bbox=box_proc)
    
    # Merge to Safety Verification
    ax.annotate("", xy=(0.5, 0.16), xytext=(0.22, 0.38), arrowprops=dict(arrowstyle="->", lw=1.2, color="#1e293b"))
    ax.annotate("", xy=(0.5, 0.16), xytext=(0.65, 0.22), arrowprops=dict(arrowstyle="->", lw=1.2, color="#1e293b"))
    ax.annotate("", xy=(0.5, 0.16), xytext=(0.88, 0.22), arrowprops=dict(arrowstyle="->", lw=1.2, color="#1e293b"))
    
    ax.text(0.5, 0.13, "Verified Academic Fact Found?", ha="center", va="center", fontsize=8.5, weight="bold", bbox=box_cond)
    
    # Final Branches
    ax.annotate("YES", xy=(0.28, 0.04), xytext=(0.42, 0.11), arrowprops=dict(arrowstyle="->", lw=1.5, color="#059669"))
    ax.text(0.28, 0.03, "Dispatch Formatted Answer Bubble\nWith Suggestion Chips & Audio", ha="center", va="center", fontsize=8.5, weight="bold", bbox=box_green)
    
    ax.annotate("NO", xy=(0.72, 0.04), xytext=(0.58, 0.11), arrowprops=dict(arrowstyle="->", lw=1.5, color="#dc2626"))
    ax.text(0.72, 0.03, "Polite Academic Referral\nContact College Office: contact@college.edu\nPhone: +91-020-12345678", ha="center", va="center", fontsize=8, bbox=box_red)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_decision_tree.png"), bbox_inches="tight")
    plt.close()
    print("Generated decision tree.")

def create_er_diagram():
    fig, ax = plt.subplots(figsize=(9, 8.5), dpi=200)
    ax.axis('off')
    
    ent_style = dict(boxstyle="round,pad=0.5", facecolor="#e0e7ff", edgecolor="#3730a3", lw=1.5)
    rel_style = dict(boxstyle="round4,pad=0.4", facecolor="#fef3c7", edgecolor="#b45309", lw=1.2)
    attr_style = dict(boxstyle="round,pad=0.3", facecolor="#f8fafc", edgecolor="#64748b", lw=1.0)
    
    # Entities
    ax.text(0.2, 0.75, "ADMINS", ha="center", va="center", fontsize=10, weight="bold", bbox=ent_style)
    ax.text(0.8, 0.75, "FAQS", ha="center", va="center", fontsize=10, weight="bold", bbox=ent_style)
    ax.text(0.2, 0.25, "CHAT_SESSIONS", ha="center", va="center", fontsize=10, weight="bold", bbox=ent_style)
    ax.text(0.8, 0.25, "CHAT_MESSAGES", ha="center", va="center", fontsize=10, weight="bold", bbox=ent_style)
    
    # Relationship: Admin Manages FAQs
    ax.text(0.5, 0.75, "MANAGES\n(1 : N)", ha="center", va="center", fontsize=8.5, weight="bold", bbox=rel_style)
    ax.plot([0.28, 0.43], [0.75, 0.75], "k-", lw=1.2)
    ax.plot([0.57, 0.72], [0.75, 0.75], "k-", lw=1.2)
    
    # Relationship: Session Contains Messages
    ax.text(0.5, 0.25, "CONTAINS\n(1 : N)", ha="center", va="center", fontsize=8.5, weight="bold", bbox=rel_style)
    ax.plot([0.31, 0.43], [0.25, 0.25], "k-", lw=1.2)
    ax.plot([0.57, 0.70], [0.25, 0.25], "k-", lw=1.2)
    
    # Relationship: Query Matches FAQ
    ax.text(0.8, 0.50, "MATCHED IN\n(N : 1)", ha="center", va="center", fontsize=8.5, weight="bold", bbox=rel_style)
    ax.plot([0.8, 0.8], [0.70, 0.56], "k--", lw=1.2)
    ax.plot([0.8, 0.8], [0.44, 0.30], "k--", lw=1.2)
    
    # Attributes for Admins
    ax.text(0.08, 0.88, "id (PK)", fontsize=7.5, bbox=attr_style)
    ax.text(0.08, 0.82, "username", fontsize=7.5, bbox=attr_style)
    ax.text(0.08, 0.76, "email", fontsize=7.5, bbox=attr_style)
    ax.text(0.08, 0.70, "password_hash", fontsize=7.5, bbox=attr_style)
    
    # Attributes for FAQs
    ax.text(0.92, 0.88, "id (PK)", fontsize=7.5, bbox=attr_style)
    ax.text(0.92, 0.82, "question", fontsize=7.5, bbox=attr_style)
    ax.text(0.92, 0.76, "answer", fontsize=7.5, bbox=attr_style)
    ax.text(0.92, 0.70, "category", fontsize=7.5, bbox=attr_style)
    
    # Attributes for Messages
    ax.text(0.92, 0.35, "id (PK)", fontsize=7.5, bbox=attr_style)
    ax.text(0.92, 0.29, "session_id (FK)", fontsize=7.5, bbox=attr_style)
    ax.text(0.92, 0.23, "role (user/bot)", fontsize=7.5, bbox=attr_style)
    ax.text(0.92, 0.17, "content", fontsize=7.5, bbox=attr_style)
    ax.text(0.92, 0.11, "source (db/ai)", fontsize=7.5, bbox=attr_style)
    
    # Legend
    legend_box = dict(boxstyle="square,pad=0.5", facecolor="#f1f5f9", edgecolor="#cbd5e1", lw=1.0)
    ax.text(0.5, 0.05, "CampusAI 3NF Relational ER Architecture\nStrict Referential Integrity • Zero Transitive Dependencies • Indexed Search Fields", 
            ha="center", va="center", fontsize=8.5, weight="bold", bbox=legend_box)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_er_diagram.png"), bbox_inches="tight")
    plt.close()
    print("Generated ER diagram.")

def create_architecture_diagram():
    fig, ax = plt.subplots(figsize=(9, 8.5), dpi=200)
    ax.axis('off')
    
    # 3 Layers
    tier_client = dict(boxstyle="round,pad=0.5", facecolor="#dbeafe", edgecolor="#1d4ed8", lw=1.5)
    tier_server = dict(boxstyle="round,pad=0.5", facecolor="#f3e8ff", edgecolor="#6b21a8", lw=1.5)
    tier_data = dict(boxstyle="round,pad=0.5", facecolor="#fef3c7", edgecolor="#b45309", lw=1.5)
    box_sub = dict(boxstyle="square,pad=0.3", facecolor="#ffffff", edgecolor="#94a3b8", lw=1.0)
    
    # Tier 1: Client
    ax.text(0.5, 0.88, "PRESENTATION TIER (CLIENT BROWSER)", ha="center", va="center", fontsize=10, weight="bold", bbox=tier_client)
    ax.text(0.2, 0.77, "Landing Screen\n(index.html)", ha="center", va="center", fontsize=8, bbox=box_sub)
    ax.text(0.4, 0.77, "Student Chat UI\n(chat.html)", ha="center", va="center", fontsize=8, bbox=box_sub)
    ax.text(0.6, 0.77, "FAQ Directory\n(faqs.html)", ha="center", va="center", fontsize=8, bbox=box_sub)
    ax.text(0.8, 0.77, "Admin Dashboard\n(admin.html)", ha="center", va="center", fontsize=8, bbox=box_sub)
    
    # Arrow 1
    ax.annotate("REST API JSON Requests (Fetch API)", xy=(0.5, 0.65), xytext=(0.5, 0.72),
                ha="center", arrowprops=dict(arrowstyle="<->", lw=1.5, color="#1e293b"), fontsize=8)
    
    # Tier 2: Application Server
    ax.text(0.5, 0.58, "APPLICATION LOGIC TIER (FLASK REST BACKEND)", ha="center", va="center", fontsize=10, weight="bold", bbox=tier_server)
    ax.text(0.25, 0.47, "REST Controller\n(app.py)", ha="center", va="center", fontsize=8, bbox=box_sub)
    ax.text(0.50, 0.47, "NLP FAQ Matcher\n(faq_service.py)", ha="center", va="center", fontsize=8, bbox=box_sub)
    ax.text(0.75, 0.47, "Bounded AI Layer\n(ai_service.py)", ha="center", va="center", fontsize=8, bbox=box_sub)
    
    # Arrow 2
    ax.annotate("SQLAlchemy ORM / SQLite Driver", xy=(0.35, 0.32), xytext=(0.35, 0.41),
                ha="center", arrowprops=dict(arrowstyle="<->", lw=1.5, color="#1e293b"), fontsize=8)
    ax.annotate("Google GenAI HTTPS API", xy=(0.75, 0.32), xytext=(0.75, 0.41),
                ha="center", arrowprops=dict(arrowstyle="<->", lw=1.5, color="#7c3aed"), fontsize=8)
    
    # Tier 3: Data Tier
    ax.text(0.35, 0.22, "DATA STORAGE TIER\nSQLite 3 (3NF Relational Store)\nadmins • faqs • chat_messages • query_logs", 
            ha="center", va="center", fontsize=8.5, weight="bold", bbox=tier_data)
    
    ax.text(0.75, 0.22, "EXTERNAL AI LAYER\nGoogle Gemini 2.5 / 3.8 Flash\nStrict Zero-Hallucination Bounding", 
            ha="center", va="center", fontsize=8.5, weight="bold", bbox=dict(boxstyle="round,pad=0.5", facecolor="#fae8ff", edgecolor="#a855f7", lw=1.5))
    
    # Performance pill
    ax.text(0.5, 0.06, "Sub-Second Latency (<300ms) • PBKDF2 Password Encryption • Offline Resilient Fallback",
            ha="center", va="center", fontsize=8.5, weight="bold", bbox=dict(boxstyle="square,pad=0.4", facecolor="#f8fafc", edgecolor="#64748b", lw=1.0))
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_architecture.png"), bbox_inches="tight")
    plt.close()
    print("Generated architecture diagram.")

def create_dfd_diagram():
    fig, ax = plt.subplots(figsize=(9, 8.5), dpi=200)
    ax.axis('off')
    
    ent = dict(boxstyle="square,pad=0.4", facecolor="#f1f5f9", edgecolor="#334155", lw=1.5)
    proc = dict(boxstyle="circle,pad=0.4", facecolor="#dbeafe", edgecolor="#1d4ed8", lw=1.5)
    store = dict(boxstyle="square,pad=0.3", facecolor="#fef3c7", edgecolor="#b45309", lw=1.2)
    
    # DFD Level 0 (Top half)
    ax.text(0.5, 0.95, "DATA FLOW DIAGRAM (DFD LEVEL 0: CONTEXT DIAGRAM)", ha="center", va="center", fontsize=9.5, weight="bold")
    ax.text(0.15, 0.82, "STUDENT\n(External Entity)", ha="center", va="center", fontsize=8.5, bbox=ent)
    ax.text(0.50, 0.82, "0.0\nCAMPUSAI\nCORE SYSTEM", ha="center", va="center", fontsize=8.5, weight="bold", bbox=proc)
    ax.text(0.85, 0.82, "ADMINISTRATOR\n(External Entity)", ha="center", va="center", fontsize=8.5, bbox=ent)
    
    ax.annotate("Query Message", xy=(0.42, 0.84), xytext=(0.23, 0.84), arrowprops=dict(arrowstyle="->", lw=1.2, color="#1e293b"), fontsize=7.5)
    ax.annotate("Verified Answer Bubble", xy=(0.23, 0.80), xytext=(0.42, 0.80), arrowprops=dict(arrowstyle="->", lw=1.2, color="#1e293b"), fontsize=7.5)
    ax.annotate("FAQ Updates / Auth", xy=(0.58, 0.84), xytext=(0.77, 0.84), arrowprops=dict(arrowstyle="<-", lw=1.2, color="#1e293b"), fontsize=7.5)
    ax.annotate("Analytics & CRUD Status", xy=(0.77, 0.80), xytext=(0.58, 0.80), arrowprops=dict(arrowstyle="<-", lw=1.2, color="#1e293b"), fontsize=7.5)
    
    ax.plot([0.05, 0.95], [0.68, 0.68], "k--", lw=0.75)
    
    # DFD Level 1 (Bottom half)
    ax.text(0.5, 0.64, "DATA FLOW DIAGRAM (DFD LEVEL 1: FUNCTIONAL DECOMPOSITION)", ha="center", va="center", fontsize=9.5, weight="bold")
    
    ax.text(0.15, 0.48, "1.0\nNormalize\n& Tokenize", ha="center", va="center", fontsize=7.5, bbox=proc)
    ax.text(0.40, 0.48, "2.0\nMatch FAQ\nCorpus", ha="center", va="center", fontsize=7.5, bbox=proc)
    ax.text(0.65, 0.48, "3.0\nBounded LLM\nFallback", ha="center", va="center", fontsize=7.5, bbox=proc)
    ax.text(0.90, 0.48, "4.0\nDispatch\nResponse", ha="center", va="center", fontsize=7.5, bbox=proc)
    
    ax.annotate("User Input", xy=(0.10, 0.48), xytext=(0.02, 0.48), arrowprops=dict(arrowstyle="->", lw=1.2), fontsize=7)
    ax.annotate("", xy=(0.35, 0.48), xytext=(0.20, 0.48), arrowprops=dict(arrowstyle="->", lw=1.2))
    ax.annotate("Score < 0.45", xy=(0.60, 0.48), xytext=(0.45, 0.48), arrowprops=dict(arrowstyle="->", lw=1.2), fontsize=7)
    ax.annotate("", xy=(0.85, 0.48), xytext=(0.70, 0.48), arrowprops=dict(arrowstyle="->", lw=1.2))
    ax.annotate("Direct Match", xy=(0.88, 0.53), xytext=(0.42, 0.53), arrowprops=dict(arrowstyle="->", lw=1.2, color="#059669"), fontsize=7)
    
    # Stores
    ax.text(0.40, 0.28, "D1: FAQS STORE\n[question, answer, category]", ha="center", va="center", fontsize=7.5, bbox=store)
    ax.text(0.65, 0.28, "D2: QUERY & CHAT LOGS\n[session_id, role, text, score]", ha="center", va="center", fontsize=7.5, bbox=store)
    ax.text(0.15, 0.28, "D3: ADMIN CREDENTIALS\n[username, pbkdf2_hash]", ha="center", va="center", fontsize=7.5, bbox=store)
    
    ax.plot([0.40, 0.40], [0.42, 0.33], "k-", lw=1.0)
    ax.plot([0.65, 0.65], [0.42, 0.33], "k->", lw=1.0)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_dfd.png"), bbox_inches="tight")
    plt.close()
    print("Generated DFD diagram.")

def create_use_case_diagram():
    fig, ax = plt.subplots(figsize=(8.5, 8.5), dpi=200)
    ax.axis('off')
    
    # Boundary box
    rect = patches.Rectangle((0.25, 0.05), 0.50, 0.90, linewidth=1.5, edgecolor='#3b82f6', facecolor='#f8fafc')
    ax.add_patch(rect)
    ax.text(0.5, 0.92, "CampusAI System Boundary", ha="center", va="center", fontsize=10, weight="bold", color="#1e3a8a")
    
    actor_box = dict(boxstyle="round,pad=0.4", facecolor="#e2e8f0", edgecolor="#475569", lw=1.2)
    uc_box = dict(boxstyle="round,pad=0.3", facecolor="#ffffff", edgecolor="#2563eb", lw=1.0)
    
    # Actors
    ax.text(0.10, 0.65, "STUDENT\n(Primary Actor)", ha="center", va="center", fontsize=8.5, weight="bold", bbox=actor_box)
    ax.text(0.90, 0.65, "ADMINISTRATOR\n(Primary Actor)", ha="center", va="center", fontsize=8.5, weight="bold", bbox=actor_box)
    ax.text(0.50, 0.02, "GEMINI AI CLOUD (Secondary Actor)", ha="center", va="center", fontsize=8, weight="bold", bbox=actor_box)
    
    # Use cases
    ucs = [
        (0.5, 0.83, "Ask College Academic FAQs"),
        (0.5, 0.74, "Use Clickable Question Chips"),
        (0.5, 0.65, "Search & Filter FAQ Directory"),
        (0.5, 0.56, "Clear Active Chat Session"),
        (0.5, 0.47, "Authenticate Admin Login (PBKDF2)"),
        (0.5, 0.38, "Create / Edit / Delete FAQs (CRUD)"),
        (0.5, 0.29, "View Real-Time System KPIs"),
        (0.5, 0.20, "Generate Bounded LLM Fallback")
    ]
    
    for x, y, label in ucs:
        ax.text(x, y, label, ha="center", va="center", fontsize=7.5, bbox=uc_box)
    
    # Connect student
    for y in [0.83, 0.74, 0.65, 0.56]:
        ax.plot([0.17, 0.37], [0.65, y], "b-", lw=1.0)
        
    # Connect admin
    for y in [0.47, 0.38, 0.29]:
        ax.plot([0.83, 0.63], [0.65, y], "g-", lw=1.0)
        
    # Connect AI
    ax.plot([0.5, 0.5], [0.06, 0.17], "m--", lw=1.2)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "campusai_use_case.png"), bbox_inches="tight")
    plt.close()
    print("Generated Use Case diagram.")

if __name__ == '__main__':
    create_decision_tree()
    create_er_diagram()
    create_architecture_diagram()
    create_dfd_diagram()
    create_use_case_diagram()
