import json

from fastapi import Request, Response, status

from src.groups.service import GroupsService
from src.utils.authentication import Authenticator, User


class GroupsController:
    def __init__(self, db, settings):
        self.service = GroupsService(db=db, settings=settings)
        self.auth = Authenticator(config=settings, db=db)

    async def create(self, request: Request):
        if await self._is_authorized(request=request) == False:
            return Response(
                content=json.dumps({"fail": "Unauthorized"}),
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        data = await request.json()
        response = await self.service.create(incoming_data=data)
        if "fail" in response:
            return Response(
                content=json.dumps(response), status_code=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            content=json.dumps(response), status_code=status.HTTP_201_CREATED
        )

    async def _is_authorized(self, request: Request):
        headers = request.headers
        if "authorization" in headers:
            token = headers["authorization"]
            user: User = await self.auth.get_current_user(token=token)
            if "fail" in user:
                return False
            elif user.verified == False:
                return False
            return True
        return False

    async def get_all_for_user(self, user_id, request: Request):
        if await self._is_authorized(request=request) == False:
            return Response(
                content=json.dumps({"fail": "Unauthorized"}),
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        groups = self.service.get_all_for_user(user_id=user_id)
        if "fail" in groups:
            return Response(
                content=json.dumps(groups), status_code=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            content=json.dumps({"groups": groups}), status_code=status.HTTP_200_OK
        )

    async def get_all(self, request: Request):
        if await self._is_authorized(request=request) == False:
            return Response(
                content=json.dumps({"fail": "Unauthorized"}),
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        groups = self.service.get_all()
        return Response(
            content=json.dumps({"groups": groups}), status_code=status.HTTP_200_OK
        )

    async def join(self, account, group, request: Request):
        if await self._is_authorized(request=request) == False:
            return Response(
                content=json.dumps({"fail": "Unauthorized"}),
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        response = self.service.join(account, group)
        if "fail" in response:
            return Response(
                content=json.dumps(response), status_code=status.HTTP_400_BAD_REQUEST
            )
        return Response(content=json.dumps(response), status_code=status.HTTP_200_OK)

    async def leave(self, account, group, request: Request):
        if await self._is_authorized(request=request) == False:
            return Response(
                content=json.dumps({"fail": "Unauthorized"}),
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        data = {"group_id": group, "user_id": account}
        response = await self.service.leave(incoming_data=data)
        if "fail" in response:
            return Response(
                content=json.dumps(response), status_code=status.HTTP_400_BAD_REQUEST
            )
        return Response(content=json.dumps(response), status_code=status.HTTP_200_OK)

    async def kick_member_out(self, id, member, admin, request: Request):
        if await self._is_authorized(request=request) == False:
            return Response(
                content=json.dumps({"fail": "Unauthorized"}),
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
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

    async def delete(self, id, admin, request: Request):
        if await self._is_authorized(request=request) == False:
            return Response(
                content=json.dumps({"fail": "Unauthorized"}),
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        data = {"group_id": id, "user_id": admin}
        response = await self.service.delete(incoming_data=data)
        if "fail" in response:
            return Response(
                content=json.dumps(response), status_code=status.HTTP_400_BAD_REQUEST
            )
        return Response(content=json.dumps(response), status_code=status.HTTP_200_OK)

    async def edit(self, id, request: Request):
        if await self._is_authorized(request=request) == False:
            return Response(
                content=json.dumps({"fail": "Unauthorized"}),
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        data = await request.json()
        data["group_id"] = id
        response = await self.service.edit(incoming_data=data)
        if "fail" in response:
            return Response(
                content=json.dumps(response), status_code=status.HTTP_400_BAD_REQUEST
            )
        return Response(content=json.dumps(response), status_code=status.HTTP_200_OK)

    async def get_group(self, request: Request):
        if await self._is_authorized(request=request) == False:
            return Response(
                content=json.dumps({"fail": "Unauthorized"}),
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        data = await request.json()
        response = self.service.get_group(incoming_data=data)
        if "fail" in response:
            return Response(
                content=json.dumps(response), status_code=status.HTTP_400_BAD_REQUEST
            )
        return Response(content=json.dumps(response), status_code=status.HTTP_200_OK)
