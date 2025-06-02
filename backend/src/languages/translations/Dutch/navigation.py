from src.languages.translations.base import Base


class NavigationDutchTranlsations(Base):
    def __init__(self):
        self.translations = {
            "login": "Login",
            "home": "Startpagina",
            "account": "Rekening",
            "groups": "Groepen",
        }

    def get_translations(self) -> dict:
        return self.translations
