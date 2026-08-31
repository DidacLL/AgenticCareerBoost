from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

TEX_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[4]
BUILD_DIR = TEX_ROOT / "build"
CATALOG = REPO_ROOT / "site" / "src" / "data" / "reports.json"
PUBLIC_REPORT_DIR = REPO_ROOT / "site" / "assets" / "files" / "reports"

def catalog_names() -> set[str]:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    return {str(item["file"]) for item in data}

def main(argv: list[str]) -> int:
    expected = catalog_names()
    available = {pdf.name: pdf for pdf in (Path(arg).resolve() for arg in argv[1:]) if pdf.suffix.lower() == ".pdf"} if len(argv) > 1 else {pdf.name: pdf for pdf in BUILD_DIR.glob("*.pdf")}
    missing = sorted(expected - available.keys())
    if missing:
        print("[publish-public-reports] Missing compiled public report PDFs: " + ", ".join(missing), file=sys.stderr)
        return 1
    PUBLIC_REPORT_DIR.mkdir(parents=True, exist_ok=True)
    for name in sorted(expected):
        shutil.copy2(available[name], PUBLIC_REPORT_DIR / name)
        print(f"[publish-public-reports] Published: site/assets/files/reports/{name}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
