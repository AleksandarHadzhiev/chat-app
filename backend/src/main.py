import json
from contextlib import asynccontextmanager

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from config import ConfigFactory
from src.db.db_factory import DBFactory
from src.groups.route import GroupsRouter
from src.languages.router import LanguagesRouter
from src.messages.router import MessagesRouter
from src.messages.service import MessagesService
from src.users.routers import UsersRouter
from src.websocket.ws_server import ConnectionManager


def create_app(server="test", secret="secret-key-placeholder"):
    config = ConfigFactory(type=server).get_config()
    config.set_secret_key(key=secret)
    db = DBFactory(config.ENVIRONMENT, settings=config).get_db()
    origins = ["http://localhost:3000"]

    connection_manager = ConnectionManager()
    users = UsersRouter(db=db, settings=config)
    languages = LanguagesRouter(db=db, settings=config)
    groups = GroupsRouter(db=db, settings=config)
    messages = MessagesRouter(db=db, settings=config)

    db.connect()

    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods="*",
        allow_headers="*",
    )
    app.include_router(users.router)
    app.include_router(languages.router)
    app.include_router(groups.router)
    app.include_router(messages.router)

    @app.get("")
    def app_is_running():
        return {"message": "App is running"}

    @app.websocket("/ws/{id}/{username}/{admin_id}")
    async def websocket_server(websocket: WebSocket, id: str, username: str, admin_id: str):
        response = await connection_manager.connect(
            ws=websocket, id=id, username=username, db=db, config=config, admin_id=admin_id
        )
        if "message" in response:
            try:
                while True:
                    data = await websocket.receive_text()
                    message = json.loads(data)
                    if (message["type"] == "message"):
                        service =MessagesService(db=db, settings=config)
                        response = await service.create(message["data"])
                        if "fail" in response:
                            data = {"type": "fail", "data": response["fail"]}
                            await connection_manager.broadcast(message=data)
                        else: await connection_manager.broadcast(message=message)

            except WebSocketDisconnect:
                await connection_manager.disconnect(id=id)
                disconnect_message = f"Client #{id} left the chat"
                await connection_manager.broadcast(disconnect_message)
        else: websocket.send_json({"type": "fail", "data": response["fail"]})
    
    return {"app": app, "config": config}
