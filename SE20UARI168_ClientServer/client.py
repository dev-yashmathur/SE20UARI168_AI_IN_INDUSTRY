import asyncio
import websockets

async def send_message():
    async with websockets.connect("ws://localhost:8765") as websocket:
        message = "This is your amazing client!"
        await websocket.send(message)
        print(f"Sent message to server: {message}")

        response = await websocket.recv()
        print(f"Received response from server: {response}")

asyncio.get_event_loop().run_until_complete(send_message())
