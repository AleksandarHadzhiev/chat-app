from fastapi import FastAPI

from config import ConfigFactory
from src.db.db_factory import DBFactory


def create_app(server="dev"):
    
    config = ConfigFactory(type=server).get_config()
    db = DBFactory(config.DATABASE_URL).get_db()
    app = FastAPI()
    print(config)
    @app.get("/")
    async def root():
        return {"message": "Hello, World!"}


    return app