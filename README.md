# AgenticCareerBoost

Public repository for Dídac Llorens' career operating system: agent rules,
state evidence, formal reports, CV artifacts, and a static website.

## Public entrypoints

- [Website](https://didacll.github.io/)
- [CV PDF](site/files/cv/didac-llorens-cv.pdf)
- [Agentic System Guide](site/files/reports/agentic-system-guide.pdf)
- [AgenticSystem refactor retrospective](site/files/reports/agentic-system-refactor-retrospective.pdf)
- [AgenticSystem evidence reconciliation](site/files/reports/agentic-system-evidence-reconciliation.pdf)
- [S-000 case study](site/files/reports/s000-agentic-os-bootstrap.pdf)
- [Sprint S-001 report](site/files/reports/s001-profile-audit-positioning.pdf)

## Structure

| Path | Purpose |
|------|---------|
| `AGENTS.md` | Root instruction entrypoint for agents |
| `agents/rules/` | Authoritative rules, workflows, roles, and templates |
| `agents/state/` | Evidence, current status, logs, research, and archives |
| `agents/reports/tex/` | LaTeX report and CV sources |
| `agents/tools/` | Repo-local validation/export tools |
| `agents/tests/` | Targeted behavior and structure checks |
| `site/` | Public website runtime, media, data, and downloadable files |
| root HTML/SEO files | GitHub Pages entrypoints and crawler files |

`agents/state/**` is useful context, but it is never authoritative for future
behavior. Agent rules live in `agents/rules/**`; state records evidence.

## Current status

No sprint is active. S-004.5 is closed, and S-005 remains the next LinkedIn
campaign kickoff seed.

Status evidence:

- [Current state](agents/state/current.md)
- [Active sprint marker](agents/state/active-sprint.md)
- [Roadmap](agents/state/roadmap.md)
- [Career direction guardrail](agents/rules/core/career-direction.md)
- [Execution modes](agents/rules/core/execution-modes.md)
- [Public copy rules](agents/rules/core/public-copy.md)

## Local checks

```bash
python agents/tools/export_status.py
python agents/tools/validate_static_site.py
bash agents/tools/validate_links.sh
python -m pytest agents/tests -q
```

The status JSON at `site/data/status.json` is generated from
`agents/state/**`. Do not edit it by hand.
