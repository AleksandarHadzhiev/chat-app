from src.languages.translations.base import Base


class RegistrationTranslations(Base):
    def __init__(self):
        self.translations = {
            "stepOne": "User Data",
            "stepTwo": "Verification",
            "stepThree": "Confirmation",
            "email": "Email",
            "exampple": "example@gmail.com",
            "password": "Password",
            "username": "Username",
            "forgot-password": "Forgot password?",
            "here": "Here",
            "button": "Continue",
            "account": "You have an account?",
            "sign in": "Sing in",
            "code": "Code",
            "thanks": "Thank you for registering.",
            "success": "Thank you for registering. You have received an email, please check it!",
            "fail": "Failed due to: ",
            "empty-email": "Empty email",
            "empty-password": "Empty password",
            "empty-username": "Empty username",
            "empty-code": "Empty code",
            "invalid-code": "Invalid code",
            "unverified": "The provided email or code is unverified",
            "offensive-speech": "The provided username is deemed offensive. Please choose different username.",
        }

    def get_translations(self) -> dict:
        return self.translations
