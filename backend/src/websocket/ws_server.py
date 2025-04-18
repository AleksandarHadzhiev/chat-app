import threading
from fastapi import WebSocket

from src.messages.service import MessagesService


class ConnectionManager:
    def __init__(self):
        self.active_connections = {}

    async def connect(self, ws: WebSocket, id: int, username: str, db, config):
        await ws.accept()
        if id not in self.active_connections:
            self.active_connections[id] = ws
            text = f"{username} joined the server"
            
            message = {
                "userId": id,
                "author": "GGC",
                "content": text,
                "groupId": 1
            }
            MessagesService(db=db, settings=config).create(data=message)
        else:
            self.active_connections[id] = ws


    async def disconnect(self, id):
        self.active_connections.pop(id)

    async def broadcast(self, id, message):
        # ws: WebSocket = self.active_connections[id]
        for connection in self.active_connections:
            json = f"""
                {
                   "author": "{message["author"]}",
                   "content": "{message["content"]}",
                   "group_id": "{message["group_id"]}",
                }
            """
            text = f"{message["author"]}: {message["content"]}"
            _socket: WebSocket = self.active_connections[connection]
            await _socket.send_text(text)
