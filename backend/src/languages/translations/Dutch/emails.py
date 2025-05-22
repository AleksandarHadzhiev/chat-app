from src.languages.translations.base import Base


class DutchEmailsTranslations(Base):
    def __init__(self):
        self.translations = {
            "verification_subject": "Verificatiecode",
            "verification_body": "Bedankt voor uw registratie. Dit is uw verificatiecode",
            "warning": "Als u dat niet was, of als de actie niet langer nodig is, negeer dan dit bericht.",
            "reset_subject": "Wachtwoord opnieuw instellen",
            "reset_body": "Hier is de link om uw wachtwoord opnieuw in te stellen"
        }

    def get_translations(self) -> dict:
        return self.translations
