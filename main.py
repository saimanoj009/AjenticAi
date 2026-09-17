import os
from http.server import HTTPServer, SimpleHTTPRequestHandler


class HealthHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>AjenticAi Service</title>
            <style>
                body {
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background: #0f172a;
                    color: #f8fafc;
                }
                .card {
                    text-align: center;
                    padding: 2.5rem;
                    background: #1e293b;
                    border-radius: 1rem;
                    box-shadow: 0 10px 25px rgba(0,0,0,0.5);
                    border: 1px solid #334155;
                    max-width: 480px;
                }
                h1 { color: #38bdf8; margin-bottom: 0.5rem; }
                p { color: #94a3b8; line-height: 1.6; font-size: 0.95rem; }
                .status {
                    display: inline-block;
                    margin-top: 1rem;
                    padding: 0.4rem 1.2rem;
                    background: #064e3b;
                    color: #34d399;
                    border-radius: 9999px;
                    font-weight: 600;
                    font-size: 0.875rem;
                }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>⚡ AjenticAi Service</h1>
                <p>Your Agentic AI application is deployed and running successfully on Render.</p>
                <div class="status">● Status: Active & Healthy</div>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html.encode("utf-8"))


def main():
    port = int(os.environ.get("PORT", 10000))
    server_address = ("0.0.0.0", port)
    httpd = HTTPServer(server_address, HealthHandler)
    print(f"AjenticAi server running on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    main()
