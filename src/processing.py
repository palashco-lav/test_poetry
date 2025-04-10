from datetime import datetime


def filter_by_state(dicts_list: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению.
    :param dicts_list:
    :param state:
    :return:
    """
    # Проверка
    if len(dicts_list) == 0:
        raise ValueError("Длина списка нулевая")
    # Если передали пустой ключ, заменяю его на значение по умолчанию
    if state == "":
        state = "EXECUTED"

    dicts_result = []

    for dictionary_index in range(len(dicts_list)):
        if dicts_list[dictionary_index].get("state") == state:
            dicts_result.append(dicts_list[dictionary_index])

    return dicts_result


def sort_by_date(dicts_to_sort: list, sort_decrease: bool = True) -> list:
    """Функция sort_by_date, которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание). Функция должна возвращать новый список,
    отсортированный по дате (date).

    :param dicts_to_sort:
    :param sort_decrease: - по умолчанию True
    :return:
    """

    # Проверка
    if len(dicts_to_sort) == 0:
        raise ValueError("Длина списка нулевая")

    if dicts_to_sort[0]["date"][-1] == "Z":
        dicts_result = sorted(
            dicts_to_sort, key=lambda p: datetime.strptime(p["date"], "%Y-%m-%dT%H:%M:%SZ"), reverse=sort_decrease
        )
    else:
        dicts_result = sorted(
            dicts_to_sort, key=lambda p: datetime.strptime(p["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=sort_decrease
        )

    return dicts_result
