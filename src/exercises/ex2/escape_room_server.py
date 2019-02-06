from escape_room import EscapeRoom
import socket


#HOST='73.39.109.232'
HOST='127.0.0.1'
PORT=1000




#server_socket.listen(1)
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
while True:
	print("0")
	#s.connect(('73.39.109.232',50911))
	print("1")
	conn, addr = s.accept()
	print(conn)
	print("2")
	room=EscapeRoom()      # create an escape room
	room.start()
	while room.status()=="locked":      # while the escape room status is locked
	#command = input (">> ")
		print("ready to receive")
		data = conn.recv(1024)              # read the data from conn
		print(data)
		print(data.decode())
		print(data.decode())
		print(data.decode())

		print(type(data.decode()))
		datastr=data.decode()
		datastr=datastr.replace('\r\n','')
		print(datastr)
		output = room.command(datastr) # encode converts from bytes to string
		print(output)
		print(type(output))
		
		conn.sendall(output.encode())               # send the output.encode() to conn (encode converts from string to bytes)

	#         if room.status()=="escaped":

	#             return "Congratulations! You escaped!"

	#         else:

	#             return "Oh no! The clock starts ringing!!! After a few seconds, the room fills with a deadly gas... Sorry. You died."
	conn.close()
