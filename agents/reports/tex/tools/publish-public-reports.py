from __future__ import annotations

import shutil
import sys
from pathlib import Path


TEX_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[4]
BUILD_DIR = TEX_ROOT / "build"
PUBLIC_REPORT_DIR = REPO_ROOT / "site" / "files" / "reports"

PRIVATE_PDF_NAMES = {"smoke.pdf"}
PRIVATE_PDF_PREFIXES = ("candidaturas_",)


def is_public_report_pdf(path: Path) -> bool:
    name = path.name
    return (
        path.suffix.lower() == ".pdf"
        and name not in PRIVATE_PDF_NAMES
        and not any(name.startswith(prefix) for prefix in PRIVATE_PDF_PREFIXES)
    )


def selected_pdfs(args: list[str]) -> list[Path]:
    if args:
        return [Path(arg).resolve() for arg in args]
    return sorted(BUILD_DIR.glob("*.pdf"))


def main(argv: list[str]) -> int:
    pdfs = selected_pdfs(argv[1:])
    if not pdfs:
        print("[publish-public-reports] No PDFs found to publish.")
        return 0

    PUBLIC_REPORT_DIR.mkdir(parents=True, exist_ok=True)
    published = 0
    for pdf in pdfs:
        if not pdf.is_file():
            print(f"[publish-public-reports] Missing PDF: {pdf}", file=sys.stderr)
            return 1
        if not is_public_report_pdf(pdf):
            continue
        destination = PUBLIC_REPORT_DIR / pdf.name
        shutil.copy2(pdf, destination)
        published += 1
        print(f"[publish-public-reports] Published: site/files/reports/{pdf.name}")

    print(f"[publish-public-reports] Public report PDFs published: {published}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
