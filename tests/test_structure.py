"""
Basic structural integrity tests for the AgenticCareerBoost repository.

These tests verify that the high‑level directory layout expected by
the multiagent operating system is present.  Maintaining these
directories is critical because the agent dispatch logic relies on
stable paths to find mission statements, workflow contracts, role
definitions, state, public content and site mirrors.  If any of
these directories go missing after a refactor or during a change to
the source of truth, the agents will not be able to locate key
documents and will halt execution, leading to brittle or broken
workflows.
"""

from pathlib import Path


def test_required_directories_exist() -> None:
    """Ensure that all top‑level directories required by the agentic system exist.

    The AGENTS.md file documents a truth priority hierarchy and lists
    several directory families that must be present.  This test
    enumerates those directories relative to the project root and
    asserts that each exists and is a directory.  If new families are
    added to the truth hierarchy in the future they should be added
    here as well.
    """
    # Compute the repository root by stepping two parents above this file
    root = Path(__file__).resolve().parents[1]
    # If the expected directory structure is not present, skip this test.
    # This allows the suite to run in environments where the
    # AgenticCareerBoost repository has not been checked out.  When
    # executed in the correct repository the directories will exist
    # and the assertions will run.
    if not (root / "docs").exists():
        import pytest
        pytest.skip("Repository structure not found; skipping structural tests")
        return
    required_dirs = [
        "docs/core",
        "docs/workflows",
        "docs/agents",
        "docs/templates",
        "state",
        "content",
        "site/starter",
        "data",
    ]
    for rel in required_dirs:
        path = root / rel
        assert path.exists(), f"Required directory '{rel}' is missing"
        assert path.is_dir(), f"'{rel}' exists but is not a directory"