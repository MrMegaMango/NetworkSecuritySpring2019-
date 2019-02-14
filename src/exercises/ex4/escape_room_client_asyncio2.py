import argparse
import asyncio
import sys
import time
stdin_queue=[]
def handle_stdin():
    line_in=sys.stdin.readline()
    line_in=line_in[:-1]
    stdin_queue.append(line_in)
async def async_input(prompt):
    print(prompt,end="",flush=True)
    while len(stdin_queue)==0:     
        await asyncio.sleep(.1)   
    return stdin_queue.pop(0)
async def game_runner(protocol):
    while True:
        command=await async_input(">> ")    
        protocol.transport.write(command.encode())
class EscapeRoomClientProtocol(asyncio.Protocol):
	def connection_made(self,transport):
		print("connection made")
		self.transport=transport
	def data_received(self,data):
		print(data.decode()+"\n>> ",end='')
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
    transport,protocol=loop.run_until_complete(coro)
    loop.add_reader(sys.stdin,handle_stdin)
    asyncio.ensure_future(game_runner(protocol)) 
    loop.run_forever()
    looop.close()
