import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [1, 3]),
        ("CANCELED", [2]),
        ("PENDING", []),
    ],
)
def test_filter_by_state_param(operations, state, expected_ids):
    result = filter_by_state(operations, state=state)
    assert [op["id"] for op in result] == expected_ids
    assert all(op.get("state") == state for op in result)


def test_filter_by_state_ignores_missing_state_key(operations):
    # операция без ключа state не должна ломать функцию и не должна попадать в результат
    result = filter_by_state(operations, state="EXECUTED")
    ids = [op["id"] for op in result]
    assert 4 not in ids


def test_sort_by_date_descending(operations):
    result = sort_by_date(operations, descending=True)
    assert [op["id"] for op in result] == [2, 1, 3, 4]


def test_sort_by_date_ascending(operations):
    result = sort_by_date(operations, descending=False)
    assert [op["id"] for op in result] == [4, 3, 1, 2]


def test_sort_by_date_missing_date_raises_keyerror():
    with pytest.raises(KeyError):
        sort_by_date([{"id": 1, "state": "EXECUTED"}])


def test_sort_by_date_bad_date_raises_valueerror():
    with pytest.raises(ValueError):
        sort_by_date([{"id": 1, "state": "EXECUTED", "date": "not-iso-date"}])


def test_sort_by_date_same_dates_keeps_relative_order() -> None:
    ops = [
        {"id": 1, "date": "2020-01-01T00:00:00"},
        {"id": 2, "date": "2020-01-01T00:00:00"},
        {"id": 3, "date": "2019-01-01T00:00:00"},
    ]
    # Python sorted() стабилен: элементы с одинаковым ключом сохраняют порядок
    result = sort_by_date(ops, descending=True)
    assert [op["id"] for op in result] == [1, 2, 3]

