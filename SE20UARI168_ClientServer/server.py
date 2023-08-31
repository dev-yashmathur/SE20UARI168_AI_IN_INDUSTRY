import asyncio
import websockets

async def server_handler(websocket, path):
    message = await websocket.recv()
    print(f"Received message from client: {message}")

    response = "Message received and processed!"
    await websocket.send(response)
    print("Sent response to client.")

start_server = websockets.serve(server_handler, "localhost", 8765)
# start_server = websocket.serve(server_handler, "SERVER_IP_HERE", SERVER_PORT_HERE)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
