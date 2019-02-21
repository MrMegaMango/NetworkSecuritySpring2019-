import asyncio
import sys
import datetime
import os
import mimetypes
from os import curdir, sep
#from datetime import datetime

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
            length=os.path.getsize(document_root+sep+path)
        except FileNotFoundError:
            print("404")
            length=0
            status="404 Not Found"


        if status=="200 OK":
            print(document_root+sep+path)
            try:
                msg=open(document_root+sep+path,"rb")
                mime_type,encoding=mimetypes.guess_type(document_root+sep+path)
            except IsADirectoryError:
                try:
                    msg=open(document_root+sep+path+"/index.html","rb")
                    mime_type,encoding=mimetypes.guess_type(document_root+sep+path+"/index.html")
                except FileNotFoundError:
                    status="404 Not Found"
                    length=0
                    response="HTTP/1.1 "+status+"\r\nDate: "+str(datetime.datetime.now())+"\r\nServer: NetSec Prototype Server 1.0\r\n\
Content-Length: "+str(length)+"\r\n\r\n"
                    print(response)
                    self.transport.write(response.encode())
                    return
            file=msg.read()
            print(file)
            statbuf=os.stat(document_root+sep+path).st_mtime
            mod_time=datetime.datetime.fromtimestamp(statbuf)
            response="HTTP/1.1 "+status+"\r\nDate: "+str(datetime.datetime.now())+"\r\nServer: NetSec Prototype Server 1.0\r\n\
Last-Modified: "+str(mod_time)+"\r\n\
Content-Length: "+str(length)+"\r\n\
Connection: close\r\n\
Content-Type: "+mime_type+"\r\n\r\n"
        else:
            response="HTTP/1.1 "+status+"\r\nDate: "+str(datetime.datetime.now())+"\r\nServer: NetSec Prototype Server 1.0\r\n\
Content-Length: "+str(length)+"\r\n\r\n"
        print(response)
        self.transport.write(response.encode())
        if status=="200 OK":
            self.transport.write(file)
        return
    def has_full_packet(self,buffer):
        if buffer[-4:]=="\r\n\r\n".encode():
            #full package
            return True
        else:
            print(buffer[-4:])
            return False



HOST='localhost'
PORT=8080
document_root = sys.argv[1] # first command line parameter (use . for current folder)
loop = asyncio.get_event_loop()
coro=loop.create_server(lambda: ExampleHttpServer(document_root), HOST, PORT)
server = loop.run_until_complete(coro)
try:
    loop.run_forever()
except:
    loop.run_until_complete(server.wait_closed())
finally:
    loop.close()
