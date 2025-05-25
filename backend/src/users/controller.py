import json

from fastapi import Request, Response, status

from src.users.service import UsersService


class UsersController:
    def __init__(self, db, settings):
        self.service = UsersService(db=db, settings=settings)

    async def register(self, request: Request):
        data: dict = await request.json()
        language = data.pop("language")
        response = await self.service.register(incoming_data=data, language=language)
        if "fail" in response:
            return Response(
                content=json.dumps(response), status_code=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            content=json.dumps(response), status_code=status.HTTP_201_CREATED
        )

    async def is_allowed_action(self, request: Request):
        data: dict = await request.json()
        
        response = await self.service.is_allowed_action(data=data)
        if "fail" in response:
            return Response(
                content=json.dumps(response), status_code=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            content=json.dumps(response), status_code=status.HTTP_201_CREATED
        )
            

    async def verify(self, request: Request):
        data = await request.json()
        response = await self.service.verify(incoming_data=data)
        if "fail" in response:
            return Response(
                content=json.dumps(response), status_code=status.HTTP_400_BAD_REQUEST
            )
        return Response(content=json.dumps(response), status_code=status.HTTP_200_OK)

    async def login(self, request: Request):
        data = await request.json()
        response = await self.service.login(incoming_data=data)
        if "fail" in response:
            return Response(
                content=json.dumps(response), status_code=status.HTTP_400_BAD_REQUEST
            )
        return Response(content=json.dumps(response), status_code=status.HTTP_200_OK)

    async def forgot_password(self, request: Request):
        data:dict = await request.json()
        language = data.pop("language")
        response = await self.service.forgot_password(incoming_data=data, language=language)
        if "fail" in response:
            return Response(
                content=json.dumps(response), status_code=status.HTTP_400_BAD_REQUEST
            )
        return Response(content=json.dumps(response), status_code=status.HTTP_200_OK)

    async def reset_password(self, request: Request):
        data = await request.json()
        response = await self.service.reset_password(incoming_data=data)
        if "fail" in response:
            return Response(
                content=json.dumps(response), status_code=status.HTTP_400_BAD_REQUEST
            )
        return Response(content=json.dumps(response), status_code=status.HTTP_200_OK)
