# Public Site Remediation

Date: 2026-06-12

## Decision Matrix

| Decision | Option | Score | Result |
|---|---|---:|---|
| Homepage role | Keep mixed portfolio + dashboard | 2 | Reject: leaks internal process |
| Homepage role | Personal professional landing only | 9 | Select |
| Dashboard access | Top-level global nav | 4 | Reject: overexposes project operations |
| Dashboard access | Linked from AgenticCareerBoost page | 9 | Select |
| Implementation | Add framework/site generator | 2 | Reject: unnecessary |
| Implementation | Plain static HTML/CSS edits | 10 | Select |

## Selected Fix

Keep the homepage human-facing and project-neutral. Move live sprint/status language behind
the AgenticCareerBoost project page. Remove recruiter/internal wording from public copy.
