# AgenticCareerBoost — Site Refactor Progress
## Execution tracker

**Master authority:** `agents/acb_site_refactor_masterplan.md`  
**This tracker does not redefine architecture.** It records execution only.  
**Baseline expected before first write:** `main@aa7d57c809db41bbbf042eebbfdeba4454476295`  
**Execution branch:** `DidacLl/siterefactor`  
**Production cutover:** outside this tracker

> All earlier trackers from this conversation are invalid and must not be used.

---

## 1. Global state

| Field | Value |
|---|---|
| Planning audit | COMPLETE |
| Repository writes authorized | YES — current user instruction authorizes P1–P3 on `DidacLl/siterefactor` only |
| Current remote baseline | `main@aa7d57c809db41bbbf042eebbfdeba4454476295` |
| `DidacLl/siterefactor` exists | YES — initial handoff commit contains only the two control documents |
| Production touched | NO |
| `didacll.github.io` touched | NO |
| PR created for refactor | NO |
| Merge performed | NO |
| Visual approval mechanism | two user local visual gates only; all objective verification remains agent-owned |
| GPT visual approval from GitHub | unavailable; GPT may visually inspect screenshots explicitly uploaded by user at V1/V2 |

---

## 2. Frozen decisions

| ID | Decision | State |
|---|---|---|
| D-01 | ACB remains canonical site source/integration repository | FROZEN |
| D-02 | Astro 7.2.9 static build | FROZEN |
| D-03 | No React/Vue/Svelte/SSR/CMS/MDX/Tailwind | FROZEN |
| D-04 | Markdown narrative + small typed frontmatter | FROZEN |
| D-05 | No JSON block DSL/client renderer/router | FROZEN |
| D-06 | Source is host/deployment agnostic | FROZEN |
| D-07 | One semantic owner for content/routes/config | FROZEN |
| D-08 | Current retro-document visual identity is preserved, not redesigned | FROZEN |
| D-09 | Only theme/gallery require client JS | FROZEN |
| D-10 | Existing binary assets stay byte-for-byte in `site/assets/img/` | FROZEN |
| D-11 | `site/assets/` is Astro `publicDir` | FROZEN |
| D-12 | `/application-tracker/` public surface retired | FROZEN |
| D-13 | `/dashboard/` and status pipeline retired | FROZEN |
| D-14 | Agent owns objective verification; user owns only two subjective visual gates | FROZEN |
| D-15 | `localdeploy.bat` is the only local site launch entrypoint | FROZEN |
| D-16 | One non-deploy branch verification workflow: build + route/link/base checks + plain Playwright 1.62.1 Chromium functional smoke; never aesthetic scoring | FROZEN |
| D-17 | No PR/merge/deploy/root-repo write in this execution | FROZEN |
| D-18 | Production cutover requires separate explicit authorization | FROZEN |

---

## 3. Pre-execution stop gate

At execution handoff, all rows must be PASS.

| Check | Expected | Result |
|---|---|---|
| ACB `main` SHA | `aa7d57c809db41bbbf042eebbfdeba4454476295` | PASS — rechecked at execution start |
| `DidacLl/siterefactor` lineage | direct descendant; handoff delta is only the two control documents | PASS — rechecked at execution start |
| No requested write to `main` | true | PASS — branch-only authority |
| No requested write to root publication repo | true | PASS — explicitly forbidden |

If any row fails: STOP; no branch/write is allowed.

---

## 4. Phase board

| Phase | Purpose | Build gate | Human visual gate | Status |
|---|---|---|---|---|
| P1 | Astro foundation + representative visual shell | autonomous build/route/link/base/browser checks | V1 REQUIRED | AWAITING V1 |
| P2 | Complete route/content migration + old runtime removal | autonomous build/route/link/base/browser checks | NONE | BLOCKED BY P1 |
| P3 | Public artifacts + CI/deploy preparation + repo alignment | autonomous checks + complete diff scope review | V2 REQUIRED | BLOCKED BY P2 |
| CUTOVER | production integration | separate plan | separate explicit approval | OUTSIDE SCOPE |

---

## 5. P1 — Astro foundation + visual shell

### Scope

Allowed:

- `agents/acb_site_refactor_masterplan.md`
- `agents/acb_site_refactor_tracker.md`
- `site/**`
- root `localdeploy.bat`
- new `.github/workflows/site-check.yml`

Forbidden:

- `main`
- `DidacLL/didacll.github.io`
- production deploy workflows except reading them
- Application Tracker implementation
- CV/report build tools
- unrelated agents/history files

### Tasks

| ID | Task | Status | Evidence |
|---|---|---|---|
| P1-01 | Recheck exact baseline SHA and execution-branch lineage | COMPLETE | `main` identical to baseline; handoff delta inspected |
| P1-02 | Use existing `DidacLl/siterefactor` branch from exact baseline | COMPLETE | pre-existing branch descends directly from baseline |
| P1-03 | Keep frozen masterplan + tracker at authoritative `agents/` paths | COMPLETE | existing handoff commit; references normalized |
| P1-04 | Add `site/package.json` with exact Astro 7.2.9 + sitemap 3.7.3 | COMPLETE | `site/package.json` |
| P1-05 | Add `.npmrc`, `astro.config.mjs`, `tsconfig.json` | COMPLETE | Astro config files |
| P1-06 | Configure static/directory/trailing-slash/publicDir/env-driven origin+base | COMPLETE | static/directory/trailing/publicDir/env config |
| P1-07 | Add content schemas and single route/path helper | COMPLETE | collections + `paths.ts` |
| P1-08 | Add global site identity/nav/UI data owner | COMPLETE | `src/data/site.ts` |
| P1-09 | Add Base/Document/Project layouts | COMPLETE | Astro layouts |
| P1-10 | Rebuild current visual tokens/shell without redesign | COMPLETE | token/base/site/print CSS |
| P1-11 | Add theme persistence and gallery behavior only | COMPLETE | theme + gallery scripts |
| P1-12 | Migrate Home | COMPLETE | `pages/home.md` + route |
| P1-13 | Migrate Projects index | COMPLETE | project index route |
| P1-14 | Migrate AgenticCareerBoost project page without tracker/dashboard | COMPLETE | ACB Markdown entry |
| P1-15 | Migrate P3CTeX project page | COMPLETE | P3CTeX Markdown entry |
| P1-16 | Update `localdeploy.bat` to double-click Astro dev launcher | COMPLETE | Astro launcher |
| P1-17 | Add `verify-build.mjs` explicit invariant verifier | COMPLETE | `verify-build.mjs` |
| P1-18 | Add minimal browser functional smoke contract | COMPLETE | `browser-smoke.mjs` |
| P1-19 | Add branch-only `site-check.yml` with concurrency cancellation | COMPLETE | `.github/workflows/site-check.yml` |
| P1-20 | Locate exact-SHA run and read jobs/logs | COMPLETE | run `33426586056`, job `99601533065` |
| P1-21 | Fix all objective failures until exact head SHA is green | COMPLETE | green exact source SHA |
| P1-22 | Compare changed paths against baseline for scope | COMPLETE | baseline compare: only P1-control/site paths |
| P1-23 | Report exact green SHA | COMPLETE | `c7607b9d84ce7476dd2ac9602685f4837f8d0c92` |
| P1-24 | V1: user opens `localdeploy.bat` and approves visual direction or reports visual defects | HUMAN VISUAL GATE | user response |

P1 cannot close without the human gate.

---

## 6. P2 — Complete public migration

### Scope

Allowed:

- `site/**`
- tracker status row updates in this file

No CI/deploy/tooling changes outside `site/` in this phase.

### Tasks

| ID | Task | Status | Evidence |
|---|---|---|---|
| P2-01 | Migrate AAAAT project | BLOCKED | Markdown |
| P2-02 | Remove AAAAT link to public tracker | BLOCKED | Markdown |
| P2-03 | Migrate IronBank project | BLOCKED | Markdown |
| P2-04 | Migrate `agents-need-receipts` historical post | BLOCKED | Markdown |
| P2-05 | Migrate `static-sites-as-workbenches` historical post without rewriting history | BLOCKED | Markdown |
| P2-06 | Migrate `sprint-review-agenticcareerboost` historical post | BLOCKED | Markdown |
| P2-07 | Migrate CV `ml` | BLOCKED | Markdown |
| P2-08 | Migrate CV `agentic` | BLOCKED | Markdown |
| P2-09 | Migrate CV `backend` | BLOCKED | Markdown |
| P2-10 | Migrate CV `print` | BLOCKED | Markdown |
| P2-11 | Derive selected CV work from project collection | BLOCKED | source |
| P2-12 | Migrate focus index | BLOCKED | page |
| P2-13 | Migrate focus `ml` | BLOCKED | Markdown |
| P2-14 | Migrate focus `agentic` | BLOCKED | Markdown |
| P2-15 | Migrate focus `backend` | BLOCKED | Markdown |
| P2-16 | Migrate Contact | BLOCKED | Markdown/page |
| P2-17 | Add static 404 page | BLOCKED | page |
| P2-18 | Add frozen alias/retirement redirects | BLOCKED | config/build output |
| P2-19 | Remove public `/dashboard/` implementation | BLOCKED | route absent/redirect |
| P2-20 | Remove public `/application-tracker/` implementation | BLOCKED | route absent/redirect |
| P2-21 | Remove tracker fragment/reference from ACB page | BLOCKED | source |
| P2-22 | Remove old `site/content/**` JSON/block content | BLOCKED | deletion |
| P2-23 | Remove old browser runtime JS modules | BLOCKED | deletion |
| P2-24 | Remove old monolithic stylesheet after replacement owns all selectors | BLOCKED | deletion |
| P2-25 | Run exact-SHA autonomous verification on complete migration | BLOCKED | Actions run |
| P2-26 | Fix objective failures until green | BLOCKED | Actions logs |
| P2-27 | Compare changed paths against baseline for scope | BLOCKED | compare |
| P2-28 | Continue directly to P3; no user gate | BLOCKED | green SHA |

---

## 7. P3 — Artifacts, CI and repository alignment

### Scope

Allowed:

- `site/**`
- `agents/cv/artifacts.json`
- `agents/cv/tools/artifact_manifest.py`
- `agents/reports/tex/tools/publish-public-reports.py`
- root `.gitignore`
- `.github/workflows/site-build.yml`
- `.github/workflows/required-ci.yml`
- delete `.github/workflows/export-status.yml`
- delete `agents/tools/export_status.py`
- delete `agents/tools/validate_static_site.py`
- root/site README/AGENTS factual alignment
- legacy root web entry files listed by masterplan
- this tracker

Still forbidden:

- `DidacLL/didacll.github.io`
- PR/merge
- `main`
- Pages deployment
- Application Tracker implementation
- broad historical cleanup

### Tasks

| ID | Task | Status | Evidence |
|---|---|---|---|
| P3-01 | Change CV public build target to `site/assets/files/cv/` | BLOCKED | manifest/tool |
| P3-02 | Add `reports.json` publication catalog for the 11 current public PDFs | BLOCKED | data file |
| P3-03 | Make report publisher consume catalog and target `site/assets/files/reports/` | BLOCKED | publisher |
| P3-04 | Make ACB project evidence library consume same report catalog | BLOCKED | source |
| P3-05 | Update ignored generated-output paths | BLOCKED | `.gitignore` |
| P3-06 | Update ACB main-only `site-build.yml` to build/upload `site/dist` | BLOCKED | workflow diff |
| P3-07 | Keep project mirror `SITE_INDEXABLE=false` | BLOCKED | workflow/config |
| P3-08 | Update `required-ci.yml` to Astro build; remove status/tracker/old validator | BLOCKED | workflow diff |
| P3-09 | Delete `export-status.yml` | BLOCKED | deletion |
| P3-10 | Delete obsolete `export_status.py` | BLOCKED | deletion |
| P3-11 | Delete obsolete `validate_static_site.py` | BLOCKED | deletion |
| P3-12 | Update `site/README.md` to factual Astro architecture | BLOCKED | doc |
| P3-13 | Update root README only for public-surface facts made stale by refactor | BLOCKED | doc |
| P3-14 | Update root AGENTS minimally for approved site architecture boundary | BLOCKED | doc |
| P3-15 | Remove unused legacy root/site web files named in masterplan | BLOCKED | deletion list |
| P3-16 | Confirm Application Tracker implementation files are untouched | BLOCKED | compare |
| P3-17 | Confirm historical logs/report/CV sources are untouched except allowed artifact path tool changes | BLOCKED | compare |
| P3-18 | Run final exact-SHA autonomous verification | BLOCKED | Actions run |
| P3-19 | Fix all objective failures until green | BLOCKED | Actions logs |
| P3-20 | Compare final branch vs frozen baseline and inspect every changed path for scope | BLOCKED | compare |
| P3-21 | Record final green branch head SHA | BLOCKED | SHA |
| P3-22 | V2: user performs final visual/feel review locally and accepts/rejects | HUMAN VISUAL GATE | user response |

---

## 8. Frozen route ledger

### Preserve

- `/`
- `/projects/`
- `/projects/agentic-career-boost/`
- `/projects/p3ctex/`
- `/projects/aaaat/`
- `/projects/ironbank/`
- `/blog/`
- `/blog/agents-need-receipts/`
- `/blog/static-sites-as-workbenches/`
- `/blog/sprint-review-agenticcareerboost/`
- `/cv/ml/`
- `/cv/agentic/`
- `/cv/backend/`
- `/cv/print/`
- `/focus/`
- `/focus/ml/`
- `/focus/agentic/`
- `/focus/backend/`
- `/contact/`

### Retire -> redirect

- `/dashboard/` -> `/projects/agentic-career-boost/`
- `/application-tracker/` -> `/projects/agentic-career-boost/`

### Legacy alias -> redirect

- `/curriculum/` -> `/cv/ml/`
- `/notes/` -> `/blog/`
- `/hire/` -> `/focus/`
- `/hire/ml/` -> `/focus/ml/`
- `/hire/agentic/` -> `/focus/agentic/`
- `/hire/backend/` -> `/focus/backend/`

No new route may be added during this refactor without explicit user scope expansion.

---

## 9. Visual gates

| Gate | Branch SHA | User result | Required action |
|---|---|---|---|
| V1 after P1 visual foundation | `c7607b9d84ce7476dd2ac9602685f4837f8d0c92` | pending | continue or targeted visual patch |
| V2 final production candidate | pending | pending | stop; cutover remains separate |

There is no P2 user gate. Objective build/function verification is agent-owned and recorded below.

---

## 10. Autonomous verification ledger

| Phase | Exact branch SHA | Run ID | Build/root+subpath | Route/link/base verifier | Browser functional smoke | Scope review |
|---|---|---|---|---|---|---|
| P1 | `c7607b9d84ce7476dd2ac9602685f4837f8d0c92` | `33426586056` | PASS | PASS | PASS | PASS |
| P2 | pending | pending | pending | pending | pending | pending |
| P3 | pending | pending | pending | pending | pending | pending |

The browser field records factual interaction/loading checks only. It never records aesthetic approval.

---

## 11. Scope-diff ledger

Complete at P3 after `compare main...DidacLl/siterefactor`.

| Category | Expected | Observed | Verdict |
|---|---|---|---|
| Astro site source/content | yes | pending | pending |
| Existing binary `site/assets/img/**` | unchanged bytes/paths | pending | pending |
| Application Tracker implementation | no changes | pending | pending |
| Private/untracked application data | inaccessible/untouched | pending | pending |
| CV publication manifest/tool | target-path changes only | pending | pending |
| Report publisher | publication-catalog/target changes only | pending | pending |
| Historical logs/rules/tests | no edits | pending | pending |
| ACB site workflows | scoped changes only | pending | pending |
| Root publication repo | no changes | pending | pending |
| `main` | no writes | pending | pending |

Any unexpected changed path is a STOP until explained or reverted within the refactor branch.

---

## 12. Deferred items — explicitly not sprint work

These are not blockers and must not expand execution:

- production cutover and root publication workflow mutation;
- binary image optimization/transcoding;
- cross-repository project metadata federation;
- Application Tracker cleanup/deletion/productization;
- AAAAT/VCVGenerator development;
- historical agent harness cleanup;
- analytics;
- new blog posts;
- redesign beyond parity/necessary responsive cleanup;
- automated aesthetic scoring.

---

## 13. Completion record

This section is filled only after P3 human approval.

```text
Final branch: DidacLl/siterefactor
Final SHA: PENDING
P1 visual gate: PENDING
P2 visual gate: PENDING
Final visual gate: PENDING
Final branch build: PENDING
Production changed: NO
PR created: NO
Merged: NO
Root publication repo changed: NO
Cutover authorized: NO
```

At that point the execution stops. The branch remains the complete development story and production candidate until the user explicitly authorizes a separate cutover.


## 14. Execution evidence addendum

- User explicitly instructed continuation through P2/P3 without pausing for V1/V2.
- P2 completed and passed site-check run `33429107445` at `2977e5102593103896cc8fb1c93d37f335e7826c`.
- P3 source verification passed site-check run `33430327781` at `765d4bbb81196ea9dcf8362f457f777a3b5cd912`: root/subpath builds, route/base verifier, and browser smoke all passed.
- No PR, merge, deployment, main write, root-publication write, or Application Tracker implementation change was made.
