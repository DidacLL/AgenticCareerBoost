# Run contract

Every non-trivial run declares its contract before workflow selection becomes operational.
The contract keeps scope, context, writes, validation, and state effects aligned with
what the user actually requested.

## Required fields

```text
mode:
requested_output:
source_authority:
write_surface:
state_effect:
validation_surface:
review_depth:
```

- `mode` comes from `agents/rules/core/execution-modes.md`.
- `requested_output` names what the user expects to receive now.
- `source_authority` names the file families needed for the run.
- `write_surface` names the artifact families that may change.
- `state_effect` is `none`, `candidate_evidence`, `activation`, or `closure`.
- `validation_surface` names the verification that proves the touched surface.
- `review_depth` names the review needed for the risk of the output.

Validation follows the touched surface. Available tooling does not define
validation.

## Sealed-context boundary

Private user material is sealed by default. A run may use it only when the user
explicitly allows that exact use, and even then it remains non-operational input.

Sealed material must not be:

- quoted, summarized, paraphrased, or converted into examples;
- used as search, grep, regex, validator, test, fixture, or prompt text;
- transformed into negative checks, sentinel terms, derived keyword lists, or
  tool arguments;
- written into repository artifacts, logs, rules, reviews, comments, commits,
  pull requests, generated outputs, or public surfaces;
- transferred to subagents unless the user explicitly authorizes that transfer
  for the current run.

Read-only access is not automatically safe. If a private input is echoed into a
command, trace, review, test, or artifact, the boundary has already failed.

Allowed use is limited to silent, in-context calibration for the current answer
or task. The output may describe the authorized use category, but must not expose
terms, concepts, examples, fingerprints, or other recognizable derivatives from
the sealed source.

## Validation by touched surface

| Touched surface | Valid validation |
|---|---|
| Chat answer or review answer | Source reading, citation, reasoning review |
| Social copy, campaign concept, or prose | Readback, voice review, human approval |
| Markdown documentation | Readback; link checks only when links changed |
| Core rules, workflows, or roles | Semantic review against truth hierarchy and affected workflows |
| Site content, public JSON, or public HTML | Static-site validation when public structure changed |
| Site runtime JS, CSS, or routing | Static-site validation and browser checks |
| Report TeX | Build only the touched report target |
| CV or cover-letter artifact pipeline | CV or letter build checks |
| Tests, validators, or CI workflows | Targeted validation of the touched tool |

## Source authority by family

| Source family | Use |
|---|---|
| Direct user prompt | Current objective and constraints |
| Core rules | Stable behavior |
| Selected workflow | Process for this run |
| Selected role | Role behavior |
| State current and active-sprint | Compact status only |
| Roadmap and backlog | Candidate seeds, not commitments |
| Logs, research, and reports | Historical evidence only |
| Work artifacts | Drafts, plans, and candidate outputs |
| Generated site files | Produced artifacts, not source authority |

Historical evidence can explain why something happened. It does not define the
next run unless a rule file promotes that behavior.
