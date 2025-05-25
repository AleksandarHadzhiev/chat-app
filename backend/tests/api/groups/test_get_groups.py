import pytest
from tests.global_fixtures.boot_up import client as api

test_data = [
    ("/groups/", {"status": 200, "json":{'groups': [{'id': 1, 'title': 'General Group Chat', 'admin_id': 1, 'members': [{'id': 1, 'name': 'administrator'}, {'id': 2, 'name': 'test-01'}]}]}}),
    ("/groups/user/1", {"status": 200, "json":{'groups': [{'id': 1, 'title': 'General Group Chat', 'admin_id': 1, 'members': [{'id': 1, 'name': 'administrator'}]}]}}),
    ("/groups/user/25", {"status": 200, "json":{'groups': []}}),
    ("/groups/user/0", {"status": 200, "json":{'groups': []}}),
    ("/groups/user/s", {"status": 400, "json":{'fail': 'invalid'}}),
]

@pytest.mark.parametrize("url, outcome", test_data)
def test_groups(api, url, outcome):
    response = api.get(url)
    assert response.status_code == outcome["status"]
    assert response.json() == outcome["json"]
