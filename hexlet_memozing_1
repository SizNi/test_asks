def memoized(func):  # декоратор, принимающий на вход функцию
    memory = {}  # словарь, в который будут запоминаться значения
    def inner(arg):  # обертка, принимающая аргументы
        memoized_result = memory.get(arg)  # присваивание переменной значения словаря с переданным аргументом
        if memoized_result is None:  # если такого аргумента нет (None)
            memoized_result = func(arg)  # то переменной присваевается результат работы оригинальной функции с переданным аргументом
            memory[arg] = memoized_result  # и добавление в словарь с переданным аргументом полученного в результате работы оригинальной функции значения
        print(memoized_result)
        return memoized_result
    return inner


@memoized # добавляем декоратор
def f(x):  # Оригинальная функция
    print('Calculating...')
    return x * 10


f(3)  # пример
