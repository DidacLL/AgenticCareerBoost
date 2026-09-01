#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="${ACB_REPO_ROOT:-$(cd "$script_dir/../.." && pwd)}"
cd "$repo_root"

if [[ $# -gt 0 ]]; then
  files=("$@")
else
  # Validate repository-owned Markdown only. Build outputs and installed
  # dependencies can contain their own incomplete documentation trees and are
  # deliberately outside this repository's link contract.
  mapfile -t files < <(git ls-files -- '*.md' \
    | grep -vE '^agents/state/(archive|logs|summaries)/' \
    || true)
fi

declare -A site_routes=()

normalize_route() {
  local route="$1"
  route="/${route#/}"
  route="$(realpath -m "$route")"
  if [[ "$route" != "/" ]]; then
    route="${route%/}"
  fi
  printf '%s\n' "$route"
}

add_site_route() {
  site_routes["$(normalize_route "$1")"]=1
}

site_base_for_file() {
  local file="$1"
  local id
  case "$file" in
    site/src/content/pages/home.md) printf '/\n' ;;
    site/src/content/pages/projects.md) printf '/projects/\n' ;;
    site/src/content/pages/blog.md) printf '/blog/\n' ;;
    site/src/content/pages/contact.md) printf '/contact/\n' ;;
    site/src/content/pages/404.md) printf '/404/\n' ;;
    site/src/content/projects/*.md)
      id="$(basename "$file" .md)"
      printf '/projects/%s/\n' "$id"
      ;;
    site/src/content/posts/*.md)
      id="$(basename "$file" .md)"
      printf '/blog/%s/\n' "$id"
      ;;
    site/src/content/cv/*.md)
      id="$(basename "$file" .md)"
      printf '/cv/%s/\n' "$id"
      ;;
    *) return 1 ;;
  esac
}

add_site_route "/"
[[ -f site/src/content/pages/projects.md ]] && add_site_route "/projects/"
[[ -f site/src/content/pages/blog.md ]] && add_site_route "/blog/"
[[ -f site/src/content/pages/contact.md ]] && add_site_route "/contact/"

shopt -s nullglob
for source in site/src/content/projects/*.md; do
  add_site_route "/projects/$(basename "$source" .md)/"
done
for source in site/src/content/posts/*.md; do
  add_site_route "/blog/$(basename "$source" .md)/"
done
for source in site/src/content/cv/*.md; do
  add_site_route "/cv/$(basename "$source" .md)/"
done
shopt -u nullglob

errors=0
checked=0
for file in "${files[@]}"; do
  [[ -f "$file" ]] || continue
  dir="$(dirname "$file")"
  while IFS= read -r target; do
    target="${target%%#*}"
    target="${target%%\?*}"
    [[ -z "$target" ]] && continue
    [[ "$target" =~ ^(https?:|mailto:|tel:) ]] && continue

    if site_base="$(site_base_for_file "$file" 2>/dev/null)"; then
      if [[ "$target" == /* ]]; then
        site_target="$(normalize_route "$target")"
      else
        site_target="$(normalize_route "${site_base}${target}")"
      fi

      if [[ -n "${site_routes[$site_target]:-}" ]]; then
        checked=$((checked + 1))
        continue
      fi

      public_asset="$repo_root/site/assets/${site_target#/}"
      if [[ -e "$public_asset" ]]; then
        checked=$((checked + 1))
        continue
      fi
    fi

    if [[ "$target" == /* ]]; then
      resolved="$repo_root${target}"
    else
      resolved="$repo_root/$dir/$target"
    fi
    resolved="$(realpath -m "$resolved")"
    if [[ "$resolved" != "$repo_root"* ]]; then
      echo "$file: path escapes repository root: $target" >&2
      errors=$((errors + 1))
      continue
    fi
    if [[ ! -e "$resolved" ]]; then
      echo "$file: broken internal reference: $target" >&2
      errors=$((errors + 1))
    fi
    checked=$((checked + 1))
  done < <(sed '/^```/,/^```/d' "$file" | grep -oP '!?\[[^\]]*\]\(\K(?!https?://|mailto:|tel:)[^)]+' 2>/dev/null || true)
done

echo "Internal Markdown links checked: $checked"
if [[ "$errors" -gt 0 ]]; then
  echo "Broken internal references: $errors" >&2
  exit 1
fi
