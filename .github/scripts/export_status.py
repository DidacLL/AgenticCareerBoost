"""Parse state files and write public status JSON artifacts."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ROOT_STATUS = ROOT / "data" / "public-status.json"
SITE_STATUS = ROOT / "site" / "assets" / "data" / "public-status.json"
STATUS_SOURCES = [
    "state/current.md",
    "state/active-sprint.md",
    "state/roadmap.md",
]


def extract_field(text: str, field: str) -> str:
    match = re.search(rf"\*\*{field}\*\*:\s*(.+)", text)
    return match.group(1).strip() if match else ""


def is_none_like(value: str) -> bool:
    normalized = value.strip().lower()
    return normalized in {"", "none", "null", "n/a"}


def extract_closure_artifacts(text: str) -> list[dict[str, str | bool]]:
    artifacts = []
    in_section = False
    for line in text.splitlines():
        if line.strip() == "## Closure artifacts":
            in_section = True
            continue
        if in_section and line.startswith("## "):
            break
        match = re.match(r"- \[(x| )\]\s+(.+)", line)
        if not match:
            continue
        checked = match.group(1) == "x"
        label = match.group(2).strip()
        artifacts.append({"complete": checked, "label": label})
    if artifacts:
        return artifacts

    in_section = False
    for line in text.splitlines():
        if line.strip() == "## Closure matrix":
            in_section = True
            continue
        if in_section and line.startswith("## "):
            break
        if not in_section:
            continue
        match = re.match(r"\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", line)
        if not match:
            continue
        dimension, state, evidence = (part.strip() for part in match.groups())
        if dimension in {"Dimension", "---"} or set(dimension) == {"-"}:
            continue
        state_normalized = state.lower()
        complete = state_normalized in {"done", "complete", "completed", "pass", "passed", "closed"}
        artifacts.append(
            {
                "complete": complete,
                "label": f"{dimension} — {state}: {evidence}",
            }
        )
    return artifacts


def split_blockers(value: str) -> list[str]:
    normalized = value.strip().lower()
    if normalized in ("none", "") or normalized.startswith("none for "):
        return []
    return [part.strip().rstrip(".") for part in value.split(";") if part.strip()]


def status_updated_at(current_text: str) -> str:
    closures = re.findall(r"\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*[^|]+?\s*\|", current_text)
    if closures:
        return closures[0]
    sprint_id = extract_field((ROOT / "state" / "active-sprint.md").read_text(encoding="utf-8"), "Sprint ID")
    return sprint_id or "unknown"


def main() -> None:
    current = (ROOT / "state" / "current.md").read_text(encoding="utf-8")
    sprint = (ROOT / "state" / "active-sprint.md").read_text(encoding="utf-8")

    workflow = extract_field(current, "Active workflow") or "none"
    active_sprint = extract_field(current, "Active sprint")
    sprint_id = None if is_none_like(active_sprint) else extract_field(sprint, "Sprint ID")
    status_raw = extract_field(sprint, "Status") if sprint_id else "idle"
    status = status_raw or "idle"

    closures = re.findall(
        r"\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*([^|]+?)\s*\|", current
    )
    last_closure_at = closures[0][0] if closures else "unknown"
    last_closure_type = closures[0][1] if closures else "unknown"

    blockers = split_blockers(extract_field(current, "Blockers"))

    roadmap = (ROOT / "state" / "roadmap.md").read_text(encoding="utf-8")
    next_seed = ""
    for sprint_id_match, title, focus in re.findall(
        r"\|\s*(S-\d+)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|", roadmap
    ):
        if "closed" in focus.lower():
            continue
        next_seed = f"{sprint_id_match}: {title}"
        break

    payload = {
        "schema_version": 1,
        "updated": status_updated_at(current),
        "sources": STATUS_SOURCES,
        "sprint_id": sprint_id,
        "workflow": workflow,
        "status": status,
        "last_closure_at": last_closure_at,
        "last_closure_type": last_closure_type,
        "artifacts": extract_closure_artifacts(sprint),
        "blockers": blockers,
        "next_sprint_seed": next_seed,
    }

    serialized = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    for out in (ROOT_STATUS, SITE_STATUS):
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(serialized, encoding="utf-8")
        print(f"Wrote {out}")


if __name__ == "__main__":
    main()
