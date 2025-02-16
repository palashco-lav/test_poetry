def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты в виде числа и
    возвращает маску номера по правилу XXXX XX** **** XXXX"""
    pass
    # Проверка, что номер карты длиной 16 символов и состоит только из цифр
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен состоять из 16 цифр")

    return card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[12:16]


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета в виде числа и
    возвращает маску номера по правилу **XXXX"""
    pass
    # Проверка, что номер счета состоит из цифр
    if len(account_number) == 0:
        raise ValueError("Аргумент функции не должен быть пустым")

    if not account_number.isdigit():
        raise ValueError("Номер счёта должен состоять из цифр")

    return "**" + account_number[-4:]
