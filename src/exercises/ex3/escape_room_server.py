from escape_room import EscapeRoom
import select
import socket
import argparse
import asyncio

async def main(PORT,loop):
	HOST='localhost'
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	s.listen(5)
	s.setblocking(False)
	global room
	room=[]
	while True:
		client,addr=await loop.sock_accept(s)
		loop.create_task(new_room(client,loop))
async def new_room(client,loop):
			#print("ok?")	
			global room
			room.append(EscapeRoom())
			room[-1].start()
			while room[-1].status()=="locked":      # while the escape room status is locked
				data =await  loop.sock_recv(client,1024)           # read the data from conn
				datastr=data.decode()
				datastr=datastr.replace('\r\n','')
				output = room[-1].command(datastr) # encode converts from bytes to string
				#print(output)
				try:					
					if output:
						await loop.sock_sendall(client,output.encode())               # send the output.encode() to conn (encode converts from string to bytes)
					else:
						await loop.sock_sendall(client,"invalid input".encode())
				except BrokenPipeError:	
					break	
			if room[-1].status()=="escaped":
				await loop.sock_sendall(client,"Congratulations! You escaped!".encode())
				
			elif room[-1].status()=="died":
				await loop.sock_sendall(client,"Oh no! The clock starts ringing!!! After a few seconds, the room fills with a deadly gas... Sorry. You died.".encode())
				







if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port",help="the port you choose")
    args=parser.parse_args()
    if args.port:
        print("We are connected to port "+args.port+". Now let't play this deadly game on client.")
        PORT=int(args.port)
    else:
        PORT=1121



    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(PORT,loop))
    loop.close()
    #main(PORT).serve()
