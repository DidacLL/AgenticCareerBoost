from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
AGENTS = ROOT / "agents"
SITE = ROOT / "site"


def git_executable() -> str | None:
    found = shutil.which("git")
    if found:
        return found
    windows_git = Path("C:/Program Files/Git/cmd/git.exe")
    if windows_git.exists():
        return str(windows_git)
    return None


def text_files():
    suffixes = {".md", ".json", ".yml", ".yaml", ".py", ".sh", ".ps1", ".tex", ".html", ".js", ".xml"}
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file() or path.suffix not in suffixes:
            continue
        yield path


def live_text_files():
    for path in text_files():
        if path.is_relative_to(AGENTS / "tests"):
            continue
        if path.is_relative_to(AGENTS / "state" / "archive"):
            continue
        if path.is_relative_to(AGENTS / "state" / "logs"):
            continue
        if path.is_relative_to(AGENTS / "state" / "research"):
            continue
        if path.is_relative_to(AGENTS / "state" / "summaries"):
            continue
        yield path


def live_instruction_files():
    roots = [ROOT / "AGENTS.md", ROOT / "README.md", AGENTS / "rules", AGENTS / "work", AGENTS / "tools", SITE]
    for root in roots:
        if root.is_file():
            yield root
            continue
        for path in text_files():
            if path.is_relative_to(root):
                yield path


def test_required_boundaries_exist():
    for path in [
        ROOT / "AGENTS.md",
        AGENTS / "rules" / "core" / "truth-hierarchy.md",
        AGENTS / "rules" / "core" / "execution-modes.md",
        AGENTS / "state" / "current.md",
        AGENTS / "state" / "active-sprint.md",
        AGENTS / "state" / "archive" / "origin" / "agent_bootstrap_prompt.md",
        SITE / "content" / "site.json",
    ]:
        assert path.exists(), path


def test_root_has_no_old_top_level_work_areas():
    forbidden = ["docs", "state", "content", "assets", "data", "scripts", "tests", "benchmarks", "bootstrap"]
    assert [name for name in forbidden if (ROOT / name).exists()] == []


def test_state_is_not_authoritative():
    hierarchy = (AGENTS / "rules" / "core" / "truth-hierarchy.md").read_text(encoding="utf-8")
    active_sprint = (AGENTS / "state" / "active-sprint.md").read_text(encoding="utf-8")
    assert "must never define behavior rules" in hierarchy
    assert "agents/state/*` | Evidence and status only" in hierarchy
    assert "agents/rules/core/*` | Stable rules" in hierarchy
    assert "status marker only" in active_sprint
    assert "acceptance criteria" not in active_sprint.lower()
    assert "current sprint contract" not in active_sprint.lower()


def test_no_live_references_to_deleted_poison_sources():
    forbidden = [
        "content/social/style-book.md",
        "content/social/drafts/",
        "assets/curriculum/DidacLL_Assaia_CoverLetter",
        "data/public-status.json",
        "site/assets/data/public-status.json",
        "site/assets/curriculum/",
    ]
    offenders: list[str] = []
    for path in live_text_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        for token in forbidden:
            if token in text:
                offenders.append(f"{path.relative_to(ROOT).as_posix()}: {token}")
    assert offenders == []


def test_live_paths_use_new_rule_and_state_roots():
    old_tokens = [
        "docs/core/",
        "docs/workflows/",
        "docs/agents/",
        "docs/templates/",
        "`state/current.md`",
        "`state/active-sprint.md`",
        "blob/main/state/current.md",
        "blob/main/state/active-sprint.md",
        "(state/current.md)",
        "(state/active-sprint.md)",
    ]
    offenders: list[str] = []
    for path in live_text_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        for token in old_tokens:
            if token in text:
                offenders.append(f"{path.relative_to(ROOT).as_posix()}: {token}")
    assert offenders == []


def test_live_rules_do_not_make_active_sprint_authoritative():
    forbidden_fragments = [
        "active-sprint.md` — task contracts",
        "active-sprint.md` — task list",
        "active-sprint.md` — fully populated sprint contract",
        "active-sprint.md` marked `status: closed`",
        "Current sprint contract",
    ]
    offenders: list[str] = []
    for path in live_instruction_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        for fragment in forbidden_fragments:
            if fragment in text:
                offenders.append(f"{path.relative_to(ROOT).as_posix()}: {fragment}")
    assert offenders == []


def test_site_json_public_file_refs_resolve():
    route_paths = {
        item["path"]
        for item in json.loads((SITE / "content" / "site.json").read_text(encoding="utf-8"))["routes"]
    }
    ref_keys = {"href", "image", "bannerImage", "legalFragment", "src", "status"}
    failures: list[str] = []

    def walk(node, pointer="$"):
        if isinstance(node, dict):
            for key, value in node.items():
                yield from walk(value, f"{pointer}.{key}")
        elif isinstance(node, list):
            for index, value in enumerate(node):
                yield from walk(value, f"{pointer}[{index}]")
        else:
            yield pointer, node

    for json_file in (SITE / "content").glob("*.json"):
        data = json.loads(json_file.read_text(encoding="utf-8"))
        for pointer, value in walk(data):
            if not isinstance(value, str):
                continue
            key = pointer.rsplit(".", 1)[-1].split("[", 1)[0]
            if key == "route":
                assert value in route_paths
            if key not in ref_keys or value.startswith(("https://", "mailto:", "tel:", "#")):
                continue
            if key == "href" and value in route_paths:
                continue
            if value.startswith("/"):
                failures.append(f"{json_file.name}:{pointer} root path {value}")
                continue
            if not (SITE / value.split("#", 1)[0].split("?", 1)[0]).is_file():
                failures.append(f"{json_file.name}:{pointer} missing {value}")
    assert failures == []


def test_no_duplicate_public_binary_hashes():
    hashes: dict[str, Path] = {}
    duplicates: list[str] = []
    for path in SITE.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".png", ".jpg", ".jpeg", ".pdf", ".svg"}:
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            if digest in hashes:
                duplicates.append(f"{path.relative_to(ROOT)} == {hashes[digest].relative_to(ROOT)}")
            else:
                hashes[digest] = path
    assert duplicates == []


def test_state_evidence_is_not_ignored_by_git():
    git = git_executable()
    assert git is not None, "git executable is required for evidence ignore checks"
    result = subprocess.run(
        [git, "ls-files", "--others", "--ignored", "--exclude-standard", "agents/state"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    ignored = [line for line in result.stdout.splitlines() if line.strip()]
    assert ignored == []


def test_root_gitignore_does_not_hide_latex_named_evidence():
    root_ignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
    risky_global_patterns = ["*.[1-9]R", "*.[1-9]", "*.aux", "*.log", "*.toc"]
    offenders = [
        pattern
        for pattern in risky_global_patterns
        if any(line.strip() == pattern for line in root_ignore.splitlines())
    ]
    assert offenders == []


def test_live_status_references_use_generated_status_json():
    offenders: list[str] = []
    for path in live_text_files():
        if path.is_relative_to(AGENTS / "reports"):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if "public-status.json" in text:
            offenders.append(path.relative_to(ROOT).as_posix())
    assert offenders == []


def test_ci_rules_match_current_docs_lint_shape():
    ci_rules = (AGENTS / "rules" / "core" / "ci-rules.md").read_text(encoding="utf-8")
    docs_lint = (ROOT / ".github" / "workflows" / "docs-lint.yml").read_text(encoding="utf-8")
    assert ".github/lychee.toml" in ci_rules
    assert ".github/lychee.toml" in docs_lint
    assert ".markdownlint.jsonc" not in ci_rules
    assert "config: `lychee.toml`" not in ci_rules
    assert "editing `lychee.toml`" not in ci_rules


def test_report_build_docs_use_agents_report_root():
    makefile = (AGENTS / "reports" / "tex" / "Makefile").read_text(encoding="utf-8")
    assert "content/reports/tex" not in makefile
    assert "agents/reports/tex" in makefile


def test_root_shell_supports_direct_clean_routes():
    index = (ROOT / "index.html").read_text(encoding="utf-8")
    os_js = (SITE / "assets" / "js" / "os.js").read_text(encoding="utf-8")
    router = (SITE / "assets" / "js" / "router.js").read_text(encoding="utf-8")
    components = (SITE / "assets" / "js" / "components.js").read_text(encoding="utf-8")
    assert 'src="/site/assets/js/os.js' in index
    assert 'href="/site/assets/css/site.css' in index
    assert 'src="site/' not in index
    assert 'href="site/' not in index
    assert "?v=" not in index
    assert "?v=" not in os_js
    assert "location.pathname" in router
    assert "window.history.pushState" in router
    assert "popstate" in router
    assert "resolveSiteUrl(item.href)" in components
