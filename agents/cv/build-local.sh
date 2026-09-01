#!/usr/bin/env bash
# Build public career PDFs from agents/cv/artifacts.json.

set -euo pipefail
cv_root="$(cd "$(dirname "$0")" && pwd)"
tex_root="$cv_root/tex"
build_root="$cv_root/build"
cd "$cv_root"

if ! command -v python &>/dev/null; then
    echo "ERROR: python not found." >&2
    exit 1
fi
if ! command -v pdflatex &>/dev/null && ! command -v latexmk &>/dev/null; then
    echo "ERROR: pdflatex or latexmk not found. Install TeX Live first." >&2
    exit 1
fi

python tools/artifact_manifest.py validate
mkdir -p "$build_root"

clean_source_aux() {
    local base_name="$1"
    local suffix
    for suffix in aux log out fls fdb_latexmk synctex.gz toc lof lot nav snm vrb bbl bcf blg run.xml xdv; do
        rm -f "$tex_root/$base_name.$suffix"
    done
}

build_tex() {
    local manifest_source="$1"
    local source_name
    local base_name
    source_name="$(basename "$manifest_source")"
    base_name="${source_name%.tex}"

    clean_source_aux "$base_name"
    echo "[cv-build] Building ${base_name}..."

    if ! (
        cd "$tex_root"
        if command -v latexmk &>/dev/null; then
            latexmk -r ../latexmkrc -pdf -interaction=nonstopmode -halt-on-error \
              -outdir=../build -auxdir=../build "$source_name"
        else
            for pass in 1 2 3; do
                printf '  pass %s/3...' "$pass"
                pdflatex -interaction=nonstopmode -halt-on-error \
                  -output-directory=../build "$source_name" >/dev/null
                echo " ok"
            done
        fi
    ); then
        clean_source_aux "$base_name"
        return 1
    fi

    clean_source_aux "$base_name"
}

mapfile -t tex_roots < <(python tools/artifact_manifest.py roots)
for tex_file in "${tex_roots[@]}"; do
    [[ -z "$tex_file" ]] && continue
    build_tex "$tex_file"
done

python tools/artifact_manifest.py publish

echo "[cv-build] Done. Generated files are under agents/cv/build/."
