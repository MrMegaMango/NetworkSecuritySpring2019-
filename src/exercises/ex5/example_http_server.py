import asyncio
import sys
import datetime
import os
from os import curdir, sep

#from http.server import HTTPServer, BaseHTTPRequestHandler

class ExampleHttpServer(asyncio.Protocol):
    def __init__(self,document_root):
        print("init")
        buffer=''.encode()
        self.buffer=buffer

    def connection_made(self,transport):
        self.transport=transport

    def data_received(self,data):
        self.buffer += data
        if not self.has_full_packet(self.buffer):
            return
        data=data.decode()
        requests=data.split()
        requests=["method"]+requests
        requests = dict(zip(requests[::2], requests[1::2]))
        if requests["method"]!="GET":
            return
        if list(requests.values())[1]!= ("HTTP/1.1" or "HTTP/1.0"):
            return
        print(requests)
        path=list(requests.keys())[1]
        status="200 OK"
        try:
            length=os.path.getsize(curdir+sep+path)
        except FileNotFoundError:
            print("404")
            length=0
            status="404 Not Found"


        #print(length)
        if status=="200 OK":
            print(path)
            msg=open(curdir+sep+path,"rb")
            file=msg.read()
            print(file)
            response="HTTP/1.1 "+status+"\r\nDate: "+str(datetime.datetime.now())+"\r\nServer: NetSec Prototype Server 1.0\r\n\
Last-Modified: "+str(datetime.datetime.now())+"\r\n\
Content-Length: "+str(length)+"\r\n\
Connection: close\r\n\
Content-Type: text/html\r\n\r\n"
        else:
            response="HTTP/1.1 "+status+"\r\nDate: "+str(datetime.datetime.now())+"\r\nServer: NetSec Prototype Server 1.0\r\n\
Content-Length: "+str(length)+"\r\n\r\n"
        print(response)
        self.transport.write(response.encode())
        if status=="200 OK":
            self.transport.write(file)
        #print("am I stuck here?")
        return
    def has_full_packet(self,buffer):
        if buffer[-4:]=="\r\n\r\n".encode():
            #print("full package")
            return True
        else:
            print(buffer[-4:])
            return False



HOST='localhost'
PORT=8080
document_root = sys.argv[1] # first command line parameter
loop = asyncio.get_event_loop()
coro=loop.create_server(lambda: ExampleHttpServer(document_root), HOST, PORT)
server = loop.run_until_complete(coro)
try:
    loop.run_forever()
except:
    loop.run_until_complete(server.wait_closed())
finally:
    loop.close()

#server.close()

#loop.close()
