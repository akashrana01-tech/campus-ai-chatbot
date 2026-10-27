import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

os.makedirs("scratch/campusai_diagrams", exist_ok=True)
out_path = "scratch/campusai_diagrams/campusai_decision_tree.png"

fig, ax = plt.subplots(figsize=(14, 8.5), dpi=300)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis("off")

# Background
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

# Colors
CLR_BORDER = "#1e293b"
CLR_LINE = "#1e293b"
CLR_TEXT = "#0f172a"
CLR_MUTED = "#334155"
CLR_BOX_BG = "#ffffff"
CLR_TERM_BG = "#f8fafc"
CLR_TERM_BORDER = "#475569"

def draw_decision_square(x, y, label, size=3.6):
    rect = patches.Rectangle((x - size/2, y - size/2), size, size,
                             linewidth=1.8, edgecolor=CLR_BORDER,
                             facecolor=CLR_BOX_BG, zorder=5)
    ax.add_patch(rect)
    ax.text(x, y, label, ha="center", va="center", fontsize=10, fontweight="bold", color=CLR_TEXT, zorder=6)

def draw_chance_circle(x, y, label, radius=1.9):
    circle = patches.Circle((x, y), radius, linewidth=1.8,
                            edgecolor=CLR_BORDER, facecolor=CLR_BOX_BG, zorder=5)
    ax.add_patch(circle)
    ax.text(x, y, label, ha="center", va="center", fontsize=10, fontweight="bold", color=CLR_TEXT, zorder=6)

def draw_branch(p1, p2, label_top="", label_bottom="", ha="center", angle_offset=1.2):
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=CLR_LINE, lw=1.8, zorder=3)
    mx = (p1[0] + p2[0]) / 2.0
    my = (p1[1] + p2[1]) / 2.0
    if label_top:
        ax.text(mx, my + angle_offset, label_top, ha=ha, va="bottom",
                fontsize=8.2, fontweight="bold", color=CLR_TEXT, zorder=4)
    if label_bottom:
        ax.text(mx, my - angle_offset, label_bottom, ha=ha, va="top",
                fontsize=7.6, fontstyle="italic", color=CLR_MUTED, zorder=4)

def draw_terminal_box(x, y, title, subtitle="", w=20, h=4.4):
    rect = patches.FancyBboxPatch((x, y - h/2), w, h, boxstyle="round,pad=0.25",
                                  linewidth=1.4, edgecolor=CLR_TERM_BORDER, facecolor=CLR_TERM_BG, zorder=5)
    ax.add_patch(rect)
    ax.text(x + w/2, y + (0.8 if subtitle else 0), title, ha="center", va="center",
            fontsize=8.0, fontweight="bold", color="#0f172a", zorder=6)
    if subtitle:
        ax.text(x + w/2, y - 0.9, subtitle, ha="center", va="center",
                fontsize=7.2, fontstyle="italic", color="#475569", zorder=6)

# Main Coordinates
# Root D1
p_D1 = (8, 50)

# C1 and D12
p_C1 = (27, 68)
p_term_D12 = (29, 28)

# Level 3: D2 & D3
p_D2 = (46, 79)
p_D3 = (46, 52)

# Level 4: from D2 -> C2 & D22
p_C2 = (66, 86)
p_term_D22 = (64, 71)

# Level 4: from D3 -> C3 & D32
p_C3 = (66, 57)
p_term_D32 = (64, 43)

# Level 5: Terminals from C2
p_term_C21 = (88, 92)
p_term_C22 = (88, 80)

# Level 5: Terminals from C3
p_term_C31 = (88, 63)
p_term_C32 = (88, 50)

# Branch 1: D1 -> C1
draw_branch((p_D1[0] + 1.8, p_D1[1]), (p_C1[0] - 1.9, p_C1[1]),
            label_top="D11: Ingest Query & Evaluate NLP",
            label_bottom="Resource: Local Tokenization (<5ms)")

# Branch 2: D1 -> D12
draw_branch((p_D1[0] + 1.8, p_D1[1]), p_term_D12,
            label_top="D12: Empty / Invalid Input",
            label_bottom="Condition: len(query) < 2")

# From C1 -> D2
draw_branch((p_C1[0] + 1.9, p_C1[1]), (p_D2[0] - 1.8, p_D2[1]),
            label_top="C11: Direct DB Match (Jaccard S >= 0.58)",
            label_bottom="Probability / Score: 0.70")

# From C1 -> D3
draw_branch((p_C1[0] + 1.9, p_C1[1]), (p_D3[0] - 1.8, p_D3[1]),
            label_top="C12: Low Overlap (Score S < 0.58)",
            label_bottom="Probability: 0.30")

# From D2 -> C2
draw_branch((p_D2[0] + 1.8, p_D2[1]), (p_C2[0] - 1.9, p_C2[1]),
            label_top="D21: Fetch Authoritative Record",
            label_bottom="Sub-second Lookup (<15ms)")

# From D2 -> D22
draw_branch((p_D2[0] + 1.8, p_D2[1]), p_term_D22,
            label_top="D22: Inactive Session",
            label_bottom="Condition: Idle > 15m")

# From C2 -> C21
draw_branch((p_C2[0] + 1.9, p_C2[1]), p_term_C21,
            label_top="C21: Voice Read-Aloud Enabled",
            label_bottom="Probability: 0.65")

# From C2 -> C22
draw_branch((p_C2[0] + 1.9, p_C2[1]), p_term_C22,
            label_top="C22: Silent Text Response",
            label_bottom="Probability: 0.35")

# From D3 -> C3
draw_branch((p_D3[0] + 1.8, p_D3[1]), (p_C3[0] - 1.9, p_C3[1]),
            label_top="D31: Invoke Gemini 2.5 Flash AI",
            label_bottom="Guardrail: Strict Zero-Hallucination")

# From D3 -> D32
draw_branch((p_D3[0] + 1.8, p_D3[1]), p_term_D32,
            label_top="D32: Standard Helpdesk Referral",
            label_bottom="Condition: Non-Academic Query")

# From C3 -> C31
draw_branch((p_C3[0] + 1.9, p_C3[1]), p_term_C31,
            label_top="C31: API Online & Context Verified",
            label_bottom="Probability: 0.85")

# From C3 -> C32
draw_branch((p_C3[0] + 1.9, p_C3[1]), p_term_C32,
            label_top="C32: API Timeout / Network Offline",
            label_bottom="Probability: 0.15")

# Draw Nodes
draw_decision_square(p_D1[0], p_D1[1], "D1")
draw_chance_circle(p_C1[0], p_C1[1], "C1")
draw_decision_square(p_D2[0], p_D2[1], "D2")
draw_decision_square(p_D3[0], p_D3[1], "D3")
draw_chance_circle(p_C2[0], p_C2[1], "C2")
draw_chance_circle(p_C3[0], p_C3[1], "C3")

# Draw Terminal Boxes
draw_terminal_box(p_term_D12[0], p_term_D12[1], "D12: Validation Prompt", "Action: Suggest 8 Domain Chips", w=19, h=4.2)
draw_terminal_box(p_term_D22[0], p_term_D22[1], "D22: Close Session", "Action: Reset Chat State", w=17, h=4.0)
draw_terminal_box(p_term_D32[0], p_term_D32[1], "D32: Office Referral", "Action: Display College Contact", w=18, h=4.0)

draw_terminal_box(p_term_C21[0], p_term_C21[1], "Verified Answer + TTS Audio", "Output: 100% Authoritative SQLite Record", w=22, h=4.4)
draw_terminal_box(p_term_C22[0], p_term_C22[1], "Verified Text Answer", "Output: Instant Fast-Path Delivery (<15ms)", w=22, h=4.4)
draw_terminal_box(p_term_C31[0], p_term_C31[1], "Context-Bounded AI Answer", "Output: Zero-Hallucination Gemini Answer", w=22, h=4.4)
draw_terminal_box(p_term_C32[0], p_term_C32[1], "Deterministic Helpdesk Referral", "Output: contact@college.edu Guidance", w=22, h=4.4)

# Professional Legend Box (Top-Left)
leg_w, leg_h = 28, 11
leg_rect = patches.FancyBboxPatch((4, 85), leg_w, leg_h, boxstyle="round,pad=0.3",
                                  linewidth=1.2, edgecolor="#64748b", facecolor="#f8fafc", zorder=6)
ax.add_patch(leg_rect)
ax.text(5.5, 93.5, "Standard Decision Tree Legend:", fontsize=8.8, fontweight="bold", color="#0f172a", zorder=7)

# Square symbol in legend
ax.add_patch(patches.Rectangle((6, 88.5), 2.4, 2.4, linewidth=1.4, edgecolor=CLR_BORDER, facecolor="#ffffff", zorder=7))
ax.text(7.2, 89.7, "D", ha="center", va="center", fontsize=8.0, fontweight="bold", color=CLR_TEXT, zorder=8)
ax.text(9.5, 89.7, "= Decision Node", ha="left", va="center", fontsize=8.0, color="#1e293b", zorder=7)

# Circle symbol in legend
ax.add_patch(patches.Circle((19.5, 89.7), 1.3, linewidth=1.4, edgecolor=CLR_BORDER, facecolor="#ffffff", zorder=7))
ax.text(19.5, 89.7, "C", ha="center", va="center", fontsize=8.0, fontweight="bold", color=CLR_TEXT, zorder=8)
ax.text(21.8, 89.7, "= Chance / Event Node", ha="left", va="center", fontsize=8.0, color="#1e293b", zorder=7)

plt.tight_layout()
plt.savefig(out_path, bbox_inches="tight", dpi=300)
plt.close()
print("[✓] Successfully rendered Business Jargons style Decision Tree to:", out_path)
