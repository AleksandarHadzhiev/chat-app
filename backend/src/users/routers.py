from fastapi import APIRouter

from src.users.controller import UsersController


class UsersRouter:
    def __init__(self, db, settings):
        self.router = APIRouter()
        self.controller = UsersController(db=db, settings=settings)
        self.router.add_api_route(
            "/register", self.controller.register, methods=["POST"]
        )
        self.router.add_api_route(
            "/verification", self.controller.verify, methods=["POST"]
        )
        self.router.add_api_route("/login", self.controller.login, methods=["POST"])
        self.router.add_api_route(
            "/forgot-password", self.controller.forgot_password, methods=["POST"]
        )
        self.router.add_api_route(
            "/reset-password", self.controller.reset_password, methods=["POST"]
        )
