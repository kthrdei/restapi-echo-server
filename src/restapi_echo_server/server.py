import json
import datetime
from urllib import parse
from http import server as http_server
import logging

logger = logging.getLogger(__name__)


class Handler(http_server.BaseHTTPRequestHandler):
    def _handle(self):
        parsed_path = parse.urlparse(self.path)

        content_length = int(self.headers.get('content-length', 0))
        body = self.rfile.read(content_length).decode('utf-8')
        
        response = {
            "method": self.command,
            "path": parsed_path.path,
            "query": parse.parse_qs(parsed_path.query),
            "headers": dict(self.headers),
            "body": body,
            "received_at": datetime.datetime.utcnow().isoformat(),
            "client": {
                "host": self.client_address[0],
                "port": self.client_address[1],
            },
            "server": {
                "host": self.server.server_address[0],
                "port": self.server.server_address[1],
            },
        }

        logger.info(f"{json.dumps(response)}")

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))

    def do_GET(self):
        self._handle()

    def do_POST(self):
        self._handle()

    def do_PUT(self):
        self._handle()

    def do_PATCH(self):
        self._handle()

    def do_DELETE(self):
        self._handle()

    def do_HEAD(self):
        self._handle()

    def do_OPTIONS(self):
        self._handle()

    def log_message(self, format, *args):
        pass


def start(host: str, port: int):
    with http_server.HTTPServer((host, port), Handler) as server:
        logger.info(f"Running on {host}:{port}")
        server.serve_forever()
