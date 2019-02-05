import socket

HOST = 'daring.cwi.nl'
PORT = 50007
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  s.endall(b'Hello, world')
  data = s.recv(1024)
  
print('Received',repr(data))