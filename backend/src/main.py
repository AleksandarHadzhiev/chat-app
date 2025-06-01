import json
from contextlib import asynccontextmanager

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from src.utils.authentication import Authenticator
from config import ConfigFactory
from src.db.db_factory import DBFactory
from src.groups.route import GroupsRouter
from src.languages.router import LanguagesRouter
from src.messages.router import MessagesRouter
from src.messages.service import MessagesService
from src.users.routers import UsersRouter
from src.websocket.ws_server import ConnectionManager


def create_app(server="test", secret="secret-key-placeholder", public_key="key-placeholder"):
    config = ConfigFactory(type=server).get_config()
    config.set_secret_key(key=secret)
    config.set_public_key(key=public_key)
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

    @app.websocket("/ws/{access_token}/{admin_id}")
    async def websocket_server(websocket: WebSocket, access_token: str, admin_id: str):
        auth = Authenticator(config=config, db=db)
        user =  await auth.get_current_user(token=access_token)
        if "fail" in user:
            await websocket.accept()
            await websocket.send_json(json.dumps({"type": "fail", "data": "Unauthorized" }))
        else:
            response = await connection_manager.connect(
                ws=websocket, user=user, db=db, config=config, admin_id=admin_id
            )
            if "message" in response:
                try:
                    while True:
                        data = await websocket.receive_text()
                        message = json.loads(data)
                        if (message["type"] == "message"):
                            message["data"]["user_id"]=user.id
                            message["data"]["author"]=user.username
                            group_id = message["data"]["group_id"]
                            code = connection_manager.generate_special_code(user_id=user.id, group_id=group_id)
                            message["data"]["code"]=code
                            service =MessagesService(db=db, settings=config)
                            response = await service.create(message["data"])
                            if "fail" in response:
                                data = {"type": "fail", "data": response["fail"]}
                                await connection_manager.broadcast(message=data)
                            else: await connection_manager.broadcast(message=message)
                        elif message["type"] == "notification":
                            message["data"]["user"] = user.username
                            await connection_manager.broadcast(message=message)

                except WebSocketDisconnect:
                    await connection_manager.disconnect(id=user.id)
            else: websocket.send_json({"type": "fail", "data": response["fail"]})
        
    return {"app": app, "config": config}
