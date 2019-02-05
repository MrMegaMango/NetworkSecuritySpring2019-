from escape_room import EscapeRoom

server_socket.listen(1)
while True:
    conn, addr = server_socket.accept()
    
    # create an escape room
    # while the escape room status is locked
        # read the data from conn
        output = room.command(data.decode()) # encode converts from bytes to string
        # send the output.encode() to conn (encode converts from string to bytes)
   conn.close()
