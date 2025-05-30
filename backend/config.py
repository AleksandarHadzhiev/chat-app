"""Starting point of the application"""


class Config:
    """Base config."""
    SMTP_SERVER = ""
    SECRET_KEY = ""
    SMTP_PORT = 1025
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    ENVIRONMENT = ""
    BASE_URL = ""
    USERNAME = ""
    PASSWORD = ""
    HOST = ""
    DATABASE_PORT = ""
    DATABASE_DB = ""
    FRONTEND_URL = ""
    CODE_LENGTH = 4
    
    def set_secret_key(self, key):
        self.SECRET_KEY = key


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
    SECRET_KEY = "secret-key-placeholder"
    SMTP_SERVER = "127.0.0.1"
    SMTP_PORT = 1025
    ENVIRONMENT = "dev"
    BASE_URL = "127.0.0.1"
    USERNAME = "user"
    PASSWORD = "user"
    HOST = "localhost"
    DATABASE_PORT = "5432"
    DATABASE_DB = "users"
    FRONTEND_URL = "https://localhost:3000"


class TestConfig(Config):
    """Test config."""
    SECRET_KEY = "secret-key-placeholder"
    SMTP_SERVER = "127.0.0.1"
    SMTP_PORT = 1025
    ENVIRONMENT = "test"
    BASE_URL = "127.0.0.1"
    FRONTEND_URL = "https://localhost:3000"
    USERNAME = "test"
    PASSWORD = "test"
    HOST = "localhost"
    DATABASE_PORT = "5432"
    DATABASE_DB = "test"


class DockerConfig(Config):
    """Docker config."""
    SECRET_KEY = "secret-key-placeholder"
    SMTP_SERVER = "mailhog"
    SMTP_PORT = 1025
    ENVIRONMENT = "docker"
    BASE_URL = "0.0.0.0"
    USERNAME = "docker"
    PASSWORD = "docker"
    HOST = "database"
    DATABASE_PORT = "5432"
    DATABASE_DB = "docker"
    FRONTEND_URL = "https://localhost:3000"

