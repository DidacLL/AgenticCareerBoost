"""
Mission file tests.

The mission statement defines the overarching goals, scope and
constraints for the entire AgenticCareerBoost project.  A change to
``docs/core/mission.md`` could inadvertently remove critical
sections or success criteria, making it harder for agents (and
humans) to understand what they are optimising for.  These tests
provide a minimum guardrail: they assert the presence of the main
headings documented in the bootstrap specification and check that
there is at least one bullet under the success criteria.
"""

from pathlib import Path


def test_mission_contains_expected_sections() -> None:
    """Check that mission.md contains Goal, Scope, Success criteria and Non-goals sections."""
    root = Path(__file__).resolve().parents[1]
    mission_file = root / "docs/core/mission.md"
    if not mission_file.exists():
        import pytest
        pytest.skip("docs/core/mission.md not found; skipping mission tests")
        return
    content = mission_file.read_text(encoding="utf-8")
    required_sections = [
        "## Goal",
        "## Scope",
        "## Success criteria",
        "## Non-goals",
    ]
    for section in required_sections:
        assert section in content, f"Section '{section}' missing from mission.md"


def test_success_criteria_have_entries() -> None:
    """Ensure there is at least one bullet under Success criteria in mission.md."""
    root = Path(__file__).resolve().parents[1]
    mission_file = root / "docs/core/mission.md"
    if not mission_file.exists():
        import pytest
        pytest.skip("docs/core/mission.md not found; skipping mission tests")
        return
    content = mission_file.read_text(encoding="utf-8")
    # Extract the Success criteria section and count list items (- or *)
    import re
    match = re.search(r"## Success criteria\n([\s\S]+?)(\n##|$)", content)
    assert match, "Success criteria section not found in mission.md"
    section_text = match.group(1)
    bullets = re.findall(r"^[\s]*[-*] ", section_text, re.MULTILINE)
    assert bullets, "Success criteria section should contain at least one bullet point"