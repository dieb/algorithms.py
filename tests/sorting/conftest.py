# -*- coding: utf-8 -*-

import pytest

from random import random, randint
from six.moves import range


LIST_SIZE_SMALL = int(10e2)
LIST_SIZE_LARGE = int(10e3)
INT_RANGE = (0, int(10e2))


def random_array(size, content='float'):
    if content == 'float':
        return [random() for _ in range(size)]
    else:
        return [randint(*INT_RANGE) for _ in range(size)]

@pytest.fixture
def assert_sorted():
    def assert_fun(original, sort_function):
        assert sorted(original[:]) == sort_function(original[:])
    return assert_fun

@pytest.fixture
def array_floats_small():
    return random_array(LIST_SIZE_SMALL, 'float')

@pytest.fixture
def array_floats_large():
    return random_array(LIST_SIZE_LARGE, 'float')

@pytest.fixture
def array_ints_small():
    return random_array(LIST_SIZE_SMALL, 'int')

@pytest.fixture
def array_ints_large():
    return random_array(LIST_SIZE_LARGE, 'int')
