import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card(fix_widget_test: list) -> None:
    """Проверка правильности преобразования значений функции"""
    for i in range(len(fix_widget_test)):
        assert mask_account_card(fix_widget_test[i].get("string")) == fix_widget_test[i].get("expected_result")


def test_mask_account_card_wrong_number() -> None:
    """Ошибки при передаче неверных параметров"""
    with pytest.raises(ValueError):
        mask_account_card("Maestro1596837868705199")

    with pytest.raises(ValueError):
        mask_account_card("Счет64686473678894779589")

    with pytest.raises(ValueError):
        mask_account_card("Visa Platinum Maestro")

    with pytest.raises(ValueError):
        mask_account_card("Счет Gold")


def test_mask_account_card_empy() -> None:
    """Ошибки при передаче неверных параметров"""
    with pytest.raises(ValueError):
        mask_account_card("")


def test_get_date(fix_widget_data_test: list) -> None:
    """Проверка правильности преобразования значений функции"""
    for i in range(len(fix_widget_data_test)):
        assert get_date(fix_widget_data_test[i].get("string")) == fix_widget_data_test[i].get("expected_result")


def test_get_date_empy() -> None:
    """Проверка при передаче пустого значения"""
    with pytest.raises(ValueError):
        get_date("")


def test_get_date_wrong() -> None:
    """Ошибки при передаче неверных параметров"""
    with pytest.raises(ValueError):
        get_date("2024-22-11T02:26:18.671407")
    with pytest.raises(ValueError):
        get_date("2024-12-40T02:26:18.671407")
    with pytest.raises(ValueError):
        get_date("asd12SSDasd3SD38837212312312")
