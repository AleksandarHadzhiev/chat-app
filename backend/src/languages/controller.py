import json

from fastapi import Request

from src.languages.service import LanguagesService


class LanguagesController:
    def __init__(self, db, settings):
        self.service = LanguagesService(db=db, settings=settings)

    async def get_lanugaes(self, request: Request):
        response = self.service.get_languages()
        return json.dumps(response)

    async def add_language(self, request: Request):
        data = await request.json()
        return self.service.add_language(incoming_data=data)

    async def get_translations(self, language: str, file: str):
        data = {"language": language, "file": file}
        return json.dumps(self.service.get_translations(data=data))

    async def add_translations(self, request: Request):
        data = await request.json()
        return self.service.add_translations(email=data)
