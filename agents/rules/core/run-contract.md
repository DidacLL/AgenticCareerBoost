# Run contract

Every non-trivial run declares its contract before workflow selection becomes
operational. The contract keeps scope, context, writes, validation, and state
effects aligned with what the user actually requested.

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

## Human surface rule

Separate three surfaces before producing work:

1. **Agent workspace** — temporary reasoning, review, scratch artifacts, or
   verbose specialist material. It is not a human review requirement.
2. **Human decision surface** — the smallest concrete summary, choice, draft, or
   verdict the user needs to act. This is the default surface for approval.
3. **Canonical state** — durable rules, accepted outputs, active state, or
   closure evidence promoted by the run contract.

A run must not make the user read the agent workspace to remain in control. When
human judgment is required, compress the agent workspace into a human decision
surface with the decision, tradeoff, evidence boundary, and next action.

Do not create additional planning artifacts merely to expose agent discussion.
Create or persist an artifact only when the run contract needs it as candidate
evidence, canonical state, or reusable source material.

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
