import select
import socket
import sys
import argparse
def main(PORT):
	HOST = '0.0.0.0'
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST,PORT))
		while True:
			command = input (">> ")
			s.send(command.encode())
			data = s.recv(1024)
			data = data.decode()
			print(data)
			if data == "You open the door.Congratulations! You escaped!" or data == "Oh no! The clock starts ringing!!! After a few seconds, the room fills with a deadly gas... Sorry. You died.":				
				break
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port",help="the port you choose")
    args=parser.parse_args()
    if args.port:
        print("We are connected to port "+args.port+". Now let't play this deadly game.")
        PORT=int(args.port)
    else:
        PORT=1121
    main(PORT)
