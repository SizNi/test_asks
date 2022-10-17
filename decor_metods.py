def method_friendly_decorator(method_to_decorate):  # сюда вызывается оригинальная функция
    def wrapper(self, lie):  # сюда передаются аргументы из оригинальной функции
        lie = lie - 3  # меняем значение lie
        return method_to_decorate(self, lie)  # возвращение оригинальной функции с новыми аргументами
    return wrapper
 
 
class Lucy(object):  # создание объекта для метода
 
    def __init__(self):
        self.age = 32
 
    @method_friendly_decorator
    def sayYourAge(self, lie):
        print(f"Мне {self.age + lie}, а ты бы сколько дал?")  # сюда в итоге поступают измененные значения
l = Lucy()
l.sayYourAge(-6)  # вызов функции с параметров lie

# то есть у нас есть объект Lucy, которому по умолчанию 32 года и она привирает на lie, который можно задавать в аргументах