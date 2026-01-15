from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(source: str) -> str:
    """
    Принимает строку с типом и номером карты или счета и возвращает строку
    с замаскированным номером.

    Примеры входных данных:
    - "Visa Platinum 7000792289606361"
    - "Maestro 7000792289606361"
    - "Счет 73654108430135874305"
    """
    value = source.strip()
    name, number = value.rsplit(" ", 1)

    name_normalized = name.lower().replace("ё", "е")
    if name_normalized.startswith("счет"):
        return f"{name} {get_mask_account(int(number))}"

    return f"{name} {get_mask_card_number(int(number))}"


def get_date(source: str) -> str:
    """
    Преобразует строку даты в формате ISO
    (например: "2024-03-11T02:26:18.671407")
    в строку формата "ДД.ММ.ГГГГ".
    """
    date_time = datetime.fromisoformat(source)
    return date_time.strftime("%d.%m.%Y")
