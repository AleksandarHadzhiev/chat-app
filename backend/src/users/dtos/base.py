from src.users.repositories.repository import Repository


class BaseDTO:
    def set(self, data, settings, rep: Repository = None):
        pass

    async def validate_data(self) -> dict:
        pass

    async def execute_validation(self) -> dict:
        pass
