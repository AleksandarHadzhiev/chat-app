from fastapi import APIRouter

from src.messages.controller import MessagesController


class MessagesRouter:
    
    def __init__(self, db, settings):
        self.router = APIRouter(prefix="/messages")
        self.controller = MessagesController(db=db, settings=settings)
        self.router.add_api_route(
            "/{group_id}", self.controller.get_all, methods=["GET"]
        )
        self.router.add_api_route(
            "/{group_id}/last-message", self.controller.get_last_message, methods=["GET"]
        )
        self.router.add_api_route(
            "/", self.controller.edit, methods=["PUT"]
        )
        self.router.add_api_route(
            "/{code}", self.controller.delete, methods=["DELETE"]
        )
