from test.conftest import fix_generators_data_rub_test, fix_generators_data_test, fix_generators_data_usd_test

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_param_executed(fix_generators_data_test: list, fix_generators_data_usd_test: list, fix_generators_data_rub_test: list) -> None:

    usd_transactions = filter_by_currency(fix_generators_data_test, "USD")
    rub_transactions = filter_by_currency(fix_generators_data_test, "RUB")

    for count in range(len(fix_generators_data_usd_test)):
        assert next(usd_transactions, "") == fix_generators_data_usd_test[count]

    for count in range(len(fix_generators_data_rub_test)):
        assert next(rub_transactions, "") == fix_generators_data_rub_test[count]


def test_filter_by_currency_param_no_value(fix_generators_data_test: list) -> None:

    it_transactions = filter_by_currency(fix_generators_data_test, "UK")

    assert next(it_transactions, "") == ""

    it_transactions = filter_by_currency([], "UK")
    assert next(it_transactions, "") == ""


def test_transaction_descriptions(fix_generators_data_test: list, fix_transaction_descriptions_test: list) -> None:
    it_transactions_descriptions = transaction_descriptions(fix_generators_data_test)

    for count in range(len(fix_transaction_descriptions_test)):
        assert next(it_transactions_descriptions, "") == fix_transaction_descriptions_test[count]



def test_transaction_descriptions_empy() -> None:
    it_transactions_descriptions = transaction_descriptions([])

    assert next(it_transactions_descriptions, "") == ""


def test_def_card_number_generator(test_def_card_number_generator: dict, test_def_card_number_generator_2: dict) -> None:
    it_card_number_generator = card_number_generator(test_def_card_number_generator["start"],
                                                     test_def_card_number_generator["stop"])

    for count in range(len(test_def_card_number_generator["expected_result"])):
        assert next(it_card_number_generator, "") == test_def_card_number_generator["expected_result"][count]

    it_card_number_generator = card_number_generator(test_def_card_number_generator_2["start"],
                                                     test_def_card_number_generator_2["stop"])

    for count in range(len(test_def_card_number_generator_2["expected_result"])):
        assert next(it_card_number_generator, "") == test_def_card_number_generator_2["expected_result"][count]


def test_def_card_number_generator_wrong_arguments() -> None:
    """Проверка на ошибку при вызове с неправильными аргументами"""
    """start больше stop"""
    it_card_number_generator = card_number_generator(5, 3)
    with pytest.raises(ValueError):
        next(it_card_number_generator)

    """stop выходит за диапазон"""
    it_card_number_generator = card_number_generator(5, 10000000000000000)
    with pytest.raises(ValueError):
        next(it_card_number_generator)

    """start отрицательное значение"""
    it_card_number_generator = card_number_generator(-5, 10000000000000)
    with pytest.raises(ValueError):
        next(it_card_number_generator)

    """start и stop отрицательное значения"""
    it_card_number_generator = card_number_generator(-5, -3)
    with pytest.raises(ValueError):
        next(it_card_number_generator)
