import json
from fastapi import Request, Response, status
from src.messages.service import MessagesService

class MessagesController:
    def __init__(self, db, settings):
        self.service = MessagesService(db=db, settings=settings)


    def get_all(self, group_id):
        messages = self.service.get_all(group_id=group_id)
        if messages != []:
            return Response(content=json.dumps({"messages": messages}), status_code=status.HTTP_200_OK)
        return Response(content=json.dumps({"messages":[]}), status_code=status.HTTP_204_NO_CONTENT)