"""Validate the plain static GitHub Pages source."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT / "site"
BASE_PATH = "/AgenticCareerBoost"

REQUIRED_FILES = [
    "index.html",
    "projects/index.html",
    "projects/agentic-career-boost/index.html",
    "projects/p3ctex/index.html",
    "projects/ironbank/index.html",
    "dashboard/index.html",
    "curriculum/index.html",
    "contact/index.html",
    "notes/index.html",
    "hire/index.html",
    "assets/css/site.css",
    "assets/js/cv.js",
    ".nojekyll",
]

REF_PATTERN = re.compile(r"""(?:href|src)=["']([^"']+)["']""")


def route_target(ref: str) -> Path | None:
    parsed = urlsplit(ref)
    if not parsed.path.startswith(f"{BASE_PATH}/") and parsed.path != f"{BASE_PATH}/":
        return None

    relative = unquote(parsed.path.removeprefix(BASE_PATH)) or "/"
    if relative.endswith("/"):
        relative = f"{relative}index.html"
    return (SITE / relative.lstrip("/")).resolve()


def html_files() -> list[Path]:
    return sorted(SITE.rglob("*.html"))


def main() -> int:
    failures: list[str] = []

    for required in REQUIRED_FILES:
        path = SITE / required
        if not path.is_file():
            failures.append(f"missing required file: site/{required}")

    ref_count = 0
    for html_file in html_files():
        text = html_file.read_text(encoding="utf-8")
        for match in REF_PATTERN.finditer(text):
            target = route_target(match.group(1))
            if target is None:
                continue
            ref_count += 1
            try:
                target.relative_to(SITE.resolve())
            except ValueError:
                failures.append(f"{html_file.relative_to(ROOT)} escapes site root: {match.group(1)}")
                continue
            if not target.is_file():
                failures.append(
                    f"{html_file.relative_to(ROOT)} references missing route: {match.group(1)}"
                )

    if failures:
        print("Static site validation failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(
        f"Static site validation passed: {len(REQUIRED_FILES)} required files, "
        f"{len(html_files())} HTML files, {ref_count} internal refs."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
