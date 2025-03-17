# Импортируем модуль logging
import logging
from pathlib import Path


logger_masks = logging.getLogger(__name__)
logger_masks.setLevel(logging.DEBUG)

# настройка обработчика и форматировщика для logger_masks
handler_masks = logging.FileHandler(f'{Path(__file__).resolve().parent.parent}\\logs\\masks.log',
                                    mode='w', encoding='utf-8')
formatter_masks = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')

# добавление форматировщика к обработчику
handler_masks.setFormatter(formatter_masks)
# добавление обработчика к логгеру
logger_masks.addHandler(handler_masks)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты в виде числа и
    возвращает маску номера по правилу XXXX XX** **** XXXX"""

    # masks_logging = setup_logging()
    logger_masks.debug(f"Введён номер карты: {card_number}")
    # Проверка, что номер карты длиной 16 символов и состоит только из цифр
    if len(card_number) != 16 or not card_number.isdigit():
        logger_masks.error("Номер карты должен состоять из 16 цифр")
        raise ValueError("Номер карты должен состоять из 16 цифр")

    logger_masks.debug(f"Получившаяся маска: '{card_number[:4]} {card_number[4:6]} ** **** P{card_number[12:16]}'")
    return card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[12:16]


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета в виде числа и
    возвращает маску номера по правилу **XXXX"""

    # logger_masks = setup_logging()

    logger_masks.debug(f'Получен номер карты: {account_number}')
    # Проверка, что номер счета состоит из цифр
    if len(account_number) == 0:
        logger_masks.error("Аргумент функции не должен быть пустым")
        raise ValueError("Аргумент функции не должен быть пустым")

    if not account_number.isdigit():
        logger_masks.error("Номер счёта должен состоять из цифр")
        raise ValueError("Номер счёта должен состоять из цифр")
    logger_masks.debug(f'Получившаяся маска: **"{account_number[-4:]}"')
    return "**" + account_number[-4:]
