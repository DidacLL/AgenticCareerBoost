"""Export public site status from non-authoritative state evidence."""

from __future__ import annotations

import json
import os
import re
from pathlib import Path


def repo_root() -> Path:
    override = os.environ.get("ACB_REPO_ROOT")
    if override:
        return Path(override).resolve()
    return Path(__file__).resolve().parents[2]


ROOT = repo_root()
AGENTS = Path(os.environ.get("ACB_AGENT_ROOT", ROOT / "agents")).resolve()
SITE = Path(os.environ.get("ACB_SITE_ROOT", ROOT / "site")).resolve()
STATE = AGENTS / "state"
OUT = SITE / "data" / "status.json"


def read_state(name: str) -> str:
    return (STATE / name).read_text(encoding="utf-8")


def field(text: str, label: str) -> str:
    match = re.search(rf"\*\*{re.escape(label)}\*\*:\s*(.+)", text)
    return match.group(1).strip() if match else ""


def none_like(value: str) -> bool:
    return value.strip().lower() in {"", "none", "null", "n/a"}


def blockers(value: str) -> list[str]:
    value = value.strip()
    if none_like(value) or value.lower().startswith("none for "):
        return []
    return [part.strip().rstrip(".") for part in value.split(";") if part.strip()]


def next_seed(roadmap: str) -> str:
    for sprint_id, title, focus in re.findall(
        r"\|\s*(S-\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", roadmap
    ):
        if "closed" not in focus.lower():
            return f"{sprint_id}: {title.strip()}"
    return ""


def recent_closure(current: str) -> tuple[str, str]:
    match = re.search(r"\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*([^|]+?)\s*\|", current)
    if not match:
        return "unknown", "unknown"
    return match.group(1), match.group(2).strip()


def main() -> int:
    current = read_state("current.md")
    active = read_state("active-sprint.md")
    roadmap = read_state("roadmap.md")

    active_sprint = field(current, "Active sprint")
    sprint_id = None if none_like(active_sprint) else field(active, "Sprint ID")
    last_at, last_type = recent_closure(current)

    payload = {
        "schema_version": 2,
        "sources": [
            "agents/state/current.md",
            "agents/state/active-sprint.md",
            "agents/state/roadmap.md",
        ],
        "workflow": field(current, "Active workflow") or "none",
        "sprint_id": sprint_id,
        "status": field(active, "Status") if sprint_id else "idle",
        "last_closure_at": last_at,
        "last_closure_type": last_type,
        "blockers": blockers(field(current, "Repo-local blockers")),
        "next_sprint_seed": next_seed(roadmap),
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
