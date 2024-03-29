from http.server import BaseHTTPRequestHandler
import os

class ServServer(BaseHTTPRequestHandler):
    def __response(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            split_path = os.path.splitext(self.path)
            request_extension = split_path[1]
            if request_extension != ".py":
                f = open(self.path[1:]).read()
                self.__response()
                self.wfile.write(bytes(f, 'utf-8'))
            else:
                f = "File not found"
                self.send_error(404, f)
        except:
            f = "File not found"
            self.send_error(404, f)
