import pytest

from conftest import fix_generators_data_test, fix_generators_data_usd_test, fix_generators_data_rub_test
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator



def test_filter_by_currency_param_executed() -> None:

    usd_transactions = filter_by_currency(fix_generators_data_test, "USD")
    rub_transactions = filter_by_currency(fix_generators_data_test, "RUB")

    assert next(usd_transactions) == fix_generators_data_usd_test[0]

    assert next(usd_transactions) == fix_generators_data_usd_test[1]

    assert next(usd_transactions) == fix_generators_data_usd_test[2]

    assert next(rub_transactions) == fix_generators_data_rub_test[0]

    assert next(rub_transactions) == fix_generators_data_rub_test[1]

def test_transaction_descriptions() -> None:
    it_transactions_descriptions = transaction_descriptions(fix_generators_data_test)

    assert next(it_transactions_descriptions) == "Перевод организации"

    assert next(it_transactions_descriptions) == "Перевод со счета на счет"

    assert next(it_transactions_descriptions) == "Перевод со счета на счет"

    assert next(it_transactions_descriptions) == "Перевод с карты на карту"

    assert next(it_transactions_descriptions) == "Перевод организации"

def test_def_card_number_generator() -> None:
    it_card_number_generator = card_number_generator(1, 5)

    assert next(it_card_number_generator) == "0000 0000 0000 0001"
    assert next(it_card_number_generator) == "0000 0000 0000 0002"
    assert next(it_card_number_generator) == "0000 0000 0000 0003"
    assert next(it_card_number_generator) == "0000 0000 0000 0004"
    assert next(it_card_number_generator) == "0000 0000 0000 0005"

    it_card_number_generator = card_number_generator(1000000000001, 1000000000005)

    assert next(it_card_number_generator) == "0001 0000 0000 0001"
    assert next(it_card_number_generator) == "0001 0000 0000 0002"
    assert next(it_card_number_generator) == "0001 0000 0000 0003"
    assert next(it_card_number_generator) == "0001 0000 0000 0004"
    assert next(it_card_number_generator) == "0001 0000 0000 0005"

def test_def_card_number_generator_wrong_arguments() -> None:
    """Проверка на ошибку при вызове с пустым аргументом"""
    it_card_number_generator = card_number_generator(5, 3)
    with pytest.raises(ValueError):
        next(it_card_number_generator)

    it_card_number_generator = card_number_generator(5, 10000000000000000)
    with pytest.raises(ValueError):
        next(it_card_number_generator)

    it_card_number_generator = card_number_generator(-5, 10000000000000)
    with pytest.raises(ValueError):
        next(it_card_number_generator)

    it_card_number_generator = card_number_generator(-5, -3)
    with pytest.raises(ValueError):
        next(it_card_number_generator)