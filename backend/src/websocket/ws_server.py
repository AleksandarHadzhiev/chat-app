from fastapi import WebSocket

class ConnectionManager:
    def __init__(self):
        self.active_connections = {}


    async def connect(self, ws: WebSocket, id):
        await ws.accept()
        self.active_connections[id] = ws
        await ws.send_text(f"{id} just connected")


    async def disconnect(self, id):
        self.active_connections.pop(id)


    async def broadcast(self, id, data):
        ws: WebSocket = self.active_connections[id]
        await ws.send_text(f"{data}")