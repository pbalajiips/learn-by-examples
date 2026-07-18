import asyncio
import json
import websockets

clients = set()

async def handler(websocket):
    clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Received client message: {message}")
    finally:
        clients.remove(websocket)

async def broadcast():
    count = 1
    while True:
        if clients:
            payload = json.dumps({"event": "notify", "count": count})
            await asyncio.wait([client.send(payload) for client in clients])
            count += 1
        await asyncio.sleep(3)

async def main():
    async with websockets.serve(handler, "0.0.0.0", 5005):
        print("WebSocket notify server started on :5005")
        await broadcast()

if __name__ == "__main__":
    asyncio.run(main())
