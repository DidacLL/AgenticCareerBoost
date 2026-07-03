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
        if path.is_relative_to(AGENTS / "reports" / "deepsearch"):
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
        AGENTS / "cv" / "README.md",
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
    ps_build = (AGENTS / "reports" / "tex" / "build-local.ps1").read_text(encoding="utf-8")
    sh_build = (AGENTS / "reports" / "tex" / "build-local.sh").read_text(encoding="utf-8")
    report_readme = (SITE / "files" / "reports" / "README.md").read_text(encoding="utf-8")
    assert "content/reports/tex" not in makefile
    assert "agents/reports/tex" in makefile
    assert "site" in ps_build and "files" in ps_build and "reports" in ps_build
    assert "Copy-Item" in ps_build
    assert "site/files/reports" in sh_build
    assert "cp " in sh_build
    assert "Do not manually copy PDFs" in report_readme


def cv_manifest() -> list[dict]:
    data = json.loads((AGENTS / "cv" / "artifacts.json").read_text(encoding="utf-8"))
    return [item for item in data["artifacts"] if item.get("publish") is True]


def safe_relative(value: str) -> Path:
    path = Path(value)
    assert not path.is_absolute()
    assert ".." not in path.parts
    return path


def test_cv_artifact_manifest_declares_public_sources():
    cv_root = AGENTS / "cv"
    required = [
        cv_root / "README.md",
        cv_root / "latexmkrc",
        cv_root / "build-local.sh",
        cv_root / "build-local.ps1",
        cv_root / "artifacts.json",
        cv_root / "tools" / "render-cover-letter.py",
        cv_root / "tools" / "artifact_manifest.py",
    ]
    for path in required:
        assert path.is_file(), path

    assert not (ROOT / "assets" / "curriculum").exists()
    artifacts = cv_manifest()
    assert artifacts
    assert {item["kind"] for item in artifacts} >= {"cv", "cover-letter"}
    for item in artifacts:
        assert item["kind"] in {"cv", "cover-letter"}
        source = safe_relative(item["source"])
        build_pdf = safe_relative(item["buildPdf"])
        site_pdf = safe_relative(item["sitePdf"])
        assert build_pdf.parts[:1] == ("build",)
        assert site_pdf.parts[:2] == ("site", "files")
        assert build_pdf.suffix == ".pdf"
        assert site_pdf.suffix == ".pdf"
        if item["kind"] == "cv":
            assert (cv_root / source).is_file()
        if item["kind"] == "cover-letter":
            data = safe_relative(item["data"])
            assert (cv_root / data).is_file()


def test_cv_public_links_follow_manifest():
    cv_text = (SITE / "content" / "cv.json").read_text(encoding="utf-8")
    projects_text = (SITE / "content" / "projects.json").read_text(encoding="utf-8")
    for item in cv_manifest():
        site_pdf = safe_relative(item["sitePdf"]).as_posix().removeprefix("site/")
        source = safe_relative(item["source"]).as_posix()
        if item["kind"] == "cv":
            source_url = f"https://github.com/DidacLL/AgenticCareerBoost/blob/main/agents/cv/{source}"
            assert site_pdf in cv_text
            assert source_url in cv_text
            assert source_url in projects_text
    for stale in ["assets/curriculum/", "site/assets/curriculum/"]:
        assert stale not in cv_text
        assert stale not in projects_text


def test_generated_cv_pdfs_are_ignored_not_tracked():
    git = git_executable()
    assert git is not None, "git executable is required for generated PDF tracking checks"
    generated_paths: list[str] = []
    for item in cv_manifest():
        source = safe_relative(item["source"])
        build_pdf = safe_relative(item["buildPdf"])
        site_pdf = safe_relative(item["sitePdf"])
        generated_paths.extend([site_pdf.as_posix(), f"agents/cv/{build_pdf.as_posix()}"])
        if source.parts[:1] == ("build",):
            generated_paths.append(f"agents/cv/{source.as_posix()}")

    tracked = subprocess.run(
        [git, "ls-files", *generated_paths],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.splitlines()
    assert tracked == []

    ignored = subprocess.run(
        [git, "check-ignore", "--no-index", *generated_paths],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.splitlines()
    assert set(ignored) == set(generated_paths)


def test_site_directory_is_canonical_public_artifact():
    root_index = (ROOT / "index.html").read_text(encoding="utf-8")
    site_index = (SITE / "index.html").read_text(encoding="utf-8")
    os_js = (SITE / "assets" / "js" / "os.js").read_text(encoding="utf-8")
    components = (SITE / "assets" / "js" / "components.js").read_text(encoding="utf-8")
    assert "site/" in root_index
    assert 'src="assets/js/os.js' in site_index
    assert 'href="assets/css/site.css' in site_index
    assert 'href="/site/' not in site_index
    assert 'src="/site/' not in site_index
    assert "?v=" not in site_index
    assert "?v=" not in os_js
    assert "resolveSiteUrl(item.href)" in components
    assert "item.newTab" in components
    assert "isStaticFileHref" in components


def test_site_runtime_routes_are_deployment_base_agnostic():
    runtime_files = [
        SITE / "index.html",
        SITE / "404.html",
        SITE / "assets" / "js" / "os.js",
        SITE / "assets" / "js" / "router.js",
        SITE / "assets" / "js" / "renderer.js",
        SITE / "assets" / "js" / "components.js",
        SITE / "assets" / "js" / "widgets.js",
        SITE / "assets" / "js" / "data-store.js",
    ]
    forbidden_tokens = ["/AgenticCareerBoost", "didacll.github.io"]
    offenders: list[str] = []
    for path in runtime_files:
        text = path.read_text(encoding="utf-8")
        for token in forbidden_tokens:
            if token in text:
                offenders.append(f"{path.relative_to(ROOT).as_posix()}: {token}")
    assert offenders == []

    router = (SITE / "assets" / "js" / "router.js").read_text(encoding="utf-8")
    components = (SITE / "assets" / "js" / "components.js").read_text(encoding="utf-8")
    widgets = (SITE / "assets" / "js" / "widgets.js").read_text(encoding="utf-8")
    data_store = (SITE / "assets" / "js" / "data-store.js").read_text(encoding="utf-8")
    assert "new URL(import.meta.url)" in router
    assert "export function siteBasePath()" in router
    assert "redirectStaticFileRoute" in router
    assert 'pushState({}, "", routeHref(route))' in router
    assert "window.location.hash" not in components
    assert 'attrs.target = "_blank"' in components
    assert "routeHref(slide.route)" in widgets
    assert "resolveSiteUrl(slide.href || \"\")" in widgets
    assert "hashHref" not in widgets
    assert "hashHref" not in data_store


def test_site_404_discovers_deployment_base():
    fallback = (SITE / "404.html").read_text(encoding="utf-8")
    assert "candidateBases(normalizedPath)" in fallback
    assert "hasSiteContent(candidate)" in fallback
    assert "content/site.json" in fallback
    assert "routeForBase(normalizedPath, base)" in fallback
    assert "isStaticFileRoute(clean)" in fallback
    assert "File not found." in fallback
    assert "${window.location.origin}${base}#${route}" in fallback
    assert "/AgenticCareerBoost" not in fallback
    assert "didacll.github.io" not in fallback


def test_site_content_routes_remain_app_internal():
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
            key = pointer.rsplit(".", 1)[-1].split("[", 1)[0]
            if key not in {"route", "path"} or not isinstance(value, str):
                continue
            if not value.startswith("/"):
                failures.append(f"{json_file.name}:{pointer} route is not app-absolute: {value}")
            if value.startswith("/AgenticCareerBoost") or value.startswith("/site/"):
                failures.append(f"{json_file.name}:{pointer} route includes deployment base: {value}")
            if "didacll.github.io" in value:
                failures.append(f"{json_file.name}:{pointer} route includes deployment host: {value}")
    assert failures == []


def test_site_file_hrefs_are_not_app_routes():
    route_paths = {
        item["path"]
        for item in json.loads((SITE / "content" / "site.json").read_text(encoding="utf-8"))["routes"]
    }
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
            key = pointer.rsplit(".", 1)[-1].split("[", 1)[0]
            if not isinstance(value, str):
                continue
            if key == "route" and value.startswith("/files/"):
                failures.append(f"{json_file.name}:{pointer} file path used as route")
            if key == "href" and value.startswith("#/files/"):
                failures.append(f"{json_file.name}:{pointer} file href uses hash routing")
            if key == "href" and value.startswith("files/"):
                local = value.split("#", 1)[0].split("?", 1)[0]
                if value in route_paths:
                    failures.append(f"{json_file.name}:{pointer} file href collides with route")
                if not (SITE / local).is_file():
                    failures.append(f"{json_file.name}:{pointer} missing file href {value}")
    assert failures == []


def test_agentic_project_page_exposes_report_library():
    projects = json.loads((SITE / "content" / "projects.json").read_text(encoding="utf-8"))
    acb = next(item for item in projects["items"] if item["id"] == "agentic-career-boost")
    rendered_text = json.dumps(acb, ensure_ascii=False)
    for label in [
        "Bootstrap Launch",
        "Initial Growth",
        "Context Poisoning",
        "End of Semester Pause",
        "Failed Campaign Kickoff",
        "Cleanup And Current Version",
    ]:
        assert label in rendered_text
    assert "Documentation gaps" not in rendered_text

    expected_reports = {
        path.name
        for path in (SITE / "files" / "reports").glob("*.pdf")
    } | {"agenticcareerboost-project-history.pdf"}
    exposed_reports: set[str] = set()
    report_items: list[dict] = []

    def walk(node):
        if isinstance(node, dict):
            if isinstance(node.get("href"), str) and node["href"].endswith(".pdf"):
                report_items.append(node)
                exposed_reports.add(Path(node["href"]).name)
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)

    walk(acb)
    assert expected_reports <= exposed_reports
    assert report_items
    assert all(item.get("newTab") is True for item in report_items)
