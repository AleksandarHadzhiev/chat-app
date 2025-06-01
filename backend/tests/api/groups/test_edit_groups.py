import json

import pytest

from tests.global_fixtures.boot_up import client as api

test_data = [
    (
        0,
        {"admin": "", "title": ""},
        {
            "status": 400,
            "json": {"fail": ["empty-title", "empty-admin", "invalid-group_id"]},
        },
    ),
    (
        1,
        {"admin": "", "title": ""},
        {"status": 400, "json": {"fail": ["empty-title", "empty-admin"]}},
    ),
    (
        1,
        {"admin": "1", "title": ""},
        {"status": 400, "json": {"fail": ["empty-title"]}},
    ),
    (
        1,
        {"admin": "0", "title": ""},
        {"status": 400, "json": {"fail": ["empty-title", "invalid-admin"]}},
    ),
    (
        1,
        {"admin": "0", "title": "s"},
        {
            "status": 400,
            "json": {
                "fail": [
                    "invalid-admin",
                ]
            },
        },
    ),
    (
        1,
        {"admin": "1", "title": ""},
        {
            "status": 400,
            "json": {
                "fail": [
                    "empty-title",
                ]
            },
        },
    ),
    (
        1,
        {"admin": "", "title": "s"},
        {
            "status": 400,
            "json": {
                "fail": [
                    "empty-admin",
                ]
            },
        },
    ),
    (
        1,
        {"admin": "1", "title": "new-name"},
        {"status": 200, "json": {"message": "edited"}},
    ),
]


@pytest.mark.order(3)
@pytest.mark.parametrize("id, data, outcome", test_data)
def test_edit_groups(api, id, data, outcome):
    response = api.put(f"/groups/{id}", content=json.dumps(data))
    assert response.status_code == outcome["status"]
    assert response.json() == outcome["json"]
