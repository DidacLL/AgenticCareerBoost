# Sprint output

## Meta

- **Sprint ID**: S-001.5
- **Goal**: Make the public profile event-ready for the VI Fira Virtual d'Ocupacio de la UOC by applying the S-001 positioning to GitHub, site, LinkedIn/JobTeaser copy, event outreach, and target-company triage.
- **Status**: reviewed / deploy pending

## Tasks

| # | Task | Target | Specialty | Scope | Writes | Acceptance | Memory | Evidence link |
|---|------|--------|-----------|-------|--------|------------|--------|---------------|
| 1 | Preserve S-001 baseline | Orchestrator | State recovery | Confirm S-001 local outputs and fix public-copy evidence issues | S-001 drafts, state notes | S-001 artifacts remain usable and no public copy repeats the 5-workflow error | none | content/social/drafts/2026-04-s001-audit-reveal-options.md |
| 2 | Event target shortlist | Developer/research | Hiring-event triage | Rank JobTeaser companies against ML/data, research, platform, fintech/regtech, and consulting-risk criteria | state/research/s0015-uoc-fair-targets.md | 10+ targets with message angle and risk notes | none | state/research/s0015-uoc-fair-targets.md |
| 3 | GitHub cleanup package | Developer + CommunityManager | Public profile | Prepare exact profile README, bio/settings, repo metadata, pin order, and archive list | content/social/drafts/2026-04-s0015-github-cleanup.md | No legacy/VladScv links; AgenticCareerBoost and P3CTeX lead | none | content/social/drafts/2026-04-s0015-github-cleanup.md |
| 4 | Recruiter landing fast rebuild | Developer | Jekyll/static site | Build fair-ready landing page with JSON-LD, OG tags, projects, curriculum, PDF CV link, contact, and current links | site/starter/**, content/site/** | 90-second recruiter scan works; no active legacy-site link; curriculum and CV path exist | none | site/starter/index.md |
| 5 | LinkedIn + JobTeaser profile kit | CommunityManager | Profile copy | Final paste-ready headline, About, Featured, Experience, JobTeaser summary, and event pitch | content/social/drafts/2026-04-s0015-linkedin-jobteaser-kit.md | Under platform-friendly length; no unsupported credentials | none | content/social/drafts/2026-04-s0015-linkedin-jobteaser-kit.md |
| 6 | Event outreach kit | CommunityManager | Recruiter messaging | Draft multilingual intros, interview request, follow-up, and company-specific angles | content/social/drafts/2026-04-s0015-uoc-fair-outreach.md | Drafts ready; sending remains user-controlled | none | content/social/drafts/2026-04-s0015-uoc-fair-outreach.md |
| 7 | Execution checklist | Orchestrator | GitHub/account operations | Separate local work from external account actions requiring confirmation | state/summaries/s0015-execution-checklist.md | Human can apply changes without guessing | none | state/summaries/s0015-execution-checklist.md |
| 8 | PairCheck | PairCheck | Evidence + public safety | Review site, CV, state sync, and public-copy kits | state/logs/S-001-5/pc-*.md | No fabricated metrics, stale links, missing curriculum, or unsupported claims | none | state/logs/S-001-5/ |
| 9 | Sprint closure | Orchestrator | State update | Update state/current, roadmap, backlog, public status | state files, data/public-status.json | S-001.5 reviewed; deploy remains pending until commit/push and GitHub Pages check | none | state/current.md |

## Pair-check assignments

| Task # | PairCheck-A | PairCheck-B | Verdict |
|--------|-------------|-------------|---------|
| 3, 5, 6 | pc-public-copy.md (public copy + evidence) | n/a | PASS |
| 4 | pc-site.md (landing page + links) | n/a | PASS |

## Closure artifacts

- [x] Repository artifact(s) — S-001.5 research, profile kits, outreach kit, execution checklist, site pages, CV source/PDF
- [ ] Website / repo update trace — recruiter landing page rebuilt in `site/starter/` and `content/site/`; GitHub Pages deploy pending push
- [x] Social / LinkedIn-ready artifact — LinkedIn/JobTeaser kit and fair outreach messages
- [x] Formal engineering documentation — S-001 report source plus S-001.5 formal CV PDF
- [x] Condensed technical backlog — see below
- [x] Condensed narrative backlog — see below

## Backlog deltas

### Technical

- T-009 NEW: Apply GitHub profile/repo metadata cleanup from S-001.5 checklist through user-controlled account actions
- T-010 NEW: Complete full S-002 site rebuild with deeper project pages, CV hardening, and stable asset pipeline
- T-008 UPDATE: S-001 LaTeX report PDF promoted locally into `content/reports/build/`; CI promotion still needs verification after push

### Narrative

- N-007 RESOLVED: Public posture chosen for event — ML/Data primary, Agentic Systems differentiator
- N-012 NEW: Apply LinkedIn and JobTeaser profile copy manually before/during UOC fair
- N-013 NEW: Track UOC fair company contacts, interview requests, and follow-ups
- N-014 NEW: Verify PUE full name, Escola Massana details, specific UOC coursework, professional email, and MemPalace contribution scope

## CI trace

- Commit(s): _(pending user commit)_
- Workflow run: local checks run before commit; GitHub Actions pending push
