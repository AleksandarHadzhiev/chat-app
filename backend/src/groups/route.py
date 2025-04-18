from fastapi import APIRouter
from src.groups.controller import GroupsController

class GroupsRouter():
    def __init__(self, db, settings):
        self.router = APIRouter(prefix="/groups")
        self.controller = GroupsController(db=db, settings=settings)
        self.router.add_api_route("/", self.controller.create, methods=["POST"])
        self.router.add_api_route("/user/{user_id}", self.controller.get_all_for_user, methods=["GET"])
        self.router.add_api_route("/", self.controller.get_all, methods=["GET"])
        self.router.add_api_route("/{id}", self.controller.get_group, methods=["GET"])
        self.router.add_api_route("/{id}", self.controller.edit, methods=["POST"])
        self.router.add_api_route("/{id}", self.controller.delete, methods=["POST"])
        self.router.add_api_route("/{account}/join/{group}", self.controller.join, methods=["POST"])
        self.router.add_api_route("/{account}/leave/{group}", self.controller.leave, methods=["POST"])
        self.router.add_api_route("/{id}/kick/{member}", self.controller.kick_member_out, methods=["POST"])