# Published reports

This directory stores the latest compiled PDFs that should remain visible in
the repository after CI completes.

- Source files live in `content/reports/tex/`.
- Local builds write to `content/reports/tex/build/`.
- Pull requests that update report sources also update the intended public PDFs
  here. CI compiles the same sources and uploads PDFs as workflow artifacts, but
  it does not auto-commit to protected `main`.
- Expected public outputs include:
  - `agentic-system-guide.pdf` — human-facing manual
  - `s000-agentic-os-bootstrap.pdf` — technical bootstrap case study
  - `s001-profile-audit-positioning.pdf` — profile audit and strategic positioning report
  - `s0015r-system-review.pdf` — corrective system-review and S-001.5 remediation report
  - `didac-llorens-cv.pdf` — recruiter-facing formal CV
- `smoke.pdf` is a CI compile check only and is not part of the published set.
