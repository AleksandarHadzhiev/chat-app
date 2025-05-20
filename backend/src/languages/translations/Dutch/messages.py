from src.languages.translations.base import Base


class MessagesDutchTranlsations(Base):
    def __init__(self):
        self.translations = {
            "search": "Zoekopdracht ...",
            "write": "Schrijf een bericht...",
            "writing": "is/zijn aan het schrijven",
            "refactor": "Bericht bewerken",
            "edit": "Bewerking",
            "delete": "Verwijderen"
        }

    def get_translations(self) -> dict:
        return self.translations
