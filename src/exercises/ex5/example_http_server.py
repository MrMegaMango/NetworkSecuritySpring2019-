import asyncio
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

class ExampleHttpServer(asyncio.Protocol):
    def __init__(self,document_root):
        print("init")

    def connection_made(self,transport):
        self.transport=transport

    def data_received(self,data):
        # self.buffer += data
        # if not self.has_full_packet(self.buffer):
        #     return
        data=data.decode()
        print(data) #data split
        requests=data.split()
        print(requests[0])
        self.transport.write("hi".encode())


HOST='localhost'
PORT=8080


document_root = sys.argv[1] # first command line parameter
loop = asyncio.get_event_loop()
coro=loop.create_server(lambda: ExampleHttpServer(document_root), HOST, PORT)
server = loop.run_until_complete(coro)
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
