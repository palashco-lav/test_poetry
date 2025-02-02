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
