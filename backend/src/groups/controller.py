import json

from fastapi import Request, Response, status

from src.groups.service import GroupsService


class GroupsController:
    def __init__(self, db, settings):
        self.service = GroupsService(db=db, settings=settings)

    async def create(self, requet: Request):
        data = await requet.json()
        response = self.service.create(incoming_data=data)
        if "fail" in response:
            return Response(
                content=json.dumps(response), status_code=status.HTTP_400_BAD_REQUEST
            )
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
        if "fail" in response:
            return Response(
                content=json.dumps(response), status_code=status.HTTP_400_BAD_REQUEST
            )
        return Response(content=json.dumps(response), status_code=status.HTTP_200_OK)

    async def leave(self, account, group):
        data = {
            "group_id": group,
            "user_id": account
        }
        response = await self.service.leave(incoming_data=data)
        if "fail" in response:
            return Response(
                content=json.dumps(response), status_code=status.HTTP_400_BAD_REQUEST
            )
        return Response(content=json.dumps(response), status_code=status.HTTP_200_OK)

    async def kick_member_out(self, id, member, admin):
        data = {}
        data["user_id"] = admin
        data["group_id"] = id
        data["member_id"] = member
        response = await self.service.kick_member_out(incoming_data=data)
        if "fail" in response:
            return Response(
                content=json.dumps(response), status_code=status.HTTP_400_BAD_REQUEST
            )
        return Response(content=json.dumps(response), status_code=status.HTTP_200_OK)

    async def delete(self, id, admin):
        data = {
            "group_id":id,
            "user_id":admin
        }
        response = await self.service.delete(incoming_data=data)
        if "fail" in response:
            return Response(
                content=json.dumps(response), status_code=status.HTTP_400_BAD_REQUEST
            )
        return Response(content=json.dumps(response), status_code=status.HTTP_200_OK)

    async def edit(self, id, request: Request):
        data = await request.json()
        data["group_id"] = id
        response = await self.service.edit(incoming_data=data)
        if "fail" in response:
            return Response(
                content=json.dumps(response), status_code=status.HTTP_400_BAD_REQUEST
            )
        return Response(content=json.dumps(response), status_code=status.HTTP_200_OK)

    async def get_group(self, request: Request):
        data = await request.json()
        response = self.service.get_group(incoming_data=data)
        if "fail" in response:
            return Response(
                content=json.dumps(response), status_code=status.HTTP_400_BAD_REQUEST
            )
        return Response(content=json.dumps(response), status_code=status.HTTP_200_OK)
