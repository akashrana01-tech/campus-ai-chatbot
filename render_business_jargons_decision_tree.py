import os
os.environ['MPLCONFIGDIR'] = '/tmp/mpl_config'
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Canvas setup - widescreen 16:9 matching Business Jargons
fig, ax = plt.subplots(figsize=(18, 9.2), dpi=300)
ax.set_facecolor('#ffffff')
fig.patch.set_facecolor('#ffffff')

# Coordinate boundaries - generous space
ax.set_xlim(2, 400)
ax.set_ylim(6, 106)
ax.axis('off')

# Styling parameters
LINE_COLOR = '#111827'       # Crisp near-black line
LINE_WIDTH = 1.7
NODE_EDGE = '#0f172a'
NODE_FILL = '#ffffff'
TITLE_COLOR = '#0f172a'     # Bold node/branch titles
SUB_COLOR = '#374151'       # Branch subtitles/probabilities
OUTCOME_COLOR = '#065f46'   # Greenish-slate for final output
ACTION_COLOR = '#1e3a8a'    # Deep blue for terminal actions

def draw_square(x, y, label, size=8.0):
    """Draws a decision square centered at (x, y) with text label."""
    half = size / 2.0
    rect = patches.Rectangle(
        (x - half, y - half), size, size,
        facecolor=NODE_FILL, edgecolor=NODE_EDGE, linewidth=2.0, zorder=5
    )
    ax.add_patch(rect)
    ax.text(x, y, label, ha='center', va='center', fontsize=12.5, fontweight='bold',
            color=NODE_EDGE, zorder=6, fontfamily='sans-serif')

def draw_circle(x, y, label, radius=4.4):
    """Draws a chance circle centered at (x, y) with text label."""
    circle = patches.Circle(
        (x, y), radius,
        facecolor=NODE_FILL, edgecolor=NODE_EDGE, linewidth=2.0, zorder=5
    )
    ax.add_patch(circle)
    ax.text(x, y, label, ha='center', va='center', fontsize=12.0, fontweight='bold',
            color=NODE_EDGE, zorder=6, fontfamily='sans-serif')

def draw_dogleg(x_start, y_start, x_elbow, y_end, x_end):
    """Draws diagonal then horizontal branch line."""
    ax.plot([x_start, x_elbow], [y_start, y_end], color=LINE_COLOR, linewidth=LINE_WIDTH, zorder=3)
    ax.plot([x_elbow, x_end], [y_end, y_end], color=LINE_COLOR, linewidth=LINE_WIDTH, zorder=3)

def draw_straight(x_start, y_start, x_end, y_end):
    """Draws a straight horizontal line."""
    ax.plot([x_start, x_end], [y_start, y_end], color=LINE_COLOR, linewidth=LINE_WIDTH, zorder=3)

# -------------------------------------------------------------------------
# NODES COORDINATES
# -------------------------------------------------------------------------
# D1 at (14, 52)
X_D1, Y_D1 = 14, 52
draw_square(X_D1, Y_D1, 'D1', size=8.0)

# C1 at (98, 72)
X_C1, Y_C1 = 98, 72
draw_circle(X_C1, Y_C1, 'C1', radius=4.4)

# D2 at (176, 88)
X_D2, Y_D2 = 176, 88
draw_square(X_D2, Y_D2, 'D2', size=8.0)

# D3 at (176, 48)
X_D3, Y_D3 = 176, 48
draw_square(X_D3, Y_D3, 'D3', size=8.0)

# C2 at (254, 96)
X_C2, Y_C2 = 254, 96
draw_circle(X_C2, Y_C2, 'C2', radius=4.4)

# -------------------------------------------------------------------------
# BRANCHES FROM D1
# -------------------------------------------------------------------------
# Branch D11 -> C1 (Diagonal up to elbow, then horizontal into C1)
draw_dogleg(X_D1 + 4.0, Y_D1, 28, Y_C1, X_C1 - 4.4)
ax.text(30, Y_C1 + 2.2, 'D11: Valid Student Query Input', fontsize=10.5, fontweight='bold', color=TITLE_COLOR)
ax.text(30, Y_C1 - 3.2, 'Length > 0 (Pre-process & Sanitize)', fontsize=9.2, color=SUB_COLOR)

# Branch D12 -> Terminal Action (Diagonal down to elbow, then horizontal)
X_D12_END = 98
draw_dogleg(X_D1 + 4.0, Y_D1, 28, 22, X_D12_END)
ax.text(30, 22 + 2.2, 'D12: Empty / Invalid Input', fontsize=10.5, fontweight='bold', color=TITLE_COLOR)
ax.text(30, 22 - 3.2, 'Cost: 0 ms / No Token Used', fontsize=9.2, color=SUB_COLOR)
# Action at end of line
ax.text(X_D12_END + 3, 22, 'Action:\nPrompt User & Display\n8 FAQ Category Chips', 
        fontsize=9.5, fontweight='bold', color='#b45309', va='center', linespacing=1.3)

# -------------------------------------------------------------------------
# BRANCHES FROM C1
# -------------------------------------------------------------------------
# Branch C11 -> D2 (FAQ Match)
draw_dogleg(X_C1 + 4.4, Y_C1, 114, Y_D2, X_D2 - 4.0)
ax.text(116, Y_D2 + 2.2, 'C11: FAQ Match (S ≥ 0.58)', fontsize=10.5, fontweight='bold', color=TITLE_COLOR)
ax.text(116, Y_D2 - 3.2, 'Probability: 0.70 (SQLite Hit)', fontsize=9.2, color=SUB_COLOR)

# Branch C12 -> D3 (FAQ Miss)
draw_dogleg(X_C1 + 4.4, Y_C1, 114, Y_D3, X_D3 - 4.0)
ax.text(116, Y_D3 + 2.2, 'C12: FAQ Miss (S < 0.58)', fontsize=10.5, fontweight='bold', color=TITLE_COLOR)
ax.text(116, Y_D3 - 3.2, 'Probability: 0.30 (Fallback Path)', fontsize=9.2, color=SUB_COLOR)

# -------------------------------------------------------------------------
# BRANCHES FROM D3
# -------------------------------------------------------------------------
# Branch D31 -> Terminal Action (Route to Gemini AI)
X_D31_END = 260
draw_straight(X_D3 + 4.0, Y_D3, X_D31_END, Y_D3)
ax.text(X_D3 + 6, Y_D3 + 2.2, 'D31: Route to Gemini 2.5 Flash API', fontsize=10.5, fontweight='bold', color=TITLE_COLOR)
ax.text(X_D3 + 6, Y_D3 - 3.2, 'Context-Bounded Prompt (<1.2s Latency)', fontsize=9.2, color=SUB_COLOR)
# Terminal action at end of D31
ax.text(X_D31_END + 3, Y_D3, 'Terminal Action:\nGenerate Verified Academic Answer\n(<1.2s, Zero Hallucination Mode)',
        fontsize=9.5, fontweight='bold', color=ACTION_COLOR, va='center', linespacing=1.3)

# -------------------------------------------------------------------------
# BRANCHES FROM D2
# -------------------------------------------------------------------------
# Branch D21 -> C2 (Serve Verified FAQ)
draw_dogleg(X_D2 + 4.0, Y_D2, 192, Y_C2, X_C2 - 4.4)
ax.text(194, Y_C2 + 2.2, 'D21: Serve Local Verified FAQ', fontsize=10.5, fontweight='bold', color=TITLE_COLOR)
ax.text(194, Y_C2 - 3.2, 'Fetch SQLite Record (<15ms)', fontsize=9.2, color=SUB_COLOR)

# Branch D22 -> Terminal Action (Duplicate Query Filter)
X_D22_END = 260
draw_dogleg(X_D2 + 4.0, Y_D2, 192, 68, X_D22_END)
ax.text(194, 68 + 2.2, 'D22: Duplicate / Spam Filter', fontsize=10.5, fontweight='bold', color=TITLE_COLOR)
ax.text(194, 68 - 3.2, 'Cost: 0 ms / No Reprocessing', fontsize=9.2, color=SUB_COLOR)
# Terminal action at end of D22
ax.text(X_D22_END + 3, 68, 'Terminal Action:\nLog Student Interaction &\nSuppress Redundant Queries',
        fontsize=9.5, fontweight='bold', color='#475569', va='center', linespacing=1.3)

# -------------------------------------------------------------------------
# BRANCHES FROM C2
# -------------------------------------------------------------------------
# Branch C21 -> Terminal Outcome (Audio Read-Aloud)
X_C21_END = 318
draw_dogleg(X_C2 + 4.4, Y_C2, 268, 102, X_C21_END)
ax.text(270, 102 + 2.2, 'C21: Voice Read-Aloud', fontsize=10.5, fontweight='bold', color=TITLE_COLOR)
ax.text(270, 102 - 3.2, 'Probability: 0.60', fontsize=9.2, color=SUB_COLOR)
# Outcome at end of line (equivalent to "Annual Cash Flow: 30 Million")
ax.text(X_C21_END + 4, 102, 'Output Result:\nInstant Chat Bubble +\nWeb Speech Voice Output',
        fontsize=9.5, fontweight='bold', color=OUTCOME_COLOR, va='center', linespacing=1.3)

# Branch C22 -> Terminal Outcome (Silent / Text-Only)
X_C22_END = 318
draw_dogleg(X_C2 + 4.4, Y_C2, 268, 84, X_C22_END)
ax.text(270, 84 + 2.2, 'C22: Silent / Text Mode', fontsize=10.5, fontweight='bold', color=TITLE_COLOR)
ax.text(270, 84 - 3.2, 'Probability: 0.40', fontsize=9.2, color=SUB_COLOR)
# Outcome at end of line (equivalent to "Annual Cash Flow: 20 Million")
ax.text(X_C22_END + 4, 84, 'Output Result:\nFast-Path Text Bubble\n(<15ms Latency, 0 Token Cost)',
        fontsize=9.5, fontweight='bold', color=OUTCOME_COLOR, va='center', linespacing=1.3)

# Save high-res
plt.tight_layout()
output_img = 'scratch/campusai_diagrams/campusai_decision_tree.png'
plt.savefig(output_img, bbox_inches='tight', dpi=300)
print('Successfully saved', output_img)
