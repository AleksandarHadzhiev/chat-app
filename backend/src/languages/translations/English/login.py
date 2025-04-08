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
        "signup": "Sing up"
    }


    def get_translations(self) -> dict:
        return self.translations