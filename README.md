# What AI Can't Reconstruct

Support repository for a Music 159r final paper on AI-generated pop-song reconstructions. The project compares Suno reconstructions of Olivia Rodrigo's "drivers license" with a Taylor Swift "Love Story" control using popular-music analysis tools: formal function, textural layers, sound-box space, vocal staging, timbre, and section-level energy.

## Repository Contents

- `paper_draft.md` / `paper_final.pdf` — final paper source and rendered PDF.
- `figures/` — paper figures plus diagnostic signal-analysis plots.
- `data/ai_audio_metrics.json` — computed duration, tempo, key-estimate, RMS, spectral-centroid, and section-window metrics.
- `scripts/` — scripts for signal analysis and figure generation.
- `prompts/` — public style descriptions used for generation.
- `docs/` — reproducibility notes, figure inventory, and publication checklist.
- `private/` — local-only working directory excluded from git for audio, complete lyrics, course materials, and process notes.

## Public-Release Boundaries

This repository intentionally does not publish:

- Complete commercial lyrics or line-by-line lyric mappings.
- Generated audio files from Suno/YuE.
- Original commercial audio files.
- Course rubric PDFs and private process notes.

These files are kept locally under `private/` and ignored by git. The public repo includes enough information to inspect the analysis, regenerate figures from local audio, and evaluate the paper's claims without redistributing copyrighted or platform-restricted materials.

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Regenerate figures from existing metrics:

```bash
python scripts/generate_class_figures.py
python scripts/generate_paper_figures.py
```

Rerun audio metrics from local generated audio:

```bash
AUDIO_DIR=private/audio python scripts/analyze_ai_audio.py
```

Render the paper:

```bash
python scripts/render_paper.py
```

Rendering requires Pandoc and a XeLaTeX installation in addition to the Python dependencies.

## Citation

Use `CITATION.cff` for citation metadata.

Before publishing to a public remote, review `docs/publication_checklist.md`.

## License

Code is released under the MIT License. Paper text, figures, prompts, and data tables are released under CC BY 4.0 unless otherwise noted. No rights are granted to third-party songs, lyrics, platforms, or generated audio files that are excluded from the public repository.
