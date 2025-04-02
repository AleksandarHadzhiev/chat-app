from fastapi import FastAPI

from config import ConfigFactory
from src.db.db_factory import DBFactory


def create_app(server="dev"):

    config = ConfigFactory(type=server).get_config()
    db = DBFactory(config.ENVIRONMENT, settings=config).get_db()
    app = FastAPI()

    @app.get("/")
    async def root():
        db.create_db_and_tables()
        return {"message": "Hello, World!"}

    return app
