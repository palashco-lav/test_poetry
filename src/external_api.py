import json
import os

import requests
from dotenv import load_dotenv


def get_exchangerates_data(amount: float, amount_from: str, amount_to: str) -> float:
    """
    Функция проводит конвертацию двух валют. С использованием API
    :param amount:          - конвертируемая сумма.
    :param amount_from:     - трехбуквенный код валюты, из которой происходит конвертация.
    :param amount_to:       - трехбуквенный код валюты, в которую происходит конвертация.
    :return:
    """


    try:
        # Загрузка переменных из .env-файла
        load_dotenv()
        url = os.getenv('BASE_URL_API')
        headers = {'api-key': os.getenv('API_KEY')}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    # запрос не может быть выполнен из-за проблем с сетью
    except requests.exceptions.ConnectionError:
        raise Exception("Connection Error. Please check your network connection.")
    # запрос не получил ответа в течение заданного времени.
    except requests.exceptions.Timeout:
        raise Exception("Request timed out. Please check your internet connection.")
    # количество перенаправлений запроса превышает максимально допустимое значение
    except requests.exceptions.TooManyRedirects:
        raise Exception("Too many redirects. Please check the URL.")
    # полученный ответ от сервера не является корректным HTTP-ответом
    except requests.exceptions.HTTPError:
        raise Exception("HTTP Error. Please check the URL.")

    data = json.loads(response.text)
    # Если статус 200 -запрос прошел успешно
    if response.status_code == 200:
        return float(data["result"])
    elif response.status_code == 400:
        raise Exception("Bad Request. The request was unacceptable, often due to missing a required parameter.")
    elif response.status_code == 401:
        raise Exception("Unauthorized. Please check your API key.")
    elif response.status_code == 403:
        raise Exception("Forbidden. Please check your API key.")
    elif response.status_code == 404:
        raise Exception("Not Found. The requested resource doesn't exist.")
    elif response.status_code == 429:
        raise Exception("Too many requests. Please check the rate limit.")
    else:
        raise Exception("Server Error. We have failed to process your request. (You can contact us anytime)")


def get_transaction_amount(transaction_data: dict) -> float:
    """
    Функция, принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли. Для конвертации валюты используется Exchange Rates Data API:
    https://apilayer.com/exchangerates_data-api.
    :param transaction_data:
    :return:
    """
    # Если транзакция в рублях сразу возвращаю сумму транзакции в рублях
    if transaction_data["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction_data["operationAmount"]["amount"])
    else:
        # если транзакция не в рублях, то выполняю конвертацию в рубли и возвращаю значение
        result = get_exchangerates_data(amount = float(transaction_data["operationAmount"]["amount"]),
                                        amount_from=transaction_data["operationAmount"]["currency"]["code"],
                                        amount_to="RUB")
        return result
