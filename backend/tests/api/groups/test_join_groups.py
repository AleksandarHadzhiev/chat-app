import json
import pytest
from tests.global_fixtures.boot_up import client as api

test_data = [
    (0, 0, {"status": 400, "json":{'fail': ['invalid-group_id', 'invalid-user_id']}}),
    (1, 0, {"status": 400, "json":{'fail': ['invalid-group_id']}}),
    (0, 1, {"status": 400, "json":{'fail': ['invalid-user_id']}}),
    (1, 1, {"status": 400, "json":{'fail': 'already a member'}}),
    (1, 2, {"status": 200, "json": {'message': 'joined'}}),
]


@pytest.mark.order(5)
@pytest.mark.parametrize("account_id, group_id, outcome", test_data)
def test_join_groups(api, account_id, group_id, outcome):
    response = api.post(f"groups/{account_id}/join/{group_id}")
    assert response.status_code == outcome["status"]
    assert response.json() == outcome["json"]
