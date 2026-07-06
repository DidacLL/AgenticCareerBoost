from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
WORKFLOWS = ROOT / ".github" / "workflows"


def git_executable() -> str | None:
    found = shutil.which("git")
    if found:
        return found
    windows_git = Path("C:/Program Files/Git/cmd/git.exe")
    if windows_git.exists():
        return str(windows_git)
    return None


def test_public_site_pdfs_are_generated_not_tracked():
    git = git_executable()
    assert git is not None, "git executable is required for generated artifact validation"
    result = subprocess.run(
        [git, "ls-files", "site/files"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    tracked = [line for line in result.stdout.splitlines() if line.lower().endswith(".pdf")]
    assert tracked == []


def test_pages_and_required_ci_generate_public_report_pdfs_before_site_validation():
    for relative in ["required-ci.yml", "site-build.yml"]:
        text = (WORKFLOWS / relative).read_text(encoding="utf-8")
        compile_reports = text.index("Compile public report PDFs")
        publish_reports = text.index("Publish public report PDFs into site artifact")
        resolve_career = text.index("Resolve career artifact build inputs")
        compile_career = text.index("Compile public career PDFs")
        publish_career = text.index("Publish generated career PDFs into site artifact")
        generate_status = text.index("Generate site status data")
        validate_site = text.index("Validate static site")
        assert compile_reports < publish_reports < validate_site
        assert resolve_career < compile_career < publish_career < validate_site
        assert generate_status < validate_site
        assert "agents/reports/tex" in text
