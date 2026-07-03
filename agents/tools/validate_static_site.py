"""Validate the canonical site/ Pages artifact."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path


def repo_root() -> Path:
    override = os.environ.get("ACB_REPO_ROOT")
    if override:
        return Path(override).resolve()
    return Path(__file__).resolve().parents[2]


ROOT = repo_root()
SITE = Path(os.environ.get("ACB_SITE_ROOT", ROOT / "site")).resolve()

REQUIRED = [
    "index.html",
    "404.html",
    ".nojekyll",
    "manifest.json",
    "assets/css/site.css",
    "assets/js/os.js",
    "assets/js/data-store.js",
    "assets/js/router.js",
    "assets/js/renderer.js",
    "assets/js/components.js",
    "assets/js/widgets.js",
    "content/site.json",
    "content/pages.json",
    "content/projects.json",
    "content/blog.json",
    "content/cv.json",
    "content/fragments/legal-disclosure.html",
    "data/status.json",
]

RUNTIME_FILES = [
    "index.html",
    "404.html",
    "assets/js/os.js",
    "assets/js/router.js",
    "assets/js/renderer.js",
    "assets/js/components.js",
    "assets/js/widgets.js",
    "assets/js/data-store.js",
]

FORBIDDEN_DEPLOYMENT_TOKENS = [
    "/AgenticCareerBoost",
    "didacll.github.io",
]

CANONICAL_CV_SOURCE = "agents/cv/tex/didac-llorens-cv.tex"
CANONICAL_CV_SOURCE_URL = f"https://github.com/DidacLL/AgenticCareerBoost/blob/main/{CANONICAL_CV_SOURCE}"

CV_REQUIRED = [
    "README.md",
    "latexmkrc",
    "build-local.sh",
    "build-local.ps1",
    "tex/didac-llorens-cv.tex",
    "tex/cover-letter-template.tex",
    "tools/render-cover-letter.py",
    "data/examples/assaia.json",
]

HIDDEN_LATEX_TOKENS = [
    r"\textcolor{white}",
    r"\resizebox{0pt}",
    r"\transparent{0}",
    r"\phantom",
    "opacity=0",
]


def git_executable() -> str | None:
    found = shutil.which("git")
    if found:
        return found
    windows_git = Path("C:/Program Files/Git/cmd/git.exe")
    if windows_git.exists():
        return str(windows_git)
    return None


def main() -> int:
    failures: list[str] = []

    for relative in REQUIRED:
        if not (SITE / relative).is_file():
            failures.append(f"missing site artifact file: site/{relative}")

    index = SITE / "index.html"
    if index.is_file():
        text = index.read_text(encoding="utf-8")
        for token in ("assets/css/site.css", "assets/js/os.js", "manifest.json"):
            if token not in text:
                failures.append(f"site/index.html missing {token}")

    for relative in RUNTIME_FILES:
        path = SITE / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for token in FORBIDDEN_DEPLOYMENT_TOKENS:
            if token in text:
                failures.append(f"site/{relative} hardcodes deployment path/token: {token}")

    router = SITE / "assets" / "js" / "router.js"
    components = SITE / "assets" / "js" / "components.js"
    widgets = SITE / "assets" / "js" / "widgets.js"
    data_store = SITE / "assets" / "js" / "data-store.js"
    if router.is_file():
        router_text = router.read_text(encoding="utf-8")
        if "new URL(import.meta.url)" not in router_text:
            failures.append("site/assets/js/router.js must derive deployment base from import.meta.url")
        if 'pushState({}, "", routeHref(route))' not in router_text:
            failures.append("site/assets/js/router.js must push base-aware routeHref(route)")
    if components.is_file():
        components_text = components.read_text(encoding="utf-8")
        if "window.location.hash" in components_text:
            failures.append("site/assets/js/components.js must not bypass router with window.location.hash")
    fallback = SITE / "404.html"
    if fallback.is_file():
        fallback_text = fallback.read_text(encoding="utf-8")
        for token in (
            "candidateBases(normalizedPath)",
            "hasSiteContent(candidate)",
            "content/site.json",
            "routeForBase(normalizedPath, base)",
            "${window.location.origin}${base}#${route}",
        ):
            if token not in fallback_text:
                failures.append(f"site/404.html missing deployment-base discovery marker: {token}")
    if widgets.is_file():
        widgets_text = widgets.read_text(encoding="utf-8")
        if "routeHref(slide.route)" not in widgets_text:
            failures.append("site/assets/js/widgets.js must use routeHref for gallery route links")
        if "hashHref" in widgets_text:
            failures.append("site/assets/js/widgets.js must not generate hash route hrefs")
    if data_store.is_file() and "hashHref" in data_store.read_text(encoding="utf-8"):
        failures.append("site/assets/js/data-store.js must not expose a second internal route href helper")

    cv_root = ROOT / "agents" / "cv"
    for relative in CV_REQUIRED:
        if not (cv_root / relative).is_file():
            failures.append(f"missing CV artifact source file: agents/cv/{relative}")

    for path in (cv_root / "tex").glob("*.tex") if (cv_root / "tex").is_dir() else []:
        text = path.read_text(encoding="utf-8")
        for token in HIDDEN_LATEX_TOKENS:
            if token in text:
                failures.append(f"{path.relative_to(ROOT).as_posix()} contains hidden parser-text token: {token}")

    cv_pdf = SITE / "files" / "cv" / "didac-llorens-cv.pdf"
    if not cv_pdf.is_file():
        failures.append("missing generated public CV PDF: site/files/cv/didac-llorens-cv.pdf")

    cover_letter_dir = SITE / "files" / "cover-letters"
    if not cover_letter_dir.is_dir() or not list(cover_letter_dir.glob("*.pdf")):
        failures.append("missing generated public cover-letter PDF in site/files/cover-letters/")

    for relative in ("site.json", "pages.json", "projects.json", "blog.json", "cv.json"):
        path = SITE / "content" / relative
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            failures.append(f"site/content/{relative} invalid JSON: {exc}")

    cv_json = SITE / "content" / "cv.json"
    if cv_json.is_file():
        cv_text = cv_json.read_text(encoding="utf-8")
        if CANONICAL_CV_SOURCE_URL not in cv_text:
            failures.append("site/content/cv.json must link the canonical agents/cv CV source")
        if "DidacLL_SoftwareEngineer_CV.site-legacy.tex" in cv_text:
            failures.append("site/content/cv.json must not link the legacy CV source")

    for relative in ("cv.json", "projects.json"):
        path = SITE / "content" / relative
        if path.is_file():
            text = path.read_text(encoding="utf-8")
            stale_site_curriculum = "site/assets/" + "curriculum/"
            for token in ("assets/curriculum/", stale_site_curriculum, "DidacLL_SoftwareEngineer_CV.site-legacy.tex"):
                if token in text:
                    failures.append(f"site/content/{relative} contains stale CV/curriculum token: {token}")

    git = git_executable()
    if git is None:
        failures.append("git executable is required for generated CV artifact validation")
    else:
        tracked = subprocess.run(
            [git, "ls-files", "site/files/cv/*.pdf", "site/files/cover-letters/*.pdf", "agents/reports/tex/guides/*cv*.pdf"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.splitlines()
        if tracked:
            failures.append(f"generated CV/cover-letter PDFs must not be tracked: {', '.join(tracked)}")
        ignored = subprocess.run(
            [git, "check-ignore", "--no-index", "site/files/cv/didac-llorens-cv.pdf", "site/files/cover-letters/assaia-ml-core-cover-letter.pdf"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        ).stdout.splitlines()
        expected_ignored = {"site/files/cv/didac-llorens-cv.pdf", "site/files/cover-letters/assaia-ml-core-cover-letter.pdf"}
        if set(ignored) != expected_ignored:
            failures.append("generated CV/cover-letter PDF paths must be ignored by .gitignore")

    if failures:
        print("Static site validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Static site validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
