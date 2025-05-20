from src.languages.translations.base import Base


class MessagesEnglishTranlsations(Base):
    def __init__(self):
        self.translations = {
            "search": "Search ...",
            "write": "Write a message...",
            "writing": "is/are writing",
            "refactor": "Edit message",
            "edit": "Edit",
            "delete": "Delete"
        }

    def get_translations(self) -> dict:
        return self.translations
