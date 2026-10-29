# -*- coding: utf-8 -*-
"""Single-predictor R² bars plus overall Shapley group contributions.

Outputs: Shapley方差分解_最终版.tiff (300 dpi TIFF).
Left panel: R² of each single predictor, coloured by its parent group.
Right inset: stacked bar of the four Shapley group shares, with the legend
placed outside the inset.
"""
import os

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import Patch

# ==================== 0. Config ====================
out_dir = r"E:\WLR17\论文\图"
out_file = os.path.join(out_dir, "Shapley方差分解_最终版.tiff")
os.makedirs(out_dir, exist_ok=True)

mpl.rcParams["font.family"] = "Times New Roman"
mpl.rcParams["mathtext.fontset"] = "stix"
mpl.rcParams["axes.unicode_minus"] = False

# ==================== 1. Data ====================
groups = ['Grain size', 'Provenance', 'Dilution', 'Age', 'Unexplained']
group_vals = [36.3, 8.7, 8.4, 0.6, 46.1]
group_colors = ['#300a8b', '#3132f0', '#b7cfe7', '#d2625f', '#e0e0e0']

single_labels = ['Fine/Coarse silt', 'Mean grain size', 'Clay (<8µm)',
                 'Zr/Hf', 'Nb/Ta', 'Th/Sc',
                 'CaO', 'TOC', 'Age']
single_r2 = [0.327, 0.018, 0.015, 0.012, 0.010, 0.008, 0.007, 0.005, 0.0002]
single_colors = ['#300a8b', '#300a8b', '#300a8b',
                 '#3132f0', '#3132f0', '#3132f0',
                 '#b7cfe7', '#b7cfe7', '#d2625f']

# 全局字号
GLOBAL_FONTSIZE = 11

# ============================================================
# 2. 画布
# ============================================================
fig = plt.figure(figsize=(10, 6))

# 左侧主图
ax1 = fig.add_axes([0.10, 0.15, 0.55, 0.75])
y_pos = np.arange(len(single_labels))
ax1.barh(y_pos, single_r2, color=single_colors, edgecolor='black',
         linewidth=0.5, height=0.6)

ax1.set_yticks(y_pos)
ax1.set_yticklabels(single_labels, fontsize=GLOBAL_FONTSIZE)
ax1.invert_yaxis()
ax1.set_xlabel("$R^2$ (variance explained by single predictor)",
               fontsize=GLOBAL_FONTSIZE)
ax1.set_xlim(0, 0.40)
ax1.set_ylim(8.8, -0.8)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.tick_params(axis='both', direction='in', length=4,
                labelsize=GLOBAL_FONTSIZE)

for i, v in enumerate(single_r2):
    offset = 0.005 if v > 0.01 else 0.008
    txt = f"{v:.3f}" if v >= 0.001 else "< 0.001"
    ax1.text(v + offset, i, txt, va='center', fontsize=GLOBAL_FONTSIZE)

# ============================================================
# 3. 右侧插图：整体堆叠柱状图
# ============================================================
ax2 = fig.add_axes([0.3, 0.25, 0.15, 0.50])
bottom = 0
for val, color in zip(group_vals, group_colors):
    ax2.bar(0, val, bottom=bottom, color=color, edgecolor='white',
            width=0.6, linewidth=1.0)
    if val > 5:
        text_color = 'white' if color in ['#300a8b', '#3132f0'] else 'black'
        ax2.text(0, bottom + val / 2, f'{val}%', ha='center', va='center',
                 fontsize=GLOBAL_FONTSIZE, color=text_color)
    bottom += val

ax2.set_xlim(-0.6, 0.6)
ax2.set_ylim(0, 100)
ax2.set_xticks([])
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
ax2.spines['left'].set_linewidth(0.8)
ax2.tick_params(axis='y', direction='in', length=3,
                labelsize=GLOBAL_FONTSIZE)
ax2.set_ylabel("Variance explained (%)", fontsize=GLOBAL_FONTSIZE)
ax2.set_title("Overall Group Contributions", fontsize=GLOBAL_FONTSIZE, pad=8)

# ============================================================
# 4. 图例：锚点相对于 ax2，落在插图右侧空白区
# ============================================================
legend_elements = [
    Patch(facecolor='#300a8b', label='Grain size (36.3%)'),
    Patch(facecolor='#3132f0', label='Provenance (8.7%)'),
    Patch(facecolor='#b7cfe7', label='Dilution (8.4%)'),
    Patch(facecolor='#d2625f', label='Age (0.6%)')
]
ax2.legend(handles=legend_elements, loc='center left',
           bbox_to_anchor=(1.2, 0.5), frameon=False,
           fontsize=GLOBAL_FONTSIZE)

# ============================================================
# 5. 导出
# ============================================================
fig.savefig(out_file, dpi=300, format="tiff", bbox_inches="tight",
            facecolor="white")
plt.close(fig)

print(f"Figure saved to: {out_file}")