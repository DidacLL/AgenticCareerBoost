# Published reports

This directory stores the latest compiled PDFs that should remain visible in
the repository after CI completes.

- Source files live in `agents/reports/tex/`.
- Local builds write to `agents/reports/tex/build/`.
- Pull requests that update report sources regenerate the intended public PDFs
  here through the LaTeX build scripts. Do not manually copy PDFs into this
  directory as a separate agent step. CI compiles the same sources and uploads
  PDFs as workflow artifacts, but it does not auto-commit to protected `main`.
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
- `smoke.pdf` is a CI compile check only and is not part of the published set.
