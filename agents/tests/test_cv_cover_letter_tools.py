from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]


def load_tool_module(name: str, relative: str):
    path = ROOT / "agents" / "cv" / "tools" / relative
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_cover_letter_output_pdf_must_be_plain_filename():
    module = load_tool_module("render_cover_letter", "render-cover-letter.py")

    assert module.safe_output_tex_name("letter.pdf") == "letter.tex"
    assert module.safe_output_tex_name("letter") == "letter.tex"

    for value in ["", "../letter.pdf", "nested/letter.pdf", "nested\\letter.pdf"]:
        with pytest.raises(ValueError, match="output_pdf must be a plain filename"):
            module.safe_output_tex_name(value)


def test_public_manifest_rejects_published_cover_letters(tmp_path):
    module = load_tool_module("artifact_manifest", "artifact_manifest.py")
    manifest = tmp_path / "artifacts.json"
    manifest.write_text(
        json.dumps(
            {
                "artifacts": [
                    {
                        "kind": "cover-letter",
                        "publish": True,
                        "data": "data/private.json",
                        "source": "build/generated/private.tex",
                        "buildPdf": "build/private.pdf",
                        "sitePdf": "site/files/" + "cover-letters/private.pdf",
                    }
                ]
            }
        ),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="cover letters are private/local working documents"):
        module.public_artifacts(manifest)
