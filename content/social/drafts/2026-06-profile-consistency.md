# Public Profile Consistency Package

- **Sprint**: S-002R Task 2
- **Date**: 2026-06-11
- **Status**: draft for human/account-owner action
- **Scope**: GitHub profile README draft, GitHub account metadata checklist,
  deprecated-link cleanup, and LinkedIn manual verification
- **Do not publish from this file**: account changes remain human-owned.

## Evidence Used

- Mission: rebuild public technical profile through visible, inspectable work.
- Marketing: repository is canonical; site is curated mirror; LinkedIn is
  selective distribution.
- Brand: technical, disciplined, direct; evidence over adjectives; no AI hype.
- Current public status: S-002R restart implementation is pending profile
  cleanup, site rebuild foundation, and LinkedIn reactivation drafts.
- Reactivation review: GitHub API showed empty `bio`, `blog`, and `hireable`;
  LinkedIn profile copy could not be externally verified due to authwall.
- Link registry: current canonical surfaces are GitHub profile, LinkedIn,
  this repository, and `https://didacll.github.io/AgenticCareerBoost/`.

## Current Gaps

- GitHub account metadata is incomplete: `bio`, `blog`, and `hireable` need
  account-owner review.
- GitHub profile README needs a current replacement that points to the
  AgenticCareerBoost proof loop and avoids legacy links.
- Deprecated surfaces still exist in `data/links.json` for tracking:
  `legacy_site_deprecated` and `legacy_repo_deprecated`.
- LinkedIn content cannot be externally verified because the public page is
  behind an authwall.
- Public campaign should not restart until GitHub, site, LinkedIn, and source
  links tell the same story.

## Decisions

### D1. GitHub Profile README Positioning

| Option | Fit | Evidence | Recruiter scan | Risk | Score |
|---|---:|---:|---:|---:|---:|
| A. ML/AI student first, agentic systems second | 8 | 8 | 8 | 8 | 32 |
| B. Agentic systems first, ML/AI as education track | 9 | 9 | 8 | 8 | 34 |
| C. Operations-to-engineering transition first | 7 | 7 | 7 | 6 | 27 |

Selected: **B**. It best matches the current repository proof while still
keeping the UOC ML/AI track visible.

### D2. Link Policy

| Option | Fit | Evidence | Cleanup value | Risk | Score |
|---|---:|---:|---:|---:|---:|
| A. Link only canonical current surfaces | 9 | 9 | 9 | 9 | 36 |
| B. Keep legacy site/repo links as history | 5 | 6 | 3 | 5 | 19 |
| C. Remove all outbound links except GitHub | 4 | 5 | 4 | 8 | 21 |

Selected: **A**. Legacy links may stay in `data/links.json` as deprecated
tracking entries, but public profile copy should not send readers there.

### D3. Account Metadata Tone

| Option | Fit | Evidence | Public safety | Risk | Score |
|---|---:|---:|---:|---:|---:|
| A. Compact proof-oriented metadata | 9 | 9 | 9 | 9 | 36 |
| B. Promotional job-seeker metadata | 6 | 6 | 6 | 5 | 23 |
| C. Minimal metadata with no positioning | 5 | 5 | 8 | 8 | 26 |

Selected: **A**. Keep profile fields factual, short, and tied to public proof.

## Proposed GitHub Profile README Replacement

Copy only the Markdown block below into `DidacLL/DidacLL/README.md` after human
review.

```markdown
# Dídac Llorens

Software engineering student at UOC, focused on ML/AI and model-agnostic
agentic systems. Building public, inspectable engineering artifacts from
Barcelona.

## Current Focus

- Path-based agentic workflows with explicit truth hierarchies, bounded roles,
  logs, tests, and human review.
- ML/AI engineering through UOC specialization work and public portfolio
  artifacts.
- LaTeX and documentation tooling for formal, reproducible technical outputs.

## Public Proof

| Surface | What to inspect |
|---|---|
| [AgenticCareerBoost](https://github.com/DidacLL/AgenticCareerBoost) | Git-based multiagent operating system, sprint records, formal reports, public site source |
| [Public site](https://didacll.github.io/AgenticCareerBoost/) | Recruiter-facing mirror of the current technical profile |
| [S-001 profile audit](https://github.com/DidacLL/AgenticCareerBoost/blob/main/content/reports/build/s001-profile-audit-positioning.pdf) | Positioning audit and evidence-backed profile rebuild |
| [Agentic System Guide](https://github.com/DidacLL/AgenticCareerBoost/blob/main/content/reports/build/agentic-system-guide.pdf) | Human-facing manual for the path-based agentic system |

## Background

Before engineering, I spent 15 years in banking and insurance operations:
regulated workflows, complex cases, stakeholder coordination, team leadership,
and failure-mode thinking. I now apply that discipline to software engineering,
ML/AI learning, and agentic workflow design.

## Contact

- LinkedIn: [linkedin.com/in/didacllorens](https://www.linkedin.com/in/didacllorens/)
- Site: [didacll.github.io/AgenticCareerBoost](https://didacll.github.io/AgenticCareerBoost/)
- Location: Barcelona, Catalonia
```

## GitHub Account Metadata Checklist

- **Bio**: `Software engineering student focused on ML/AI and model-agnostic
  agentic systems. Building public, inspectable engineering artifacts.`
- **Blog / Website**: `https://didacll.github.io/AgenticCareerBoost/`
- **Location**: `Barcelona, Catalonia`
- **Hireable**: set to true only if the account owner wants public recruiter
  contact through GitHub now.
- **Pinned repositories**: prioritize `AgenticCareerBoost`; add P3CTeX or other
  repos only if their current README/build state is public-safe.
- **Profile README repo topics/description**: keep neutral; do not use
  `config`, `github-config`, or legacy-site language.

## Deprecated-Link Cleanup

- Do not use `https://didacll.github.io/Didac-dev-project/` in profile README,
  LinkedIn Featured, first-comment source bundles, or site navigation.
- Do not use `https://github.com/DidacLL/Didac-dev-project` as a current proof
  link.
- Keep deprecated entries in `data/links.json` only as explicit cleanup
  tracking until a later task removes or archives them.
- Canonical current proof links:
  `https://github.com/DidacLL/AgenticCareerBoost`,
  `https://didacll.github.io/AgenticCareerBoost/`,
  `https://github.com/DidacLL`, and
  `https://www.linkedin.com/in/didacllorens/`.

## LinkedIn Manual Verification Checklist

- Confirm headline names software engineering, ML/AI, and agentic systems
  without hype or apology framing.
- Confirm About section points to inspectable public work, not generic
  self-description.
- Confirm Featured section links to the AgenticCareerBoost site, the repository,
  and current PDFs only.
- Remove or demote legacy site/repo links if present.
- Confirm location and education are consistent with Barcelona and UOC.
- Confirm first reactivation post links only to current public artifacts or
  primary/high-credibility sources.
- Do not launch the main profile-audit campaign until either the three-post
  low-heat reactivation sequence is complete or an explicit waiver is recorded.

## Publication Gate

Ready for human review after local Markdown/JSON checks. Not ready for account
publication until the GitHub metadata fields and LinkedIn profile are manually
verified by the account owner.
