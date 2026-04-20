# Published reports

This directory stores the latest compiled PDFs that should remain visible in
the repository after CI completes.

- Source files live in `content/reports/tex/`.
- Local builds write to `content/reports/tex/build/`.
- `latex-build.yml` promotes PDFs from the local build directory into this
  folder on pushes that update `content/reports/tex/`, refreshing the
  published set from CI.
- Expected public outputs include:
  - `agentic-system-guide.pdf` — human-facing manual
  - `s000-agentic-os-bootstrap.pdf` — technical bootstrap case study
- `smoke.pdf` is a CI compile check only and is not part of the published set.
