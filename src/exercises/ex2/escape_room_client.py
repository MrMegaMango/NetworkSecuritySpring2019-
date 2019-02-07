import socket
HOST = '0.0.0.0'
PORT = 11113
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	while True:
		command = input (">> ")
		s.send(command.encode())
		data = s.recv(1024)
		data = data.decode()
		print(data)
		if data == "You open the door.Congratulations! You escaped!" or data == "Oh no! The clock starts ringing!!! After a few seconds, the room fills with a deadly gas... Sorry. You died.":
			break
