from src.languages.translations.base import Base


class ResetPasswordTranslations(Base):
    def __init__(self):
        self.translations = {
            "header": "Reset Password",
            "password": "Password",
            "button": "Submit",
            "example": "example@email.com",
            "account": "You don't have an account?",
            "signup": "Sing up",
            "missing-code":"Code not provided",
            "missing-email":"Email not provided",
            "unauthorized":"You have no access to this page.",
            "authorized":"",
            "user-not-found":"User does not exist.",
            "unverified": "The provided email or code is unverified.",
            "empty-password": "Empty password",
            "empty-email": "Empty email",
            "invalid-email":"Invalid email",
            "empty-code": "Empty code",
            "invalid-code": "Invalid code",
            "fail": "Failed due to: ",
            "success":"Your password has been reset."
        }

    def get_translations(self) -> dict:
        return self.translations
