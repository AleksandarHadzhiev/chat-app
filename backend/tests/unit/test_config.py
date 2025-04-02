from config import ConfigFactory

def test_create_dev_config():
    env = "dev"
    config = ConfigFactory(type=env).get_config()
    assert config.ENVIRONMENT == env


def test_create_test_config():
    env = "test"
    config = ConfigFactory(type=env).get_config()
    assert config.ENVIRONMENT == env


def test_create_docker_config():
    env = "docker"
    config = ConfigFactory(type=env).get_config()
    assert config.ENVIRONMENT == env


def test_create_no_config():
    env = "no"
    config = ConfigFactory(type=env).get_config()
    assert config == None