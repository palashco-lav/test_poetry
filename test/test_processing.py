import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "string, expected_result",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        )
    ],
)
def test_filter_by_state_param_executed(string: list, expected_result: str) -> None:
    assert filter_by_state(string) == expected_result


@pytest.mark.parametrize(
    "string, expected_result",
    [
        (
            [
                {"id": 34228829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939559570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {"id": 34228829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939559570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        )
    ],
)
def test_filter_by_state_param_executed_2(string: list, expected_result: str) -> None:
    assert filter_by_state(string, "EXECUTED") == expected_result


@pytest.mark.parametrize(
    "string, expected_result",
    [
        (
            [
                {"id": 34228829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939559570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        )
    ],
)
def test_filter_by_state_param_executed_canceled(string: list, expected_result: list) -> None:
    assert filter_by_state(string, "CANCELED") == expected_result


def test_filter_by_state_param_fixture(
    fix_process: list, fix_process_executed: list, fix_process_canceled: list
) -> None:
    assert filter_by_state(fix_process, "CANCELED") == fix_process_canceled
    assert filter_by_state(fix_process_executed, "EXECUTED") == fix_process_executed
    assert filter_by_state(fix_process_executed, "") == fix_process_executed


def test_filter_by_state_empy() -> None:
    """Проверка исключения при передаче пустых аргументов"""
    with pytest.raises(ValueError):
        filter_by_state([])
    with pytest.raises(ValueError):
        filter_by_state([], "")


def test_sort_by_date(fix_process: list, fix_process_sort_decrease: list, fix_process_sort_increase: list) -> None:
    """Проверка сортировки по дате с разными вызовами"""
    assert sort_by_date(fix_process) == fix_process_sort_decrease
    assert sort_by_date(fix_process, True) == fix_process_sort_decrease
    assert sort_by_date(fix_process, False) == fix_process_sort_increase


def test_sort_by_date_empy() -> None:
    """Проверка вызова с пустыми параметрами"""
    with pytest.raises(ValueError):
        sort_by_date([])
