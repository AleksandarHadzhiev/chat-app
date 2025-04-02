from config import ConfigFactory
from src.db.db_factory import DBFactory
from src.db.mysql import MySQL
from src.db.postgres import PostgresSQL
from src.db.sqlite import SQLite


def test_create_dev_config():
    env = "dev"
    config = ConfigFactory(type=env).get_config()
    db_factory = DBFactory(env=env, settings=config)
    db = db_factory.get_db()
    assert config.ENVIRONMENT == env
    assert type(db) == type(PostgresSQL())


def test_create_test_config():
    env = "test"
    config = ConfigFactory(type=env).get_config()
    db_factory = DBFactory(env=env, settings=config)
    db = db_factory.get_db()
    assert config.ENVIRONMENT == env
    assert type(db) == type(SQLite())


def test_create_docker_config():
    env = "docker"
    config = ConfigFactory(type=env).get_config()
    db_factory = DBFactory(env=env, settings=config)
    db = db_factory.get_db()

    assert config.ENVIRONMENT == env
    assert type(db) == type(MySQL())


def test_create_none():
    env = "None"
    config = ConfigFactory(type=env).get_config()

    assert config == None

    db_factory = DBFactory(env=env, settings=config)
    db = db_factory.get_db()

    assert db == None
