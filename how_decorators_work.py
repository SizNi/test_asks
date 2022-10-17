def my_new_dec(function):
    def wrapper(arg1, arg2):  # аргументы передаются сюда и в оригинальную функцию ниже
        print('работает перед оригинальной функцией')
        function(arg1, arg2)  # вызов оригинальной функции
        print('работает после оригинальной функции')
    return wrapper  # возвращает обертку вокруг оригинала + оригинал

@my_new_dec
def original_function(first_name, last_name):
    print(f'это попадет в декоратор {first_name} {last_name}')

original_function('Nik', 'Siz')
# запись выше эквивалентна следующей:
# original_function_decorated = my_new_dec(original_function)
# original_function_decorated()



