"""
Workflow contract tests.

The workflow definitions in ``docs/workflows/`` serve as contracts
governing how agents coordinate to plan, execute and review work.  To
avoid regressions when editing these files, this test suite checks
that each workflow document contains the standard heading structure
and that certain invariants (such as the presence of numbered steps
and outputs) are maintained.  These tests are not exhaustive but
provide early warning if a structural section is removed or renamed.
"""

import re
from pathlib import Path


# Standard section headings that every workflow contract should include
REQUIRED_HEADINGS = [
    "## Trigger",
    "## Inputs",
    "## Steps",
    "## Outputs",
    "## Exit criteria",
]


def test_workflow_files_have_required_sections() -> None:
    """Verify that each workflow Markdown file contains the required headings."""
    root = Path(__file__).resolve().parents[1]
    wf_dir = root / "docs/workflows"
    if not wf_dir.exists():
        import pytest
        pytest.skip("docs/workflows directory not found; skipping workflow tests")
        return
    for wf_file in wf_dir.glob("*.md"):
        content = wf_file.read_text(encoding="utf-8")
        for heading in REQUIRED_HEADINGS:
            assert heading in content, f"{wf_file.name} missing required section '{heading}'"


def test_workflow_steps_are_numbered() -> None:
    """Ensure that each workflow contains at least one numbered step in the Steps section."""
    root = Path(__file__).resolve().parents[1]
    wf_dir = root / "docs/workflows"
    if not wf_dir.exists():
        import pytest
        pytest.skip("docs/workflows directory not found; skipping workflow numbering test")
        return
    for wf_file in wf_dir.glob("*.md"):
        content = wf_file.read_text(encoding="utf-8")
        # Extract the Steps section
        match = re.search(r"## Steps\n(.+?)(\n##|$)", content, re.DOTALL)
        assert match, f"Steps section not found in {wf_file.name}"
        steps_section = match.group(1)
        numbered_steps = re.findall(r"^\s*\d+\.", steps_section, re.MULTILINE)
        assert numbered_steps, f"No numbered steps found in {wf_file.name}"


def test_sprint_workflow_closure_outputs() -> None:
    """For the sprint workflow, validate that six closure artifacts are enumerated."""
    root = Path(__file__).resolve().parents[1]
    sprint_file = root / "docs/workflows/sprint.md"
    if not sprint_file.exists():
        import pytest
        pytest.skip("docs/workflows/sprint.md not found; skipping sprint outputs test")
        return
    content = sprint_file.read_text(encoding="utf-8")
    match = re.search(r"## Outputs.*?\n([\s\S]+?)(\n##|$)", content)
    if match:
        outputs_section = match.group(1)
        checkboxes = re.findall(r"- \[[ xX]\]", outputs_section)
        assert len(checkboxes) >= 6, (
            "Sprint workflow Outputs section should enumerate at least six closure artifacts"
        )