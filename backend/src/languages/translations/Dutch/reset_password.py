from src.languages.translations.base import Base


class DutchResetPasswordTranslations(Base):
    def __init__(self):
        self.translations = {
            "header": "Wachtwoord opnieuw instellen",
            "password": "Wachtwoord",
            "button": "Indienen",
            "example": "example@email.com",
            "account": "Heb je nog geen account?",
            "signup": "Zing mee",
            "missing-code":"Code niet verstrekt",
            "missing-email":"E-mailadres niet opgegeven",
            "unauthorized":"Je hebt geen toegang tot deze pagina.",
            "authorized":"",
            "user-not-found":"Gebruiker bestaat niet.",
            "unverified": "Het opgegeven e-mailadres of de code is niet geverifieerd.",
            "empty-password": "Leeg wachtwoord",
            "empty-email": "Lege e-mail",
            "invalid-email":"Ongeldig e-mailadres",
            "empty-code": "Lege code",
            "invalid-code": "Ongeldige code",
            "fail": "Mislukt vanwege:",
            "success":"Uw wachtwoord is gereset."
        }

    def get_translations(self) -> dict:
        return self.translations
