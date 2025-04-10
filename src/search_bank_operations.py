import re
from collections import Counter


def filter_transactions(transactions_in: list[dict], search_string: str) -> list[dict]:
    """
    Функция принимает список словарей с данными о банковских операциях и строку поиска, а возвращать
    список словарей, у которых в описании есть данная строка.
    :param transactions_in:
    :param search_string:
    :return:
    """
    filtered_transactions: list[dict] = []
    pattern = re.compile(search_string, flags=re.IGNORECASE)
    for transactions_element in transactions_in:
        if "description" in transactions_element and pattern.search(transactions_element["description"]):
            filtered_transactions.append(transactions_element)
    return filtered_transactions


def count_transactions_by_category(transactions: list[dict], categories: list) -> dict:
    """
    Функция принимает список словарей с данными о банковских операциях и список категорий операций.
    Возвращать словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    :param transactions: Список словарей с данными о банковских операциях.
    :param categories: Список категорий операций.
    :return:
    """
    category_counts: dict = {category: 0 for category in categories}  # Инициализируем словарь
    result_1: list = []
    for transaction in transactions:
        if transaction.get("description", "") in categories:
            result_1.append(transaction.get("description", ""))

    category_counts = dict(Counter(result_1))

    return category_counts
