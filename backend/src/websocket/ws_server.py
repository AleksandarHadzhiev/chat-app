import datetime
import threading

from fastapi import WebSocket

from src.messages.service import MessagesService


class ConnectionManager:
    def __init__(self):
        self.active_connections = {}

    async def connect(self, ws: WebSocket, id: int, username: str, db, config, admin_id: int):
        await ws.accept()
        if id not in self.active_connections:
            self.active_connections[id] = ws
            text = f"{username} joined the server"
            message = {
                "user_id": int(admin_id), 
                "author": "GGC", 
                "content": text, 
                "group_id": 1, 
                "code": f"1-1-{self.generate_special_code()}",
                "created_at": f"{str(datetime.datetime.now())}"
            }
            response = await MessagesService(db=db, settings=config).create(data=message)
            if "fail" in response:
                return response
            return {"message": "success"}
        else:
            self.active_connections[id] = ws
            return {"message": "success"}

    def generate_special_code(self):
        initial_state = str(datetime.datetime.now())
        without_space = initial_state.replace(" ", "-")
        without_column = without_space.replace(":","-")
        return without_column

    async def disconnect(self, id):
        self.active_connections.pop(id)

    async def broadcast(self, message):
        for connection in self.active_connections:
            _socket: WebSocket = self.active_connections[connection]
            await _socket.send_json(message)
