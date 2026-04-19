# Makefile — Thin wrapper around latexmk for AgenticCareerBoost LaTeX reports
# Run from content/reports/tex/

LATEXMK = latexmk -r latexmkrc -pdf
SPRINTS = $(wildcard sprints/*.tex)

.PHONY: all s000 smoke clean

all: $(SPRINTS)
	$(LATEXMK) $(SPRINTS)

s000:
	$(LATEXMK) sprints/s000-agentic-os-bootstrap.tex

smoke:
	$(LATEXMK) smoke.tex

clean:
	$(LATEXMK) -C
	rm -rf build/
