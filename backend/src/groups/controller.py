import json

from fastapi import Request, Response, status

from src.groups.service import GroupsService


class GroupsController:
    def __init__(self, db, settings):
        self.service = GroupsService(db=db, settings=settings)

    async def create(self, requet: Request):
        data = await requet.json()
        print(data)
        response = self.service.create(incoming_data=data)
        return Response(
            content=json.dumps(response), status_code=status.HTTP_201_CREATED
        )

    async def get_all_for_user(self, user_id):
        groups = self.service.get_all_for_user(user_id=user_id)
        return Response(
            content=json.dumps({"groups": groups}), status_code=status.HTTP_200_OK
        )

    async def get_all(self):
        groups = self.service.get_all()
        return Response(
            content=json.dumps({"groups": groups}), status_code=status.HTTP_200_OK
        )

    async def join(self, account, group):
        response = self.service.join(account, group)
        return Response(content=json.dumps(response), status_code=status.HTTP_200_OK)

    async def leave(self, request: Request):
        print(request)

    async def kick_member_out(self, request: Request):
        print(request)

    async def delete(self, request: Request):
        print(request)

    async def edit(self, request: Request):
        print(request)

    async def get_group(self, request: Request):
        print(request)
