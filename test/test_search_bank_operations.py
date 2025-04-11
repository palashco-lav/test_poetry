import json

from src.search_bank_operations import count_transactions_by_category, filter_transactions


def test_filter_transactions(test_get_json_list: str) -> None:
    """Проверка функции filter_transactions"""
    data = json.loads(test_get_json_list)
    result = filter_transactions(data, "Перевод")

    assert len(result) == 2

    result = filter_transactions(data, "Открытие")

    assert len(result) == 1


def test_count_transactions_by_category(test_get_json_list: str) -> None:
    """Проверка функции count_transactions_by_category"""

    categories = ["Открытие вклада", "Перевод со счета на счет", "Перевод организации", "Перевод с карты на карту"]
    data = json.loads(test_get_json_list)
    result = count_transactions_by_category(data, categories)

    assert result == {"Открытие вклада": 1, "Перевод организации": 2}
