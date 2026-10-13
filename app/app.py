import os
from http.server import BaseHTTPRequestHandler, HTTPServer

VERSION = os.getenv("APP_VERSION", "1.0.0")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        html = f"""
        <html>
          <head><title>My DevOps Lab</title></head>
          <body style="font-family:Arial;text-align:center;margin-top:80px">
            <h1>My updated Kubernetes application!</h1>
            <p>It is running inside a Docker container.</p>
            <p>Application version: {VERSION}</p>
          </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
