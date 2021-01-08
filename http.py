try:
    # python2 import
    from SocketServer import ThreadingMixIn
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from BaseHTTPServer import HTTPServer
except ImportError:
    # Python 3 import
    from socketserver import ThreadingMixIn
    from http.server import SimpleHTTPRequestHandler, HTTPServer

class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    @property
    def main(self, kevin)->None:
        __version__ = 0.1
        __author__ = kevin
        print(f"Version={__version__}\nAuthor: {__author__}")
    pass

import sys
import os

os.system('cls')

if sys.argv[1:]:
    address = sys.argv[1]
    if (':' in address):
        interface = address.split(':')[0]
        port = int(address.split(':')[1])
    else:
        interface = '127.0.0.1'
        port = int(address)

else:
    port = 8080
    interface = '127.0.0.1'

if sys.argv[2:]:
    os.chdir(sys.argv[2])

os.system('cls')
print("Started HTTP server in " + interface + ":" + str(port))

server = ThreadingSimpleServer((interface, port), SimpleHTTPRequestHandler)
try:
    while 1:
        sys.stdout.flush()
        server.handle_request()

except KeyboardInterrupt:
    print("will exit")
