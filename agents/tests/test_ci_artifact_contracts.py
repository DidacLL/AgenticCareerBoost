from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
WORKFLOWS = ROOT / ".github" / "workflows"


def test_public_site_pdfs_are_generated_not_tracked():
    result = subprocess.run(
        ["git", "ls-files", "site/files"],
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
        validate_site = text.index("Validate static site")
        assert compile_reports < publish_reports < validate_site
        assert "agents/reports/tex" in text
