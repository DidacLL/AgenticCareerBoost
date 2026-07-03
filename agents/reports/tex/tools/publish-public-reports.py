from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path


TEX_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[4]
BUILD_DIR = TEX_ROOT / "build"
SITE_ROOT = REPO_ROOT / "site"
PUBLIC_REPORT_DIR = SITE_ROOT / "files" / "reports"


def walk_json(node):
    if isinstance(node, dict):
        for value in node.values():
            yield from walk_json(value)
    elif isinstance(node, list):
        for value in node:
            yield from walk_json(value)
    else:
        yield node


def linked_report_names() -> set[str]:
    names: set[str] = set()
    for json_file in (SITE_ROOT / "content").glob("*.json"):
        data = json.loads(json_file.read_text(encoding="utf-8"))
        for value in walk_json(data):
            if not isinstance(value, str):
                continue
            local = value.split("#", 1)[0].split("?", 1)[0]
            if local.startswith("files/reports/") and local.lower().endswith(".pdf"):
                names.add(Path(local).name)
    return names


def selected_pdfs(args: list[str]) -> list[Path]:
    if args:
        return [Path(arg).resolve() for arg in args]
    return sorted(BUILD_DIR.glob("*.pdf"))


def main(argv: list[str]) -> int:
    expected = linked_report_names()
    if not expected:
        print("[publish-public-reports] No public report PDF links declared in site/content/.")
        return 0

    available = {pdf.name: pdf for pdf in selected_pdfs(argv[1:]) if pdf.suffix.lower() == ".pdf"}
    missing = sorted(expected - available.keys())
    if missing:
        print("[publish-public-reports] Missing compiled public report PDFs: " + ", ".join(missing), file=sys.stderr)
        return 1

    PUBLIC_REPORT_DIR.mkdir(parents=True, exist_ok=True)
    for name in sorted(expected):
        destination = PUBLIC_REPORT_DIR / name
        shutil.copy2(available[name], destination)
        print(f"[publish-public-reports] Published: site/files/reports/{name}")

    print(f"[publish-public-reports] Public report PDFs published: {len(expected)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
