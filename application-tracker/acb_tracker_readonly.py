"""Read-only local wrapper for the Application Tracker dashboard.

This module intentionally reuses ``acb_tracker`` instead of duplicating the
Application Tracker dashboard UI. It serves the same private SQLite-backed
tracker view with the Raw intake/write surface removed.
"""

from __future__ import annotations

import argparse
import re
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import acb_tracker


INTAKE_SECTION_PATTERN = re.compile(
    r"\n\s*<section class=\"intake\">.*?</section>",
    re.DOTALL,
)


def readonly_dashboard_html() -> str:
    """Return the real dashboard HTML without the Raw intake section."""
    html = acb_tracker.dashboard_html(acb_tracker.application_payload())
    return INTAKE_SECTION_PATTERN.sub("", html)


class ReadOnlyDashboardHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802
        if self.path.split("?", 1)[0] not in {"/", "/dashboard.html", "/readonly", "/readonly.html"}:
            self.send_error(404)
            return
        content = readonly_dashboard_html().encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def log_message(self, format: str, *args: object) -> None:
        return


def serve(args: argparse.Namespace) -> None:
    acb_tracker.init_db()
    server = ThreadingHTTPServer((args.host, args.port), ReadOnlyDashboardHandler)
    print(f"serving read-only Application Tracker at http://{args.host}:{args.port}")
    server.serve_forever()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8766)
    parser.set_defaults(func=serve)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
