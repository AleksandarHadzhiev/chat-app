from src.languages.translations.base import Base


class NavigationEnglishTranlsations(Base):
    def __init__(self):
        self.translations = {
            "login": "Login",
            "home": "Home",
            "account": "Account",
            "groups": "Groups",
        }

    def get_translations(self) -> dict:
        return self.translations
