from src.languages.translations.base import Base


class DutchResetPasswordTranslations(Base):
    def __init__(self):
        self.translations = {
            "header": "Wachtwoord opnieuw instellen",
            "password": "Wachtwoord",
            "button": "Indienen",
            "account": "Heb je nog geen account?",
            "signup": "Zing mee",
        }

    def get_translations(self) -> dict:
        return self.translations
