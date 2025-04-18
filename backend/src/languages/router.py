from fastapi import APIRouter

from src.languages.controller import LanguagesController


class LanguagesRouter:
    def __init__(self, db, settings):
        self.router = APIRouter(prefix="/languages")
        self.controller = LanguagesController(db=db, settings=settings)
        self.router.add_api_route("/", self.controller.get_lanugaes, methods=["GET"])
        self.router.add_api_route("/", self.controller.add_language, methods=["POST"])
        self.router.add_api_route(
            "/translations/{language}/{file}",
            self.controller.get_translations,
            methods=["GET"],
        )
        self.router.add_api_route(
            "/translations", self.controller.add_translations, methods=["POST"]
        )
