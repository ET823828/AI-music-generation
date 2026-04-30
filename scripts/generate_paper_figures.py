"""
Paper-ready visualization figures for the §3-§6 ablation argument.

Reads data/ai_audio_metrics.json (objective signal metrics from analyze_ai_audio.py)
+ section-level RMS / centroid / key data, and produces 8 figures focused on
the paper's quantitative findings F1-F9.

All figures use a consistent color scheme:
  - dl V_A (Suno v5.5, no tags):  steelblue
  - dl V_B (Suno v5.5, with tags): darkorange
  - dl V_B (Suno v4.5):            forestgreen
  - LS (Suno v5.5):                purple
  - dl original design ref:        crimson dashed
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches

ROOT = Path(__file__).resolve().parent.parent
FIG_DIR = ROOT / "figures"
FIG_DIR.mkdir(exist_ok=True)
METRICS_PATH = ROOT / "data" / "ai_audio_metrics.json"
if not METRICS_PATH.exists():
    METRICS_PATH = ROOT / "ai_audio_metrics.json"

# Load metrics
with open(METRICS_PATH) as f:
    M = json.load(f)

# Color scheme (consistent across all figures)
COL = {
    "dl_VarA_v5.5":     "#2E5E9B",   # steelblue
    "dl_VarB_v5.5":     "#E07B0F",   # darkorange
    "dl_VarB_v4.5":     "#2E8B5E",   # forestgreen
    "love_story_v5.5":  "#7A3CA0",   # purple
    "design":           "#C72A2A",   # crimson
}
LABEL = {
    "dl_VarA_v5.5":    "dl V_A (Suno v5.5, no tags)",
    "dl_VarB_v5.5":    "dl V_B (Suno v5.5, with tags)",
    "dl_VarB_v4.5":    "dl V_B (Suno v4.5)",
    "love_story_v5.5": "Love Story (Suno v5.5, control)",
    "design":          "Original design (target)",
}

DL_SECTIONS = ["V1", "V2", "C1", "V3", "C2", "Br", "C3", "Out"]
LS_SECTIONS = ["V1", "PC1", "C1", "V2", "PC2", "C2", "PostC", "Br", "C3*", "Out"]

# Estimated dl original section-level RMS targets (from close-reading + literature)
DL_DESIGN_RMS = {
    "V1": -32, "V2": -27, "C1": -18, "V3": -28,
    "C2": -18, "Br": -22, "C3": -19, "Out": -28,
}


# ============================================================
# Figure 1: Per-section RMS — dl three variants vs original design
# ============================================================
def fig1_dl_rms_per_section():
    fig, ax = plt.subplots(figsize=(11, 5))
    x = np.arange(len(DL_SECTIONS))

    for label in ["dl_VarA_v5.5", "dl_VarB_v5.5", "dl_VarB_v4.5"]:
        rms = M[label]["rms_by_section_db"]
        y = [rms.get(s, np.nan) for s in DL_SECTIONS]
        ax.plot(x, y, marker="o", linewidth=2.2, markersize=8,
                color=COL[label], label=LABEL[label])

    # Design reference line
    design = [DL_DESIGN_RMS[s] for s in DL_SECTIONS]
    ax.plot(x, design, marker="*", markersize=14, linewidth=2.5,
            linestyle="--", color=COL["design"], label=LABEL["design"], alpha=0.85)

    # Annotations for key findings
    ax.annotate("F4: v4.5 alone\npreserves bridge\ninverse density",
                xy=(5, M["dl_VarB_v4.5"]["rms_by_section_db"]["Br"]),
                xytext=(5.2, -38), fontsize=9, color=COL["dl_VarB_v4.5"],
                arrowprops=dict(arrowstyle="->", color=COL["dl_VarB_v4.5"], lw=1.4),
                ha="left", weight="bold")
    ax.annotate("F7: V_A's V1 closest\nto original ASMR",
                xy=(0, M["dl_VarA_v5.5"]["rms_by_section_db"]["V1"]),
                xytext=(0.4, -38), fontsize=9, color=COL["dl_VarA_v5.5"],
                arrowprops=dict(arrowstyle="->", color=COL["dl_VarA_v5.5"], lw=1.4),
                ha="left", weight="bold")
    ax.annotate("F5: outro no fade\n(all 3 dl variants)",
                xy=(7, M["dl_VarA_v5.5"]["rms_by_section_db"]["Out"]),
                xytext=(6.0, -10), fontsize=9, color="black",
                arrowprops=dict(arrowstyle="->", color="black", lw=1.2),
                ha="left", weight="bold")

    ax.set_xticks(x)
    ax.set_xticklabels(DL_SECTIONS, fontsize=11)
    ax.set_xlabel("Section (Genius 8-section labeling)", fontsize=11)
    ax.set_ylabel("RMS (dB)", fontsize=11)
    ax.set_title("Per-section loudness across drivers license generations\n"
                 "(lower = quieter; original design requires V1 valleys and bridge subtraction)",
                 fontsize=12, weight="bold")
    ax.set_ylim(-40, -8)
    ax.grid(True, alpha=0.3, linestyle=":")
    ax.legend(loc="lower right", fontsize=9, framealpha=0.95)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig1_dl_rms_per_section.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


# ============================================================
# Figure 2: Per-section RMS — Love Story (mainstream control) vs dl AI
# ============================================================
def fig2_ls_vs_dl_flatness():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 4.5))

    # Left: Love Story per-section RMS (mainstream control, near-flat)
    ls_rms = M["love_story_v5.5"]["rms_by_section_db"]
    x_ls = np.arange(len(LS_SECTIONS))
    y_ls = [ls_rms.get(s, np.nan) for s in LS_SECTIONS]
    ax1.plot(x_ls, y_ls, marker="o", linewidth=2.2, markersize=8,
             color=COL["love_story_v5.5"], label=LABEL["love_story_v5.5"])

    ls_spread = max(y_ls) - min(y_ls)
    ax1.axhline(np.mean(y_ls), color=COL["love_story_v5.5"], linestyle=":", alpha=0.6)
    ax1.text(0.3, np.mean(y_ls) + 0.4, f"spread = {ls_spread:.1f} dB",
             color=COL["love_story_v5.5"], fontsize=10, weight="bold")
    ax1.set_xticks(x_ls)
    ax1.set_xticklabels(LS_SECTIONS, fontsize=10, rotation=0)
    ax1.set_ylabel("RMS (dB)", fontsize=11)
    ax1.set_title("Love Story (Suno v5.5, control)\n"
                  "near-flat profile = mainstream centroid signature",
                  fontsize=11, weight="bold")
    ax1.set_ylim(-35, -8)
    ax1.grid(True, alpha=0.3, linestyle=":")

    # Right: dl V_A spread (target was ~17 dB but only V_A reaches it via deep V1)
    va_rms = M["dl_VarA_v5.5"]["rms_by_section_db"]
    x_dl = np.arange(len(DL_SECTIONS))
    y_dl = [va_rms.get(s, np.nan) for s in DL_SECTIONS]
    ax2.plot(x_dl, y_dl, marker="o", linewidth=2.2, markersize=8,
             color=COL["dl_VarA_v5.5"], label=LABEL["dl_VarA_v5.5"])
    design = [DL_DESIGN_RMS[s] for s in DL_SECTIONS]
    ax2.plot(x_dl, design, marker="*", markersize=12, linewidth=2.0,
             linestyle="--", color=COL["design"], alpha=0.85, label="dl design target")
    dl_spread = max(y_dl) - min(y_dl)
    design_spread = max(design) - min(design)
    ax2.text(0.3, -10, f"AI spread = {dl_spread:.1f} dB\ndesign = {design_spread:.0f} dB",
             color=COL["dl_VarA_v5.5"], fontsize=10, weight="bold")
    ax2.set_xticks(x_dl)
    ax2.set_xticklabels(DL_SECTIONS, fontsize=10)
    ax2.set_ylabel("RMS (dB)", fontsize=11)
    ax2.set_title("drivers license V_A (Suno v5.5)\n"
                  "compressed version of design's tail-spread",
                  fontsize=11, weight="bold")
    ax2.set_ylim(-35, -8)
    ax2.grid(True, alpha=0.3, linestyle=":")
    ax2.legend(loc="lower right", fontsize=9)

    fig.suptitle("Love Story (centroid-typical) reproduces flatness; "
                 "drivers license (centroid-distant) does not reach the deep V1 valley",
                 fontsize=12, weight="bold", y=1.02)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig2_ls_flat_vs_dl_compressed.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


# ============================================================
# Figure 3: Dynamic range bar chart (4 generations) — F6 evidence
# ============================================================
def fig3_dynamic_range_bars():
    fig, ax = plt.subplots(figsize=(10, 5))

    labels = ["dl_VarA_v5.5", "dl_VarB_v5.5", "dl_VarB_v4.5", "love_story_v5.5"]
    dr = [M[lbl]["dynamic_range_p95_p5_db"] for lbl in labels]
    colors = [COL[lbl] for lbl in labels]
    short = ["dl V_A\n(v5.5)", "dl V_B\n(v5.5)", "dl V_B\n(v4.5)", "Love Story\n(v5.5, control)"]

    bars = ax.bar(short, dr, color=colors, edgecolor="black", linewidth=1.2)
    for bar, val in zip(bars, dr):
        ax.text(bar.get_x() + bar.get_width()/2, val + 0.4,
                f"{val:.1f} dB", ha="center", fontsize=11, weight="bold")

    # design reference shaded band
    ax.axhspan(15, 22, alpha=0.13, color=COL["design"],
               label="dl design target (≈17–20 dB)")
    ax.axhline(13, color=COL["love_story_v5.5"], linestyle=":", linewidth=1.5,
               alpha=0.7)
    ax.text(3.4, 12.5, "LS achieves\nmainstream-flat", fontsize=8.5,
            color=COL["love_story_v5.5"], ha="right", style="italic")

    ax.set_ylabel("Dynamic range (p95 – p5, dB)", fontsize=11)
    ax.set_title("Dynamic range across four AI generations:\n"
                 "centroid-distant (dl) over-spreads while centroid-typical (LS) hits mainstream-flat",
                 fontsize=12, weight="bold")
    ax.set_ylim(0, 32)
    ax.grid(True, axis="y", alpha=0.3, linestyle=":")
    ax.legend(loc="upper right", fontsize=9)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig3_dynamic_range_bars.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


# ============================================================
# Figure 4: Key fidelity scatter — F2 evidence
# ============================================================
def fig4_key_fidelity():
    fig, ax = plt.subplots(figsize=(10, 5))

    # x = generation, y = semitone offset from prompted key
    KEY_DATA = [
        ("dl V_A v5.5", "B", "B♭", +1, COL["dl_VarA_v5.5"], 0.907),
        ("dl V_B v5.5", "B", "B♭", +1, COL["dl_VarB_v5.5"], 0.866),
        ("dl V_B v4.5", "E♭", "B♭", +5, COL["dl_VarB_v4.5"], 0.907),
        ("LS v5.5",    "D", "D",  0, COL["love_story_v5.5"], 0.873),
    ]
    x = np.arange(len(KEY_DATA))
    offsets = [d[3] for d in KEY_DATA]
    confs = [d[5] for d in KEY_DATA]
    colors = [d[4] for d in KEY_DATA]
    short = [d[0] for d in KEY_DATA]

    sizes = [c * 800 for c in confs]
    sc = ax.scatter(x, offsets, s=sizes, c=colors, edgecolor="black",
                    linewidth=1.4, alpha=0.85, zorder=3)

    for i, (lbl, est, prompt, off, col, conf) in enumerate(KEY_DATA):
        ax.annotate(f"{est}\n(prompt: {prompt})\nconf={conf:.2f}",
                    xy=(i, off), xytext=(i, off + 1.2),
                    ha="center", fontsize=9, weight="bold")

    ax.axhline(0, color="black", linestyle="-", linewidth=1.5, zorder=1)
    ax.axhspan(-0.3, 0.3, alpha=0.15, color="green", zorder=0,
               label="Correct key (offset = 0 semitones)")

    ax.set_xticks(x)
    ax.set_xticklabels(short, fontsize=10)
    ax.set_ylabel("Semitones offset from prompted key\n(positive = upward)", fontsize=10)
    ax.set_title("Key fidelity: drivers license loses prompted key with high model confidence;\n"
                 "Love Story control reproduces it",
                 fontsize=12, weight="bold")
    ax.set_ylim(-1, 7)
    ax.grid(True, axis="y", alpha=0.3, linestyle=":")
    ax.legend(loc="upper left", fontsize=9)

    # marker size legend
    ax.text(3.5, 6.3, "Marker size ∝\nKrumhansl confidence",
            fontsize=8.5, ha="center", style="italic",
            bbox=dict(facecolor="white", edgecolor="gray", alpha=0.9))

    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig4_key_fidelity.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


# ============================================================
# Figure 5: V1 retreat — V_A vs V_B (F7 evidence)
# ============================================================
def fig5_v1_retreat():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))

    # Left: V1 RMS comparison
    labels = ["V_A\n(no tags)", "V_B\n(with tags)"]
    v1_rms = [M["dl_VarA_v5.5"]["rms_by_section_db"]["V1"],
              M["dl_VarB_v5.5"]["rms_by_section_db"]["V1"]]
    cols = [COL["dl_VarA_v5.5"], COL["dl_VarB_v5.5"]]

    bars = ax1.bar(labels, v1_rms, color=cols, edgecolor="black", linewidth=1.5, width=0.55)
    for bar, val in zip(bars, v1_rms):
        ax1.text(bar.get_x() + bar.get_width()/2, val - 1,
                 f"{val:.1f} dB", ha="center", fontsize=12, weight="bold", color="white")

    ax1.axhline(DL_DESIGN_RMS["V1"], color=COL["design"], linestyle="--",
                linewidth=2, label=f"dl design target ({DL_DESIGN_RMS['V1']} dB)")
    ax1.set_ylabel("V1 RMS (dB)", fontsize=11)
    ax1.set_title("V1 loudness", fontsize=11, weight="bold")
    ax1.set_ylim(-35, -15)
    ax1.invert_yaxis()  # quieter at top to visualize "retreat"
    ax1.grid(True, axis="y", alpha=0.3, linestyle=":")
    ax1.legend(loc="lower right", fontsize=9)

    # Right: V1 spectral centroid (brightness)
    v1_sc = [M["dl_VarA_v5.5"]["centroid_by_section_hz"]["V1"],
             M["dl_VarB_v5.5"]["centroid_by_section_hz"]["V1"]]
    bars = ax2.bar(labels, v1_sc, color=cols, edgecolor="black", linewidth=1.5, width=0.55)
    for bar, val in zip(bars, v1_sc):
        ax2.text(bar.get_x() + bar.get_width()/2, val + 60,
                 f"{val} Hz", ha="center", fontsize=12, weight="bold")

    ax2.set_ylabel("V1 spectral centroid (Hz)", fontsize=11)
    ax2.set_title("V1 brightness", fontsize=11, weight="bold")
    ax2.set_ylim(0, 3000)
    ax2.grid(True, axis="y", alpha=0.3, linestyle=":")

    fig.suptitle("Verse-1 retreat: inline emotional tags push V1 louder and brighter,\n"
                 "away from the original's close-mic intimacy",
                 fontsize=12, weight="bold", y=1.04)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig5_v1_retreat.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


# ============================================================
# Figure 6: Bridge inversion — F4 cross-version finding
# ============================================================
def fig6_bridge_inversion():
    fig, ax = plt.subplots(figsize=(10, 5))

    labels = ["dl V_A\n(v5.5)", "dl V_B\n(v5.5)", "dl V_B\n(v4.5)"]
    keys = ["dl_VarA_v5.5", "dl_VarB_v5.5", "dl_VarB_v4.5"]
    cols = [COL[k] for k in keys]

    # Bars: bridge RMS vs surrounding chorus mean
    bridge_rms = [M[k]["rms_by_section_db"]["Br"] for k in keys]
    chorus_mean = [
        np.mean([M[k]["rms_by_section_db"][s] for s in ["C1", "C2", "C3"]])
        for k in keys
    ]

    x = np.arange(len(labels))
    width = 0.35

    b1 = ax.bar(x - width/2, chorus_mean, width, color=cols, alpha=0.5,
                edgecolor="black", label="Mean of choruses (C1, C2, C3)")
    b2 = ax.bar(x + width/2, bridge_rms, width, color=cols, alpha=1.0,
                edgecolor="black", linewidth=1.8, label="Bridge")

    # annotations
    for i in range(3):
        diff = bridge_rms[i] - chorus_mean[i]
        sign = "+" if diff > 0 else ""
        is_inversion = "bridge-region dip" if diff < -2 else "no bridge dip"
        ax.text(i, max(chorus_mean[i], bridge_rms[i]) + 1.0,
                f"Δ = {sign}{diff:.1f} dB\n{is_inversion}",
                ha="center", fontsize=10, weight="bold",
                color=COL["dl_VarB_v4.5"] if diff < -2 else "darkred")

    ax.axhline(DL_DESIGN_RMS["Br"], color=COL["design"], linestyle="--",
               linewidth=1.8, alpha=0.85,
               label=f"dl design target bridge ({DL_DESIGN_RMS['Br']} dB,\n"
                     f"below surrounding ~{DL_DESIGN_RMS['C1']} dB choruses)")

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=11)
    ax.set_ylabel("RMS (dB)", fontsize=11)
    ax.set_title("Reference-window bridge loudness across drivers license generations:\n"
                 "v4.5 shows a bridge-region dip; v5.5 keeps the bridge-region at/above chorus level",
                 fontsize=12, weight="bold")
    ax.set_ylim(-30, -10)
    ax.grid(True, axis="y", alpha=0.3, linestyle=":")
    ax.legend(loc="lower left", fontsize=9, framealpha=0.95)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig6_bridge_inversion.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


# ============================================================
# Figure 7: Spectral centroid time-course — small multiples
# ============================================================
def fig7_centroid_time_4gen():
    fig, axes = plt.subplots(4, 1, figsize=(13, 9), sharex=False)
    keys = ["dl_VarA_v5.5", "dl_VarB_v5.5", "dl_VarB_v4.5", "love_story_v5.5"]

    for ax, k in zip(axes, keys):
        cb = M[k]["centroid_by_section_hz"]
        secs = DL_SECTIONS if M[k]["song_ref"] == "drivers license" else LS_SECTIONS
        x = np.arange(len(secs))
        y = [cb.get(s, np.nan) for s in secs]
        ax.plot(x, y, marker="o", linewidth=2.5, markersize=9, color=COL[k])
        ax.fill_between(x, y, alpha=0.15, color=COL[k])
        ax.set_xticks(x)
        ax.set_xticklabels(secs, fontsize=10)
        ax.set_ylabel("Centroid (Hz)", fontsize=10)
        ax.set_title(LABEL[k], fontsize=11, weight="bold", loc="left")
        ax.grid(True, alpha=0.3, linestyle=":")
        ax.set_ylim(1500, 5000)

    axes[0].set_title("Spectral centroid (brightness) trajectory across sections\n"
                      "Per-generation timbre arc; LS sits at uniform high brightness;\n"
                      "dl V_A's V1 is uniquely dark, closest to the original's close-mic intimacy",
                      fontsize=11, weight="bold", loc="left")
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig7_centroid_time_4gen.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


# ============================================================
# Figure 8: Textural-layer chart — original dl design (Moore framework)
# ============================================================
def fig8_textural_layer_dl_design():
    """
    Moore textural-layer chart for the dl original (design).
    Rows = tracks, cols = sections, fill = density (×=full, ·=weak, blank=absent).
    """
    tracks = [
        "Sound design (V1 first 7s)",
        "Upright piano",
        "Synth pad",
        "Sub-bass",
        "Soft kick",
        "Lead vocal",
        "Octave-down doubling",
        "L/R harmonies",
        "Stacked harmonies (multi-layer)",
        '"Ooh ooh-ooh" ad-libs',
    ]
    # rows = tracks, cols = DL_SECTIONS
    # encoding: 2 = full, 1 = weak, 0 = absent
    matrix = np.array([
        [2, 0, 0, 0, 0, 0, 0, 0],          # sound design (V1 only)
        [2, 2, 2, 2, 2, 1, 2, 2],          # piano
        [0, 1, 2, 0, 2, 0, 2, 1],          # pad
        [0, 0, 2, 0, 2, 1, 2, 0],          # sub-bass
        [0, 0, 2, 0, 2, 0, 2, 0],          # kick
        [2, 2, 2, 2, 2, 2, 2, 1],          # lead vocal
        [0, 1, 2, 0, 2, 1, 2, 0],          # octave doubling
        [0, 0, 2, 0, 2, 1, 2, 0],          # L/R harmonies
        [0, 0, 1, 0, 1, 2, 2, 0],          # stacked harmonies (peak in bridge)
        [0, 0, 0, 0, 0, 2, 0, 0],          # ad-libs (bridge only)
    ])

    fig, ax = plt.subplots(figsize=(11, 6))

    # custom colormap: 0 = white, 1 = light, 2 = dark
    from matplotlib.colors import ListedColormap
    cmap = ListedColormap(["white", "#cdd9e8", "#2E5E9B"])

    im = ax.imshow(matrix, aspect="auto", cmap=cmap, vmin=0, vmax=2)

    # cell text
    sym = {0: "", 1: "·", 2: "×"}
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            v = matrix[i, j]
            color = "white" if v == 2 else "black"
            ax.text(j, i, sym[v], ha="center", va="center",
                    fontsize=18, weight="bold", color=color)

    # gridlines
    ax.set_xticks(np.arange(len(DL_SECTIONS)))
    ax.set_xticklabels(DL_SECTIONS, fontsize=11)
    ax.set_yticks(np.arange(len(tracks)))
    ax.set_yticklabels(tracks, fontsize=10)
    ax.set_xticks(np.arange(-.5, len(DL_SECTIONS), 1), minor=True)
    ax.set_yticks(np.arange(-.5, len(tracks), 1), minor=True)
    ax.grid(which="minor", color="gray", linestyle="-", linewidth=0.5)
    ax.tick_params(which="minor", bottom=False, left=False)

    # bridge highlight box
    ax.add_patch(Rectangle((4.5, -0.5), 1, len(tracks),
                           fill=False, edgecolor="crimson", linewidth=2.5,
                           linestyle="--", label="Bridge (instrument-strip + voice-stack inversion)"))

    ax.set_title("Moore textural-layer chart: drivers license original design\n"
                 "Bridge boxed in red — the strip-and-stack inversion (instruments retreat, voices flood in)",
                 fontsize=12, weight="bold")
    legend_elements = [
        mpatches.Patch(facecolor="#2E5E9B", label="× active"),
        mpatches.Patch(facecolor="#cdd9e8", label="· weak"),
        mpatches.Patch(facecolor="white", edgecolor="gray", label="(blank) absent"),
        mpatches.Patch(facecolor="none", edgecolor="crimson", linestyle="--",
                       label="Bridge inversion zone"),
    ]
    ax.legend(handles=legend_elements, loc="upper left",
              bbox_to_anchor=(1.02, 1), fontsize=9, framealpha=0.95)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig8_textural_layer_dl_design.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def main():
    fig1_dl_rms_per_section()
    fig2_ls_vs_dl_flatness()
    fig3_dynamic_range_bars()
    fig4_key_fidelity()
    fig5_v1_retreat()
    fig6_bridge_inversion()
    fig7_centroid_time_4gen()
    fig8_textural_layer_dl_design()
    print("Generated 8 paper-ready figures:")
    for p in sorted(FIG_DIR.glob("fig*_*.png")):
        print(f"  {p.name}  ({p.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
