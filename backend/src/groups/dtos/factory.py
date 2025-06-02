from src.groups.dtos.base import BaseDTO
from src.groups.dtos.create_group_dto import CreateGroupDTO
from src.groups.dtos.edit_group_dto import EditGroupDTO
from src.groups.dtos.join_group_dto import JoinGroupDTO
from src.groups.dtos.kick_member_out_dto import KickMemberOutDTO
from src.groups.repositories.repository import Repository


class DTOFactory:
    def __init__(self, data, settings, repository: Repository):
        self.incomind_data = data
        self.settings = settings
        self.rep = repository
        self.supported_formats = [
            [{"title": "", "admin": ""}, CreateGroupDTO()],
            [{"group_id": "", "user_id": ""}, JoinGroupDTO()],
            [{"user_id": "", "group_id": "", "member_id": ""}, KickMemberOutDTO()],
            [{"admin": "", "title": "", "group_id": ""}, EditGroupDTO()],
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
