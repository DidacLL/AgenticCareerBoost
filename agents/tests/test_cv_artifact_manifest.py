from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]


def load_manifest_module():
    path = ROOT / "agents" / "cv" / "tools" / "artifact_manifest.py"
    spec = importlib.util.spec_from_file_location("artifact_manifest", path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_public_manifest_rejects_non_cv_public_artifacts(tmp_path):
    module = load_manifest_module()
    manifest = tmp_path / "artifacts.json"
    manifest.write_text(
        json.dumps(
            {
                "artifacts": [
                    {
                        "kind": "letter",
                        "publish": True,
                        "source": "build/generated/example.tex",
                        "buildPdf": "build/example.pdf",
                        "sitePdf": "site/files/example.pdf",
                    }
                ]
            }
        ),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="unsupported public artifact kind"):
        module.public_artifacts(manifest)
