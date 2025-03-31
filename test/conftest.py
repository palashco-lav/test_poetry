import pytest


@pytest.fixture
def fix_mask() -> str:
    return "0123456789012345"


@pytest.fixture
def fix_process() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def fix_process_canceled() -> list:
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def fix_process_executed() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def fix_process_sort_decrease() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def fix_process_sort_increase() -> list:
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def fix_widget_test() -> list:
    return [
        {"string": "Maestro 1596837868705199", "expected_result": "Maestro 1596 83** **** 5199"},
        {"string": "Счет 64686473678894779589", "expected_result": "Счет **9589"},
        {"string": "MasterCard 7158300734726758", "expected_result": "MasterCard 7158 30** **** 6758"},
        {"string": "Счет 35383033474447895560", "expected_result": "Счет **5560"},
        {"string": "Visa Classic 6831982476737658", "expected_result": "Visa Classic 6831 98** **** 7658"},
        {"string": "Visa Platinum 8990922113665229", "expected_result": "Visa Platinum 8990 92** **** 5229"},
        {"string": "Visa Gold 5999414228426353", "expected_result": "Visa Gold 5999 41** **** 6353"},
        {"string": "Счет 73654108430135874305", "expected_result": "Счет **4305"},
    ]


@pytest.fixture
def fix_widget_data_test() -> list:
    return [
        #           2024-03-11T02:26:18.671407
        {"string": "2024-03-01T02:26:18.671407", "expected_result": "01.03.2024"},
        {"string": "2021-11-30T06:15:14.334677", "expected_result": "30.11.2021"},
        {"string": "2022-02-21T02:50:55.232343", "expected_result": "21.02.2022"},
        {"string": "2016-05-17T20:42:45.596871", "expected_result": "17.05.2016"},
        {"string": "2013-08-20T15:31:36.671407", "expected_result": "20.08.2013"},
        {"string": "2017-04-08T18:25:25.123407", "expected_result": "08.04.2017"},
        {"string": "2013-01-06T13:16:22.671407", "expected_result": "06.01.2013"},
        {"string": "2002-09-25T22:06:11.987407", "expected_result": "25.09.2002"},
    ]


@pytest.fixture
def fix_generators_data_test() -> list:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def fix_generators_data_usd_test() -> list:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]


@pytest.fixture
def fix_generators_data_rub_test() -> list:
    return [
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def fix_transaction_descriptions_test() -> list:
    return [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


@pytest.fixture
def test_def_card_number_generator() -> dict:
    return {
        "start": 1,
        "stop": 5,
        "expected_result": [
            "0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003",
            "0000 0000 0000 0004",
            "0000 0000 0000 0005",
        ],
    }


@pytest.fixture
def test_def_card_number_generator_2() -> dict:
    return {
        "start": 1000000000001,
        "stop": 1000000000005,
        "expected_result": [
            "0001 0000 0000 0001",
            "0001 0000 0000 0002",
            "0001 0000 0000 0003",
            "0001 0000 0000 0004",
            "0001 0000 0000 0005",
        ],
    }


@pytest.fixture
def test_get_exchangerates_data_fix() -> list:
    return [
        {
            "data": """{
                    "date": "2018-02-22",
                    "historical": "",
                    "info": {
                        "rate": 148.972231,
                        "timestamp": 1519328414
                        },
                    "query": {
                        "amount": 25,
                        "from": "USD",
                        "to": "RUB"
                        },
                    "result": 1111.1,
                    "success": true
                }""",
            "result": 1111.1,
        },
        {
            "data": """{
                        "date": "2018-02-22",
                        "historical": "",
                        "info": {
                            "rate": 148.972231,
                            "timestamp": 1519328414
                        },
                        "query": {
                            "amount": 25,
                            "from": "EUR",
                            "to": "RUB"
                        },
                        "result": 2222.2,
                        "success": true
                    }""",
            "result": 2222.2,
        },
        {
            "data": """{
                    "date": "2018-02-22",
                    "historical": "",
                    "info": {
                        "rate": 148.972231,
                        "timestamp": 1519328414
                    },
                    "query": {
                        "amount": 25,
                        "from": "EUR",
                        "to": "RUB"
                    },
                    "result": 3333.3,
                    "success": true
                }""",
            "result": 3333.3,
        },
    ]


@pytest.fixture
def test_get_json_list() -> str:
    return """[
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                    "amount": "31957.58",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589"
            },
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "8221.37",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560"
            },
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                }
            }
        ]"""


@pytest.fixture
def test_log_decorator_data() -> list:
    return [
        {"x": 1, "y": 2, "expected_result": "my_function ok\n"},
        {"x": 6, "y": 2, "expected_result": "my_function ok\n"},
        {"x": 16, "y": 22, "expected_result": "my_function ok\n"},
        {"x": 21, "y": 15, "expected_result": "my_function ok\n"},
        {"x": 10, "y": 7, "expected_result": "my_function ok\n"},
    ]


@pytest.fixture
def test_log_decorator_data_errors() -> list:
    return [
        {
            "x": -1,
            "y": -2,
            "expected_result": "my_function error: Переменные должны быть положительные. Inputs: (-1, -2), {}\n",
        },
        {
            "x": "X",
            "y": "Y",
            "expected_result": "my_function error: Переменные должны быть числами. Inputs: (X, Y), {}\n",
        },
    ]


@pytest.fixture
def test_read_financial_trans_xlsx_data() -> dict:
    return {
        "name": ["Xavier", "Ann", "Jana", "Yi", "Robin", "Amal", "Nori"],
        "city": ["Mexico City", "Toronto", "Prague", "Shanghai", "Manchester", "Cairo", "Osaka"],
        "age": [41, 28, 33, 34, 38, 31, 37],
        "py-score": [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0],
    }


@pytest.fixture
def test_read_financial_trans_csv_data() -> str:
    return """id;state;date;amount;currency_name;currency_code;from;to;description
        650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;\
        Счет 39745660563456619397;Перевод организации"""
