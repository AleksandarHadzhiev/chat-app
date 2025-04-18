from src.languages.translations.base import Base


class ResetPasswordTranslations(Base):
    def __init__(self):
        self.translations = {
            "header": "Reset Password",
            "password": "Password",
            "button": "Submit",
            "account": "You don't have an account?",
            "signup": "Sing up",
        }

    def get_translations(self) -> dict:
        return self.translations
