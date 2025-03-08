import os
import pytest
from dotenv import load_dotenv
import json
from unittest.mock import Mock, patch
from src.external_api import get_exchangerates_data, get_transaction_amount
from test.conftest import test_get_exchangerates_data_fix, fix_generators_data_usd_test, fix_generators_data_usd_test


@patch('requests.request')
def test_get_exchangerates_data(mock_get_exchangerates_data, test_get_exchangerates_data_fix) -> None:
    """
    Функция тест функции get_exchangerates_data - проверят правильность преобразования данных от API запроса
    :param mock_get_exchangerates_data:
    :return:
    """
    mock_get_exchangerates_data.return_value.status_code = 200
    mock_get_exchangerates_data.return_value.text = test_get_exchangerates_data_fix[0]["data"]

    assert (get_exchangerates_data(amount=31957.58, amount_from="USD", amount_to="RUB") ==
            test_get_exchangerates_data_fix[0]["result"])

    headers = {'api-key': os.getenv('API_KEY')}
    payload = {}
    params = {'amount': 31957.58, 'from': "USD", 'to': "RUB"}

    mock_get_exchangerates_data.assert_called_once_with("GET", os.getenv('BASE_URL'), headers=headers, data=payload)

@patch('requests.request')
def test_get_exchangerates_data_error_400(mock_get_exchangerates_data_error_400,
                                          test_get_exchangerates_data_fix) -> None:
    """
    Функция тест функции get_exchangerates_data - проверка на возврат status_code = 400
    :param mock_get_exchangerates_data_error_400:
    :return:
    """
    mock_get_exchangerates_data_error_400.return_value.status_code = 400
    mock_get_exchangerates_data_error_400.return_value.text = test_get_exchangerates_data_fix[0]["data"]

    with pytest.raises(Exception):
        get_exchangerates_data(amount=31957.58, amount_from="USD", amount_to="RUB")


@patch('requests.request')
def test_get_transaction_amount(mock_get_transaction_amount,
                                test_get_exchangerates_data_fix,
                                fix_generators_data_usd_test) -> None:
    mock_get_transaction_amount.return_value.status_code = 200
    mock_get_transaction_amount.return_value.text = test_get_exchangerates_data_fix[0]["data"]
    test_data = fix_generators_data_usd_test
    assert get_transaction_amount(test_data[0]) == test_get_exchangerates_data_fix[0]["result"]

    mock_get_transaction_amount.return_value.text = test_get_exchangerates_data_fix[1]["data"]
    assert get_transaction_amount(test_data[1]) == test_get_exchangerates_data_fix[1]["result"]

    mock_get_transaction_amount.return_value.text = test_get_exchangerates_data_fix[2]["data"]
    assert get_transaction_amount(test_data[2]) == test_get_exchangerates_data_fix[2]["result"]
