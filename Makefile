.PHONY: figures metrics paper

figures:
	python scripts/generate_class_figures.py
	python scripts/generate_paper_figures.py

metrics:
	AUDIO_DIR=private/audio python scripts/analyze_ai_audio.py

paper:
	python scripts/render_paper.py

