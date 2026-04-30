# Publication Checklist

Before publishing this folder as an independent public repository:

1. Confirm the repository is initialized at this folder, not at a broader parent directory.
2. Run `git status --ignored --short .` and verify that `private/`, audio files, full lyrics, course materials, and process notes are ignored.
3. Run `git add -n .` and review the staged-file preview before any real commit.
4. Do not add generated audio, original commercial audio, complete lyrics, line-by-line lyric mappings, course PDFs, or private process notes.
5. If publishing to GitHub, add the actual repository URL to `CITATION.cff` only after the remote exists.
6. Re-run `make figures` and `make paper` before tagging a release.
7. If metrics are recomputed from local audio, run `make metrics` first, then regenerate figures and paper.

