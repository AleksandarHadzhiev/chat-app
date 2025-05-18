import json

from fastapi import Request, Response, status

from src.messages.service import MessagesService


class MessagesController:
    def __init__(self, db, settings):
        self.service = MessagesService(db=db, settings=settings)

    def get_all(self, group_id):
        messages = self.service.get_all(group_id=group_id)
        if messages != []:
            return Response(
                content=json.dumps({"messages": messages}),
                status_code=status.HTTP_200_OK,
            )
        return Response(
            content=json.dumps({"messages": []}), status_code=status.HTTP_204_NO_CONTENT
        )

    async def edit(self, request: Request):
        data = await request.json()
        print(data)
        response = self.service.edit(data=data)
        if "fail" in response:
            return Response(content=json.dumps(response), status_code=status.HTTP_400_BAD_REQUEST)
        return Response(content=json.dumps(response), status_code=status.HTTP_200_OK)

    async def delete(self, code):
        response = self.service.delete(code)
        if "fail" in response:
            return Response(content=json.dumps(response), status_code=status.HTTP_400_BAD_REQUEST)
        return Response(content=json.dumps(response), status_code=status.HTTP_200_OK)
