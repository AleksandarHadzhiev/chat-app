from src.languages.translations.base import Base


class DutchLoginTranlsations(Base):
    def __init__(self):
        self.translations = {
            "header": "Welkom terug",
            "login": "Login",
            "email": "E-mail",
            "exampple": "voorbeeld@gmail.com",
            "password": "Wachtwoord",
            "forgot-password": "Wachtwoord vergeten?",
            "here": "Hier",
            "button": "Aanmelden",
            "account": "Heb je nog geen account?",
            "signup": "Zing mee",
            "fail": "Mislukt vanwege: ",
            "empty-email": "Lege e-mail",
            "empty-password": "Leeg wachtwoord",
            "wrong-credentials": "Het e-mailadres of wachtwoord is onjuist",
            "user-not-found": "De gebruiker bestaat niet.",
            "unverified": "De gebruiker is niet geverifieerd.",
        }

    def get_translations(self) -> dict:
        return self.translations
