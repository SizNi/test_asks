def decorator_with_args(decorator_to_enhance):  # это декоратор для декораторов, дает возможность любому декоратору принимать произвольные аргументы
    def decorator_maker(*args, **kwargs):  # создатель декораторов, который принимает аргументы
        def decorator_wrapper(func):  # декоратор, принимающий на вход функцию и имеющий доступ к аргументам args, kwargs
            return decorator_to_enhance(func, *args, **kwargs)  #  возвращаем то, что вернет нам изначальный декоратор, который в свою очередь просто функция, возвращающая функцию. Обязательно такой порядок и количество аргументов
        return decorator_wrapper
    return decorator_maker
# создаём функцию, которую будем использовать как декоратор и декорируем её
# не забыть, что она должна иметь вид "decorator(func, *args, **kwargs)"
@decorator_with_args
def decorated_decorator(func, *args, **kwargs):  # это функция декоратор, поступающая decorator_with_args
    def wrapper(function_arg1, function_arg2):
        print("Мне тут передали...:", args, kwargs)
        return func(function_arg1, function_arg2)
    return wrapper

@decorated_decorator(42, 404, 1024)  # это аргументы функции декоратора выше
def decorated_function(function_arg1, function_arg2):  # это оригинальная функция, которая вызывается ниже с аргументами
    print("Привет", function_arg1, function_arg2)
 
decorated_function("Вселенная и", "всё прочее")

# Итого: мы вызвали decorated_function, для нее сделали декоратор decorated_decorator
# для которого был сделан декоратор decorator with args и так далее