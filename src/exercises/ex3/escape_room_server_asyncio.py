from escape_room import EscapeRoom
import select
import socket
import argparse
import asyncio

class EscapeRoomServerClientProtocol(asyncio.Protocol):
	def connection_made(self,transport):
		self.transport=transport
	def data_received(self,data):
		message=data.decode()
		print(message)
		return message		
		#self.transport.write(output)
		

		global room
		room.append(EscapeRoom())
		room[-1].start()
		while room[-1].status()=="locked":      # while the escape room status is locked
			#data =await  loop.sock_recv(client,1024)           # read the data from conn
						
			datastr=data.decode()
			datastr=datastr.replace('\r\n','')
			output = room[-1].command(datastr) # encode converts from bytes to string
			#print(output)
			try:					
				if output:
					self.transport.write(output.encode())               # send the output.encode() to conn (encode converts from string to bytes)
				else:
					loop.sock_sendall(client,"invalid input".encode())
			except BrokenPipeError:	
				break	
		if room[-1].status()=="escaped":
			self.transport.write("Congratulations! You escaped!".encode())
					
		elif room[-1].status()=="died":
			self.transport.write("Oh no! The clock starts ringing!!! After a few seconds, the room fills with a deadly gas... Sorry. You died.".encode())
					







async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port",help="the port you choose")
    args=parser.parse_args()
    if args.port:
        print("We are connected to port "+args.port+". Now let't play this deadly game on client.")
        PORT=int(args.port)
    else:
        PORT=1121


    global room
    room=[]
    loop = asyncio.get_event_loop()
    coro = loop.create_server(EscapeRoomServerClientProtocol, '0.0.0.0',PORT)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
    #main(PORT).serve()

