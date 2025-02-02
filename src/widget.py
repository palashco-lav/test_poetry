import masks

def mask_account_card(card_type_and_number: str) -> str:
    """Функция принимает на вход тип карты и её номер возвращает
    строку с маскированным номером"""
    divided_card_type_and_number = card_type_and_number.split(" ")
    if not divided_card_type_and_number[-1].isdigit():
        raise ValueError("Данные не содержат номер карты либо не соответствуют формату")
    #выделаю в отдельную переменную номер


    if divided_card_type_and_number[0] == "Счёт" or divided_card_type_and_number[0] == "Счет" :
        mask_result = masks.get_mask_account(divided_card_type_and_number[-1])
    else:
        mask_result = masks.get_mask_card_number(divided_card_type_and_number[-1])

    return ''.join(divided_card_type_and_number[x] + " " for x in range(len(divided_card_type_and_number) - 1)) + mask_result


def get_date(time_to_convert: str) -> str:
    """Функция преобразует формат даты "2024-03-11T02:26:18.671407" в "ДД.ММ.ГГГГ"
    :param time_to_convert:
    :return:
    """
    divided_time_to_convert = (time_to_convert.split("T")[0]).split("-") #Сначала отсекаю всё что после символа "T",
    #затем разделяю по символу ":" для пересборки

    return divided_time_to_convert[2] + "." + divided_time_to_convert[1] + "." + divided_time_to_convert[0]