import pytest


@pytest.fixture
def fix_mask() -> str:
    return '0123456789012345'


@pytest.fixture
def fix_process() -> list:
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


@pytest.fixture
def fix_process_canceled() -> list:
    return [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


@pytest.fixture
def fix_process_executed() -> list:
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.fixture
def fix_process_sort_decrease() -> list:
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.fixture
def fix_process_sort_increase() -> list:
    return [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]


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
        {"string": "Счет 73654108430135874305", "expected_result": "Счет **4305"}
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
