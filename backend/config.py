class Config:
    DATABASE_URL = ""
    FRONTEND_URL = ""
    FRONTEND_URL = ""


class ConfigFactory:
    def __init__(self, type="dev"):
        self.type = type
        self.types = {"dev": DevConfig(), "test": TestConfig()}

    def get_config(self) -> Config:
        if self.type in self.types:
            return self.types[self.type]


class DevConfig(Config):
    USERNAME = "user"
    PASSWORD = "user"
    FRONTEND_URL = "https://localhost:3000"
    DATABASE_URL = f"postgresql://postgres:{USERNAME}#{PASSWORD}@localhost/dev"


class TestConfig(Config):
    USERNAME = "test"
    PASSWORD = "test"
    FRONTEND_URL = "https://localhost:3000"
    DATABASE_URL = f"sqlite:///"
