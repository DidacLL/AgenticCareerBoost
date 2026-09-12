# Application Tracker Prototype

This folder contains scratch tooling created for my own job-search workflow.
It is useful evidence, but it is not the future product architecture.

The tracker work here is a precursor to AAAAT. Keep it understandable and
preserve the local workflow.

## Valuable Workflow

The cover-letter renderer is the important working path:

```powershell
.\letter.ps1 example-slug
```

Expected local files:

- input: `.private/example-slug.json`
- input contract: `letter-input.schema.json`
- template: `templates/letter-template.tex`
- renderer: `render_letter.py`
- output: `.private/generated/`

The `.private` directory contains live local data and must not be committed or
copied into docs, prompts, tests, or public examples.

The JSON schema belongs only to the standalone cover-letter input. ACB does not
use or define a CV JSON format: tailored CV artifacts use the existing LaTeX CV
system. See `agents/cv/APPLICATION_WORKFLOW.md` for format precedence and combined
versus separate application deliverables.

## Prototype Tracker

The tracker scripts and static demo are kept as prototype evidence for AAAAT.
They are useful for understanding the workflow, but they should not be treated
as a production implementation.
