def my_new_dec(function):
    def wrapper():
        print('работает перед оригинальной функцией')
        function()  # вызов оригинальной функции
        print('работает после оригинальной функции')
    return wrapper  # возвращает обертку вокруг оригинала + оригинал

def original_function():
    print('это попадет в декоратор')

original_function_decorated = my_new_dec(original_function)
original_function_decorated()