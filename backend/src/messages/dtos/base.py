class BaseDTO:
    def set(self, data, settings):
        pass

    def validate_data(self) -> dict:
        pass

    async def execute_validation(self) -> dict:
        pass
