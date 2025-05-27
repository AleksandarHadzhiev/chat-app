import json
import pytest
from tests.global_fixtures.boot_up import client as api

test_data = [
    ({"title": "", "admin": ""}, {"status": 400, "json":{'fail': ['empty-admin', 'empty-title']}}),
    ({"title": "ss", "admin": ""}, {"status": 400, "json":{'fail': ['empty-admin']}}),
    ({"title": "", "admin": "1"}, {"status": 400, "json":{'fail': ['empty-title']}}),
    ({"title": "INVALID-ADMIN", "admin": "0"}, {"status": 400, "json":{'fail': ['invalid-admin',]}}),
    ({"title": "VALUD-ADMIN", "admin": "2"}, {"status": 201, "json": {'message': 'created group'}}),
]


@pytest.mark.order(2)
@pytest.mark.parametrize("data, outcome", test_data)
def test_create_groups(api, data, outcome):
    response = api.post("/groups", content=json.dumps(data))
    assert response.status_code == outcome["status"]
    assert response.json() == outcome["json"]
