from fastapi.testclient import TestClient
import pytest

from src.main import create_app


@pytest.fixture(scope="session")
def client():
    app = create_app(server="test")
    client = TestClient(app=app)
    return client
