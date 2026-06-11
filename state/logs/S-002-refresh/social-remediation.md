# S-002R Social/Profile Remediation

- Date: 2026-06-11
- Scope: PairCheck-A/B defects for S-002R profile/social only
- Status: bounded remediation note

## Decisions

### Decision 1: Repair the research-currentness gap by adding 2026 source anchors

Scoring: 1 low, 10 high. Higher total is better.

| Option | Description | Current-source fit | Public safety | Draft continuity | Effort | Total | Decision |
|---|---|---:|---:|---:|---:|---:|---|
| A | Add verified 2026 arXiv anchors and keep vendor posts as market context | 10 | 9 | 9 | 8 | 36 | Selected |
| B | Reframe the file as a non-June evergreen refresh without adding sources | 5 | 9 | 8 | 9 | 31 | Rejected |

Rationale: PairCheck-B challenged the source base, not the post strategy. Adding 2026 oversight, dataset, and benchmark anchors resolves the currency defect while preserving the low-heat sequence.

### Decision 2: Update source bundles without rewriting post bodies

| Option | Description | Link-placement safety | Source inheritance | Tone stability | Effort | Total | Decision |
|---|---|---:|---:|---:|---:|---:|---|
| A | Add current 2026 links to first-comment bundles and safety notes only | 10 | 9 | 10 | 9 | 38 | Selected |
| B | Rewrite all three post bodies to mention every new source | 6 | 8 | 5 | 5 | 24 | Rejected |

Rationale: The existing drafts already passed tone and body-link checks. First-comment bundles are the right place to carry source repair without adding body links or turning drafts into literature summaries.

### Decision 3: Update status as PARTIAL, not closed

| Option | Description | Truthfulness | Closure discipline | Blocker preservation | Effort | Total | Decision |
|---|---|---:|---:|---:|---:|---:|---|
| A | Mark profile/social artifacts present and site still PARTIAL due missing Ruby/Bundler gates | 10 | 10 | 10 | 8 | 38 | Selected |
| B | Mark S-002R complete because profile/social defects are fixed | 3 | 2 | 4 | 9 | 18 | Rejected |

Rationale: PairCheck-A's stale-status defect needed repair, but the sprint must remain open because Jekyll/browser/print gates and human-owned account checks are still blocked.

## Verification Notes

- Verified public arXiv pages for:
  - `https://arxiv.org/abs/2606.05391`
  - `https://arxiv.org/abs/2605.15226`
  - `https://arxiv.org/abs/2602.09185`
  - `https://arxiv.org/abs/2601.11077`
- Kept post bodies link-free; added current anchors only to first-comment bundles and safety notes.
- Preserved the rule against private project naming; no private reference names were introduced.
