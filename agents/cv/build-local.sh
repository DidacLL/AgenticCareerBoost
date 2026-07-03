#!/usr/bin/env bash
# Build public CV and cover-letter PDFs from agents/cv/artifacts.json.

set -euo pipefail
cd "$(dirname "$0")"
repo_root="$(cd ../.. && pwd)"

if ! command -v python &>/dev/null; then
    echo "ERROR: python not found." >&2
    exit 1
fi
if ! command -v pdflatex &>/dev/null && ! command -v latexmk &>/dev/null; then
    echo "ERROR: pdflatex or latexmk not found. Install TeX Live first." >&2
    exit 1
fi

python tools/artifact_manifest.py validate
python tools/render-cover-letter.py --all
mkdir -p build

build_tex() {
    local tex_file="$1"
    local label="$2"
    echo "[cv-build] Building ${label}..."
    if command -v latexmk &>/dev/null; then
        latexmk -r latexmkrc -pdf -interaction=nonstopmode -halt-on-error "$tex_file"
    else
        for pass in 1 2 3; do
            printf '  pass %s/3...' "$pass"
            pdflatex -interaction=nonstopmode -halt-on-error \
              -output-directory=build -aux-directory=build "$tex_file" >/dev/null
            echo " ok"
        done
    fi
}

mapfile -t tex_roots < <(python tools/artifact_manifest.py roots)
for tex_file in "${tex_roots[@]}"; do
    [[ -z "$tex_file" ]] && continue
    base_name="$(basename "${tex_file%.tex}")"
    build_tex "$tex_file" "$base_name"
done

python tools/artifact_manifest.py publish

echo "[cv-build] Done."
