"""
Agent definition tests.

This module verifies that the central index of agents in ``AGENTS.md``
is consistent with the actual role definition files under
``docs/agents/``.  Each role listed in the ``Role index`` table of
AGENTS.md should have a corresponding Markdown file describing the
role’s responsibilities and constraints.  If a role is added or
renamed in AGENTS.md without adding the corresponding file, agents
attempting to instantiate that role will fail.  Conversely, if a
file exists without being indexed, the orchestrator may not be able
to route to it.
"""
import re
from pathlib import Path

def test_agent_index_matches_files() -> None:
    root = Path(__file__).resolve().parents[1]
    agents_md = root / "AGENTS.md"
    if not agents_md.exists():
        import pytest; pytest.skip("AGENTS.md not found; skipping agent index test")
        return
    text = agents_md.read_text(encoding="utf-8")
    # Capturamos solo la ruta interna y la normalizamos
    pattern = re.compile(r"\((docs/agents/[^)]+)\)")
    referenced_files = [m.strip() for m in pattern.findall(text)]
    assert referenced_files, "No agent files referenced in AGENTS.md Role index"
    for rel_path in referenced_files:
        path = root / rel_path
        assert path.exists(), f"Agent file '{rel_path}' referenced in AGENTS.md but not found"
        assert path.is_file(), f"Agent path '{rel_path}' is not a file"

def test_agent_files_are_indexed() -> None:
    root = Path(__file__).resolve().parents[1]
    agents_dir = root / "docs/agents"
    if not agents_dir.exists():
        import pytest; pytest.skip("docs/agents directory not found; skipping agent indexing test")
        return
    agents_md = (root / "AGENTS.md")
    if not agents_md.exists():
        import pytest; pytest.skip("AGENTS.md not found; skipping agent indexing test")
        return
    agents_md_text = agents_md.read_text(encoding="utf-8")
    # Extraemos las rutas del índice y las normalizamos
    index_pattern = re.compile(r"\((docs/agents/[^)]+)\)")
    indexed_paths = {m.strip() for m in index_pattern.findall(agents_md_text)}
    md_files = [p for p in agents_dir.glob("*.md") if p.name != "autoagents.md"]
    for file in md_files:
        rel = file.relative_to(root).as_posix()
        assert rel in indexed_paths, f"Agent file '{rel}' exists but is not listed in AGENTS.md"