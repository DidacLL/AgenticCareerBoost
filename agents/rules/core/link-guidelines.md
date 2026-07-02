# Link Guidelines

Rules for including links in documentation, research artifacts, and site content.

## Quick Reference

| Link type | How to write it | CI behaviour |
|-----------|----------------|-------------|
| Internal file in this repo | Relative path `../../agents/state/roadmap.md` | **Blocking** - must resolve |
| Main public site | Use relative site routes in source; resolve the deployed origin at runtime or publication time | Advisory check (non-blocking) |
| AgenticCareerBoost project references | Repo URL or site project route, depending on context | Advisory check for public URLs |
| Official standard / stable docs | Absolute URL | Advisory check (non-blocking) |
| LLM-cited article / blog post | Absolute URL **or** omit | Advisory check (non-blocking) |

---

## 1. Internal References

Always use **relative Markdown paths** to reference files within this repository.

```markdown
<!-- correct - relative path from a root-level file -->
Check the [roadmap](../../state/roadmap.md) for upcoming work.

<!-- wrong - absolute GitHub blob URL may 404 on non-main branches -->
Check the [roadmap](https://github.com/DidacLL/AgenticCareerBoost/blob/main/agents/state/roadmap.md)
```

Why: Relative paths are validated by `agents/tools/validate_links.sh` in CI. Absolute
GitHub blob URLs point to the `main` branch and always 404 on feature branches.

## 2. Public Site URL Policy

Use deployment-derived URLs for the main public site and recruiter-facing
identity surface. Do not commit a literal Pages host or repository subpath as
the public-site origin. Treat `AgenticCareerBoost` as the project/repository
name, not as the canonical public-site path.

Use the repository URL `https://github.com/DidacLL/AgenticCareerBoost` when the
reader needs the source system, issue history, reports, or implementation files.
Use the public site route when the reader needs the curated human-facing page.

## 3. External Citations from LLM Research

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

## 4. Domains with Known CI Issues

The following domains are excluded from Lychee checks in `.github/lychee.toml` because
they fail reliably in CI for reasons outside our control:

| Domain | Reason |
|--------|--------|
| `linkedin.com` | Blocks automated traffic (403/429) |
| `humaneer.me` | TLS handshake failure in CI |
| `tiaeastwood.com` | Connection reset by peer |
| Public site host | Resolve at deployment/publication time; do not hardcode it in canonical files |

To add a new exclusion, append a regex pattern to the `exclude` list in
[`lychee.toml`](../../../.github/lychee.toml).

## 5. CI Workflow Behaviour

The `docs-lint` workflow runs three jobs:

1. **markdownlint** – checks formatting rules (blocking)
2. **internal-linkcheck** - runs `agents/tools/validate_links.sh`, validates that
   every relative file path in `.md` files resolves to a real file (blocking)
3. **external-linkcheck** – runs Lychee on all URLs, reports broken links as
   warnings in the job summary and uploads `lychee/out.md` as an artefact
   (non-blocking – never fails the build)

## 6. Pre-Commit Usage

Run the internal link validator locally before pushing:

```bash
bash agents/tools/validate_links.sh
```

Or to check specific files:

```bash
bash agents/tools/validate_links.sh agents/rules/core/mission.md agents/state/roadmap.md
```
