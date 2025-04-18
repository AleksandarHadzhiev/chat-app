from src.languages.translations.base import Base


class DutchForgotPasswordTranslations(Base):
    def __init__(self):
        self.translations = {
            "header": "Wachtwoord vergeten",
            "email": "E-mail",
            "exampple": "voorbeeld@gmail.com",
            "button": "Indienen",
            "account": "Heb je nog geen account?",
            "signup": "Zing mee",
        }

    def get_translations(self) -> dict:
        return self.translations
