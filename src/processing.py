def filter_by_state(dict_list: list, state: str = 'EXECUTED') -> list:
    """Функция принимает список словарей и опционально значение для ключа state  (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению.
    :param dict_list:
    :param state:
    :return:
    """
    # Проверка
    if len(dict_list) == 0:
        raise ValueError("Номер карты должен состоять из 16 цифр")

    dict_result = []

    for dict_num in range(len(dict_list)):
        if dict_list[dict_num].get('state') == state:
            dict_result.append(dict_list[dict_num])

    return dict_result