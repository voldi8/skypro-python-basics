import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        (1234567812345678, "1234 56** **** 5678"),
        (7000792289606361, "7000 79** **** 6361"),
    ],
)
def test_get_mask_card_number_ok(card_number: int, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "card_number",
    [
        123,                 # < 16 цифр
        12345678123456789,   # 17 цифр
        -1234567812345678,   # '-' -> isdigit() False
    ],
)
def test_get_mask_card_number_bad(card_number: int) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


@pytest.mark.parametrize(
    "account_number, expected",
    [
        (73654108430135874305, "**4305"),
        (1234, "**1234"),
    ],
)
def test_get_mask_account_ok(account_number: int, expected: str) -> None:
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize(
    "account_number",
    [
        123,     # < 4 цифр
        -12345,  # '-' -> isdigit() False
    ],
)
def test_get_mask_account_bad(account_number: int) -> None:
    with pytest.raises(ValueError):
        get_mask_account(account_number)
