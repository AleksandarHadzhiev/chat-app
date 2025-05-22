from src.languages.translations.base import Base


class EnglishEmailsTranslations(Base):
    def __init__(self):
        self.translations = {
            "verification_subject": "Verification Code",
            "verification_body": "Thank you for registering. This is your verification code",
            "warning": "If that was not you, or the action is no longer needed. Ignore this message",
            "reset_subject": "Reset Password",
            "reset_body": "Here is the link to reset your password: "
        }

    def get_translations(self) -> dict:
        return self.translations
