"""
Benchmark execution script for AgenticCareerBoost.

This module provides a simple harness for running static benchmark
checks defined in ``tasks.json``.  It is intended to be executed
within a ``pytest`` session (similar to the unit tests under
``tests/``) and will raise assertion failures when a benchmark
condition is not met.  While the tasks defined here are simple, the
framework can be extended to include more sophisticated checks such
as LLM output evaluation, tool invocation logging and invariant
monitoring.

Each task in ``tasks.json`` may specify one or more of the following
fields:

* ``expected_substring`` – the file must contain this substring.
* ``min_steps`` – the file must contain at least this many numbered
  steps (e.g. ``1.``, ``2.``, etc.).
* ``expected_checklist_count`` – the file must contain at least this
  many checklist items (e.g. ``- [ ]``) in the section under test.

Additional fields can be added as needed and supported in the
``run_task`` function.
"""

import json
import re
from pathlib import Path


def load_tasks() -> list[dict]:
    """Load the benchmark tasks from tasks.json in this directory."""
    tasks_file = Path(__file__).resolve().parent / "tasks.json"
    with tasks_file.open(encoding="utf-8") as f:
        return json.load(f)


def count_numbered_steps(text: str) -> int:
    """Count lines that start with a numbered list marker (e.g. '1.')."""
    return len(re.findall(r"^\s*\d+\.", text, re.MULTILINE))


def count_checklist_items(text: str) -> int:
    """Count Markdown checklist items in the given text (e.g. '- [ ]')."""
    return len(re.findall(r"- \[[ xX]\]", text))


def run_task(task: dict, root: Path) -> None:
    """Execute a single benchmark task against the repository root.

    :param task: The task definition loaded from tasks.json.
    :param root: The repository root directory.
    :raises AssertionError: If the task's condition is not satisfied.
    """
    file_path = root / task["file"]
    # If the target file does not exist in the current environment, skip the
    # benchmark rather than failing.  This allows the suite to run in
    # contexts (such as CI against unrelated components) where the
    # AgenticCareerBoost repository may not be present.  When run in the
    # actual repository the files will exist and the assertions below
    # will apply.
    if not file_path.exists():
        import pytest  # imported here to avoid a hard dependency for non‑pytest users
        pytest.skip(f"Benchmark file '{task['file']}' not found; skipping task '{task['name']}'")
        return
    content = file_path.read_text(encoding="utf-8")
    # Check for expected substring
    if "expected_substring" in task:
        expected = task["expected_substring"]
        assert expected in content, (
            f"Benchmark '{task['name']}' failed: expected substring '{expected}' not found in {task['file']}"
        )
    # Check minimum number of steps
    if "min_steps" in task:
        steps = count_numbered_steps(content)
        assert steps >= task["min_steps"], (
            f"Benchmark '{task['name']}' failed: found {steps} numbered steps in {task['file']},"
            f" expected at least {task['min_steps']}"
        )
    # Check number of checklist items
    if "expected_checklist_count" in task:
        # Restrict the search to the Outputs section for clarity.  If the
        # Outputs section cannot be found then fallback to counting all
        # checkboxes in the file.
        outputs_match = re.search(r"## Outputs[\s\S]+?(?=\n##|$)", content)
        search_text = outputs_match.group(0) if outputs_match else content
        count = count_checklist_items(search_text)
        assert count >= task["expected_checklist_count"], (
            f"Benchmark '{task['name']}' failed: found {count} checklist items in {task['file']},"
            f" expected at least {task['expected_checklist_count']}"
        )


def test_benchmark_tasks() -> None:
    """Run all benchmark tasks defined in tasks.json."""
    root = Path(__file__).resolve().parents[1]
    tasks = load_tasks()
    for task in tasks:
        run_task(task, root)