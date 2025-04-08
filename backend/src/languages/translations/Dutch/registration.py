from src.languages.translations.base import Base


class DutchRegistrationTranslations(Base):
    def __init__(self):
        self.translations ={
            "stepOne": "Gebruikersgegevens",
            "stepTwo": "Verificatie",
            "stepThree": "Bevestiging",
            "email":"E-mail",
            "exampple": "voorbeeld@gmail.com",
            "password": "Wachtwoord",
            "username": "Gebruikersnaam",
            "button": "Doorgaan",
            "account": "Je hebt een account?",
            "sign in": "Aanmelden",
            "code": "Code",
            "thanks": "Bedankt voor uw registratie."
        }


    def get_translations(self) -> dict:
        return self.translations