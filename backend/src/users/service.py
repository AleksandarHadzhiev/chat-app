import random
import string
from src.users.repositories.factory import RepositoryFactory
from src.users.dtos.factory import DTOFactory
from src.emails.mailhog_smtp import SMTPServer


class UsersService():
    def __init__(self, db, settings):
        self.settings = settings
        self.db = db
        self.repository = RepositoryFactory(db=db).get_db()
        self.code_length = settings.CODE_LENGTH
        self.verifications = {}


    def login(self, incoming_data):
        factory = DTOFactory(data=incoming_data, settings=self.settings)
        dto = factory.get_dto()
        data = dto.validate_data()
        if "fail" in data:
            return data
        response = self.repository.login(data=data)
        if response:
            print(response)
            return response
        return {"error":"wrong-credentials"}


    def register(self, incoming_data):
        factory = DTOFactory(data=incoming_data, settings=self.settings)
        dto = factory.get_dto()
        data = dto.validate_data()
        if "fail" in data:
            return data
        self.repository.register(data=data)
        self._email_flow(data)
        return {"message": "success"}


    def _email_flow(self, data):
        email = data["email"]
        code = self._generate_code(email=email)
        smtp = SMTPServer()
        smtp.send_email(code=code, email=email)
        return code


    def _generate_code(self, email):
        code = ""
        index = 0
        while index < self.code_length:
            index+=1
            code += random.choice(string.ascii_letters)
        self.verifications[email] = code
        return code


    def verify(self, incoming_data):
        factory = DTOFactory(data=incoming_data, settings=self.settings)
        dto = factory.get_dto()
        data = dto.validate_data()
        code = data["code"]
        email = data["email"]
        if "fail" in data:
            return data
        if self.verifications[email] == code:
            self.repository.verify(email=email)
            return {"message": "success"}
        return {"error": "unverified"}


    def forgot_password(self, incoming_data):
        factory = DTOFactory(data=incoming_data, settings=self.settings)
        dto = factory.get_dto()
        data = dto.validate_data()
        response = self.repository.get_by_email(data=data)
        if response is None:
            return {"fail": "User does not exist or is not verified."}
        self._email_flow(data=data)


    def reset_password(self, incoming_data):
        factory = DTOFactory(data=incoming_data, settings=self.settings)
        dto = factory.get_dto()
        data = dto.validate_data()
        self.repository.reset_password(data=data)
        return {"message": "Your password has been reset. Login again to complete the process."}
