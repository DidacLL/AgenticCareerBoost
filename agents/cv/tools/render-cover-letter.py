"""Render cover-letter TeX sources from explicit local JSON data."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CV_ROOT = ROOT / "agents" / "cv"
DEFAULT_TEMPLATE = CV_ROOT / "tex" / "cover-letter-template.tex"
DEFAULT_OUTPUT_DIR = CV_ROOT / "build" / "generated"

REQUIRED_STRINGS = [
    "slug",
    "output_pdf",
    "candidate_name",
    "headline",
    "email",
    "portfolio_url",
    "github_url",
    "linkedin_url",
    "recipient",
    "role",
    "location",
    "greeting",
    "closing",
    "public_note",
    "parser_summary",
]

LATEX_REPLACEMENTS = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}


def latex_escape(value: object) -> str:
    text = str(value)
    return "".join(LATEX_REPLACEMENTS.get(char, char) for char in text)


def safe_url(value: object) -> str:
    text = str(value).strip()
    if not text.startswith(("https://", "mailto:")):
        raise ValueError(f"unsupported URL value: {text}")
    if any(char in text for char in "{} \n\r\t"):
        raise ValueError(f"unsafe URL value: {text}")
    return text


def load_letter(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    missing = [key for key in REQUIRED_STRINGS if not str(data.get(key, "")).strip()]
    if missing:
        raise ValueError(f"{path}: missing required fields: {', '.join(missing)}")
    if not isinstance(data.get("paragraphs"), list) or not data["paragraphs"]:
        raise ValueError(f"{path}: paragraphs must be a non-empty list")
    if not isinstance(data.get("keywords"), list) or not data["keywords"]:
        raise ValueError(f"{path}: keywords must be a non-empty list")
    return data


def placeholder_map(data: dict) -> dict[str, str]:
    pdf_title = f"{data['candidate_name']} -- Cover Letter -- {data['role']}"
    pdf_subject = f"Cover letter for {data['role']}"
    paragraphs = "\n\n".join(latex_escape(item) for item in data["paragraphs"])
    return {
        "PDF_TITLE": latex_escape(pdf_title),
        "PDF_SUBJECT": latex_escape(pdf_subject),
        "PDF_KEYWORDS": latex_escape(", ".join(data["keywords"])),
        "CANDIDATE_NAME": latex_escape(data["candidate_name"]),
        "HEADLINE": latex_escape(data["headline"]),
        "EMAIL": latex_escape(data["email"]),
        "PORTFOLIO_URL": safe_url(data["portfolio_url"]),
        "GITHUB_URL": safe_url(data["github_url"]),
        "LINKEDIN_URL": safe_url(data["linkedin_url"]),
        "RECIPIENT": latex_escape(data["recipient"]),
        "ROLE": latex_escape(data["role"]),
        "LOCATION": latex_escape(data["location"]),
        "GREETING": latex_escape(data["greeting"]),
        "BODY_PARAGRAPHS": paragraphs,
        "CLOSING": latex_escape(data["closing"]),
        "PUBLIC_NOTE": latex_escape(data["public_note"]),
        "PARSER_SUMMARY": latex_escape(data["parser_summary"]),
    }


def render_letter(data_path: Path, template_path: Path, output_dir: Path) -> Path:
    data = load_letter(data_path)
    output_name = str(data["output_pdf"]).removesuffix(".pdf") + ".tex"
    output_path = output_dir / output_name
    output_dir.mkdir(parents=True, exist_ok=True)
    rendered = template_path.read_text(encoding="utf-8")
    for key, value in placeholder_map(data).items():
        rendered = rendered.replace(f"{{{{{key}}}}}", value)
    unresolved = [part.split("}}", 1)[0] for part in rendered.split("{{")[1:] if "}}" in part]
    if unresolved:
        raise ValueError(f"unresolved template placeholders: {', '.join(sorted(set(unresolved)))}")
    output_path.write_text(rendered, encoding="utf-8", newline="\n")
    return output_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="One cover-letter JSON file")
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output_path = render_letter(args.input.resolve(), args.template.resolve(), args.output_dir.resolve())
    print(f"rendered {output_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
