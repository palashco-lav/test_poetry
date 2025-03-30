import pandas as pd


def read_financial_trans_csv(file_path: str) -> list:
    """
    Функция для считывает финансовые операций из CSV файла.
    :param file_path: - путь к файлу
    :return:
    """
    with open(file_path) as file:
        # Загружаем CSV файл в DataFrame
        df = pd.read_csv(file, sep=";")

        # Преобразуем DataFrame в список словарей
        dict_list = df.to_dict(orient="records")
        return dict_list


def read_financial_trans_xlsx(file_path: str) -> list:
    """
    Функция для считывает финансовые операций из XLSX файла.
    :param file_path: - путь к файлу
    :return:
    """
    with pd.ExcelFile(file_path) as xlsx_file:
        df = pd.read_excel(xlsx_file, sheet_name=0)
        dict_list = df.to_dict(orient="records")
        return dict_list
