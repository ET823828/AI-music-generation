"""
Objective signal analysis for AI-generated reconstructions.
Outputs per-file metrics into data/ and 4 figures per file (mel-spec, RMS,
spectral centroid, chromagram) into figures/.

Drives the form, texture, and spectrogram portions of the analysis; vocal
staging, mood, and production decisions are evaluated through close listening.
"""
from pathlib import Path
import json
import os
import numpy as np
import librosa
import librosa.display
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
FIG_DIR = ROOT / "figures"
DATA_DIR.mkdir(exist_ok=True)
FIG_DIR.mkdir(exist_ok=True)
AUDIO_DIR = Path(os.environ.get("AUDIO_DIR", ROOT / "private" / "audio"))

# Reference: drivers license original — B♭ major, 144 BPM notated / 72 half-time, 4:02
# Eight reference windows (s) used for close-listening comparison.
DL_SECTIONS = [
    ("V1",     0.0,   30.0),
    ("V2",    30.0,   54.0),
    ("C1",    54.0,   87.0),
    ("V3",    87.0,  110.0),
    ("C2",   110.0,  143.0),
    ("Br",   143.0,  175.0),
    ("C3",   175.0,  197.0),
    ("Out",  197.0,  242.0),
]
DL_REF = {"key": "B♭ major", "tempo_bpm": [72, 144], "duration_s": 242.0, "sections": DL_SECTIONS}

# Reference: Love Story — D major with upward final-chorus modulation cue, 119 BPM, 3:55
# Ten reference windows (s) used for close-listening comparison.
LS_SECTIONS = [
    ("V1",     0.0,   23.0),
    ("PC1",   23.0,   38.0),
    ("C1",    38.0,   54.0),
    ("V2",    54.0,   73.0),
    ("PC2",   73.0,   88.0),
    ("C2",    88.0,  115.0),
    ("PostC", 115.0, 129.0),
    ("Br",   129.0,  150.0),
    ("C3*",  150.0,  198.0),  # modulated
    ("Out",  198.0,  235.0),
]
LS_REF = {"key": "D major", "tempo_bpm": [119], "duration_s": 235.0, "sections": LS_SECTIONS}

FILES = [
    {"label": "dl_VarA_v5.5",         "path": "driver_license_with_no_emotion.wav",        "ref": DL_REF, "song": "drivers license"},
    {"label": "dl_VarB_v5.5",         "path": "driver_license_with_detailed_emotion.wav",  "ref": DL_REF, "song": "drivers license"},
    {"label": "dl_VarB_v4.5",         "path": "driver_license_suno_v4.5.wav",              "ref": DL_REF, "song": "drivers license"},
    {"label": "love_story_v5.5",      "path": "love_story_suno.wav",                       "ref": LS_REF, "song": "Love Story"},
]


def audio_path(filename: str) -> Path:
    """Resolve local audio without requiring redistributable audio in the repo."""
    candidates = [AUDIO_DIR / filename, ROOT / filename]
    for path in candidates:
        if path.exists():
            return path
    return candidates[0]

KS_MAJ = np.array([6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88])
KS_MIN = np.array([6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17])
PCS = ["C", "C#", "D", "E♭", "E", "F", "F#", "G", "A♭", "A", "B♭", "B"]


def estimate_key(chroma_mean: np.ndarray) -> tuple[str, str, float]:
    best = ("", "", -np.inf)
    for tonic in range(12):
        for mode_name, profile in (("major", KS_MAJ), ("minor", KS_MIN)):
            shifted = np.roll(profile, tonic)
            corr = float(np.corrcoef(chroma_mean, shifted)[0, 1])
            if corr > best[2]:
                best = (PCS[tonic], mode_name, corr)
    return best


def section_rms(rms_db: np.ndarray, times: np.ndarray, sections: list) -> dict:
    """Per-section median RMS (dB)."""
    out = {}
    for name, t0, t1 in sections:
        mask = (times >= t0) & (times < t1)
        if mask.sum() == 0:
            continue
        out[name] = round(float(np.median(rms_db[mask])), 2)
    return out


def section_centroid(sc: np.ndarray, sc_times: np.ndarray, sections: list) -> dict:
    out = {}
    for name, t0, t1 in sections:
        mask = (sc_times >= t0) & (sc_times < t1)
        if mask.sum() == 0:
            continue
        out[name] = int(float(np.median(sc[mask])))
    return out


def detect_segments(y: np.ndarray, sr: int, n_seg: int = 8) -> list[float]:
    chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
    bounds = librosa.segment.agglomerative(chroma, k=n_seg)
    return [round(float(t), 2) for t in librosa.frames_to_time(bounds, sr=sr)]


def analyze(entry: dict) -> dict:
    label = entry["label"]
    path = audio_path(entry["path"])
    ref = entry["ref"]
    print(f"\n=== {label}  ({path.name}, ref={entry['song']}) ===")
    if not path.exists():
        print(f"SKIP: not found at {path}")
        return {"label": label, "missing": True}

    y, sr = librosa.load(path, sr=None, mono=False)
    n_channels = y.shape[0] if y.ndim == 2 else 1
    y_mono = librosa.to_mono(y) if y.ndim == 2 else y
    duration = float(librosa.get_duration(y=y_mono, sr=sr))

    tempo, _ = librosa.beat.beat_track(y=y_mono, sr=sr)
    tempo = float(np.atleast_1d(tempo)[0])

    chroma = librosa.feature.chroma_cqt(y=y_mono, sr=sr)
    chroma_mean = chroma.mean(axis=1)
    chroma_mean /= (chroma_mean.sum() + 1e-9)
    key_root, key_mode, key_conf = estimate_key(chroma_mean)

    rms = librosa.feature.rms(y=y_mono, frame_length=2048, hop_length=512)[0]
    rms_db = 20 * np.log10(rms + 1e-9)
    rms_smooth = np.convolve(rms_db, np.ones(50) / 50, mode="same")
    times = librosa.times_like(rms_db, sr=sr, hop_length=512)

    sc = librosa.feature.spectral_centroid(y=y_mono, sr=sr)[0]
    sc_times = librosa.times_like(sc, sr=sr)
    sf = float(librosa.feature.spectral_flatness(y=y_mono)[0].mean())

    boundaries_auto = detect_segments(y_mono, sr, n_seg=len(ref["sections"]))

    # per-section dynamics (clipped to actual duration)
    valid_sections = [(n, t0, min(t1, duration)) for n, t0, t1 in ref["sections"] if t0 < duration]
    rms_by_section = section_rms(rms_db, times, valid_sections)
    sc_by_section = section_centroid(sc, sc_times, valid_sections)

    metrics = {
        "label": label,
        "song_ref": entry["song"],
        "file": path.name,
        "duration_s": round(duration, 2),
        "duration_str": f"{int(duration//60)}:{duration%60:05.2f}",
        "duration_vs_ref": round(duration - ref["duration_s"], 1),
        "sample_rate": sr,
        "channels": n_channels,
        "tempo_estimated_bpm": round(tempo, 1),
        "tempo_ref_bpm": ref["tempo_bpm"],
        "key_estimated": f"{key_root} {key_mode}",
        "key_ref": ref["key"],
        "key_correlation": round(key_conf, 3),
        "rms_median_db": round(float(np.median(rms_db)), 2),
        "rms_peak_db": round(float(np.max(rms_db)), 2),
        "rms_p95_db": round(float(np.percentile(rms_db, 95)), 2),
        "rms_p5_db": round(float(np.percentile(rms_db, 5)), 2),
        "dynamic_range_p95_p5_db": round(float(np.percentile(rms_db, 95) - np.percentile(rms_db, 5)), 2),
        "spectral_centroid_mean_hz": round(float(sc.mean()), 0),
        "spectral_centroid_std_hz": round(float(sc.std()), 0),
        "spectral_flatness_mean": round(sf, 4),
        "rms_by_section_db": rms_by_section,
        "centroid_by_section_hz": sc_by_section,
        "auto_segment_boundaries_s": boundaries_auto,
    }
    print(json.dumps(metrics, indent=2, ensure_ascii=False))

    # === Figures ===
    # 1. Mel-spectrogram with section boundaries
    fig, ax = plt.subplots(figsize=(14, 4))
    S = librosa.feature.melspectrogram(y=y_mono, sr=sr, n_mels=128, fmax=8000)
    img = librosa.display.specshow(librosa.power_to_db(S, ref=np.max),
                                    x_axis="time", y_axis="mel", sr=sr, fmax=8000, ax=ax, cmap="magma")
    fig.colorbar(img, ax=ax, format="%+2.0f dB")
    for name, t0, _ in valid_sections:
        ax.axvline(t0, color="cyan", lw=0.7, alpha=0.8)
        ax.text(t0 + 0.3, 7000, name, color="cyan", fontsize=8, alpha=0.95, weight="bold")
    ax.set_title(f"Mel-spectrogram — {label}  |  ref: {entry['song']}  (cyan = original section starts)")
    fig.tight_layout()
    fig.savefig(FIG_DIR / f"spec_{label}.png", dpi=140)
    plt.close(fig)

    # 2. RMS envelope
    fig, ax = plt.subplots(figsize=(14, 3.8))
    ax.plot(times, rms_db, color="lightgray", lw=0.4, label="RMS (frame)")
    ax.plot(times, rms_smooth, color="black", lw=1.0, label="RMS (smoothed)")
    for name, t0, _ in valid_sections:
        ax.axvline(t0, color="cyan", lw=0.6, alpha=0.7)
        ax.text(t0 + 0.3, np.percentile(rms_db, 95) + 0.5, name, color="cyan", fontsize=8, weight="bold")
    for b in boundaries_auto:
        ax.axvline(b, color="red", lw=0.6, alpha=0.4, linestyle="--")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("RMS (dB)")
    ax.set_title(f"RMS envelope — {label}  (cyan=original sections, red dashed=auto-detected)")
    ax.legend(loc="lower right", fontsize=8)
    ax.set_xlim(0, max(duration, ref["duration_s"]))
    fig.tight_layout()
    fig.savefig(FIG_DIR / f"rms_{label}.png", dpi=140)
    plt.close(fig)

    # 3. Spectral centroid (brightness)
    fig, ax = plt.subplots(figsize=(14, 3))
    ax.plot(sc_times, sc, color="darkgreen", lw=0.4, alpha=0.6)
    ax.plot(sc_times, np.convolve(sc, np.ones(50) / 50, mode="same"), color="black", lw=1.0)
    for name, t0, _ in valid_sections:
        ax.axvline(t0, color="cyan", lw=0.6, alpha=0.7)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Spectral centroid (Hz)")
    ax.set_title(f"Spectral centroid — {label}")
    ax.set_xlim(0, max(duration, ref["duration_s"]))
    fig.tight_layout()
    fig.savefig(FIG_DIR / f"centroid_{label}.png", dpi=140)
    plt.close(fig)

    # 4. Chromagram + key profile
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 5), gridspec_kw={"height_ratios": [3, 1]})
    librosa.display.specshow(chroma, x_axis="time", y_axis="chroma", ax=ax1, cmap="coolwarm")
    ax1.set_title(f"Chromagram — {label}  |  estimated: {key_root} {key_mode} (corr={key_conf:.3f})  |  ref: {ref['key']}")
    ax2.bar(PCS, chroma_mean, color="steelblue")
    ax2.set_ylabel("Weight")
    ax2.set_title("Mean chroma profile (12 pitch classes)")
    fig.tight_layout()
    fig.savefig(FIG_DIR / f"chroma_{label}.png", dpi=140)
    plt.close(fig)

    return metrics


def main() -> None:
    results = {}
    for entry in FILES:
        results[entry["label"]] = analyze(entry)
    out_json = DATA_DIR / "ai_audio_metrics.json"
    out_json.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nWrote {out_json}")
    print(f"Wrote {len(list(FIG_DIR.glob('*.png')))} figures to {FIG_DIR}/")


if __name__ == "__main__":
    main()
