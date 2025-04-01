class Config:
    DATABASE_URL = ""
    FRONTEND_URL = ""
    FRONTEND_URL = ""
    ENVIRONMENT = ""


class ConfigFactory:
    def __init__(self, type="dev"):
        self.type = type
        self.types = {"dev": DevConfig(), "test": TestConfig(), "docker": DockerConfig()}

    def get_config(self) -> Config:
        if self.type in self.types:
            return self.types[self.type]


class DevConfig(Config):
    ENVIRONMENT = "dev"
    
    USERNAME = "user"
    PASSWORD = "user"
    HOST = "localhost"
    DATABASE_PORT = "5432"
    DATABASE_DB = "users"
    ENVIRONMENT = "dev"
    FRONTEND_URL = "https://localhost:3000"

class TestConfig(Config):
    ENVIRONMENT = "test"
    
    FRONTEND_URL = "https://localhost:3000"
    DATABASE_URL = f"sqlite:///"    


class DockerConfig(Config):
    ENVIRONMENT = "docker"

    HOST = "database"
    FRONTEND_URL = "https://localhost:3000" # When the dockerization is complete will be changed
    DATABASE_NAME = "employees"
    DATABASE_USER = "user"
    DATABASE_PASSWORD = "password"
    PORT_NUMBER = 3306 
