import random
import string

from src.emails.mailhog_smtp import SMTPServer
from src.users.dtos.factory import DTOFactory
from src.users.repositories.factory import RepositoryFactory


class UsersService:
    def __init__(self, db, settings):
        self.settings = settings
        self.db = db
        self.repository = RepositoryFactory(db=db).get_db()
        self.code_length = settings.CODE_LENGTH
        self.verifications = {}

    async def login(self, incoming_data):
        factory = DTOFactory(data=incoming_data, settings=self.settings, rep=self.repository)
        dto = factory.get_dto()
        data = await dto.execute_validation()
        if "fail" in data:
            return data
        response = self.repository.login(data=data)
        if response:
            return response
        return {"error": "wrong-credentials"}

    async def is_allowed_action(self, code: str, email: str):
        if code is None or code.replace(" ", "") == "":
            return {"fail": "missing-code"}
        elif email is None or email.replace(" ", "") == "":
            return {"fail": "missing-email"}
        elif email not in self.verifications or self.verifications[email] != code:
            return {"fail": "unauthorized"}
        else: return {"message": "authorized"}
        

    async def register(self, incoming_data, language: str):
        factory = DTOFactory(data=incoming_data, settings=self.settings, rep=self.repository)
        dto = factory.get_dto()
        data = await dto.execute_validation()
        print(data)
        if "fail" in data:
            return data
        email = data["email"]
        code = self._generate_code(email=email)
        email_data = {
            "body": code,
            "receiver": email
        }
        if "unverified" not in data:
            self.repository.register(data=data)
            self._email_flow(data=email_data, language=language)
        else:
            await self.repository.update_user(data=data)
            self._email_flow(data=email_data, language=language)
        return {"message": "success"}

    def _email_flow(self, data, language="EN", subject="verification"):
        smtp = SMTPServer(language=language, subject=subject)
        smtp.send_email(data=data["body"], email=data["receiver"])

    def _generate_code(self, email):
        code = ""
        index = 0
        while index < self.code_length:
            index += 1
            code += random.choice(string.ascii_letters)
        self.verifications[email] = code
        return code

    async def verify(self, incoming_data):
        factory = DTOFactory(data=incoming_data, settings=self.settings)
        dto = factory.get_dto()
        data = await dto.execute_validation()
        code = data["code"]
        email = data["email"]
        if "fail" in data:
            return data
        if self.verifications[email] == code:
            self.repository.verify(email=email)
            return {"message": "success"}
        return {"error": "unverified"}

    async def forgot_password(self, incoming_data, language: str):
        factory = DTOFactory(data=incoming_data, settings=self.settings, rep=self.repository)
        dto = factory.get_dto()
        data = await dto.execute_validation()

        if "fail" in data:
            return data
        email_data = {
            "body": self._generate_url_for_reset_password(data=data),
            "receiver": data["email"]
        }
        self._email_flow(data=email_data, language=language, subject="reset")
        return {"message": "success"}

    def _generate_url_for_reset_password(self, data):
        code = self._generate_code(email=data["email"])
        url = f"http://localhost:3000/reset-password?code={code}&email={data["email"]}"
        return url

    async def reset_password(self, incoming_data):
        factory = DTOFactory(data=incoming_data, settings=self.settings, rep=self.repository)
        dto = factory.get_dto()
        data = await dto.execute_validation()
        if "fail" in data:
            return data
        if self.verifications[data["email"]] == data["code"]:
            self.repository.reset_password(data=data)
            return {"message": "success"}
        return {"error": "unverified"}
