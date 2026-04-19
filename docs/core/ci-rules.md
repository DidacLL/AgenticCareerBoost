# CI rules

Stable rules for the two docs-lint jobs. Agents **must not** change these
configs without a matching update to this file.

## Markdownlint (`markdownlint-cli2`, config: `.markdownlint.jsonc`)

| Rule | Setting | Reason |
|------|---------|--------|
| MD013 (line length) | disabled | Templates and generated content exceed 80 chars |
| MD024 (duplicate headings) | siblings_only | Duplicate headings across sections are intentional |
| MD025 (single title) | front_matter_title: "" | Jekyll front-matter titles must not trigger H1 conflicts |
| MD026 (trailing punctuation) | disabled | Headings ending in `?` are allowed |
| MD033 (inline HTML) | disabled | HTML comments and templates are present throughout |

## Lychee link checker (`lychee`, config: `lychee.toml`)

Lychee version pinned in workflow: **v0.23.0**. Always verify field names
against that version before editing `lychee.toml`.

| Field | Value | Reason |
|-------|-------|--------|
| `include_mail` | `false` | Do **not** use the removed `exclude_mail` field; the correct inverse is `include_mail = false` |
| `accept` | 200, 204, 301, 302, 403, 429 | 403/429 are common rate-limit responses from LinkedIn and similar |
| `exclude_path` | `docs/templates/` | Templates contain placeholder URLs that are not real links |
| `exclude` | `https://www.linkedin.com/.*` | LinkedIn aggressively rate-limits CI crawlers |

### Common config mistakes to avoid

- `exclude_mail` — **does not exist** in lychee ≥ v0.16. Use `include_mail = false`.
- Removing `exclude_path` for `docs/templates/` will cause false-positive link failures.
- Removing `403`/`429` from `accept` will cause spurious failures on LinkedIn links.
