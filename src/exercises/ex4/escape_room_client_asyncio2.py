import argparse
import asyncio
import sys

stdin_queue=[]
def handle_stdin():
    line_in=sys.stdin.readline()
    line_in=line_in[:-1]
    #asyncio.async(q.put(sys.stdin.readline()))
async def async_input(prompt):
    print(prompt,end="")
    sys.stdout.flush()
    while len(stdin_queue)==0:
        print(stin_queue)
        await asyncio.sleep(.1)
        
    
    return stdin_queue.pop(0)
async def async_output():
    print("output")
async def game_runner(protocol):
    while True:
        command=await async_input(">>> ")
        print("huh")
        protocol.transport.write(command.encode())
        response=await async_output()
        print("response")
class EscapeRoomClientProtocol(asyncio.Protocol):
	def connection_made(self,transport):
		print("connection made")
		#command=asyncio.async(q.get())
		#command.add_done_callback(self.write_reply)
		#self.transport=transport
	def data_received(self,data):
		print("receive")
		#command=asyncio.async(q.get())
		#command.add_done_callback(self.write_reply)
	def write_reply(self,command):
		#reply = command.result()
		#self.transport.write(reply.encode())
                print("write")
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
    #q=asyncio.Queue()
    loop.add_reader(sys.stdin,handle_stdin)
    asyncio.ensure_future(game_runner(protocol)) 
    loop.run_forever()
    looop.close()
 
