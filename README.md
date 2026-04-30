# AI Music Generation

This repository supports the Music 159r final paper **"What AI Can't Reconstruct: A Comparative Analysis of Pop Songs and Their AI-Generated Reconstructions."** The project compares AI-generated reconstructions of Olivia Rodrigo's "drivers license" with a Taylor Swift "Love Story" control, using popular-music analysis methods such as formal function, textural layers, sound-box space, vocal staging, timbre, and section-level energy.

The central question is not whether an AI system can make a plausible pop track. It is whether prompt-based generation preserves the production decisions that make a specific recording distinctive: close-mic vocal intimacy, instrumental subtraction, bridge design, dynamic restraint, and outro dissolution.

## Contents

- `paper_draft.md` and `paper_final.pdf` — paper source and compiled PDF.
- `private/audio/` — generated audio outputs analyzed in the paper, tracked with Git LFS.
- `data/ai_audio_metrics.json` — derived signal-analysis metrics for the retained generations.
- `figures/` — paper figures and diagnostic plots.
- `scripts/` — audio-analysis, figure-generation, and paper-rendering scripts.
- `prompts/` — public style descriptions used for generation.
- `docs/` — reproducibility notes, figure inventory, and publication checklist.

## Audio Files

The repository includes generated audio outputs for auditability:

- `private/audio/driver_license_with_no_emotion.wav` — Suno v5.5, Variant A.
- `private/audio/driver_license_with_detailed_emotion.wav` — Suno v5.5, Variant B.
- `private/audio/driver_license_suno_v4.5.wav` — Suno v4.5, Variant B.
- `private/audio/love_story_suno.wav` — Suno v5.5, control.
- `private/audio/YuE_driver_license.mp3` — YuE boundary comparison.

These files are research artifacts, not source recordings. They are included to make the paper's listening and signal-analysis claims auditable. They are not covered by the MIT or CC BY licenses in this repository.

## Not Included

The public repository does not include complete commercial lyrics, near-verbatim lyric prompts, line-by-line lyric mappings, original commercial recordings, course rubrics, or private process notes. Those materials are excluded to avoid redistributing copyrighted or course-restricted content.

## Reproducing Figures

Install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Regenerate figures from the stored metrics:

```bash
make figures
```

Recompute metrics from the included generated audio:

```bash
make metrics
```

Render the paper:

```bash
make paper
```

Rendering requires Pandoc and a XeLaTeX installation in addition to the Python dependencies.

## Citation

Use `CITATION.cff` for citation metadata.

## License

Code is released under the MIT License. Paper text, original figures, public prompts, and derived data tables are released under CC BY 4.0 unless otherwise noted. Generated audio, third-party songs, commercial lyrics, platform outputs, and course materials are not relicensed by this repository.
