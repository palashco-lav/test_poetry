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

### Модуль decorators
    log(filename="") - декоратор ведения лгов для функций
    filename - путь к фалу храненния логов. По умолчанию вывод ведётся  в консоль
    
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

test_decorators.py      - проверка модуля decorators, покрытие 100%

    Проверка корректности работы декоратора log при записи в файл
        test_log_decorator_file_out

    Проверка корректности работы декоратора log при выводе данных в консоль
        test_log_decorator_console_out

    Проверка обработки исключений случаев log при выводе данных в консоль 
        test_log_decorator_error_console_out

    Проверка обработки исключений случаев log при записи в файл    
        test_log_decorator_error_file_out
## Документация:

Для получения дополнительной информации обратитесь к [документации](README.md).

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).