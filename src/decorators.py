from functools import wraps


def log(filename=""):
    def wrapper(func):
        @wraps(func)
        def inner(x, y):
            try:
                result = func(x, y)
                # Если имя файла определено, то пишем в файл
                if filename != "":
                    file = open(filename, "a") # открываю файл с дописыванием информации в конец
                    file.write("my_function ok\n")
                    file.close()
                # Если файл не определён, но выводи принтом
                else:
                    print("my_function ok")
                return result
            except Exception as test_exception:
                # Если имя файла определено, то пишем в файл
                if filename != "":
                    file = open(filename, "a") # открываю файл с дописыванием информации в конец
                    file.write("".join(f'my_function error: {test_exception}. Inputs: ({x}, {y}), {{}}\n'))
                    file.close()
                # Если файл не определён, но выводи принтом
                else:
                    print_data = "".join(f'my_function error: {test_exception}. Inputs: ({x}, {y}), {{}}')
                    print(print_data, end='\n')
        return inner
    return wrapper