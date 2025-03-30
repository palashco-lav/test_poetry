# The decorators module.

from collections.abc import Callable
from functools import wraps


def log(filename: str = ""):  # type: ignore
    """
    Декоратор ведения log файлов. Сохраняет либо в указанный файл либо выводит в консоль
    :param filename:
    :return:
    """

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(x: int, y: int) -> int:
            try:
                result: int = func(x, y)
                # Если имя файла определено, то пишем в файл
                if filename != "":
                    file = open(filename, "a")  # открываю файл с дописыванием информации в конец
                    file.write("my_function ok\n")
                    file.close()
                # Если файл не определён, но выводи принтом
                else:
                    print("my_function ok")
                return result
            except Exception as test_exception:
                # Если имя файла определено, то пишем в файл
                if filename != "":
                    file = open(filename, "a")  # открываю файл с дописыванием информации в конец
                    file.write("".join(f"my_function error: {test_exception}. Inputs: ({x}, {y}), {{}}\n"))
                    file.close()
                # Если файл не определён, но выводи принтом
                else:
                    print_data = "".join(f"my_function error: {test_exception}. Inputs: ({x}, {y}), {{}}")
                    print(print_data, end="\n")
                return 0

        return inner

    return wrapper
