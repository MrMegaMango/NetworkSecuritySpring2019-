from escape_room import EscapeRoom

server_socket.listen(1)
while True:
    conn, addr = server_socket.accept()
    room=EscapeRoom()      # create an escape room
    room.start()
    while room.status()=="locked":      # while the escape room status is locked
        #command = input (">> ")

        data = conn.recv(1024)              # read the data from conn

        output = room.command(data.decode()) # encode converts from bytes to string
        
        conn.sendall(data)               # send the output.encode() to conn (encode converts from string to bytes)
        
#         if room.status()=="escaped":

#             return "Congratulations! You escaped!"

#         else:

#             return "Oh no! The clock starts ringing!!! After a few seconds, the room fills with a deadly gas... Sorry. You died."
   conn.close()
