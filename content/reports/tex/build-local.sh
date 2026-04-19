#!/usr/bin/env bash
# Local LaTeX build script for AgenticCareerBoost reports.
# Mirrors the CI pipeline (.github/workflows/latex-build.yml) exactly.
#
# Usage:
#   ./build-local.sh          # build all sprint documents
#   ./build-local.sh s000     # Sprint S-000 only
#   ./build-local.sh smoke    # preamble smoke test only
#   ./build-local.sh clean    # remove build artifacts

set -euo pipefail
cd "$(dirname "$0")"

COMMON_ARGS="-r latexmkrc -pdf -interaction=nonstopmode -halt-on-error"

if ! command -v latexmk &>/dev/null; then
    echo "ERROR: latexmk not found. Install TeX Live (full) first." >&2
    exit 1
fi

case "${1:-all}" in
    clean)
        echo "[build-local] Cleaning build artifacts..."
        latexmk -r latexmkrc -C 2>/dev/null || true
        rm -rf build/
        echo "[build-local] Clean complete."
        ;;
    smoke)
        echo "[build-local] Building smoke test..."
        latexmk $COMMON_ARGS smoke.tex
        echo "[build-local] OK: build/smoke.pdf"
        ;;
    s000)
        echo "[build-local] Building Sprint S-000..."
        latexmk $COMMON_ARGS sprints/s000-agentic-os-bootstrap.tex
        echo "[build-local] OK: build/s000-agentic-os-bootstrap.pdf"
        ;;
    all)
        for f in sprints/*.tex; do
            [ -f "$f" ] || continue
            echo "[build-local] Building $f..."
            latexmk $COMMON_ARGS "$f"
        done
        echo "[build-local] Done. PDFs in build/"
        ls -la build/*.pdf 2>/dev/null || echo "No PDFs produced."
        ;;
    *)
        echo "Usage: $0 [all|s000|smoke|clean]" >&2
        exit 1
        ;;
esac
