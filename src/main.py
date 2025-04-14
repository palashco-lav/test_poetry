from pathlib import Path

from src.generators import filter_by_currency
from src.load_data import read_financial_trans_csv as csv_read
from src.load_data import read_financial_trans_xlsx as xlsx_read
from src.processing import filter_by_state, sort_by_date
from src.search_bank_operations import filter_transactions
from src.utils import get_transaction_data as json_read
from src.widget import get_date, mask_account_card


def main() -> None:
    answer: str = ""
    read_data: list = []
    param_select: dict = {
        "file_select": "EMPY",
        "operation_status": "EMPY",
        "data_sort": "EMPY",
        "sort_direction": "EMPY",
        "RUB_only": "EMPY",
        "filter_words": "EMPY",
    }

    base_dir = Path(__file__).resolve().parent.parent

    while param_select["file_select"] == "EMPY":
        print(
            """Программа: Привет! Добро пожаловать в программу работы
с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
        )

        # Получаем ответ
        answer_1 = input()
        if answer_1 == "1":
            print("Для обработки выбран JSON-файл.")
            param_select["file_select"] = "JSON"
            read_data = json_read(f"{base_dir}\\data\\operations.json")
            break
        elif answer_1 == "2":
            print("Для обработки выбран CSV-файл.")
            param_select["file_select"] = "CSV"
            read_data = csv_read(f"{base_dir}\\data\\transactions.csv")
            break
        elif answer_1 == "3":
            print("Для обработки выбран XLSX-файл.")
            param_select["file_select"] = "XLSX"
            read_data = xlsx_read(f"{base_dir}\\data\\transactions_excel.xlsx")
            break
        else:
            print("Данного пункта не существует.")

    while param_select["operation_status"] == "EMPY":
        print(
            """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
        )
        answer = input().upper()
        if answer == "EXECUTED":
            param_select["operation_status"] = "EXECUTED"
            break
        elif answer == "CANCELED":
            param_select["operation_status"] = "CANCELED"
            break
        elif answer == "PENDING":
            param_select["operation_status"] = "PENDING"
            break
        else:
            print(f'Статус операции "{answer}" недоступен')
    print(f'Операции отфильтрованы по статусу "{param_select["operation_status"]}"')
    read_data = filter_by_state(read_data, param_select["operation_status"])

    while param_select["data_sort"] == "EMPY":
        print("""Отсортировать операции по дате? Да/Нет""")
        answer = input().upper()
        if answer == "ДА":
            param_select["data_sort"] = "ДА"
            break
        elif answer == "НЕТ":
            param_select["data_sort"] = "НЕТ"
            break
        else:
            print("Выберете корректно.")

    if param_select["data_sort"] == "ДА":
        while param_select["sort_direction"] == "EMPY":
            print("""Отсортировать по возрастанию или по убыванию?""")
            answer = input().upper()
            if answer == "ПО ВОЗРАСТАНИЮ":
                param_select["sort_direction"] = "ПО ВОЗРАСТАНИЮ"
                break
            elif answer == "ПО УБЫВАНИЮ":
                param_select["sort_direction"] = "ПО УБЫВАНИЮ"
                break
            else:
                print("Выберете корректную сортировку.")

    if param_select["data_sort"] == "ДА":
        if param_select["sort_direction"] == "ПО ВОЗРАСТАНИЮ":
            read_data = sort_by_date(read_data, False)
        else:
            read_data = sort_by_date(read_data, True)

    while param_select["RUB_only"] == "EMPY":
        print("""Выводить только рублевые транзакции? Да/Нет""")
        answer = input().upper()
        if answer == "ДА":
            param_select["RUB_only"] = "ДА"
            break
        elif answer == "НЕТ":
            param_select["RUB_only"] = "НЕТ"
            break
        else:
            print("Введите корректный параметр.")

    if param_select["RUB_only"] == "ДА":
        temp_data = read_data
        read_data.clear()
        for count in range(len(temp_data)):
            read_data.append(filter_by_currency(temp_data, "RUB"))

    while param_select["filter_words"] == "EMPY":
        print("""Отфильтровать список транзакций по определенному слову в описании? Да/Нет""")
        answer = input().upper()
        if answer == "ДА":
            while param_select["filter_words"] == "EMPY":
                print("""Введите слово для фильтрации.""")
                answer = input().lower()
                if len(answer) > 0:
                    param_select["filter_words"] = answer
                    break
                else:
                    print("Введённое слово не корректно.")
            break
        elif answer == "НЕТ":
            param_select["filter_words"] = "НЕТ"
            break
        else:
            print("Введите корректный параметр.")

    if param_select["filter_words"] != "НЕТ":
        transactions_by_word = filter_transactions(read_data, param_select["filter_words"])
        """
        transactions_by_word = []
        word_found = False
        # filter_transactions
        for transaction in read_data:
            if param_select["filter_words"] in transaction["description"].lower():
                transactions_by_word.append(transaction)
                word_found = True"""

        if len(transactions_by_word) == 0:
            print(f'Слова "{param_select["filter_words"]}" нет в списке транзакций.')
        else:
            for transaction in transactions_by_word:
                print(f'\n{get_date(transaction["date"])} {transaction["description"]}')
                print(f'{mask_account_card(transaction["from"])} -> {mask_account_card(transaction["to"])}')
                if param_select["file_select"] != "JSON":
                    print(f'Сумма: {transaction["amount"]}')
                else:
                    print(f'Сумма: {transaction["operationAmount"]["amount"]}')


main()
