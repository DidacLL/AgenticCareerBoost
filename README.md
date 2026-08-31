# AgenticCareerBoost

AgenticCareerBoost is my personal career workspace and public proof record. It
holds the practical systems, LaTeX work, public site assets, and scratch tooling
I use while improving my job-search workflow.

This repository is not a generic software product. Some tools inside it are
prototypes or temporary local workflow, and some material is intentional public
career evidence.

## What Is Here

- `application-tracker/` - scratch tracker and cover-letter renderer, kept as
  evidence of the local workflow that later informed AAAAT.
- `application-tracker/letter.ps1` - simple local cover-letter generation flow.
- `agents/cv/` - public/general CV LaTeX workflow and related build material.
- `site/` - personal public site and portfolio proof.
- `agents/reports/` - historical public proof/report material where still useful.
- `agents/work/social/` - preserved campaign planning, research, and social
  scratch material.
- `agents/state/` - historical logs, decisions, research, and previous run
  records.
- `agents/rules/` and `agents/tests/` - legacy harness material kept as
  evidence, not as the current control system.

## Private Boundary

This repo is currently also my live local workspace, so private application data
may exist locally. That data must remain local.

Do not stage or share:

- `application-tracker/.private/`
- tailored cover-letter JSON;
- raw job offers or recruiter messages;
- SQLite/databases;
- generated private letters or CV variants;
- private notes.

Public/general CV and personal site assets may remain when they are intentional
public proof. They should not be reused as fixtures for future tooling.

## Current Useful Workflow

The valuable working path is the simple cover-letter renderer:

```powershell
cd application-tracker
.\letter.ps1 example-slug
```

It reads local JSON from `.private/example-slug.json`, renders a TeX cover
letter with `render_letter.py`, and writes generated files under
`.private/generated/`.

The canonical/general CV source remains under `agents/cv/`. Tailored variants
should stay private or ignored.

The historical `agents/` material is intentionally preserved because this is a
proof repo. It shows the research, campaign work, earlier system design, and
failure/correction history. It should not be read as mandatory process for new
work.

## Project Boundary

Application Tracker is preserved here as prototype evidence and as a local
renderer workflow. Product development for the next job-search tools happens
outside this repository.

The goal here is a clean, understandable career workspace that shows practical
engineering judgment: useful local automation, careful data boundaries, strong
LaTeX/document work, and honest public evidence.
