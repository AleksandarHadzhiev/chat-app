from fastapi import FastAPI, WebSocketDisconnect, WebSocket

from config import ConfigFactory
from src.websocket.ws_server import ConnectionManager
from src.db.db_factory import DBFactory
from fastapi.middleware.cors import CORSMiddleware


def create_app(server="dev"):

    config = ConfigFactory(type=server).get_config()
    db = DBFactory(config.ENVIRONMENT, settings=config).get_db()
    app = FastAPI()
    origins = [
        "http://localhost:3000/"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods="*",
        allow_headers="*"
    )
    
    connection_manager = ConnectionManager()
    @app.get("/")
    async def root():
        db.create_db_and_tables()
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
