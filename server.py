import sys
import http.server
import socketserver

if sys.argv[1:]:
    PORT = int(sys.argv[1])
else:
    PORT = 8000

if sys.argv[2:]:
    SERVER = str(sys.argv[2])
else:
    SERVER = '127.0.0.1'


class ServerRequestHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)



def run(port=PORT, server=SERVER):
    Handler = ServerRequestHandler

    with socketserver.TCPServer((server, port), Handler) as httpd:
        print("Serving on port: {sv}:{pt}".format(sv=SERVER, pt=PORT))
        httpd.serve_forever()

run(PORT, SERVER)
