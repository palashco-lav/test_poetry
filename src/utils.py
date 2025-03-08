import json


def get_transaction_data(file_path: str) -> list:
    """
    Функция чтения JSON-файла принимает путь к файлу JSON в качестве аргумента.
    Функция чтения JSON-файла возвращает список словарей с данными о финансовых транзакциях.
    Если JSON-файл пустой, содержит не-список или не найден, возвращается пустой список
    :param file_path:
    :return:
    """
    try:
        # открываем файл
        with open(file_path, 'r', encoding='utf-8') as f:
            transaction_data = json.load(f)
            if isinstance(transaction_data, list):
                # если тип данных список - возвращаем список
                return transaction_data
            else:
                # если не список - возвращаем пустой список
                return []
    except FileNotFoundError:
        # файл не найдем - возвращаю пустой список
        return []
    except json.decoder.JSONDecodeError:
        # JSON файл не декодировался - возвращаю пустой список
        return []
    return []
