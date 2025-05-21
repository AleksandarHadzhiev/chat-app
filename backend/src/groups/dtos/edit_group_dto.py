from src.groups.dtos.base import BaseDTO
from src.groups.dtos.fields.admin import AdminField
from src.groups.dtos.fields.title import TitleField
from src.groups.dtos.fields.group_id import GroupIdField

class EditGroupDTO(BaseDTO):
    def set(self, data, settings):
        self.settings = settings
        self.errors = []
        self.set_title(data=data)
        self.set_admin(data=data)
        self.set_group_id(data=data)

    def set_title(self, data):
        response = TitleField(
            data=data["title"], settings=self.settings
        ).validate_data()
        if type(response) == str:
            self.errors.append(response)
        else:
            self.title = response["title"]

    def set_admin(self, data):
        response = AdminField(
            data=data["admin"], settings=self.settings
        ).validate_data()
        if type(response) == str:
            self.errors.append(response)
        else:
            self.admin = response["admin"]

    def set_group_id(self, data):
        response = GroupIdField(
            data=data["group_id"], settings=self.settings
        ).validate_data()
        if type(response) == str:
            self.errors.append(response)
        else:
            self.group_id = response["group_id"]

    def validate_data(self):
        if len(self.errors) > 0:
            return {"fail": self.errors}
        return {
            "title": self.title,
            "admin": self.admin,
            "group_id": self.group_id
        }
