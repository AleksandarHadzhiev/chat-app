from src.users.dtos.base import BaseDTO
from src.users.dtos.code import CodeDTO
from src.users.dtos.forgot_password import ForgotPasswordDTO
from src.users.dtos.login_dto import LoginDTO
from src.users.dtos.reset_password_dto import ResetPasswordDTO
from src.users.dtos.user_dto import UserDTO
from src.users.repositories.repository import Repository


class DTOFactory:
    def __init__(self, data, settings=None, rep: Repository = None):
        self.rep = rep
        self.incomind_data = data
        self.settings = settings
        self.supported_formats = [
            [{"email": "", "password": "", "username": ""}, UserDTO()],
            [{"email": "", "code": ""}, CodeDTO()],
            [{"email": "", "password": ""}, LoginDTO()],
            [{"email": ""}, ForgotPasswordDTO()],
            [{"email": "", "code": "", "password": ""}, ResetPasswordDTO()],
        ]

    def get_dto(self) -> BaseDTO:
        for dto in self.supported_formats:
            keys = list(dict(dto[0]).keys())
            incoming_keys = list(self.incomind_data.keys())
            if incoming_keys == keys:
                _dto: BaseDTO = dto[1]
                _dto.set(data=self.incomind_data, settings=self.settings, rep=self.rep)
                return _dto
        return None
