from fastapi import APIRouter

from src.groups.controller import GroupsController


class GroupsRouter:
    def __init__(self, db, settings):
        self.router = APIRouter(prefix="/groups")
        self.controller = GroupsController(db=db, settings=settings)
        self.router.add_api_route("/", self.controller.create, methods=["POST"])
        self.router.add_api_route(
            "/{user_id}", self.controller.get_all_for_user, methods=["GET"]
        )
        self.router.add_api_route("/", self.controller.get_all, methods=["GET"])
        self.router.add_api_route("/{id}", self.controller.get_group, methods=["GET"])
        self.router.add_api_route("/{id}", self.controller.edit, methods=["PUT"])
        self.router.add_api_route("/{id}/{admin}", self.controller.delete, methods=["DELETE"])
        self.router.add_api_route(
            "/{account}/join/{group}", self.controller.join, methods=["POST"]
        )
        self.router.add_api_route(
            "/{account}/leave/{group}", self.controller.leave, methods=["POST"]
        )
        self.router.add_api_route(
            "/{id}/kick/{member}/{admin}", self.controller.kick_member_out, methods=["DELETE"]
        )
