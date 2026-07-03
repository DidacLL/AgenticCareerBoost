#!/usr/bin/env bash
# Build public CV and public-safe cover-letter PDFs.

set -euo pipefail
cd "$(dirname "$0")"
repo_root="$(cd ../.. && pwd)"
public_cv_dir="$repo_root/site/files/cv"
public_letter_dir="$repo_root/site/files/cover-letters"

if ! command -v python &>/dev/null; then
    echo "ERROR: python not found." >&2
    exit 1
fi
if ! command -v pdflatex &>/dev/null && ! command -v latexmk &>/dev/null; then
    echo "ERROR: pdflatex or latexmk not found. Install TeX Live first." >&2
    exit 1
fi

python tools/render-cover-letter.py --all
mkdir -p build "$public_cv_dir" "$public_letter_dir"

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

build_tex tex/didac-llorens-cv.tex "CV"
cp build/didac-llorens-cv.pdf "$public_cv_dir/didac-llorens-cv.pdf"
echo "[cv-build] Published: site/files/cv/didac-llorens-cv.pdf"

shopt -s nullglob
for tex_file in build/generated/*.tex; do
    base_name="$(basename "${tex_file%.tex}")"
    build_tex "$tex_file" "$base_name"
    cp "build/${base_name}.pdf" "$public_letter_dir/${base_name}.pdf"
    echo "[cv-build] Published: site/files/cover-letters/${base_name}.pdf"
done

echo "[cv-build] Done."
