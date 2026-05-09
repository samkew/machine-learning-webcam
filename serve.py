#!/usr/bin/env python3
"""Serve this project directory over HTTP on port 8000."""

from __future__ import annotations

import http.server
import os
import socketserver

PORT = 8000
ROOT = os.path.dirname(os.path.abspath(__file__))


class _Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)


def main() -> None:
    os.chdir(ROOT)
    with socketserver.TCPServer(("", PORT), _Handler) as httpd:
        print(f"Serving http://127.0.0.1:{PORT}/")
        print(f"Directory: {ROOT}")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
