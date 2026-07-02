#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="${ACB_REPO_ROOT:-$(cd "$script_dir/../.." && pwd)}"
cd "$repo_root"

if [[ $# -gt 0 ]]; then
  files=("$@")
else
  mapfile -t files < <(find . -type f -name '*.md' \
    ! -path './.git/*' \
    ! -path './agents/state/archive/*' \
    ! -path './agents/state/logs/*' \
    ! -path './agents/state/summaries/*' \
    | sed 's#^\./##')
fi

errors=0
checked=0
for file in "${files[@]}"; do
  [[ -f "$file" ]] || continue
  dir="$(dirname "$file")"
  while IFS= read -r target; do
    target="${target%%#*}"
    [[ -z "$target" ]] && continue
    [[ "$target" =~ ^(https?:|mailto:|tel:) ]] && continue
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
