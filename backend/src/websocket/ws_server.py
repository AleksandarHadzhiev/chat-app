import datetime
import threading

from fastapi import WebSocket

from src.messages.service import MessagesService
from src.utils.authentication import User

class ConnectionManager:
    def __init__(self):
        self.active_connections = {}

    async def connect(self, ws: WebSocket, user: User, db, config, admin_id: int):
        await ws.accept()
        if user.id not in self.active_connections:
            self.active_connections[user.id] = ws
            text = f"{user.username} joined the server"
            message = {
                "content": text, 
                "group_id": 1, 
                "created_at": f"{str(datetime.datetime.now())}",
                "user_id": int(admin_id), 
                "author": "GGC", 
                "code": self.generate_special_code()
            }
            response = await MessagesService(db=db, settings=config).create(data=message)
            if "fail" in response:
                return response
            return {"message": "success"}
        else:
            self.active_connections[user.id] = ws
            return {"message": "success"}

    def generate_special_code(self, user_id=1, group_id=1):
        initial_state = str(datetime.datetime.now())
        without_space = initial_state.replace(" ", "-")
        without_column = without_space.replace(":","-")
        final_code = f"{user_id}-{group_id}-{without_column}"
        return final_code

    async def disconnect(self, id):
        socket: WebSocket = self.active_connections[id]
        socket.close()

    async def broadcast(self, message):
        for connection in self.active_connections:
            _socket: WebSocket = self.active_connections[connection]
            if _socket != None:
                await _socket.send_json(message)
