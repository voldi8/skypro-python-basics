"""
Тесты для функции пересечения списков.
"""

from src.intersections import intersections


def test_intersections_basic() -> None:
    """Базовый кейс: пересечение двух списков."""
    assert intersections([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]


def test_intersections_preserves_order_of_a() -> None:
    """Порядок результата соответствует порядку элементов в списке a."""
    assert intersections([4, 3, 2, 3], [3, 4]) == [4, 3, 3]


def test_intersections_with_duplicates_in_b() -> None:
    """Дубликаты во втором списке не влияют на результат."""
    assert intersections([1, 2, 2, 3], [2, 2]) == [2, 2]


def test_intersections_no_common() -> None:
    """Если общих элементов нет — возвращается пустой список."""
    assert intersections([1, 2], [3, 4]) == []
