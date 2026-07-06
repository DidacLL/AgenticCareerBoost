"""Local SQLite application tracker with an HTML dashboard."""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import sqlite3
from datetime import date, datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

TRACKER_ROOT = Path(__file__).resolve().parent
REPO_ROOT = TRACKER_ROOT.parent
DEFAULT_HOME = TRACKER_ROOT / ".private"
DB_NAME = "applications.sqlite"
STATUSES = [
    "found",
    "evaluating",
    "ready_to_apply",
    "applied",
    "follow_up",
    "interview",
    "technical_test",
    "offer",
    "rejected",
    "rejected_by_me",
    "archived",
]


def private_home() -> Path:
    configured = os.environ.get("ACB_APPLICATION_TRACKER_HOME")
    path = Path(configured).expanduser() if configured else DEFAULT_HOME
    return path.resolve()


def assert_safe_home(path: Path) -> None:
    resolved = path.resolve()
    try:
        resolved.relative_to(REPO_ROOT.resolve())
    except ValueError:
        return
    try:
        resolved.relative_to(DEFAULT_HOME.resolve())
    except ValueError as exc:
        raise SystemExit(
            "Application Tracker data inside this repository must stay under "
            "application-tracker/.private/. Set ACB_APPLICATION_TRACKER_HOME for an external store."
        ) from exc


def db_path() -> Path:
    home = private_home()
    assert_safe_home(home)
    return home / DB_NAME


def connect() -> sqlite3.Connection:
    path = db_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db() -> None:
    home = private_home()
    assert_safe_home(home)
    (home / "attachments").mkdir(parents=True, exist_ok=True)
    (home / "generated").mkdir(parents=True, exist_ok=True)
    with connect() as conn:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS applications (
                id TEXT PRIMARY KEY,
                company TEXT NOT NULL,
                role TEXT NOT NULL,
                source TEXT,
                source_url TEXT,
                location TEXT,
                remote_mode TEXT,
                status TEXT NOT NULL DEFAULT 'found',
                priority TEXT NOT NULL DEFAULT 'medium',
                created_at TEXT NOT NULL,
                applied_at TEXT,
                last_touch TEXT NOT NULL,
                next_action TEXT,
                notes TEXT
            );

            CREATE TABLE IF NOT EXISTS offer_snapshots (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                application_id TEXT NOT NULL REFERENCES applications(id) ON DELETE CASCADE,
                raw_text TEXT NOT NULL,
                cleaned_text TEXT,
                captured_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS company_research (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                application_id TEXT REFERENCES applications(id) ON DELETE CASCADE,
                company TEXT NOT NULL,
                summary TEXT,
                business_model TEXT,
                red_flags TEXT,
                sources_json TEXT,
                updated_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS evaluations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                application_id TEXT NOT NULL REFERENCES applications(id) ON DELETE CASCADE,
                verdict TEXT,
                fit_score INTEGER,
                risk_score INTEGER,
                effort_score INTEGER,
                reasoning TEXT,
                created_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS form_answers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                application_id TEXT NOT NULL REFERENCES applications(id) ON DELETE CASCADE,
                question TEXT NOT NULL,
                draft_answer TEXT,
                submitted_answer TEXT,
                submitted_at TEXT
            );

            CREATE TABLE IF NOT EXISTS cover_letters (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                application_id TEXT NOT NULL REFERENCES applications(id) ON DELETE CASCADE,
                draft_text TEXT,
                submitted_text TEXT,
                version TEXT,
                created_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS interview_guides (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                application_id TEXT NOT NULL REFERENCES applications(id) ON DELETE CASCADE,
                guide_text TEXT NOT NULL,
                created_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS stack_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                application_id TEXT NOT NULL REFERENCES applications(id) ON DELETE CASCADE,
                term TEXT NOT NULL,
                meaning TEXT,
                why_it_matters TEXT,
                my_positioning TEXT,
                refresh_needed INTEGER NOT NULL DEFAULT 0
            );
            """
        )
    print(f"initialized {db_path()}")


def slugify(value: str) -> str:
    text = value.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "application"


def make_id(company: str, role: str) -> str:
    base = f"{date.today().isoformat()}-{slugify(company)}-{slugify(role)}"
    candidate = base
    with connect() as conn:
        index = 2
        while conn.execute("SELECT 1 FROM applications WHERE id = ?", (candidate,)).fetchone():
            candidate = f"{base}-{index}"
            index += 1
    return candidate


def create_application(args: argparse.Namespace) -> None:
    init_db()
    now = datetime.now().isoformat(timespec="seconds")
    app_id = args.id or make_id(args.company, args.role)
    with connect() as conn:
        conn.execute(
            """
            INSERT INTO applications (
                id, company, role, source, source_url, location, remote_mode,
                status, priority, created_at, last_touch, next_action, notes
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                app_id,
                args.company,
                args.role,
                args.source,
                args.source_url,
                args.location,
                args.remote_mode,
                args.status,
                args.priority,
                now,
                now,
                args.next_action,
                args.notes,
            ),
        )
    print(app_id)


def read_text_arg(value: str | None, file_value: str | None) -> str:
    if file_value:
        return Path(file_value).read_text(encoding="utf-8")
    if value is None:
        raise SystemExit("provide --text or --file")
    return value


def ingest_offer(args: argparse.Namespace) -> None:
    init_db()
    text = read_text_arg(args.text, args.file)
    now = datetime.now().isoformat(timespec="seconds")
    with connect() as conn:
        require_app(conn, args.id)
        conn.execute(
            "INSERT INTO offer_snapshots(application_id, raw_text, cleaned_text, captured_at) VALUES (?, ?, ?, ?)",
            (args.id, text, args.cleaned_text, now),
        )
        touch(conn, args.id, args.next_action)
    print(f"stored offer snapshot for {args.id}")


def update_application(args: argparse.Namespace) -> None:
    init_db()
    updates = []
    values: list[object] = []
    for field in ["status", "priority", "next_action", "notes", "applied_at"]:
        value = getattr(args, field)
        if value is not None:
            updates.append(f"{field} = ?")
            values.append(value)
    updates.append("last_touch = ?")
    values.append(datetime.now().isoformat(timespec="seconds"))
    values.append(args.id)
    with connect() as conn:
        require_app(conn, args.id)
        conn.execute(f"UPDATE applications SET {', '.join(updates)} WHERE id = ?", values)
    print(f"updated {args.id}")


def add_text(args: argparse.Namespace) -> None:
    init_db()
    text = read_text_arg(args.text, args.file)
    now = datetime.now().isoformat(timespec="seconds")
    with connect() as conn:
        require_app(conn, args.id)
        if args.kind == "evaluation":
            conn.execute(
                "INSERT INTO evaluations(application_id, verdict, fit_score, risk_score, effort_score, reasoning, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (args.id, args.verdict, args.fit_score, args.risk_score, args.effort_score, text, now),
            )
        elif args.kind == "cover-letter":
            conn.execute(
                "INSERT INTO cover_letters(application_id, draft_text, submitted_text, version, created_at) VALUES (?, ?, ?, ?, ?)",
                (args.id, text, args.submitted_text, args.version, now),
            )
        elif args.kind == "interview-guide":
            conn.execute(
                "INSERT INTO interview_guides(application_id, guide_text, created_at) VALUES (?, ?, ?)",
                (args.id, text, now),
            )
        touch(conn, args.id, args.next_action)
    print(f"stored {args.kind} for {args.id}")


def require_app(conn: sqlite3.Connection, app_id: str) -> sqlite3.Row:
    row = conn.execute("SELECT * FROM applications WHERE id = ?", (app_id,)).fetchone()
    if row is None:
        raise SystemExit(f"unknown application: {app_id}")
    return row


def touch(conn: sqlite3.Connection, app_id: str, next_action: str | None = None) -> None:
    if next_action is None:
        conn.execute("UPDATE applications SET last_touch = ? WHERE id = ?", (datetime.now().isoformat(timespec="seconds"), app_id))
    else:
        conn.execute(
            "UPDATE applications SET last_touch = ?, next_action = ? WHERE id = ?",
            (datetime.now().isoformat(timespec="seconds"), next_action, app_id),
        )


def list_applications(args: argparse.Namespace) -> None:
    init_db()
    query = "SELECT * FROM applications"
    values: list[object] = []
    clauses = []
    if args.status:
        clauses.append("status = ?")
        values.append(args.status)
    if args.search:
        clauses.append("(company LIKE ? OR role LIKE ? OR notes LIKE ?)")
        pattern = f"%{args.search}%"
        values.extend([pattern, pattern, pattern])
    if clauses:
        query += " WHERE " + " AND ".join(clauses)
    query += " ORDER BY created_at DESC"
    with connect() as conn:
        rows = conn.execute(query, values).fetchall()
    for row in rows:
        print(f"{row['status']:14} {row['priority']:7} {row['id']} :: {row['company']} — {row['role']}")


def application_payload() -> dict:
    init_db()
    with connect() as conn:
        applications = [dict(row) for row in conn.execute("SELECT * FROM applications ORDER BY created_at DESC")]
        counts = {
            row["status"]: row["total"]
            for row in conn.execute("SELECT status, COUNT(*) AS total FROM applications GROUP BY status")
        }
        latest_text = {}
        for table, key, field in [
            ("evaluations", "evaluation", "reasoning"),
            ("cover_letters", "cover_letter", "draft_text"),
            ("interview_guides", "interview_guide", "guide_text"),
        ]:
            rows = conn.execute(
                f"SELECT application_id, {field} AS value, MAX(id) AS latest_id FROM {table} GROUP BY application_id"
            ).fetchall()
            for row in rows:
                latest_text.setdefault(row["application_id"], {})[key] = row["value"]
    for item in applications:
        item["texts"] = latest_text.get(item["id"], {})
    return {"generated_at": datetime.now().isoformat(timespec="seconds"), "statuses": STATUSES, "counts": counts, "applications": applications}


def dashboard_html(payload: dict) -> str:
    data = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    return f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
  <title>Application Tracker</title>
  <style>
    :root {{ font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, \"Segoe UI\", sans-serif; color: #111827; background: #f8fafc; }}
    body {{ margin: 0; }}
    header {{ padding: 1.2rem 1.4rem; background: #111827; color: white; }}
    main {{ padding: 1rem; display: grid; gap: 1rem; }}
    .toolbar {{ display: flex; gap: .75rem; flex-wrap: wrap; align-items: center; }}
    input, select {{ padding: .55rem .65rem; border: 1px solid #cbd5e1; border-radius: .55rem; background: white; }}
    .board {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: .85rem; }}
    .column {{ background: #e5e7eb; border-radius: .85rem; padding: .7rem; min-height: 10rem; }}
    .column h2 {{ font-size: .86rem; text-transform: uppercase; letter-spacing: .08em; color: #334155; margin: .2rem .15rem .65rem; }}
    .card {{ background: white; border: 1px solid #dbe3ef; border-radius: .75rem; padding: .75rem; margin-bottom: .65rem; box-shadow: 0 1px 2px rgba(15, 23, 42, .06); cursor: pointer; }}
    .card h3 {{ margin: 0 0 .25rem; font-size: .95rem; }}
    .meta {{ color: #64748b; font-size: .82rem; }}
    .detail {{ background: white; border: 1px solid #dbe3ef; border-radius: .85rem; padding: 1rem; }}
    .detail h2 {{ margin-top: 0; }}
    pre {{ white-space: pre-wrap; background: #f1f5f9; padding: .8rem; border-radius: .65rem; overflow: auto; }}
    .empty {{ color: #64748b; font-style: italic; }}
  </style>
</head>
<body>
<header>
  <h1>Application Tracker</h1>
  <div>Generated {html.escape(payload['generated_at'])}</div>
</header>
<main>
  <section class=\"toolbar\">
    <input id=\"search\" type=\"search\" placeholder=\"Search company, role, notes\">
    <select id=\"status\"><option value=\"\">All statuses</option></select>
  </section>
  <section id=\"board\" class=\"board\"></section>
  <section id=\"detail\" class=\"detail\"><p class=\"empty\">Select an application.</p></section>
</main>
<script type=\"application/json\" id=\"payload\">{data}</script>
<script>
const payload = JSON.parse(document.getElementById('payload').textContent);
const board = document.getElementById('board');
const detail = document.getElementById('detail');
const search = document.getElementById('search');
const statusFilter = document.getElementById('status');
for (const status of payload.statuses) {{
  const option = document.createElement('option');
  option.value = status;
  option.textContent = `${{status}} (${{payload.counts[status] || 0}})`;
  statusFilter.appendChild(option);
}}
function matches(app) {{
  const needle = search.value.trim().toLowerCase();
  if (statusFilter.value && app.status !== statusFilter.value) return false;
  if (!needle) return true;
  return [app.company, app.role, app.notes, app.next_action].some(value => String(value || '').toLowerCase().includes(needle));
}}
function renderBoard() {{
  board.textContent = '';
  const visible = payload.applications.filter(matches);
  for (const status of payload.statuses) {{
    const column = document.createElement('section');
    column.className = 'column';
    const title = document.createElement('h2');
    title.textContent = status;
    column.appendChild(title);
    for (const app of visible.filter(item => item.status === status)) {{
      const card = document.createElement('article');
      card.className = 'card';
      card.innerHTML = `<h3>${{escapeHtml(app.company)}} — ${{escapeHtml(app.role)}}</h3>
        <div class=\"meta\">${{escapeHtml(app.priority)}} · ${{escapeHtml(app.last_touch || '')}}</div>
        <div class=\"meta\">${{escapeHtml(app.next_action || 'No next action')}}</div>`;
      card.addEventListener('click', () => renderDetail(app));
      column.appendChild(card);
    }}
    board.appendChild(column);
  }}
}}
function renderDetail(app) {{
  const texts = app.texts || {{}};
  detail.innerHTML = `<h2>${{escapeHtml(app.company)}} — ${{escapeHtml(app.role)}}</h2>
    <p><strong>Status:</strong> ${{escapeHtml(app.status)}} · <strong>Priority:</strong> ${{escapeHtml(app.priority)}}</p>
    <p><strong>Source:</strong> ${{escapeHtml(app.source || '')}} ${{app.source_url ? `<a href=\"${{escapeAttr(app.source_url)}}\" target=\"_blank\" rel=\"noreferrer\">open</a>` : ''}}</p>
    <p><strong>Location:</strong> ${{escapeHtml(app.location || '')}} · <strong>Remote:</strong> ${{escapeHtml(app.remote_mode || '')}}</p>
    <p><strong>Next action:</strong> ${{escapeHtml(app.next_action || '')}}</p>
    <p><strong>Notes:</strong> ${{escapeHtml(app.notes || '')}}</p>
    <h3>Evaluation</h3><pre>${{escapeHtml(texts.evaluation || 'No evaluation stored.')}}</pre>
    <h3>Cover letter</h3><pre>${{escapeHtml(texts.cover_letter || 'No cover letter stored.')}}</pre>
    <h3>Interview guide</h3><pre>${{escapeHtml(texts.interview_guide || 'No interview guide stored.')}}</pre>`;
}}
function escapeHtml(value) {{
  return String(value ?? '').replace(/[&<>\"]/g, ch => ({{'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;'}}[ch]));
}}
function escapeAttr(value) {{ return escapeHtml(value).replace(/'/g, '&#39;'); }}
search.addEventListener('input', renderBoard);
statusFilter.addEventListener('change', renderBoard);
renderBoard();
</script>
</body>
</html>
"""


def export_dashboard(args: argparse.Namespace) -> None:
    payload = application_payload()
    output = Path(args.output).expanduser() if args.output else private_home() / "dashboard.html"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(dashboard_html(payload), encoding="utf-8", newline="\n")
    print(output)


class DashboardHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        if parsed.path not in {"/", "/dashboard.html"}:
            self.send_error(404)
            return
        content = dashboard_html(application_payload()).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def log_message(self, format: str, *args: object) -> None:
        return


def serve_dashboard(args: argparse.Namespace) -> None:
    init_db()
    server = ThreadingHTTPServer((args.host, args.port), DashboardHandler)
    print(f"serving http://{args.host}:{args.port}")
    server.serve_forever()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init")
    init.set_defaults(func=lambda args: init_db())

    new = sub.add_parser("new")
    new.add_argument("--id")
    new.add_argument("--company", required=True)
    new.add_argument("--role", required=True)
    new.add_argument("--source")
    new.add_argument("--source-url")
    new.add_argument("--location")
    new.add_argument("--remote-mode")
    new.add_argument("--status", choices=STATUSES, default="found")
    new.add_argument("--priority", default="medium")
    new.add_argument("--next-action")
    new.add_argument("--notes")
    new.set_defaults(func=create_application)

    offer = sub.add_parser("ingest-offer")
    offer.add_argument("--id", required=True)
    offer.add_argument("--text")
    offer.add_argument("--file")
    offer.add_argument("--cleaned-text")
    offer.add_argument("--next-action")
    offer.set_defaults(func=ingest_offer)

    update = sub.add_parser("update")
    update.add_argument("--id", required=True)
    update.add_argument("--status", choices=STATUSES)
    update.add_argument("--priority")
    update.add_argument("--next-action")
    update.add_argument("--notes")
    update.add_argument("--applied-at")
    update.set_defaults(func=update_application)

    add = sub.add_parser("add-text")
    add.add_argument("--id", required=True)
    add.add_argument("--kind", choices=["evaluation", "cover-letter", "interview-guide"], required=True)
    add.add_argument("--text")
    add.add_argument("--file")
    add.add_argument("--verdict")
    add.add_argument("--fit-score", type=int)
    add.add_argument("--risk-score", type=int)
    add.add_argument("--effort-score", type=int)
    add.add_argument("--submitted-text")
    add.add_argument("--version")
    add.add_argument("--next-action")
    add.set_defaults(func=add_text)

    listing = sub.add_parser("list")
    listing.add_argument("--status", choices=STATUSES)
    listing.add_argument("--search")
    listing.set_defaults(func=list_applications)

    export = sub.add_parser("export-dashboard")
    export.add_argument("--output")
    export.set_defaults(func=export_dashboard)

    dashboard = sub.add_parser("dashboard")
    dashboard.add_argument("--host", default="127.0.0.1")
    dashboard.add_argument("--port", type=int, default=8765)
    dashboard.set_defaults(func=serve_dashboard)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
