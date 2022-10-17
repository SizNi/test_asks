from functools import wraps
i = 0
a = 0
def memoizing(arg1):  # сюда передается аргумент из аргумента декоратора
    def memoized(func):  # сюда передается функция и есть доступ к аргументу выше
        memory = {}  # словарь
        key_memory = [] # список для ключей, чтоб удалять по ним элементы словаря
        def inner(arg2):  # обертка, получающая аргументы функции и имеющая доступ ко всем аргументам
            key_memory.append(arg2)  # добавили ключ в список для удаления
            print(f'{key_memory} записали в список для удаления ключа')
            global i
            global a
            if i < arg1:  # если счетчик меньше арг1 - то спокойно записываем все в словарь
                memoized_result = memory.get(arg2)
                if memoized_result is None:
                    memoized_result = func(arg2)
                    memory[arg2] = memoized_result
                    i += 1
                    print(f'{memory} - ключи в мемори, а мемозед-резалт = {memoized_result}')
            else:  # если счетчик меньше - то удаляем из memory по номеру ключа, записанного в список key_memory
                memory.pop(key_memory[i-3])  # удаляем i ый элемент из словаря по элементу в списке
                memoized_result = memory.get(arg2)
                i += 1
                if memoized_result is None:
                    memoized_result = func(arg2)
                    memory[arg2] = memoized_result
                    print(f'{memory} - ключи в мемори, а мемозед-резалт = {memoized_result}') 
            return memoized_result
        return inner
    return memoized


@memoizing(3)
def f(x):
    print('Calculating...')
    print(x * 10)
    return x * 10
 
f(1)
f(2)
f(3)
f(30)
f(40)
f(50)
f(77)
