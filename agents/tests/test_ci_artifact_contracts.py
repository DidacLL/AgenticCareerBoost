from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
WORKFLOWS = ROOT / ".github" / "workflows"


def test_public_site_pdfs_are_generated_not_tracked():
    result = subprocess.run(
        ["git", "ls-files", "site/files/*.pdf", "site/files/**/*.pdf"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    tracked = [line for line in result.stdout.splitlines() if line.strip()]
    assert tracked == []


def test_public_site_pdf_paths_are_ignored_for_local_builds():
    result = subprocess.run(
        [
            "git",
            "check-ignore",
            "--no-index",
            "site/files/reports/example.pdf",
            "site/files/cv/example.pdf",
            "site/files/cover-letters/example.pdf",
        ],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    ignored = set(result.stdout.splitlines())
    assert ignored == {
        "site/files/reports/example.pdf",
        "site/files/cv/example.pdf",
        "site/files/cover-letters/example.pdf",
    }


def test_checkout_uses_latest_ref_without_numbered_version():
    offenders: list[str] = []
    for workflow in WORKFLOWS.glob("*.yml"):
        text = workflow.read_text(encoding="utf-8")
        if "actions/checkout@v" in text:
            offenders.append(workflow.relative_to(ROOT).as_posix())
        if "actions/checkout" in text and "actions/checkout@main" not in text:
            offenders.append(workflow.relative_to(ROOT).as_posix())
    assert sorted(set(offenders)) == []


def test_pages_and_required_ci_generate_public_report_pdfs_before_site_validation():
    for relative in ["required-ci.yml", "site-build.yml"]:
        text = (WORKFLOWS / relative).read_text(encoding="utf-8")
        compile_reports = text.index("Compile public report PDFs")
        publish_reports = text.index("Publish public report PDFs into site artifact")
        validate_site = text.index("Validate static site")
        assert compile_reports < publish_reports < validate_site
        assert "agents/reports/tex" in text
        assert "site/files/reports" in text
