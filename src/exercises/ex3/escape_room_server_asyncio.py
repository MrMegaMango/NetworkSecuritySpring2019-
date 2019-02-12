import argparse
import asyncio
class EscapeRoomClientProtocol(asyncio.Protocol):

	def connection_made(self,transport):
		command= input(">> ")
		self.command=command
		self.transport=transport
		transport.write(self.command.encode())

	def data_received(self,data):
		print(data.decode())
		command = input (">> ")
		self.transport.write(command.encode())

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port",help="the port you choose")
    args=parser.parse_args()
    if args.port:
        print("We are connected to port "+args.port+". Now let't play this deadly game.")
        PORT=int(args.port)
    else:
        PORT=1121
    loop=asyncio.get_event_loop()
    coro=loop.create_connection(lambda: EscapeRoomClientProtocol(),'0.0.0.0',PORT)
    loop.run_until_complete(coro)
    loop.run_forever()
    looop.close()
