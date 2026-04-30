# Reproducibility Notes

## What Can Be Reproduced Publicly

From the public repository alone, a reader can:

1. Inspect the final paper and its cited claims.
2. Inspect the derived metrics in `data/ai_audio_metrics.json`.
3. Regenerate all paper figures from the stored metrics.
4. Rerun signal analysis on the included generated audio files.
5. Review the public style descriptions used for generation.
6. Re-render the paper PDF from Markdown.

## Included Generated Audio

The generated audio analyzed in the paper is tracked under `private/audio/` with Git LFS:

- `driver_license_with_no_emotion.wav`
- `driver_license_with_detailed_emotion.wav`
- `driver_license_suno_v4.5.wav`
- `love_story_suno.wav`
- `YuE_driver_license.mp3`

The analysis script uses the first four files above. The YuE file is retained as a boundary-comparison artifact discussed in the paper. The script also accepts a custom audio directory:

```bash
AUDIO_DIR=/path/to/audio python scripts/analyze_ai_audio.py
```

## Commands

Install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Regenerate figures from existing metrics:

```bash
make figures
```

Recompute metrics from local audio:

```bash
make metrics
```

Render the paper:

```bash
make paper
```

## Methodological Boundaries

The audio metrics use shared Genius-derived reference-section windows across retained generations. They are intended as descriptive anchors. The paper's main evidence remains close listening with Moore-style formal, textural, sound-box, and vocal-staging analysis.

Complete commercial lyrics, near-verbatim lyric prompts, and line-by-line lyric mappings are intentionally excluded from the public repository.
