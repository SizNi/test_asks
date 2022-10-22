import os
from solution import fill
import pytest

import right
import solution
import wrong1
import wrong2
import wrong3


@pytest.fixture(name='fill')
def _fill():
    name = os.environ['FUNCTION_VERSION']
    return {
        "user_implementation": solution,
        "right": right,
        "wrong1": wrong1,
        "wrong2": wrong2,
        "wrong3": wrong3,
    }[name].fill


@pytest.fixture(name='collection')
def _collection():
    return [1, 2, 3, 4]


def test_fill(collection, fill):
    fill(collection, '*', 1, 3)
    assert collection == [1, '*', '*', 4]


# BEGIN (write your solution here)
@pytest.fixture
def coll():
    return [1, 2, 3, 4]
def test_fill_1():
    fill(coll, '*', 1, 3)
    assert coll == [1, '*', '*', 4]

def test_fill_2():
    fill(coll, '*')
    assert coll == ['*', '*', '*', '*']

def test_fill_3():
    fill(coll, '*', 4)
    assert coll == [1, 2, 3, 4]

def test_fill_3():
    fill(coll, '*', 0, 10)
    assert coll == ['*', '*', '*', '*']

# END
