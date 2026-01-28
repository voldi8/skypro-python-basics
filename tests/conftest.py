import pytest


@pytest.fixture
def operations():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-01-01T00:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2020-01-01T00:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2018-01-01T00:00:00"},
        {"id": 4, "date": "2017-01-01T00:00:00"},  # без state
    ]
