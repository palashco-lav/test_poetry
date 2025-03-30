import json
from pathlib import Path
from unittest.mock import Mock

from src.utils import get_transaction_data

BASE_DIR = Path(__file__).resolve().parent.parent


def test_get_transaction_data_test_file() -> None:
    """
    Тестирование исключений:
    не указан путь к файлу -> пустой список
    файл не найден -> пустой список
    файл пустой -> пустой список
    :return:
    """
    assert get_transaction_data("") == []
    assert get_transaction_data(f"{BASE_DIR}/test/no_file.json") == []
    assert get_transaction_data(f"{BASE_DIR}/test/empy_file") == []


def test_get_transaction_data(test_get_json_list: str) -> None:
    """
    Проверяю функцию get_transaction_data на обработку данных с подменой данных от файла с помощью Mock
    :param test_get_json_list:
    :return:
    """
    data = json.loads(test_get_json_list)
    mock_json_load = Mock(return_value=data)
    json.load = mock_json_load
    assert get_transaction_data(f"{BASE_DIR}/data/operations.json") == json.load(test_get_json_list)
