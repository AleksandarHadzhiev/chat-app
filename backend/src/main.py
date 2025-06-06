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
from src.utils.authentication import Authenticator
from src.utils.rsa_generator import RSAGenerator
from src.websocket.ws_server import ConnectionManager


def create_app(server="test", password="secret-key-placeholder"):
    rsa_gen = RSAGenerator(password=password)
    private_key = rsa_gen.get_private_key()
    public_key = rsa_gen.get_public_key()
    config = ConfigFactory(type=server).get_config()
    config.set_secret_key(key=private_key)
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
        user = await auth.get_current_user(token=access_token)
        if "fail" in user:
            await websocket.accept()
            await websocket.send_json(
                json.dumps({"type": "fail", "data": "Unauthorized"})
            )
        else:
            response = await connection_manager.connect(
                ws=websocket, user=user, db=db, config=config, admin_id=admin_id
            )
            if "message" in response:
                try:
                    while True:
                        data = await websocket.receive_text()
                        message = json.loads(data)
                        if message["type"] == "message":
                            await _send_message(message=message, user=user)
                        elif message["type"] == "notification":
                            await _send_notificatio(message=message, user=user)
                except WebSocketDisconnect:
                    await connection_manager.disconnect(id=user.id)
            else:
                websocket.send_json({"type": "fail", "data": response["fail"]})

    async def _send_message(message, user):
        message["data"]["user_id"] = user.id
        message["data"]["author"] = user.username
        group_id = message["data"]["group_id"]
        code = connection_manager.generate_special_code(
            user_id=user.id, group_id=group_id
        )
        message["data"]["code"] = code
        service = MessagesService(db=db, settings=config)
        response = await service.create(message["data"])
        await _handle_broadcast(response=response, message=message)

    async def _handle_broadcast(response, message):
        if "fail" in response:
            data = {"type": "fail", "data": response["fail"]}
            await connection_manager.broadcast(message=data)
        else:
            await connection_manager.broadcast(message=message)

    async def _send_notificatio(message, user):
        message["data"]["user"] = user.username
        await connection_manager.broadcast(message=message)

    return {"app": app, "config": config}
