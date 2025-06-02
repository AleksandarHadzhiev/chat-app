from src.groups.repositories.repository import Repository


class BaseDTO:
    def set(self, data, settings, rep: Repository = None):
        pass

    def validate_data(self) -> dict:
        pass
