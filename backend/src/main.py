from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from config import ConfigFactory
from src.db.db_factory import DBFactory
from src.websocket.ws_server import ConnectionManager
from src.users.routers import UsersRouter
from src.languages.router import LanguagesRouter
def create_app(server="dev"):

    config = ConfigFactory(type=server).get_config()
    db = DBFactory(config.ENVIRONMENT, settings=config).get_db()
    app = FastAPI()
    origins = ["http://localhost:3000"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods="*",
        allow_headers="*",
    )

    connection_manager = ConnectionManager()
    users = UsersRouter(db=db, settings=config)
    languages = LanguagesRouter(db=db, settings=config)
    app.include_router(users.router)
    app.include_router(languages.router)

    @app.on_event("startup")
    def bootup():
        db.create_db_and_tables()

    @app.get("/")
    async def root():
        return {"message": "Hello, World!"}

    @app.websocket("/ws/{id}")
    async def websocket_server(websocket: WebSocket, id: str):
        await connection_manager.connect(ws=websocket, id=id)
        try:
            while True:
                data = await websocket.receive_text()
                data = f"{id}: {data}"
                await connection_manager.broadcast(id=id, data=data)
        except WebSocketDisconnect:
            connection_manager.disconnect(id=id)
            disconnect_message = f"Client #{id} left the chat"
            await connection_manager.broadcast(id, disconnect_message)

    return app
