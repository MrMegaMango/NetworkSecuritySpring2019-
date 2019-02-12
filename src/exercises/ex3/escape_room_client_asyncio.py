import argparse
import asyncio
import sys
def got_stdin_data(q):
    asyncio.async(q.put(sys.stdin.readline()))
class EscapeRoomClientProtocol(asyncio.Protocol):
	def connection_made(self,transport):
		print(">> ",end='',flush=True)
		command=asyncio.async(q.get())
		command.add_done_callback(self.write_reply)
		self.transport=transport
	def data_received(self,data):
		print(data.decode()+"\n>> ",end='')
		command=asyncio.async(q.get())
		command.add_done_callback(self.write_reply)
	def write_reply(self,command):
		reply = command.result()
		self.transport.write(reply.encode())
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
    q=asyncio.Queue()
    loop.add_reader(sys.stdin,got_stdin_data,q)
    coro=loop.create_connection(lambda: EscapeRoomClientProtocol(),'0.0.0.0',PORT)
    loop.run_until_complete(coro)
    loop.run_forever()
    looop.close()
