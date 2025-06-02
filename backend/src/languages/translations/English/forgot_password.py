from src.languages.translations.base import Base


class ForgotPasswordTranslations(Base):
    def __init__(self):
        self.translations = {
            "header": "Forgot Password",
            "fail": "Failed due to: ",
            "email": "Email",
            "example": "example@gmail.com",
            "button": "Submit",
            "account": "You don't have an account?",
            "signup": "Sing up",
            "empty-email": "The email is empty",
            "invalid-email": "The email format is invalid",
            "user-not-found": "User does not exist.",
            "unverified": "User is not verified.",
            "success": "You have received an email. Check it to continue.",
        }

    def get_translations(self) -> dict:
        return self.translations
