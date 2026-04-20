#!/usr/bin/env bash
# Local LaTeX build script for AgenticCareerBoost reports.
# Mirrors the CI pipeline (.github/workflows/latex-build.yml) closely.
#
# Usage:
#   ./build-local.sh          # build all report documents
#   ./build-local.sh s000     # Sprint S-000 only
#   ./build-local.sh guide    # Agentic system guide only
#   ./build-local.sh smoke    # preamble smoke test only
#   ./build-local.sh clean    # remove build artifacts

set -euo pipefail
cd "$(dirname "$0")"

COMMON_ARGS=(-r latexmkrc -pdf -interaction=nonstopmode -halt-on-error)

if ! command -v pdflatex &>/dev/null; then
    echo "ERROR: pdflatex not found. Install TeX Live first." >&2
    exit 1
fi

use_latexmk=false
if command -v latexmk &>/dev/null; then
    use_latexmk=true
fi

build_with_pdflatex() {
    local tex_file="$1"
    local label="$2"
    mkdir -p build
    echo "[build-local] Building ${label}..."
    for pass in 1 2 3; do
        printf '  pass %s/3...' "$pass"
        pdflatex -interaction=nonstopmode -halt-on-error \
          -output-directory=build -aux-directory=build "$tex_file" >/dev/null
        echo " ok"
    done
    echo "[build-local] OK: build/$(basename "${tex_file%.tex}").pdf"
}

build_with_latexmk() {
    local tex_file="$1"
    local label="$2"
    echo "[build-local] Building ${label}..."
    latexmk "${COMMON_ARGS[@]}" "$tex_file"
    echo "[build-local] OK: build/$(basename "${tex_file%.tex}").pdf"
}

build_tex_file() {
    local tex_file="$1"
    local label="$2"
    if [[ "$use_latexmk" == true ]]; then
        build_with_latexmk "$tex_file" "$label"
    else
        build_with_pdflatex "$tex_file" "$label"
    fi
}

case "${1:-all}" in
    clean)
        echo "[build-local] Cleaning build artifacts..."
        if [[ "$use_latexmk" == true ]]; then
            latexmk -r latexmkrc -C 2>/dev/null || true
        fi
        rm -rf build/
        echo "[build-local] Clean complete."
        ;;
    smoke)
        build_tex_file smoke.tex "smoke test"
        ;;
    s000)
        build_tex_file sprints/s000-agentic-os-bootstrap.tex "Sprint S-000"
        ;;
    guide)
        build_tex_file guides/agentic-system-guide.tex "Agentic system guide"
        ;;
    all)
        shopt -s nullglob
        files=(sprints/*.tex guides/*.tex)
        if (( ${#files[@]} == 0 )); then
            echo "No report documents found."
            exit 0
        fi
        for f in "${files[@]}"; do
            build_tex_file "$f" "$f"
        done
        echo "[build-local] Done. PDFs in build/"
        ls -la build/*.pdf 2>/dev/null || echo "No PDFs produced."
        ;;
    *)
        echo "Usage: $0 [all|s000|guide|smoke|clean]" >&2
        exit 1
        ;;
esac
