from src.languages.translations.base import Base


class GroupsEnglishTranlsations(Base):
    def __init__(self):
        self.translations = {
            "join": "Join",
            "leave": "Leave",
            "cancel": "Cancel",
            "submit": "Submit",
            "search": "Search",
            "edit": "Edit",
            "delete": "Delete",
            "kick": "Kick member out",
            "name": "Name",
            "current name": "Current name",
            "new name": "New name",
            "loading": "Loacding...",
            "role": "Role",
            "actions": "Actions",
            "members": "Members:",
            "created group": "You have created a group. Make it popular.",
            "edited": "You have changed the name of the group.",
            "deleted": "You have deleted the group.",
            "left":"You have left the group",
            "kicked": "You have kicked the member out of the group."     
        }

    def get_translations(self) -> dict:
        return self.translations
