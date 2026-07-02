# CI rules

Stable rules for CI and advisory docs checks. Agents **must not** change these
configs without a matching update to this file.

## Markdown checks

Blocking Markdown validation is the repo-local internal link validator:
`agents/tools/validate_links.sh`, run from `required-ci`.

External HTTP link checking is advisory only and runs from
`.github/workflows/docs-lint.yml` with Lychee. It reports problems without
failing the build.

## Lychee link checker (`lychee`, config: `.github/lychee.toml`)

Lychee is provided by `lycheeverse/lychee-action@v2`. Always verify field names
against the action's bundled Lychee version before editing `.github/lychee.toml`.

| Field | Value | Reason |
|-------|-------|--------|
| `include_mail` | `false` | Do **not** use the removed `exclude_mail` field; the correct inverse is `include_mail = false` |
| `accept` | 200, 204, 301, 302, 403, 429 | 403/429 are common rate-limit responses from LinkedIn and similar |
| `exclude_path` | `agents/rules/templates/` | Templates contain placeholder URLs that are not real links |
| `exclude` | `https://www.linkedin.com/.*` | LinkedIn aggressively rate-limits CI crawlers |

### Common config mistakes to avoid

- `exclude_mail` — **does not exist** in lychee ≥ v0.16. Use `include_mail = false`.
- Removing `exclude_path` for `agents/rules/templates/` will cause false-positive link failures.
- Removing `403`/`429` from `accept` will cause spurious failures on LinkedIn links.
