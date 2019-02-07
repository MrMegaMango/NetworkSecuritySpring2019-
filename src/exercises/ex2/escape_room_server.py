from escape_room import EscapeRoom
import socket
HOST='0.0.0.0'
PORT=11113
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
while True:
	conn, addr = s.accept()
	room=EscapeRoom()      # create an escape room
	room.start()
	while room.status()=="locked":      # while the escape room status is locked
		data = conn.recv(1024)              # read the data from conn
		datastr=data.decode()
		datastr=datastr.replace('\r\n','')
		output = room.command(datastr) # encode converts from bytes to string
		if output:
			conn.sendall(output.encode())               # send the output.encode() to conn (encode converts from string to bytes)
		else:
			conn.sendall("invalid input".encode())
	if room.status()=="escaped":
		conn.sendall("Congratulations! You escaped!".encode())
	else:
		conn.sendall("Oh no! The clock starts ringing!!! After a few seconds, the room fills with a deadly gas... Sorry. You died.".encode())
	conn.close()
	break
