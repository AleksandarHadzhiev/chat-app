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
            "thanks": "Bedankt voor uw registratie.",
            "success": "Bedankt voor uw registratie. U hebt een e-mail ontvangen, controleer deze!",
            "fail": "Mislukt vanwege: ",
            "empty-email": "Lege e-mail",
            "empty-password": "Leeg wachtwoord",
            "empty-username": "Lege gebruikersnaam",
            "empty-code": "Lege code",
            "invalid-code": "Ongeldige code",
            "unverified": "Het opgegeven e-mailadres of de code is niet geverifieerd"
        }


    def get_translations(self) -> dict:
        return self.translations