from fastapi import APIRouter

from src.messages.controller import MessagesController


class MessagesRouter:
    def __init__(self, db, settings):
        self.router = APIRouter(prefix="/messages")
        self.controller = MessagesController(db=db, settings=settings)
        self.router.add_api_route(
            "/{group_id}", self.controller.get_all, methods=["GET"]
        )
