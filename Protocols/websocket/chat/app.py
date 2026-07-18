import asyncio
import websockets

connected = set()

async def handler(websocket):
    connected.add(websocket)
    try:
        async for message in websocket:
            for client in connected:
                if client != websocket:
                    await client.send(f"Peer says: {message}")
    finally:
        connected.remove(websocket)

async def main():
    async with websockets.serve(handler, "0.0.0.0", 5004):
        print("WebSocket chat server started on :5004")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
