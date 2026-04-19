# Link Guidelines

Rules for including links in documentation, research artifacts, and site content.

## Quick Reference

| Link type | How to write it | CI behaviour |
|-----------|----------------|-------------|
| Internal file in this repo | Relative path `../../state/roadmap.md` | **Blocking** – must resolve |
| GitHub Pages (this project) | Absolute URL `https://didacll.github.io/…` | Excluded until site is live |
| Official standard / stable docs | Absolute URL | Advisory check (non-blocking) |
| LLM-cited article / blog post | Absolute URL **or** omit | Advisory check (non-blocking) |

---

## 1. Internal References

Always use **relative Markdown paths** to reference files within this repository.

```markdown
<!-- ✅ correct – relative path from site/starter/projects/index.md to repo root -->
Check the [roadmap](../../../state/roadmap.md) for upcoming work.

<!-- ❌ wrong – absolute GitHub blob URL may 404 on non-main branches -->
Check the [roadmap](https://github.com/DidacLL/AgenticCareerBoost/blob/main/state/roadmap.md)
```

Why: Relative paths are validated by `scripts/validate-links.sh` in CI. Absolute
GitHub blob URLs point to the `main` branch and always 404 on feature branches.

## 2. External Citations from LLM Research

LLM-generated research may cite articles that are unreachable (TLS errors,
paywalls, connection resets, or hallucinated URLs). These links are checked
**non-blocking** by Lychee but follow these guidelines:

- **Verify existence** before committing: open the URL in a browser and confirm
  the page loads with the expected content.
- If a source cannot be verified, **omit the URL** and keep only the title and
  author as a textual reference.
- Never cite a URL solely because an LLM produced it.

```markdown
<!-- ✅ verified external citation -->
| S5 | "AI LinkedIn Posts That Don't Sound Fake" | Humaneer | <https://humaneer.me/…> | … |

<!-- ✅ unverifiable source – omit URL, keep reference -->
| S5 | "AI LinkedIn Posts That Don't Sound Fake" | Humaneer | *(source unavailable)* | … |
```

## 3. Domains with Known CI Issues

The following domains are excluded from Lychee checks in `lychee.toml` because
they fail reliably in CI for reasons outside our control:

| Domain | Reason |
|--------|--------|
| `linkedin.com` | Blocks automated traffic (403/429) |
| `humaneer.me` | TLS handshake failure in CI |
| `tiaeastwood.com` | Connection reset by peer |
| `didacll.github.io/AgenticCareerBoost` | Site not yet deployed |

To add a new exclusion, append a regex pattern to the `exclude` list in
[`lychee.toml`](../lychee.toml).

## 4. CI Workflow Behaviour

The `docs-lint` workflow runs three jobs:

1. **markdownlint** – checks formatting rules (blocking)
2. **internal-linkcheck** – runs `scripts/validate-links.sh`, validates that
   every relative file path in `.md` files resolves to a real file (blocking)
3. **external-linkcheck** – runs Lychee on all URLs, reports broken links as
   warnings in the job summary and uploads `lychee/out.md` as an artefact
   (non-blocking – never fails the build)

## 5. Pre-Commit Usage

Run the internal link validator locally before pushing:

```bash
bash scripts/validate-links.sh
```

Or to check specific files:

```bash
bash scripts/validate-links.sh docs/core/mission.md state/roadmap.md
```
