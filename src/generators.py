from typing import Iterator


def filter_by_currency(dicts_list: list, value: str) -> Iterator[list]:
    """Функция принимает на вход список словарей, представляющих транзакции.
    Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD).
    :rtype: object
    :param dicts_list:
    :param value:
    :return:
    """

#    if len(dicts_list) == 0:
#        raise ValueError("Входной список словарей не должен быть пустым")
#
#    if value == "":
#        raise ValueError("Валюта операции не должна быть пустой")

    for dict_element in dicts_list:
        if dict_element["operationAmount"]["currency"]["code"] == value:
            yield dict_element


def transaction_descriptions(dicts_list: list) -> Iterator[str]:
    """
    Функция принимает список словарей с транзакциями и возвращает
    описание каждой операции по очереди
    :param dicts_list:
    :return:
    """
    for dict_element in dicts_list:
        yield dict_element["description"]


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Функция, которая выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где
    X — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    :param start:
    :param stop:
    :return:
    """

    if start < 0 or stop < 0:
        raise ValueError("Значения диапазона должны быть положительными")

    if start > stop:
        raise ValueError("Начальное значение диапазона не должно превышать конечное")

    if stop > 9999999999999999:
        raise ValueError("Конечное значение превышает максимальное установленное значение в 9999999999999999")

    for i in range(start, stop + 1):
        text_result = str(i)
        while len(text_result) < 16:
            text_result = "0" + text_result
        yield text_result[0:4] + " " + text_result[4:8] + " " + text_result[8:12] + " " + text_result[12:16]
