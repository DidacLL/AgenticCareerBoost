# Published reports

This directory is the public report mount point inside the generated `site/` artifact.

PDF files in this directory are generated build outputs. They must not be committed to the repository, because committed PDFs can drift from the canonical LaTeX sources and can accidentally preserve temporary validation outputs.

- Source files live in `agents/reports/tex/`.
- Local builds write to `agents/reports/tex/build/`.
- CI builds the public report PDFs from the LaTeX sources and copies them here before validating and uploading the site artifact.
- Static site validation fails if any PDF under `site/files/` is tracked by git.
- `site/content/projects.json` may link to `files/reports/*.pdf`, but those links are valid only after the CI build has produced the deploy artifact.
- Do not manually copy PDFs into this directory as a separate agent step.
- Expected public outputs include:
  - `agenticcareerboost-project-history.pdf` — project-history bridge and evidence map
  - `agentic-system-guide.pdf` — human-facing manual
  - `agentic-system-evidence-reconciliation.pdf` — local-vs-remote reconciliation, drift repairs, and validation ledger
  - `agentic-system-refactor-retrospective.pdf` — AgenticSystem refactor and cleanup retrospective
  - `s000-agentic-os-bootstrap.pdf` — technical bootstrap case study
  - `s001-profile-audit-positioning.pdf` — profile audit and strategic positioning report
  - `s0015r-system-review.pdf` — corrective system-review and S-001.5 remediation report
  - `s002-restart-refresh.pdf` — S-002R restart review and repo-local closure report
  - `s003-website-os-clarity.pdf` — S-003 public route-map and website clarity report
  - `s004-documentation-alignment.pdf` — S-004 career guardrail and relaunch calibration report
  - `s0045-site-quality.pdf` — S-004.5 site quality and runtime validation report
- `smoke.pdf` and private local candidate PDFs are compile checks only and are not part of the published set.
