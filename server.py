from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # Username and Password
    USERNAME = "udemyl10n"
    PASSWORD = "9_>*4x64FZ{3}"

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        params = parse_qs(post_data)

        # Check if username and password are correct
        if 'username' in params and 'password' in params:
            username = params['username'][0]
            password = params['password'][0]
            if username == self.USERNAME and password == self.PASSWORD:
                self.send_response(303)
                self.send_header('Location', '/index.html')
                self.end_headers()
                return
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Invalid credentials. Please try again.".encode('utf-8'))

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('login.html', 'rb') as f:
                self.wfile.write(f.read())
        elif self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as f:
                self.wfile.write(f.read())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write("404 Not Found".encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on http://localhost:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
