```markdown
# Виджет банковских операций

## Цель проекта
Проект предназначен для обработки и отображения банковских операций клиента.
Реализованы функции фильтрации операций по статусу и сортировки по дате.

## Установка
1. Клонировать репозиторий
2. Установить зависимости:
```bash
poetry install
```

## Использование

### Фильтрация операций по статусу

Функция `filter_by_state` возвращает список операций с заданным статусом
(по умолчанию — `EXECUTED`).

```python
from src.processing import filter_by_state

operations = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
]

executed_operations = filter_by_state(operations)
canceled_operations = filter_by_state(operations, "CANCELED")
```

### Сортировка операций по дате

```python
from src.processing import sort_by_date

sorted_operations = sort_by_date(operations)
```
