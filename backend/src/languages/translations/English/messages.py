from src.languages.translations.base import Base


class MessagesEnglishTranlsations(Base):
    def __init__(self):
        self.translations = {
            "search": "Search ...",
            "write": "Write a message...",
            "writing": "is/are writing",
            "refactor": "Edit message",
            "edit": "Edit",
            "delete": "Delete",
            "missing-id": "Afzender ontbreekt",
            "fail":"Mislukt vanwege: ",
            "Incorrect data":"Gegevens zijn onjuist",
            "undefined-user":"Schrijver niet gedefinieerd",
            "undefined-group": "Doel niet gedefinieerd",
            "empty-author": "Auteur ontbreekt",
            "empty-content": "Inhoud ontbreekt",
            "offensive-speech": "U heeft aanstootgevende taal gebruikt.",
            "empty-created_at":"Aanmaakdatum ontbreekt",
            "empty-code":"Code is niet opgegeven",
            "success":"",
            "is-not-member": "Geen lid van de groep.",
            "is-not-author": "Niet uw bericht."
        }

    def get_translations(self) -> dict:
        return self.translations
