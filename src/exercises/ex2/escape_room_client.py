import socket
HOST = '127.0.0.1'
PORT = 50054
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  l='look'
  b=b'look'
  print(b)
  print(type(b))
  s.send(b'look')
  print("ok?")
  data = s.recv(1024)
  
print('Received',repr(data))
