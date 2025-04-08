from src.languages.translations.base import Base

class ForgotPasswordTranslations(Base):
    def __init__(self):
        self.translations = {
            "header": "Forgot Password",
            "email": "Email",
            "exampple": "example@gmail.com",
            "button": "Submit",
            "account": "You don't have an account?",
            "signup": "Sing up"
        }
        

    def get_translations(self) -> dict:
        return self.translations