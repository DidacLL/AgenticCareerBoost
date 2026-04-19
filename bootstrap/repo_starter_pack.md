# REPO STARTER PACK

This file defines the initial repository skeleton for the public profile rebuild system.

It assumes the mission and operating law already defined in `AGENT_BOOTSTRAP_PROMPT.md`.

This starter pack is intentionally compact.
Its job is to create a repository that humans and agents can both navigate with low friction and low token cost.

---

# 1. Design goal

Build a repository that is:

- public and inspectable
- model-agnostic
- path-based
- concise
- modular
- resistant to noisy or contradictory agent output

The repository must clearly separate:

- stable truth
- workflow rules
- agent role definitions
- volatile current state
- public content artifacts

---

# 2. Core repository rules

## Rule 1 — Source of truth
GitHub repository + GitHub Projects are the operational source of truth.

## Rule 2 — Canonical text first
All durable instructions and knowledge must exist first as plain text in the repository.

## Rule 3 — Public mirror
The website is a curated public mirror, not the workflow engine.

## Rule 4 — Distribution
LinkedIn / social distributes selected narrative artifacts.

## Rule 5 — Brevity by default
Files must be brief unless detail is strictly necessary.

Prefer:
- short sections
- checklists
- compact task contracts
- minimal templates
- dense Markdown

Avoid:
- long essays
- repeated context
- decorative prose
- giant rule dumps

## Rule 6 — Truth priority
When files conflict, use this order:
1. direct user prompt
2. `docs/core/`
3. `docs/workflows/`
4. `docs/agents/`
5. `state/`
6. logs, backlogs, summaries, scratch files

## Rule 7 — No orphan work
A meaningful sprint output should connect, when applicable, to:
- one repository artifact
- one website trace or update
- one social-ready artifact or queued narrative candidate

This rule is strict for sprints, lighter for hotfixes, and optional for pure chat/system-review workflows.

---

# 3. Minimal initial repository tree

```text
public-profile-rebuild/
├─ README.md
├─ AGENTS.md
├─ LICENSE
├─ .gitignore
├─ .github/
│  ├─ ISSUE_TEMPLATE/
│  │  ├─ sprint-task.yml
│  │  ├─ hotfix-task.yml
│  │  ├─ system-review.yml
│  │  ├─ website-update.yml
│  │  └─ social-post.yml
│  ├─ PULL_REQUEST_TEMPLATE.md
│  └─ workflows/
│     ├─ docs-lint.yml
│     ├─ site-build.yml
│     └─ export-status.yml
├─ docs/
│  ├─ core/
│  │  ├─ mission.md
│  │  ├─ brand.md
│  │  ├─ marketing.md
│  │  ├─ constraints.md
│  │  ├─ truth-hierarchy.md
│  │  └─ tool-policy.md
│  ├─ workflows/
│  │  ├─ plan.md
│  │  ├─ sprint.md
│  │  ├─ hotfix.md
│  │  ├─ chat.md
│  │  └─ system-review.md
│  └─ agents/
│     ├─ orchestrator.md
│     ├─ developer.md
│     ├─ paircheck.md
│     ├─ cicd.md
│     ├─ documentation.md
│     └─ community-manager.md
├─ state/
│  ├─ current.md
│  ├─ roadmap.md
│  ├─ active-sprint.md
│  ├─ backlog.md
│  ├─ logs/
│  └─ summaries/
├─ content/
│  ├─ social/
│  ├─ site/
│  └─ reports/
├─ site/
│  └─ starter/
├─ data/
│  ├─ public-status.json
│  └─ links.json
└─ assets/