from src.languages.translations.base import Base


class MessagesDutchTranlsations(Base):
    def __init__(self):
        self.translations = {
            "search": "Zoekopdracht ...",
            "write": "Schrijf een bericht...",
            "writing": "is/zijn aan het schrijven",
            "refactor": "Bericht bewerken",
            "edit": "Bewerking",
            "delete": "Verwijderen",
            "missing-id": "",
            "fail": "Failed due: ",
            "Incorrect data": "",
            "undefined-user": "",
            "undefined-group": "",
            "empty-author": "",
            "empty-content": "",
            "offensive-speech": "",
            "empty-created_at": "",
            "empty-code": "",
            "success": "",
        }

    def get_translations(self) -> dict:
        return self.translations
