import pytest

from src.masks import get_mask_account, get_mask_card_number


# Тесты для функции get_mask_card_number
@pytest.mark.parametrize("string, expected_result", [
    ("0123456789012345", "0123 45** **** 2345"),
    ("6325485693256988", "6325 48** **** 6988"),
    ("0000000000000000", "0000 00** **** 0000"),
    ("5987463325178856", "5987 46** **** 8856"),
])
def test_get_mask_card_number(string: str, expected_result: str) -> None:
    """Проверка работоспособности основного функционала параметризацией"""
    assert get_mask_card_number(string) == expected_result


def test_get_mask_card_number_fixture(fix_mask: str) -> None:
    """Проверка работы фикстурой"""
    pass
    # Проверка работоспособности маски
    assert get_mask_card_number(fix_mask) == '0123 45** **** 2345'


def test_get_mask_card_number_errors() -> None:
    """Проверка на ошибку по количеству цифр"""
    with pytest.raises(ValueError):
        get_mask_card_number("012345678901234")

    with pytest.raises(ValueError):
        get_mask_card_number("01234567890123456")

    with pytest.raises(ValueError):
        get_mask_card_number("012345678")

# Проверка на символы вместо цифр
    with pytest.raises(ValueError):
        get_mask_card_number("asddsDSADFASDDW")


def test_get_mask_card_number_empy() -> None:
    """Проверка на ошибку при передачи пустого аргумента"""
    with pytest.raises(ValueError):
        get_mask_card_number('')


# Тесты для функции test_get_mask_account
@pytest.mark.parametrize("string, expected_result", [
    ("0123456789012345", "**2345"),
    ("6325486988", "**6988"),
    ("00000000000", "**0000"),
    ("59874638856", "**8856"),
])
def test_get_mask_account(string: str, expected_result: str) -> None:
    """Проверка работоспособности основного функционала параметризацией"""
    assert get_mask_account(string) == expected_result


def test_get_mask_account_fixture(fix_mask: str) -> None:
    """Проверка работы фикстурой"""
    assert get_mask_account(fix_mask) == "**2345"


def test_get_mask_account_empy() -> None:
    """Проверка на ошибку при вызове с пустым аргументом"""
    with pytest.raises(ValueError):
        get_mask_account('')


def test_get_mask_account_wrong() -> None:
    """Проверка на ошибку при вызове с буквами вместо и вместе цифрами"""
    with pytest.raises(ValueError):
        get_mask_account('12544ПРН')

    with pytest.raises(ValueError):
        get_mask_account('asdefaSDAEFASd')
# Разбавляю нули символом "O"
    with pytest.raises(ValueError):
        get_mask_account('0000OOOO0000')
