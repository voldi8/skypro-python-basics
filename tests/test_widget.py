import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "source, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1234567812345678", "Maestro 1234 56** **** 5678"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счёт 73654108430135874305", "Счёт **4305"),  # 'ё' нормализуется для распознавания
        ("   Счет 73654108430135874305   ", "Счет **4305"),  # strip() должен сработать
    ],
)
def test_mask_account_card_ok(source: str, expected: str) -> None:
    assert mask_account_card(source) == expected


@pytest.mark.parametrize(
    "bad_source",
    [
        "Visa Platinum",       # нет номера -> rsplit(" ", 1) не распакуется
        "Visa Platinum abcd",  # int("abcd") -> ValueError
        "Счет abcd",           # int("abcd") -> ValueError
        "",                    # rsplit не распакуется
        "   ",                 # rsplit не распакуется
    ],
)
def test_mask_account_card_bad_input(bad_source: str) -> None:
    with pytest.raises(ValueError):
        mask_account_card(bad_source)


@pytest.mark.parametrize(
    "source, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2020-01-01T00:00:00", "01.01.2020"),
    ],
)
def test_get_date_ok(source: str, expected: str) -> None:
    assert get_date(source) == expected


@pytest.mark.parametrize(
    "bad_source",
    [
        "not-a-date",
        "2024/03/11",
        "",
        "   ",
    ],
)
def test_get_date_bad_input(bad_source: str) -> None:
    with pytest.raises(ValueError):
        get_date(bad_source)
