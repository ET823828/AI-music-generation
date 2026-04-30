"""Render the final paper PDF from paper_draft.md."""

from pathlib import Path

import pypandoc


ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    pypandoc.convert_file(
        str(ROOT / "paper_draft.md"),
        "pdf",
        outputfile=str(ROOT / "paper_final.pdf"),
        extra_args=[
            "--pdf-engine=xelatex",
            f"--include-in-header={ROOT / 'latex_header.tex'}",
        ],
    )
    print(f"Wrote {ROOT / 'paper_final.pdf'}")


if __name__ == "__main__":
    main()

