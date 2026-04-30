# Publication Checklist

Before publishing this folder as an independent public repository:

1. Confirm the repository is initialized at this folder, not at a broader parent directory.
2. Run `git lfs ls-files` and verify that generated `.wav` and `.mp3` files are tracked by Git LFS.
3. Run `git status --ignored --short .` and verify that `.claude/`, `private/lyrics/`, course materials, and process notes are ignored.
4. Run `git add -n .` and review the staged-file preview before any real commit.
5. Do not add original commercial audio, complete lyrics, near-verbatim lyric prompts, line-by-line lyric mappings, course PDFs, or private process notes.
6. If publishing to GitHub, add the actual repository URL to `CITATION.cff` only after the remote exists.
7. Re-run `make figures` and `make paper` before tagging a release.
8. If metrics are recomputed from local audio, run `make metrics` first, then regenerate figures and paper.
