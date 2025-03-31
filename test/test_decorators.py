import os

import pytest

from src.decorators import log


def test_log_decorator_file_out(test_log_decorator_data: list) -> None:
    """
    Проверка корректности работы
    :param test_log_decorator_data:
    :return:
    """

    @log(filename="test_mylog.txt")
    def my_function(x: int, y: int) -> int:
        """
        Суммирование двух чисел
        :param x:
        :param y:
        :return:
        """
        return x + y

    # Удаляю файл тестового вывода данных
    if os.path.isfile("test_mylog.txt"):
        os.remove("test_mylog.txt")

    for data_test in test_log_decorator_data:
        my_function(data_test["x"], data_test["y"])

    file = open("test_mylog.txt", "r")
    count = 0
    for line in file:
        assert test_log_decorator_data[count]["expected_result"] == line
        count += 1
    file.close()
    os.remove("test_mylog.txt")


def test_log_decorator_console_out(capsys: pytest.CaptureFixture[str], test_log_decorator_data: list) -> None:
    """
    Проверка вывода данных в консоль
    :param capsys:
    :return:
    """

    @log()
    def my_function_console_out(x: int, y: int) -> int:
        """
        Суммирование двух чисел
        :param x:
        :param y:
        :return:
        """
        return x * y

    for data_test in test_log_decorator_data:
        my_function_console_out(data_test["x"], data_test["y"])
        captured = capsys.readouterr()
        assert data_test["expected_result"] == captured.out


def test_log_decorator_error_console_out(
    capsys: pytest.CaptureFixture[str], test_log_decorator_data_errors: list
) -> None:
    """
    Проверка вывода данных в консоль
    :param capsys:
    :return:
    """

    @log()  #
    def my_function_console_out(x: int, y: int) -> int:
        """
        Суммирование двух чисел
        :param x:
        :param y:
        :return:
        """
        if not ((isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float))):
            raise ValueError("Переменные должны быть числами")
        if x < 0 or y < 0:
            raise ValueError("Переменные должны быть положительные")
        return x + y

    for data_test in test_log_decorator_data_errors:
        my_function_console_out(data_test["x"], data_test["y"])
        captured = capsys.readouterr()
        assert data_test["expected_result"] == captured.out


def test_log_decorator_error_file_out(
    capsys: pytest.CaptureFixture[str], test_log_decorator_data_errors: list
) -> None:
    """
    Проверка вывода данных в консоль
    :param capsys:
    :return:
    """

    @log(filename="test_mylog.txt")  #
    def my_function_file_out_2(x: int, y: int) -> int:
        """
        Суммирование двух чисел
        :param x:
        :param y:
        :return:
        """
        if not ((isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float))):
            raise ValueError("Переменные должны быть числами")
        if x < 0 or y < 0:
            raise ValueError("Переменные должны быть положительные")
        return x + y

    # Удаляю файл тестового вывода данных
    if os.path.isfile("test_mylog.txt"):
        os.remove("test_mylog.txt")

    for data_test in test_log_decorator_data_errors:
        my_function_file_out_2(data_test["x"], data_test["y"])

    file = open("test_mylog.txt", "r")
    count = 0
    for line in file:
        assert test_log_decorator_data_errors[count]["expected_result"] == line
        count += 1
    file.close()
    os.remove("test_mylog.txt")
