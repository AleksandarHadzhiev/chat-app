from src.languages.translations.base import Base


class RegistrationTranslations(Base):
    def __init__(self):
        self.translations = {
            "stepOne": "User Data",
            "stepTwo": "Verification",
            "stepThree": "Confirmation",
            "email":"Email",
            "exampple": "example@gmail.com",
            "password": "Password",
            "username": "Username",
            "forgot-password": "Forgot password?",
            "here": "Here",
            "button": "Continue",
            "account": "You have an account?",
            "sign in": "Sing in",
            "code": "Code",
            "thanks": "Thank you for registering."
        }


    def get_translations(self) -> dict:
        return self.translations