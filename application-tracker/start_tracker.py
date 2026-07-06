"""Launch the local Application Tracker in a browser."""

from __future__ import annotations

import argparse
import threading
import time
import webbrowser
from http.server import ThreadingHTTPServer

import acb_tracker
import acb_tracker_readonly


def open_browser_later(url: str) -> None:
    time.sleep(0.8)
    webbrowser.open(url)


def serve(args: argparse.Namespace) -> None:
    host = args.host
    port = args.port if args.port is not None else (8766 if args.mode == "readonly" else 8765)
    handler = acb_tracker_readonly.ReadOnlyDashboardHandler if args.mode == "readonly" else acb_tracker.DashboardHandler
    acb_tracker.init_db()
    server = ThreadingHTTPServer((host, port), handler)
    url = f"http://{host}:{port}/"
    print(f"Opening Application Tracker: {url}")
    threading.Thread(target=open_browser_later, args=(url,), daemon=True).start()
    server.serve_forever()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=["full", "readonly"], default="full")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int)
    parser.set_defaults(func=serve)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
