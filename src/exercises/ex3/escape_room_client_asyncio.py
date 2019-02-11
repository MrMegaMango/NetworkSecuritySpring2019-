import select
import socket
import sys
import argparse
import asyncio
import time
class EscapeRoomClientProtocol(asyncio.Protocol):
	def __init__(self,message):
		message = ""
		self.message=message
		#global PORT
		#HOST = '0.0.0.0'
			#print("init")
		#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			#s.connect((HOST,PORT))

			#command = input (">> ")
				




	def connection_made(self,transport):
		time.sleep(1)
		message = input (">> ")
		print("stop")
		self.message=message
		transport.write(self.message.encode())
	def data_received(self,data):
		print(data.decode())
		

if __name__=="__main__":
    #global PORT
    parser = argparse.ArgumentParser()
    parser.add_argument("--port",help="the port you choose")
    args=parser.parse_args()
    if args.port:
        print("We are connected to port "+args.port+". Now let't play this deadly game.")
        PORT=int(args.port)
    else:
        PORT=1121
    #main(PORT)
    loop=asyncio.get_event_loop()
    message = "hi88"
    coro=loop.create_connection(lambda: EscapeRoomClientProtocol(message),'0.0.0.0',PORT)
    print("hi")
    loop.run_until_complete(coro)
    print("hi2")
    loop.run_forever()
    looop.close()
