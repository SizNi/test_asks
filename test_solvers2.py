# мое решение по задаче с тестами с комментариями
from cart import get_implementations
import pytest
import os

make_cart = get_implementations()  # называем функцию поудобнее


good1 = {'name': 'car', 'price': 1}  # объекты, на которых будем тестировать
good2 = {'name': 'car', 'price': 2}
count1 = 10
count2 = 2
    
# BEGIN (write your solution here)
def test_get_items():  # тут по хорошему надо было назвать по имени всей функции, а не ее части
    x = make_cart()  # создаем корзину из созданных выше объектов
    make_cart.add_item(x, good1, count1)  # здесь и ниже проверяем на соответствие условий
    make_cart.add_item(x, good2, count2)
    assert make_cart.get_items(x) == [{'good': {'name': 'car', 'price': 1}, 'count': 10}, {'good': {'name': 'car', 'price': 2}, 'count': 2}]
    assert make_cart.get_cost(x) == 14
    assert make_cart.get_count(x) == 12
    

    
# END
