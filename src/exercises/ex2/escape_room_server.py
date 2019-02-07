from escape_room import EscapeRoom
import select
import socket
import argparse
def main(PORT):
	HOST='0.0.0.0'
	#PORT=1117
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	room=[]
	i=-1

	s.bind((HOST, PORT))
	inputs=[s]


	s.listen(1)
	while True:
		read_ready, _, _ = select.select(inputs,[],[])
		for server in read_ready:
			if s == server:
				
				conn, addr = server.accept()
				inputs.append(conn)			

			else:
				room.append(EscapeRoom())
				i=i+1     # create an escape room
				room[i].start()
				while room[i].status()=="locked":      # while the escape room status is locked
					data = server.recv(1024)              # read the data from conn
					datastr=data.decode()
					datastr=datastr.replace('\r\n','')
					output = room[i].command(datastr) # encode converts from bytes to string
					if output:
						server.sendall(output.encode())               # send the output.encode() to conn (encode converts from string to bytes)
					else:
						server.sendall("invalid input".encode())
				if room[i].status()=="escaped":
					server.sendall("Congratulations! You escaped!".encode())
				else:
					server.sendall("Oh no! The clock starts ringing!!! After a few seconds, the room fills with a deadly gas... Sorry. You died.".encode())
				server.close()
				break


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port",help="the port you choose")
    args=parser.parse_args()
    if args.port:
        print("We are connected to port "+args.port+". Now let't play this deadly game on client.")
        PORT=int(args.port)
    else:
        PORT=1121
    main(PORT)
