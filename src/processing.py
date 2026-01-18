from datetime import datetime
from typing import Any


def filter_by_state(
    operations: list[dict[str, Any]],
    state: str = "EXECUTED",
) -> list[dict[str, Any]]:
    """
    Фильтрует список операций по значению ключа state.

    :param operations: список словарей с данными операций
    :param state: значение state для фильтрации (по умолчанию 'EXECUTED')
    :return: новый список операций с указанным state
    """
    return [
        operation
        for operation in operations
        if operation.get("state") == state
    ]


def sort_by_date(
    operations: list[dict[str, Any]],
    descending: bool = True,
) -> list[dict[str, Any]]:
    """
    Сортирует список операций по дате.

    :param operations: список словарей с данными операций
    :param descending: порядок сортировки (по умолчанию убывание)
    :return: новый список операций, отсортированный по дате
    """
    return sorted(
        operations,
        key=lambda operation: datetime.fromisoformat(operation["date"]),
        reverse=descending,
    )
