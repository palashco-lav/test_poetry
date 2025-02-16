from datetime import datetime

from src import masks


def mask_account_card(card_type_and_number: str) -> str:
    """Функция принимает на вход тип карты и её номер возвращает
    строку с маскированным номером"""
    divided_card_type_and_number = card_type_and_number.split(" ")
    if not divided_card_type_and_number[-1].isdigit():
        raise ValueError("Данные не содержат номер карты либо не соответствуют формату")

    if divided_card_type_and_number[0] == "Счёт" or divided_card_type_and_number[0] == "Счет" :
        # Выполняю маскирование счета
        mask_result = masks.get_mask_account(divided_card_type_and_number[-1])
    else:
        # Выполняю маркирование карты
        mask_result = masks.get_mask_card_number(divided_card_type_and_number[-1])

    title = ' '.join(divided_card_type_and_number[:-1])
    return f"{title} {mask_result}"


def get_date(time_to_convert: str) -> str:
    """Функция преобразует формат даты "2024-03-11T02:26:18.671407" в "ДД.ММ.ГГГГ"
    """

    if time_to_convert == '':
        raise ValueError("Данные для обработки отсутствуют")
    try:
        time_to_convert_2 = datetime.strptime(time_to_convert, '%Y-%m-%dT%H:%M:%S.%f')

    except ValueError:
        raise ValueError("Это не дата")

    return time_to_convert_2.strftime('%d.%m.%Y')
