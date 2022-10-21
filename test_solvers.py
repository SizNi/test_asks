# разбор решения преподавателя для тестов
# результат работы функции set_
coll = {'a': {'b': {'c': 3}}}
set_(coll, ['a', 'b', 'c'], 4)
coll['a']['b']['c']  # 4
set_(coll, ['x', 'y', 'z'], 5)
coll['x']['y']['z']  # 5

import copy
import pytest
# тесты
@pytest.fixture
def data(): # фиксируем переменную, которую будет передавать
    return {"a": {"b": {"c": "d"}}}


def test_plain_set(data):
    data_copy = copy.deepcopy(data)  # создаем полноценную (глубокую) копию, а не копию со ссылками
    set_(data, ['a'], 'value')  # получаем объект по ключу 'a' из оригинальной data
    data_copy['a'] = 'value'  # получаем объект по ключу 'a' из глубокой копии
    assert data_copy == data  # сравниваем их, если они равны - возвращаем True


def test_nested_set(data):
    data_copy = copy.deepcopy(data) # создаем полноценную (глубокую) копию, а не копию со ссылками
    set_(data, ['a', 'b', 'c'], 'value')  # получаем результат работы set по всем трем ключам
    data_copy['a']['b']['c'] = 'value'  # присваеваем ключу по указанному пути в словаре data_copy значение value
    assert data_copy == data  # и сравниваем его с результатом, равны - возвращаем True


def test_new_property_set(data):
    data_copy = copy.deepcopy(data)  # создаем полноценную (глубокую) копию, а не копию со ссылками
    set_(data, ['a', 'b', 'd'], 'value')  # проверяем оригинал с ошибочным путем
    data_copy['a']['b']['d'] = 'value'
    assert data_copy == data  # получиться должно то же самое, что и с оригинальным словарем