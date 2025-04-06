from src.users.service import UsersService
from fastapi import Request
import json

class UsersController():
    def __init__(self, db, settings):
        self.service = UsersService(db=db, settings=settings)


    async def register(self, request: Request):
        data = await request.json()
        return self.service.register(incoming_data=data)


    async def verify(self, request: Request):
        data = await request.json()
        return self.service.verify(incoming_data=data)

    async def login(self, request: Request):
        data = await request.json()
        return json.dumps(self.service.login(incoming_data=data))


    async def forgot_password(self, request: Request):
        data = await request.json()
        return self.service.forgot_password(incoming_data=data)


    async def reset_password(self, request: Request):
        data = await request.json()
        return self.service.reset_password(incoming_data=data)