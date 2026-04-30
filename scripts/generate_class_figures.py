"""
Course-style figures for Music 159r popular music analysis.

Following Moore (2012) Song Means and Zagorski-Thomas (2014):
  Figure A — Formal-functional diagram (timeline, multi-version stacked)
  Figure B — Sound-box triptych (V1 / Chorus / Bridge of dl original)
  Figure C — Textural-layer comparison matrix (design vs V_A vs V_B vs v4.5)
  Figure D — Vocal-staging summary chart

These replace the ML-style quantitative bars and align the paper's visuals
with the analytical vocabulary the course teaches.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, Polygon, Circle
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches

ROOT = Path(__file__).resolve().parent.parent
FIG_DIR = ROOT / "figures"
FIG_DIR.mkdir(exist_ok=True)

# Set publication-grade style
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "DejaVu Serif"],
    "font.size": 10,
    "axes.titlesize": 11,
    "axes.labelsize": 10,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9,
    "figure.titlesize": 12,
})


# Color palette: section-function semantic colors (Moore-style)
SECTION_COL = {
    "Intro":  "#9E9E9E",
    "V1":     "#5B8FB9",    # verse blue
    "V2":     "#5B8FB9",
    "V3":     "#5B8FB9",
    "PC1":    "#7E57C2",    # pre-chorus violet
    "PC2":    "#7E57C2",
    "C1":     "#E07B0F",    # chorus orange
    "C2":     "#E07B0F",
    "C3":     "#E07B0F",
    "C3*":    "#D32F2F",    # modulated chorus = darker red
    "PostC":  "#FFB300",    # post-chorus amber
    "Br":     "#388E3C",    # bridge green
    "Out":    "#6D4C41",    # outro brown
}


# ============================================================
# FIGURE A — FORMAL-FUNCTIONAL DIAGRAM (timeline, multi-version)
# ============================================================
def figA_formal_functional_timeline():
    """
    Stacked timeline showing how 4 versions structure the song relative to
    the original's Genius 8-section design. Each row = one version; each
    coloured block = one functional section.
    """
    versions = [
        {
            "label": "Original\n(design)",
            "duration": 242,
            "sections": [  # (name, start, end)
                ("V1",  0,   30),
                ("V2",  30,  54),
                ("C1",  54,  87),
                ("V3",  87,  110),
                ("C2",  110, 143),
                ("Br",  143, 175),
                ("C3",  175, 197),
                ("Out", 197, 242),
            ],
            "note": "8 sections · V-V-C-V-C-B-C-O · double-verse opening",
        },
        {
            "label": "V_A\nSuno v5.5",
            "duration": 268,
            "sections": [  # close-listening segmentation
                ("V1",  0,   21),
                ("V2",  21,  41),
                ("C1",  41,  71),
                ("V3",  71,  112),
                ("C2",  112, 142),
                ("Br",  142, 183),
                ("C3",  183, 212),
                ("Out", 212, 268),
            ],
            "note": "4:28 · +26 s long · bridge ramps loudest, no inversion",
        },
        {
            "label": "V_B\nSuno v5.5",
            "duration": 223,
            "sections": [
                ("V1",  0,   15),
                ("V2",  15,  31),
                ("C1",  31,  57),
                ("V3",  57,  87),
                ("C2",  87,  112),
                ("Br",  112, 139),
                ("C3",  139, 206),
                ("Out", 206, 223),
            ],
            "note": "3:43 · -19 s short · meta-tags increase macro-contour",
        },
        {
            "label": "v4.5\nSuno v4.5",
            "duration": 239,
            "sections": [
                ("V1",  0,   14),
                ("V2",  14,  28),
                ("C1",  28,  50),
                ("V3",  50,  88),
                ("C2",  88,  112),
                ("Br",  112, 150),
                ("C3",  150, 191),
                ("Out", 191, 239),
            ],
            "note": "3:59 · only version where bridge sits below choruses",
        },
        {
            "label": "Love Story\n(control,\nv5.5)",
            "duration": 270,
            "sections": [  # auto-segment derived, mapped to Genius 10 segs
                ("V1",   0,   16),
                ("PC1",  16,  31),
                ("C1",   31,  66),
                ("V2",   66,  88),
                ("PC2",  88,  128),
                ("C2",   128, 182),
                ("PostC", 182, 200),
                ("Br",   200, 222),
                ("C3*",  222, 266),
                ("Out",  266, 270),
            ],
            "note": "4:30 · 10-section V-PC-C × 2 · centroid form, AI follows",
        },
    ]

    n = len(versions)
    fig, ax = plt.subplots(figsize=(14, 5.5))
    row_h = 0.65
    pad_y = 0.35

    max_dur = max(v["duration"] for v in versions)

    for i, v in enumerate(versions):
        y_top = (n - i - 1) * (row_h + pad_y) + pad_y / 2
        # version label on left
        ax.text(-12, y_top + row_h/2, v["label"], ha="right", va="center",
                fontsize=10, weight="bold")
        # note on right
        ax.text(v["duration"] + 4, y_top + row_h/2, v["note"], ha="left", va="center",
                fontsize=8, style="italic", color="#444444")

        for name, t0, t1 in v["sections"]:
            col = SECTION_COL.get(name, "#999999")
            rect = Rectangle((t0, y_top), t1 - t0, row_h,
                              facecolor=col, edgecolor="black", linewidth=0.5,
                              alpha=0.85)
            ax.add_patch(rect)
            # section label inside if wide enough
            if (t1 - t0) >= 12:
                txt_col = "white" if name in ("Br", "Out", "C3*") else "black"
                ax.text((t0 + t1)/2, y_top + row_h/2, name,
                        ha="center", va="center", fontsize=9, weight="bold",
                        color=txt_col)
            # duration in seconds at bottom of block
            ax.text((t0 + t1)/2, y_top - 0.05, f"{t1-t0}s",
                    ha="center", va="top", fontsize=6.5, color="#555555")

    # Time axis
    ax.set_xlim(-50, max_dur + 70)
    ax.set_ylim(-0.5, n * (row_h + pad_y) + 0.2)
    ax.set_xticks(np.arange(0, max_dur + 30, 30))
    ax.set_xticklabels([f"{t//60}:{t%60:02d}" for t in np.arange(0, max_dur + 30, 30)])
    ax.set_xlabel("Time (m:ss)", fontsize=10)
    ax.set_yticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    # Legend
    legend_handles = [
        mpatches.Patch(color="#5B8FB9", label="Verse"),
        mpatches.Patch(color="#7E57C2", label="Pre-Chorus"),
        mpatches.Patch(color="#E07B0F", label="Chorus"),
        mpatches.Patch(color="#D32F2F", label="Modulated Chorus"),
        mpatches.Patch(color="#FFB300", label="Post-Chorus"),
        mpatches.Patch(color="#388E3C", label="Bridge"),
        mpatches.Patch(color="#6D4C41", label="Outro"),
    ]
    ax.legend(handles=legend_handles, loc="lower center",
              bbox_to_anchor=(0.5, -0.18), ncol=7, frameon=False, fontsize=8)

    ax.set_title(
        "Formal-functional diagram: how four AI generations structure the song\n"
        "relative to the original's eight-section design (after Moore 2012)",
        fontsize=11, weight="bold", pad=12)

    fig.tight_layout()
    fig.savefig(FIG_DIR / "figA_formal_functional_timeline.png",
                dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)


# ============================================================
# FIGURE B — SOUND-BOX TRIPTYCH (V1 / Chorus / Bridge)
# ============================================================
def _draw_box(ax, depth_offset=(0.55, 0.4)):
    """Draw a 2D oblique-projection box (Moore sound-box)."""
    dx, dy = depth_offset
    # front face
    front = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
    # back face
    back = [(p[0] + dx, p[1] + dy) for p in front]
    # connecting edges
    for f, b in zip(front, back):
        ax.plot([f[0], b[0]], [f[1], b[1]], color="#444444", lw=1.0)
    # back rectangle
    bx = [p[0] for p in back] + [back[0][0]]
    by = [p[1] for p in back] + [back[0][1]]
    ax.plot(bx, by, color="#444444", lw=1.0)
    # front rectangle
    fx = [p[0] for p in front] + [front[0][0]]
    fy = [p[1] for p in front] + [front[0][1]]
    ax.plot(fx, fy, color="black", lw=1.6)
    return dx, dy


def _project(x, y, z, dx, dy):
    """Project 3D (x=L-R, y=Low-High, z=Front[-1]-Back[+1]) into 2D."""
    z_norm = (z + 1) / 2  # 0 (front) to 1 (back)
    return x + dx * z_norm, y + dy * z_norm


def _plot_source(ax, name, x, y, z, dx, dy, color="#1E3A5F",
                 size=180, fontsize=8, offset=(0.04, 0.07)):
    px, py = _project(x, y, z, dx, dy)
    z_norm = (z + 1) / 2
    alpha = 1.0 - 0.45 * z_norm  # rear sources fade
    ax.scatter(px, py, s=size, c=color, alpha=alpha,
               edgecolors="black", linewidths=1.0, zorder=3)
    ax.annotate(name, xy=(px, py),
                xytext=(px + offset[0], py + offset[1]),
                fontsize=fontsize, color="#222222",
                bbox=dict(boxstyle="round,pad=0.18", facecolor="white",
                          edgecolor="none", alpha=0.85),
                zorder=4)


def figB_sound_box_triptych():
    fig, axes = plt.subplots(1, 3, figsize=(15, 5.4))

    # ---------------- V1 — Verse 1 ----------------
    ax = axes[0]
    dx, dy = _draw_box(ax)
    # axis labels on the box
    ax.annotate("low", xy=(-1, -1), xytext=(-1.05, -1.18), fontsize=8, ha="right")
    ax.annotate("high", xy=(-1, 1), xytext=(-1.05, 1.05), fontsize=8, ha="right")
    ax.annotate("L", xy=(-1, -1.05), xytext=(-1.0, -1.32), fontsize=8, ha="center")
    ax.annotate("R", xy=(1, -1.05), xytext=(1.0, -1.32), fontsize=8, ha="center")
    ax.annotate("front", xy=(0, -1), xytext=(-0.2, -1.5), fontsize=8, ha="center", style="italic")
    ax.annotate("back", xy=(dx, dy - 1), xytext=(dx + 0.05, dy - 1.32), fontsize=8, ha="left", style="italic")
    # sources: lead vocal (front, mid-high), piano (mid, mid)
    _plot_source(ax, "Lead vocal\n(close-mic, breathy)",
                 0.0, 0.45, -0.85, dx, dy, color="#C72A2A", size=320, fontsize=8.5,
                 offset=(0.06, 0.08))
    _plot_source(ax, "Upright piano\n(sparse, dry)",
                 0.0, 0.05, 0.05, dx, dy, color="#7A4F1A", size=200, fontsize=8,
                 offset=(0.06, -0.18))
    ax.set_title("(a) Verse 1\n‘intimate, narrow, dry’", fontsize=10.5, weight="bold")
    ax.set_xlim(-1.6, 1.85)
    ax.set_ylim(-1.6, 1.65)
    ax.set_aspect("equal")
    ax.axis("off")

    # ---------------- Chorus 1 — full band drop ----------------
    ax = axes[1]
    dx, dy = _draw_box(ax)
    ax.annotate("low", xy=(-1, -1), xytext=(-1.05, -1.18), fontsize=8, ha="right")
    ax.annotate("high", xy=(-1, 1), xytext=(-1.05, 1.05), fontsize=8, ha="right")
    ax.annotate("L", xy=(-1, -1.05), xytext=(-1.0, -1.32), fontsize=8, ha="center")
    ax.annotate("R", xy=(1, -1.05), xytext=(1.0, -1.32), fontsize=8, ha="center")
    ax.annotate("front", xy=(0, -1), xytext=(-0.2, -1.5), fontsize=8, ha="center", style="italic")
    ax.annotate("back", xy=(dx, dy - 1), xytext=(dx + 0.05, dy - 1.32), fontsize=8, ha="left", style="italic")
    # full band drop
    _plot_source(ax, "Lead vocal", 0.0, 0.45, -0.6, dx, dy, color="#C72A2A", size=280, fontsize=8,
                 offset=(0.06, 0.10))
    _plot_source(ax, "Octave\ndoubling", 0.0, -0.35, 0.0, dx, dy, color="#A03030", size=180, fontsize=7.5,
                 offset=(0.06, -0.18))
    _plot_source(ax, "L harmonies", -0.65, 0.30, 0.3, dx, dy, color="#D67373", size=160, fontsize=7.5,
                 offset=(-0.45, 0.10))
    _plot_source(ax, "R harmonies", 0.65, 0.30, 0.3, dx, dy, color="#D67373", size=160, fontsize=7.5,
                 offset=(0.06, 0.08))
    _plot_source(ax, "Pad", -0.95, -0.35, 0.6, dx, dy, color="#5B8FB9", size=160, fontsize=8,
                 offset=(-0.30, -0.15))
    _plot_source(ax, "Pad", 0.95, -0.35, 0.6, dx, dy, color="#5B8FB9", size=160, fontsize=8,
                 offset=(0.06, -0.15))
    _plot_source(ax, "Sub-bass", 0.0, -0.92, 0.0, dx, dy, color="#1E3A5F", size=200, fontsize=8,
                 offset=(0.06, -0.20))
    _plot_source(ax, "Kick", 0.0, -0.65, 0.0, dx, dy, color="#1E3A5F", size=170, fontsize=8,
                 offset=(0.06, 0.05))
    _plot_source(ax, "Piano", 0.18, 0.10, 0.35, dx, dy, color="#7A4F1A", size=140, fontsize=7.5,
                 offset=(0.06, -0.18))
    ax.set_title("(b) Chorus\n‘wide, full, mid-distance’", fontsize=10.5, weight="bold")
    ax.set_xlim(-1.6, 1.85)
    ax.set_ylim(-1.6, 1.65)
    ax.set_aspect("equal")
    ax.axis("off")

    # ---------------- Bridge — strip + stack ----------------
    ax = axes[2]
    dx, dy = _draw_box(ax)
    ax.annotate("low", xy=(-1, -1), xytext=(-1.05, -1.18), fontsize=8, ha="right")
    ax.annotate("high", xy=(-1, 1), xytext=(-1.05, 1.05), fontsize=8, ha="right")
    ax.annotate("L", xy=(-1, -1.05), xytext=(-1.0, -1.32), fontsize=8, ha="center")
    ax.annotate("R", xy=(1, -1.05), xytext=(1.0, -1.32), fontsize=8, ha="center")
    ax.annotate("front", xy=(0, -1), xytext=(-0.2, -1.5), fontsize=8, ha="center", style="italic")
    ax.annotate("back", xy=(dx, dy - 1), xytext=(dx + 0.05, dy - 1.32), fontsize=8, ha="left", style="italic")
    # bridge: strip instruments, stack vocals
    _plot_source(ax, "Main vocal", 0.0, 0.45, -0.7, dx, dy, color="#C72A2A", size=280, fontsize=8,
                 offset=(0.06, 0.10))
    _plot_source(ax, "Stack 1 (L)", -0.55, 0.55, 0.0, dx, dy, color="#D67373", size=200, fontsize=7.5,
                 offset=(-0.40, 0.08))
    _plot_source(ax, "Stack 2 (R)", 0.55, 0.55, 0.0, dx, dy, color="#D67373", size=200, fontsize=7.5,
                 offset=(0.06, 0.08))
    _plot_source(ax, "Stack 3\n(long reverb)", 0.0, 0.85, 0.7, dx, dy, color="#E89B9B", size=220,
                 fontsize=7.5, offset=(-0.10, 0.10))
    _plot_source(ax, "Ad-libs L", -0.85, 0.20, 0.55, dx, dy, color="#F0BBBB", size=130, fontsize=7,
                 offset=(-0.30, -0.15))
    _plot_source(ax, "Ad-libs R", 0.85, 0.20, 0.55, dx, dy, color="#F0BBBB", size=130, fontsize=7,
                 offset=(0.06, -0.15))
    _plot_source(ax, "Piano (weak)", 0.18, 0.05, 0.45, dx, dy, color="#B89060", size=110,
                 fontsize=7, offset=(0.05, -0.18))
    # annotation: "no kick / no sub-bass"
    ax.text(-1.5, -0.92, "(no kick,\nno sub-bass)",
            fontsize=8, color="#888888", style="italic", ha="left",
            bbox=dict(boxstyle="round,pad=0.18", facecolor="#F0F0F0",
                      edgecolor="#CCCCCC"))
    ax.set_title("(c) Bridge\n‘strip + stack: vocal saturation peak’", fontsize=10.5, weight="bold")
    ax.set_xlim(-1.6, 1.85)
    ax.set_ylim(-1.6, 1.65)
    ax.set_aspect("equal")
    ax.axis("off")

    fig.suptitle(
        "Sound-box of the original drivers license at three section types\n"
        "(after Moore 2012: lateral × proximity × frequency register)",
        fontsize=12, weight="bold", y=1.02
    )
    fig.tight_layout()
    fig.savefig(FIG_DIR / "figB_sound_box_triptych.png",
                dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)


# ============================================================
# FIGURE C — TEXTURAL-LAYER COMPARISON MATRIX (4 versions × 8 sections)
# ============================================================
def figC_textural_comparison():
    """
    Four sub-panels (design / V_A / V_B / v4.5) on the same Genius 8-section
    grid. Encoded:  2 = full,  1 = weak,  0 = absent.
    """
    sections = ["V1", "V2", "C1", "V3", "C2", "Br", "C3", "Out"]

    tracks = [
        "Sound design (V1 first 7s)",
        "Upright piano",
        "Synth pad",
        "Sub-bass",
        "Soft kick",
        "Drum kit (with snare/hat)",
        "Lead vocal",
        "Octave doubling",
        "L/R harmonies",
        "Stacked harmonies (multi-layer)",
        "‘Ooh ooh-ooh’ ad-libs",
    ]

    # Original design from Moore-style close reading.
    DESIGN = np.array([
        [2, 0, 0, 0, 0, 0, 0, 0],
        [2, 2, 2, 2, 2, 1, 2, 2],
        [0, 1, 2, 0, 2, 0, 2, 1],
        [0, 0, 2, 0, 2, 1, 2, 0],
        [0, 0, 2, 0, 2, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],   # NO drum kit (no snare/hi-hat)
        [2, 2, 2, 2, 2, 2, 2, 1],
        [0, 1, 2, 0, 2, 1, 2, 0],
        [0, 0, 2, 0, 2, 1, 2, 0],
        [0, 0, 1, 0, 1, 2, 2, 0],
        [0, 0, 0, 0, 0, 2, 0, 0],
    ])

    # V_A (Suno v5.5, no tags) — from close listening.
    # V1 guitar+piano+vocal, then drums + more layers from C1 onward,
    # bridge same as chorus (no inversion), C3 has background vocals
    V_A = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0],   # NO sound design intro
        [2, 2, 2, 2, 2, 2, 2, 2],   # piano throughout
        [1, 1, 2, 1, 2, 2, 2, 1],   # synth pad pretty filled
        [0, 0, 2, 1, 2, 2, 2, 1],   # sub-bass present in choruses + bridge (over-filled)
        [0, 0, 2, 1, 2, 2, 2, 1],   # kick same
        [0, 0, 2, 2, 2, 2, 2, 1],   # FULL DRUM KIT (against design)
        [2, 2, 2, 2, 2, 2, 2, 2],   # vocal throughout
        [1, 1, 2, 1, 2, 2, 2, 1],   # generic doubling
        [0, 1, 2, 1, 2, 2, 2, 1],   # generic L/R harmonies
        [0, 0, 0, 0, 0, 1, 1, 0],   # weak stacked harmonies in bridge/C3
        [0, 0, 0, 0, 0, 0, 0, 0],   # NO ad-libs
    ])

    # V_B (Suno v5.5, with inline tags) — slightly more dynamic but bridge still loud
    V_B = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0],
        [2, 2, 2, 2, 2, 2, 2, 1],
        [1, 1, 2, 1, 2, 2, 2, 1],
        [0, 1, 2, 1, 2, 2, 2, 1],
        [0, 1, 2, 1, 2, 2, 2, 1],
        [0, 1, 2, 1, 2, 2, 2, 1],   # full drum kit again
        [2, 2, 2, 2, 2, 2, 2, 1],
        [1, 1, 2, 1, 2, 2, 2, 1],
        [1, 1, 2, 1, 2, 2, 2, 1],
        [0, 0, 1, 0, 1, 2, 2, 0],   # SOME stacked harmonies in bridge (tag effect)
        [0, 0, 0, 0, 0, 1, 0, 0],   # some ad-libs
    ])

    # v4.5 (Suno v4.5) — abrupt transitions; bridge LIGHTER
    V45 = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0],
        [2, 2, 2, 2, 2, 1, 2, 2],   # piano weakens in bridge →OK
        [0, 1, 1, 0, 1, 0, 1, 0],   # less pad
        [0, 0, 2, 0, 2, 0, 2, 0],   # sub-bass drops in bridge →OK
        [0, 0, 2, 0, 2, 0, 2, 0],   # kick drops in bridge →OK
        [2, 2, 2, 2, 2, 0, 2, 0],   # Percussion intro; drum drops in bridge.
        [2, 2, 2, 2, 2, 2, 2, 2],
        [0, 1, 2, 0, 2, 1, 2, 0],
        [0, 0, 2, 0, 2, 1, 2, 0],
        [0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
    ])

    matrices = [
        ("(a) Original design", DESIGN, "—"),
        ("(b) Variant A — Suno v5.5 (no tags)", V_A, "no inversion"),
        ("(c) Variant B — Suno v5.5 (with tags)", V_B, "no inversion"),
        ("(d) Variant B — Suno v4.5", V45, "partial inversion →OK"),
    ]

    fig, axes = plt.subplots(2, 2, figsize=(15, 11))
    cmap = ListedColormap(["white", "#cdd9e8", "#1E3A5F"])
    sym = {0: "", 1: "·", 2: "×"}

    for ax, (title, mat, note) in zip(axes.flat, matrices):
        im = ax.imshow(mat, aspect="auto", cmap=cmap, vmin=0, vmax=2)
        for i in range(mat.shape[0]):
            for j in range(mat.shape[1]):
                v = mat[i, j]
                color = "white" if v == 2 else "#444"
                ax.text(j, i, sym[v], ha="center", va="center",
                        fontsize=15, weight="bold", color=color)
        ax.set_xticks(np.arange(len(sections)))
        ax.set_xticklabels(sections, fontsize=10)
        ax.set_yticks(np.arange(len(tracks)))
        ax.set_yticklabels(tracks, fontsize=8.5)
        ax.set_xticks(np.arange(-.5, len(sections), 1), minor=True)
        ax.set_yticks(np.arange(-.5, len(tracks), 1), minor=True)
        ax.grid(which="minor", color="gray", linestyle="-", linewidth=0.4)
        ax.tick_params(which="minor", bottom=False, left=False)
        # bridge highlight
        edgecolor = "#388E3C" if "→OK" in note else "#C72A2A"
        ax.add_patch(Rectangle((4.5, -0.5), 1, len(tracks),
                                fill=False, edgecolor=edgecolor, linewidth=2.0,
                                linestyle="--"))
        ax.set_title(f"{title}  —  bridge: {note}",
                     fontsize=10.5, weight="bold", loc="left")

    fig.suptitle(
        "Textural-layer comparison: original design vs three Suno reconstructions\n"
        "Bridge boxed (red = no inversion, green = partial inversion). "
        "Filled = ×; weak = ·; absent = blank.",
        fontsize=12, weight="bold", y=0.998)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "figC_textural_comparison.png",
                dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)


# ============================================================
# FIGURE D — VOCAL-STAGING SUMMARY
# ============================================================
def figD_vocal_staging():
    """
    Vocal-staging summary chart following Moore (2012) staging vocabulary.
    Rows: original design + 4 generations.
    Columns: V1 / Chorus / Bridge proximity, reverb depth, doubling density,
              processing/compression, mood-fit.
    Encoded as ordinal score 0–3, plotted as filled-square heatmap with
    text annotation.
    """
    rows = ["Original design", "V_A (v5.5, no tags)", "V_B (v5.5, with tags)",
            "v4.5 (with tags)", "Love Story (control)"]
    cols = ["V1\nproximity", "Chorus\nproximity", "Bridge\nproximity",
            "Reverb depth\n(verses → bridge)", "Doubling /\nharmonic stack",
            "Processing\nrestraint", "Mood-fit\nto prompt"]

    # ordinal scores 0=absent/wrong, 1=partial, 2=close, 3=on-design
    # Original design is by definition 3 across the board (it IS the target)
    scores = np.array([
        [3, 3, 3, 3, 3, 3, 3],      # original design (target)
        [3, 2, 1, 1, 1, 2, 1],      # V_A (no tags) — V1 close, bridge fails, restrained
        [1, 2, 1, 2, 2, 1, 1],      # V_B (with tags) — V1 louder, more dynamic, mood still off
        [2, 2, 2, 1, 1, 1, 1],      # v4.5 — bridge partially works, but abrupt
        [3, 3, 3, 3, 3, 3, 3],      # LS — centroid, AI matches design (= LS design)
    ])

    cell_text = np.array([
        ["close-mic",     "wide",          "stack peak",   "long tail",   "multi-stack", "minimal AT", "heart-warm"],
        ["close-mic →OK",   "mid",           "loud, no inv.", "moderate",   "generic",     "moderate",   "off"],
        ["mid (tag↑)",    "mid",           "loud, no inv.", "moderate",   "fuller",      "moderate",   "off"],
        ["mid",           "mid",           "thinner →OK",     "weak",       "generic",     "moderate",   "off"],
        ["mid (matches)", "wide (matches)", "soften (matches)", "matches", "matches",     "matches",    "matches"],
    ])

    fig, ax = plt.subplots(figsize=(14, 5.4))

    # custom colormap: 0 -> red, 1 -> light yellow, 2 -> light green, 3 -> deep green
    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list(
        "fit", ["#C72A2A", "#F4D58D", "#A8D5A2", "#2E8B5E"], N=4)

    im = ax.imshow(scores, aspect="auto", cmap=cmap, vmin=0, vmax=3)

    for i in range(scores.shape[0]):
        for j in range(scores.shape[1]):
            ax.text(j, i, cell_text[i, j], ha="center", va="center",
                    fontsize=8.5, weight="normal", color="black",
                    wrap=True)

    ax.set_xticks(np.arange(len(cols)))
    ax.set_xticklabels(cols, fontsize=9)
    ax.set_yticks(np.arange(len(rows)))
    ax.set_yticklabels(rows, fontsize=9.5)
    ax.set_xticks(np.arange(-.5, len(cols), 1), minor=True)
    ax.set_yticks(np.arange(-.5, len(rows), 1), minor=True)
    ax.grid(which="minor", color="white", linestyle="-", linewidth=2.0)
    ax.tick_params(which="minor", bottom=False, left=False)

    # colorbar
    cbar = fig.colorbar(im, ax=ax, ticks=[0, 1, 2, 3], pad=0.02, shrink=0.7)
    cbar.set_ticklabels(["off-design", "partial", "close", "on-design"])
    cbar.ax.tick_params(labelsize=8)
    cbar.set_label("Fit to original-design target", fontsize=9)

    ax.set_title(
        "Vocal-staging summary: how four AI generations recreate the original's\n"
        "voice-and-space decisions across seven analytical dimensions (after Moore 2012)",
        fontsize=11, weight="bold", pad=10)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "figD_vocal_staging.png",
                dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def main():
    figA_formal_functional_timeline()
    figB_sound_box_triptych()
    figC_textural_comparison()
    figD_vocal_staging()
    print("Generated 4 course-style figures:")
    for p in sorted(FIG_DIR.glob("fig[A-D]_*.png")):
        print(f"  {p.name}  ({p.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
