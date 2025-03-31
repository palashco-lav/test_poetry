# SuperITFeature

## Описание:

SuperITFeature - IT-отдел крупного банка делает новую фичу для личного кабинета клиента. Это виджет, который показывает 
несколько последних успешных банковских операций клиента. 

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/palashco-lav/test_poetry.git
```
## Реализовано:
### Модуль masks:
    get_mask_card_number - Функция принимает на вход номер карты в виде числа и возвращает маску номера по правилу XXXX XX** **** XXXX"""
    :param card_number: str - номер карты для маскирования

    get_mask_account - Функция принимает на вход номер счета в виде числа и возвращает маску номера по правилу **XXXX
    :param account_number: str - омер счета в виде числа

### Модуль widget
    mask_account_card - Функция принимает на вход тип карты и её номер возвращает строку с маскированным номером
    :param card_type_and_number: str

    get_date - Функция преобразует формат даты "2024-03-11T02:26:18.671407" в "ДД.ММ.ГГГГ
    :param time_to_convert: str

### Модуль processing
    filter_by_state - Функция принимает список словарей и опционально значение для ключа state  (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    :param dicts_list:
    :param state:

    sort_by_date - Функция sort_by_date, которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание). Функция должна возвращать новый список,
    отсортированный по дате (date).
    :param dicts_to_sort:
    :param sort_decrease: - по умолчанию True

### Модуль generators
    filter_by_currency - Функция принимает на вход список словарей, представляющих транзакции.     Функция возвращает 
    итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD).
    :rtype: object
    :param dicts_list:
    :param value:
    :return:

    transaction_descriptions - Функция принимает список словарей с транзакциями и возвращает     описание каждой 
    операции по очереди
    :param dicts_list:

    card_number_generator - Функция, которая выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра 
    номера карты. Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 
    9999 9999 9999 9999.
    :param start:
    :param stop:
    :return:

### Модуль external_api
    get_transaction_amount - Функция, принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип 
    данных — float. Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса
    валют и конвертации суммы операции в рубли. Для конвертации валюты используется Exchange Rates Data API:
    https://apilayer.com/exchangerates_data-api.
    :param transaction_data:
    :return:

    get_exchangerates_data - Функция проводит конвертацию двух валют. С использованием API
    :param amount:          - конвертируемая сумма.
    :param amount_from:     - трехбуквенный код валюты, из которой происходит конвертация.
    :param amount_to:       - трехбуквенный код валюты, в которую происходит конвертация.
    :return:

### Модуль utils
    get_transaction_data - Функция чтения JSON-файла принимает путь к файлу JSON в качестве аргумента.
    Функция чтения JSON-файла возвращает список словарей с данными о финансовых транзакциях.
    Если JSON-файл пустой, содержит не-список или не найден, возвращается пустой список
    :param file_path:
    :return:

### Модуль decorators
    log(filename="") - декоратор ведения логов для функций
    filename - путь к фалу храненния логов. По умолчанию вывод ведётся  в консоль
    
### Модуль load_data
    read_financial_trans_csv
    Функция для считывает финансовые операций из CSV файла.
    :param file_path: - путь к файлу

    read_financial_trans_xlsx
    Функция для считывает финансовые операций из XLSX файла.
    :param file_path: - путь к файлу    
    

### Тестирование
test_masks.py       - проверка модуля masks, покрытие 100%

Проверка функции get_mask_card_number

    Проверка работоспособности основного функционала параметризацией
        test_get_mask_card_number(string: str, expected_result: str) -> None:
        
    Проверка работы фикстурой
        test_get_mask_card_number_fixture(fix_mask: str) -> None
        
    Проверка на ошибку по количеству цифр
        test_get_mask_card_number_errors() -> None:

    Проверка на ошибку при передаче пустого аргумента
        test_get_mask_card_number_empy() -> None:

Проверка функции get_mask_account

    Проверка работоспособности основного функционала параметризацией
        test_get_mask_account(string: str, expected_result: str) -> None

    Проверка работы фикстурой
        test_get_mask_account_fixture(fix_mask: str) -> None

    Проверка на ошибку при вызове с пустым аргументом
        test_get_mask_account_empy() -> None
    
    Проверка на ошибку при вызове с буквами вместо и вместе цифрами
        test_get_mask_account_wrong() -> None
            
test_processing.py  - проверка модуля processing, покрытие 100%

Проверка функции filter_by_state

    Проверка работоспособности основного функционала параметризацией
        test_filter_by_state_param_executed(string: list, expected_result: str) -> None 
        test_filter_by_state_param_executed_2(string: list, expected_result: str) -> None
        test_filter_by_state_param_executed_canceled(string: list, expected_result: list) -> None
    
    Проверка работы фикстурой
        test_filter_by_state_param_fixture
    
    Проверка исключения при передаче пустых аргументов
        test_filter_by_state_empy() -> None

Проверка функции sort_by_date

    Проверка сортировки по дате с разными вызовами
        test_sort_by_date(fix_process: list, fix_process_sort_decrease: list, fix_process_sort_increase: list) -> None

    Проверка вызова с пустыми параметрами
        est_sort_by_date_empy() -> None

test_widget.py      - проверка модуля widget, покрытие 100%

Проверка функции mask_account_card

    Проверка правильности преобразования значений функции
        test_mask_account_card(fix_widget_test: list) -> None

    Ошибки при передаче неверных параметров
        test_mask_account_card_wrong_number() -> None

    Ошибки при передаче неверных параметров
        test_mask_account_card_empy() -> None

Проверка функции get_date

    Проверка правильности преобразования значений функции
        test_get_date(fix_widget_data_test: list) -> None

    Проверка при передаче пустого значения
        test_get_date_empy() -> None

    Ошибки при передаче неверных параметров
        test_get_date_wrong() -> None

test_generators.py      - проверка модуля generators, покрытие 100%
    
    Прроверка работоспособности функции filter_by_currency
        test_filter_by_currency_param_executed()
    
    Провертка обработки пустых аргументов функции filter_by_currency
        test_filter_by_currency_param_no_value()
    
    Прроверка работоспособности функции transaction_descriptions
        test_transaction_descriptions()
    
    Провертка обработки пустых аргументов функции transaction_descriptions
        test_transaction_descriptions_empy()
    
    Прроверка работоспособности функции card_number_generator
        test_def_card_number_generator()
    
    Прроверка реакции функции неверные входные аргументы
        test_def_card_number_generator_wrong_arguments()

test_load_data.py - проверка модуля loaf_data, покрытие 100%

    Проверка работоспособности функции загрузки данных из CVS файла
        test_read_financial_trans_csv

    Проверка работоспособности функции загрузки данных из XLSX файла
        test_read_financial_trans_xlsx



## Документация:

Для получения дополнительной информации обратитесь к [документации](README.md).

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).