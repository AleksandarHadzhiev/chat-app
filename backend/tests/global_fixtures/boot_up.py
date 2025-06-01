import pytest
from fastapi.testclient import TestClient

from src.main import create_app


@pytest.fixture(scope="session")
def client():
    app = create_app(server="test")["app"]
    client = TestClient(app=app)
    return client
