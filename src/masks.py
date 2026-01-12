"""Функции маскировки банковских реквизитов."""


def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер банковской карты.

    Принимает номер карты и возвращает строку в формате:
    XXXX XX** **** XXXX
    """
    card_str = str(card_number)

    if len(card_str) != 16 or not card_str.isdigit():
        raise ValueError("Номер карты должен состоять из 16 цифр")

    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер банковского счёта.

    Возвращает строку в формате:
    **XXXX
    """
    acc_str = str(account_number)

    if len(acc_str) < 4 or not acc_str.isdigit():
        raise ValueError("Номер счёта должен содержать минимум 4 цифры")

    return f"**{acc_str[-4:]}"
