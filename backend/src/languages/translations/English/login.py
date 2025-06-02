from src.languages.translations.base import Base


class LoginTranlsations(Base):
    def __init__(self):
        self.translations = {
            "header": "Welcome back",
            "login": "Login",
            "email": "Email",
            "exampple": "example@gmail.com",
            "password": "Password",
            "forgot-password": "Forgot password?",
            "here": "Here",
            "button": "Sign in",
            "account": "You don't have an account?",
            "signup": "Sing up",
            "fail": "Failed due to: ",
            "empty-email": "Empty email",
            "empty-password": "Empty password",
            "wrong-credentials": "Either email or password is incorrect",
            "user-not-found": "The user doesn't exist.",
            "unverified": "The user is not verified.",
        }

    def get_translations(self) -> dict:
        return self.translations
