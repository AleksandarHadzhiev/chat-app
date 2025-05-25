"""Starting point of the application"""


class Config:
    """Base config."""

    DATABASE_URL = ""
    FRONTEND_URL = ""
    FRONTEND_URL = ""
    ENVIRONMENT = ""
    CODE_LENGTH = 4


class ConfigFactory:
    """Config factory for using the appropriate environment configuration."""

    def __init__(self, type):
        """Init the facotry."""
        self.type = type
        self.types = {
            "dev": DevConfig(),
            "test": TestConfig(),
            "docker": DockerConfig(),
        }

    def get_config(self) -> Config:
        """Get the environment config."""
        if self.type in self.types:
            return self.types[self.type]
        return None


class DevConfig(Config):
    """Development config."""

    ENVIRONMENT = "dev"

    USERNAME = "user"
    PASSWORD = "user"
    HOST = "localhost"
    DATABASE_PORT = "5432"
    DATABASE_DB = "users"
    FRONTEND_URL = "https://localhost:3000"


class TestConfig(Config):
    """Test config."""

    ENVIRONMENT = "test"

    FRONTEND_URL = "https://localhost:3000"
    USERNAME = "test"
    PASSWORD = "test"
    HOST = "localhost"
    DATABASE_PORT = "5432"
    DATABASE_DB = "test"


class DockerConfig(Config):
    """Docker config."""

    ENVIRONMENT = "docker"

    USERNAME = "docker"
    PASSWORD = "docker"
    HOST = "database"
    DATABASE_PORT = "5432"
    DATABASE_DB = "docker"
    FRONTEND_URL = "https://localhost:3000"

