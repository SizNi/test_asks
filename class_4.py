from functools import wraps

def suppress(exception, *, or_return=None):  # принимает аргументы
    """Suppress exceptions of provided class(es) and return a value instead."""
    def wrapper(function):  # принимает функцию
        # заменяет атрибуты декоратора supress
        # на атрибуты полученной функции
        @wraps(function)
        def inner(*args, **kwargs):  # принимает функцию
            try:  # запускает функцию, в кторой могут быть проблемы
                return function(*args, **kwargs)
            except exception:  # перехватывает исключение, из переменной декоратора
                return or_return  # возвращает заданное значение (по умолчанию None)
        return inner
    return wrapper