#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="${ACB_REPO_ROOT:-$(cd "$script_dir/../.." && pwd)}"
cd "$repo_root"

if [[ $# -gt 0 ]]; then
  files=("$@")
else
  mapfile -t files < <(git ls-files -- '*.md' \
    | grep -vE '^agents/state/(archive|logs|summaries)/' \
    || true)
fi

declare -A site_routes=()

normalize_route() {
  local route="$1"
  route="/${route#/}"
  route="$(realpath -m "$route")"
  if [[ "$route" != "/" ]]; then route="${route%/}"; fi
  printf '%s\n' "$route"
}

while IFS= read -r route; do
  [[ -n "$route" ]] && site_routes["$(normalize_route "$route")"]=1
done < <(node site/scripts/content-routes.mjs)

site_base_for_file() {
  local file="$1"
  local rel collection rest locale="" prefix="" id
  [[ "$file" == site/src/content/* ]] || return 1
  rel="${file#site/src/content/}"
  collection="${rel%%/*}"
  rest="${rel#*/}"
  if [[ "$rest" == es/* || "$rest" == ca/* ]]; then
    locale="${rest%%/*}"
    rest="${rest#*/}"
    prefix="/$locale"
  fi
  id="$(basename "$rest" .md)"
  case "$collection" in
    pages)
      case "$id" in
        home) printf '%s/\n' "$prefix" ;;
        projects) printf '%s/projects/\n' "$prefix" ;;
        blog) printf '%s/blog/\n' "$prefix" ;;
        contact) printf '%s/contact/\n' "$prefix" ;;
        *) return 1 ;;
      esac
      ;;
    projects) printf '%s/projects/%s/\n' "$prefix" "$id" ;;
    posts) printf '%s/blog/%s/\n' "$prefix" "$id" ;;
    cv) printf '%s/cv/%s/\n' "$prefix" "$id" ;;
    *) return 1 ;;
  esac
}

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
