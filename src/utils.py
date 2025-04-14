import json

# Импортируем модуль logging
import logging
from pathlib import Path

logger_utils = logging.getLogger(__name__)
logger_utils.setLevel(logging.DEBUG)

# настройка обработчика и форматировщика для logger_masks
handler_utils = logging.FileHandler(
    f"{Path(__file__).resolve().parent.parent}\\logs\\utils.log", mode="w", encoding="utf-8"
)
formatter_utils = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")

# добавление форматировщика к обработчику
handler_utils.setFormatter(formatter_utils)
# добавление обработчика к логгеру
logger_utils.addHandler(handler_utils)


def get_transaction_data(file_path: str) -> list:
    """
    Функция чтения JSON-файла принимает путь к файлу JSON в качестве аргумента.
    Функция чтения JSON-файла возвращает список словарей с данными о финансовых транзакциях.
    Если JSON-файл пустой, содержит не-список или не найден, возвращается пустой список
    :param file_path:
    :return:
    """
    # utils_logger = setup_logging()

    try:
        logger_utils.debug(f'Попытка открыть файл: "{file_path}"')
        # открываем файл
        with open(file_path, "r", encoding="utf-8") as f:
            logger_utils.debug(f'Файл успешно открыт: "{file_path}"')
            transaction_data = json.load(f)
            if isinstance(transaction_data, list):
                # если тип данных список - возвращаем список
                logger_utils.debug("Файл содержит список - функция возвращает значение списка")
                return transaction_data
            else:
                # если не список - возвращаем пустой список
                logger_utils.debug("Файл содержит список - функция возвращает пустой список")
                return []
    except FileNotFoundError:
        # файл не найдем - возвращаю пустой список
        logger_utils.error(f'Файл: "{file_path}" не найден - возвращаю пустой список')
        return []
    except json.decoder.JSONDecodeError:
        logger_utils.error(f'JSON файл: "{file_path}" не декодировался - возвращаю пустой список')
        # JSON файл не декодировался - возвращаю пустой список
        return []
