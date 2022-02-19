import sys, getopt
from http.server import HTTPServer
from server.server_config import ServServer

def get_options(args, HOST, PORT):

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
    return HOST, PORT

def serv_it(host, port):

    httpd = HTTPServer((host, int(port)), ServServer)
    print("Serving on port: {host}:{port}".format(host=host, port=port))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("Closing on port: {host}:{port}".format(host=host, port=port))

if __name__ == "__main__":
    HOST = PORT = ''
    argvs = sys.argv[1:]
    if argvs: HOST, PORT = get_options(argvs, HOST, PORT)

    if not HOST: HOST = '127.0.0.1'
    if not PORT: PORT = 8000

    serv_it(HOST, PORT)
