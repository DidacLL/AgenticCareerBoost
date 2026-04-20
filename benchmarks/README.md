# Benchmarks and evaluation

This folder contains a nascent benchmark suite for evaluating the
AgenticCareerBoost system.

## Motivation

Recent work highlights that evaluating agentic AI systems requires
moving beyond simple task completion.  Agentic systems introduce new
sources of uncertainty—including non‑deterministic decision making,
tool failure modes and hallucinations—so evaluations need to measure
how well the system follows policy constraints, uses memory,
selects and sequences tools and interacts with its environment【425091462893398†L96-L123】【756543260852092†L54-L69】.
A robust evaluation framework should assess behaviour at multiple
levels: the underlying LLM, individual agents and the overall
multi‑agent system【756543260852092†L90-L113】.  It should also
incorporate static analysis of specifications, dynamic runtime
monitoring and human judgements【425091462893398†L160-L170】.

## Benchmark design

The initial benchmarks supplied here focus on static checks that can
run in CI.  They complement the unit tests under `tests/` and
provide early warning when changes to the source of truth break
contractual assumptions.  In the future these can be extended to
dynamic execution and judge‑based evaluations.

### Task format

Each benchmark task is defined in `tasks.json` with the following
fields:

* `name` – a unique identifier.
* `description` – human‑readable explanation of what is being tested.
* `file` – path to the Markdown file under test.
* Additional keys describing the expected property (e.g.
  `expected_substring`, `min_steps`, `expected_checklist_count`).

### Execution

The script `test_agentic_system.py` loads `tasks.json`, reads the
specified file and performs the appropriate check.  For example, the
`mission_goal_phrase` benchmark asserts that the mission statement
still contains the phrase “Rebuild a public technical profile”.  The
`plan_workflow_steps_count` benchmark counts numbered steps in
`docs/workflows/plan.md` and ensures there are at least seven,
guarding against oversimplification of the planning process.  The
`sprint_workflow_closure_artifacts` benchmark counts the number of
checklist items in the sprint workflow’s Outputs section and ensures
there are at least six (the current contract lists six closure
artefacts【306433475537055†L52-L63】).

### Extending benchmarks

The literature suggests that full agentic evaluation should capture
dimensions such as instruction following and safety alignment for the
LLM, storage and retrieval correctness for memory, tool selection and
sequencing and handling of environment constraints【425091462893398†L96-L124】.
To incorporate these dimensions you might:

* Add golden datasets of prompts and expected outputs and use an
  LLM evaluator (e.g. [DeepEval](https://github.com/confident-ai/deepeval)) to compute
  adherence, factuality and safety scores.
* Instrument agent runtime to log tool invocations and memory
  operations, then build assertions about tool selection accuracy,
  parameter mapping and sequencing.
* Define system invariants (e.g. “no orphan work”, “no double writes”)
  and monitor for violations during multi‑agent sprints【756543260852092†L149-L201】.
* Run scenarios under both in‑distribution and out‑of‑distribution
  conditions and compare behaviour.

By starting with these static tests and extending toward dynamic and
judge‑based evaluations, you can build a trustworthy evaluation
framework that catches regressions early and supports continuous
improvement of the AgenticCareerBoost system.
