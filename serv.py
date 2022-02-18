import sys, getopt
from http.server import HTTPServer
from server import Server

def serv_it(host, port):

    httpd = HTTPServer((host, int(port)), Server)
    print("Serving on port: {host}:{port}".format(host=host, port=port))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("Stopping on port: {host}:{port}".format(host=host, port=port))

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 8000
    argvs = sys.argv[1:]
    if argvs:
        try:
            opts, args = getopt.getopt(argvs,"ih:p:", ["host=","port="])
        except getopt.GetoptError:
            print("python serv.py -i <info> -h <host> -p <port>")
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-i':
                print("python serv.py -i <info> -h <host> -p <port>")
                sys.exit()
            elif opt in ['-h', '--host']:
                HOST = arg
            elif opt in ['-p', '--port']:
                PORT = arg
        serv_it(HOST, PORT)
    else:
        serv_it(HOST, PORT)
