import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"DevMate is alive!")

    def log_message(self, format, *args):
        return  # Silence HTTP logs


def start_health_server():
    port = int(os.environ.get("PORT", 10000))

    server = HTTPServer(("0.0.0.0", port), Handler)

    Thread(target=server.serve_forever, daemon=True).start()