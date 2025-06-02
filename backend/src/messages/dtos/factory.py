from src.messages.dtos.base import BaseDTO
from src.messages.dtos.edit_message import EditMessageDTO
from src.messages.dtos.message_dto import MessageDTO
from src.messages.repositories.repository import Repository


class DTOFactory:
    def __init__(self, data, settings, rep: Repository = None):
        self.rep = rep
        self.data = data
        self.settings = settings
        self.supported_formats = [
            [
                {
                    "content": "",
                    "group_id": int(0),
                    "created_at": "",
                    "user_id": int(0),
                    "author": "",
                    "code": "",
                },
                MessageDTO(),
            ],
            [
                {"content": "", "code": "", "user_id": int(0), "group_id": int(0)},
                EditMessageDTO(),
            ],
        ]

    def get_dto(self) -> BaseDTO:
        for dto in self.supported_formats:
            keys = list(dict(dto[0]).keys())
            data_keys = list(self.data.keys())
            if data_keys == keys:
                _dto: BaseDTO = dto[1]
                _dto.set(data=self.data, settings=self.settings, rep=self.rep)
                return _dto
        return None
