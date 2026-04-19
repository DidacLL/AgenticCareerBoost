#!/usr/bin/env bash
# validate-links.sh
# Validates that internal file references in Markdown documents resolve to
# real files in the repository. Intended for use as a pre-commit hook and
# as the "critical" stage in CI.
#
# Usage:
#   scripts/validate-links.sh [file ...]
#   If no files are supplied every *.md file tracked by git is checked.
#
# Exit codes:
#   0 – all internal references are valid
#   1 – one or more broken internal references were detected

set -euo pipefail

REPO_ROOT="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
cd "$REPO_ROOT"

# ── helpers ──────────────────────────────────────────────────────────────────

RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
RESET='\033[0m'

info()    { echo -e "${GREEN}[INFO]${RESET}  $*"; }
warn()    { echo -e "${YELLOW}[WARN]${RESET}  $*"; }
error()   { echo -e "${RED}[ERROR]${RESET} $*" >&2; }

# ── file list ────────────────────────────────────────────────────────────────

if [[ $# -gt 0 ]]; then
    FILES=("$@")
else
    mapfile -t FILES < <(git ls-files '*.md')
fi

if [[ ${#FILES[@]} -eq 0 ]]; then
    info "No Markdown files found – nothing to check."
    exit 0
fi

# ── validation ───────────────────────────────────────────────────────────────

ERRORS=0
CHECKED=0

for md_file in "${FILES[@]}"; do
    [[ -f "$md_file" ]] || continue
    dir="$(dirname "$md_file")"

    # Extract Markdown link targets from [text](target) and ![alt](target).
    # We match only the target portion immediately after ]( or ](,
    # which excludes plain parenthetical prose like "(see below)".
    # Code fences are stripped first to avoid matching example links.
    # Only relative paths (no scheme like http:// or mailto:) are checked.
    while IFS= read -r raw_target; do
        # Strip trailing anchor fragment
        path_part="${raw_target%%#*}"
        # Strip trailing whitespace
        path_part="${path_part%"${path_part##*[![:space:]]}"}"
        [[ -z "$path_part" ]] && continue

        # Resolve relative to the containing file's directory
        if [[ "$path_part" == /* ]]; then
            resolved="$REPO_ROOT$path_part"
        else
            resolved="$REPO_ROOT/$dir/$path_part"
        fi

        # Normalise (resolve . and .. segments) without requiring path to exist
        resolved="$(realpath -m "$resolved")"

        # Must stay inside the repository
        if [[ "$resolved" != "$REPO_ROOT"* ]]; then
            error "$md_file: path escapes repository root: $raw_target"
            (( ERRORS++ )) || true
            continue
        fi

        if [[ ! -e "$resolved" ]]; then
            error "$md_file: broken internal reference → $raw_target"
            (( ERRORS++ )) || true
        fi

        (( CHECKED++ )) || true
    done < <(
        # Match !?[label](target) – capture only the target between ]( and )
        # Exclude http/https/ftp/mailto schemes (those are external links)
        # Strip fenced code blocks first to avoid matching example links
        sed '/^```/,/^```/d' "$md_file" \
            | grep -oP '!?\[[^\]]*\]\(\K(?!https?://|ftp://|mailto:)[^)]+' \
            2>/dev/null || true
    )
done

# ── summary ──────────────────────────────────────────────────────────────────

echo ""
info "Internal link check complete."
info "Files checked      : ${#FILES[@]}"
info "References checked : $CHECKED"

if [[ $ERRORS -gt 0 ]]; then
    error "Broken internal references : $ERRORS"
    echo ""
    error "Fix the broken references above before merging."
    exit 1
else
    info "All internal references are valid."
    exit 0
fi