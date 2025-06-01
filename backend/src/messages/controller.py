import json

from fastapi import Request, Response, status

from src.messages.service import MessagesService
from src.utils.authentication import Authenticator, User

class MessagesController:
    def __init__(self, db, settings):
        self.service = MessagesService(db=db, settings=settings)
        self.auth = Authenticator(config=settings, db=db)

    async def get_all(self, group_id, request: Request):
        if (await self._is_authorized(request=request) == False):
            return Response(content=json.dumps({"fail": "Unauthorized"}), status_code=status.HTTP_401_UNAUTHORIZED)
        messages = self.service.get_all(group_id=group_id)
        if messages != []:
            if "fail" in messages:
                return Response(content=json.dumps(messages), status_code=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(
                content=json.dumps({"messages": messages}),
                status_code=status.HTTP_200_OK,
            )
        return Response(
            content=json.dumps({"messages": []}), status_code=status.HTTP_204_NO_CONTENT
        )

    async def _is_authorized(self, request: Request):
        headers = request.headers
        if "authorization" in headers:
            token = headers["authorization"]
            user: User= await self.auth.get_current_user(token=token)
            if "fail" in user:
                return False
            elif user.verified == False:
                return False
            return True
        return False

    async def edit(self, request: Request):
        if (await self._is_authorized(request=request) == False):
            return Response(content=json.dumps({"fail": "Unauthorized"}), status_code=status.HTTP_401_UNAUTHORIZED)
        data = await request.json()
        response = await self.service.edit(data=data)
        if "fail" in response:
            return Response(content=json.dumps(response), status_code=status.HTTP_400_BAD_REQUEST)
        return Response(content=json.dumps(response), status_code=status.HTTP_200_OK)

    async def delete(self, request: Request):
        if (await self._is_authorized(request=request) == False):
            return Response(content=json.dumps({"fail": "Unauthorized"}), status_code=status.HTTP_401_UNAUTHORIZED)
        queries = request.query_params
        code = queries.get("code")
        group_id = queries.get("group_id")
        user_Id = queries.get("user_id")
        response = self.service.delete(code, group_id, user_Id)
        if "fail" in response:
            return Response(content=json.dumps(response), status_code=status.HTTP_400_BAD_REQUEST)
        return Response(content=json.dumps(response), status_code=status.HTTP_200_OK)

    async def get_last_message(self, group_id, request: Request):
        if (await self._is_authorized(request=request) == False):
            return Response(content=json.dumps({"fail": "Unauthorized"}), status_code=status.HTTP_401_UNAUTHORIZED)
        message = self.service.get_last_message(group_id=group_id)
        if message:
            if "fail" in message:
                return Response(content=json.dumps(message), status_code=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(
                content=json.dumps({"message": message}),
                status_code=status.HTTP_200_OK,
            )
        return Response(
            content=json.dumps({"messages": []}), status_code=status.HTTP_204_NO_CONTENT
        )