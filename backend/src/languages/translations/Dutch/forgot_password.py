from src.languages.translations.base import Base


class DutchForgotPasswordTranslations(Base):
    def __init__(self):
        self.translations = {
            "header": "Wachtwoord vergeten",
            "email": "E-mail",
            "example": "voorbeeld@gmail.com",
            "fail": "Mislukt vanwege: ",
            "button": "Indienen",
            "account": "Heb je nog geen account?",
            "signup": "Zing mee",
            "empty-email": "De e-mail is leeg",
            "invalid-email": "Het e-mailformaat is ongeldig",
            "user-not-found": "Gebruiker bestaat niet.",
            "unverified": "Gebruiker is niet geverifieerd.",
        }

    def get_translations(self) -> dict:
        return self.translations
