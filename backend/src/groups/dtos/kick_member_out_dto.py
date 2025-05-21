from src.groups.dtos.base import BaseDTO
from src.groups.dtos.fields.group_id import GroupIdField
from src.groups.dtos.fields.user_id import UserIdField
from src.groups.dtos.fields.member_id import MemberIdField

class KickMemberOutDTO(BaseDTO):
    def set(self, data, settings):
        self.settings = settings
        self.errors = []
        self.set_group_id(data=data)
        self.set_user_id(data=data)
        self.set_member_id(data=data)

    def set_group_id(self, data):
        response = GroupIdField(
            data=data["group_id"], settings=self.settings
        ).validate_data()
        if type(response) == str:
            self.errors.append(response)
        else:
            self.group_id = response["group_id"]

    def set_user_id(self, data):
        response = UserIdField(
            data=data["user_id"], settings=self.settings
        ).validate_data()
        if type(response) == str:
            self.errors.append(response)
        else:
            self.user_id = response["user_id"]

    def set_member_id(self, data):
        response = MemberIdField(
            data=data["member_id"], settings=self.settings
        ).validate_data()
        if type(response) == str:
            self.errors.append(response)
        else:
            self.member_id = response["member_id"]

    def validate_data(self):
        if len(self.errors) > 0:
            return {"fail": self.errors}
        return {
            "group_id": self.group_id,
            "user_id": self.user_id,
            "member_id": self.member_id
        }