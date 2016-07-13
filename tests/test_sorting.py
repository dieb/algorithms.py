# -*- coding: utf-8 -*-

import random

from six.moves import range

from algorithms.sorting.bucket import bucket_sort
from algorithms.sorting.insertion import insertion_sort


def assert_sorted(original, result):
    assert sorted(original) == list(result)


def seed_array_floats(size):
    return [random.random() for _ in range(size)]


def seed_array_ints(size):
    return [random.randint(0,1000) for _ in range(size)]


def test_bucket_sort_small():
    array = seed_array_floats(100)
    result = bucket_sort(array, 5)
    assert_sorted(array, result)


def test_bucket_sort_large():
    array = seed_array_floats(1000000)
    result = bucket_sort(array, 10)
    assert_sorted(array, result)


def test_insertion_small():
    array = seed_array_ints(100)
    result = insertion_sort(array[:])
    assert_sorted(array, result)


def test_insertion_large():
    array = seed_array_ints(10000)
    result = insertion_sort(array[:])
    assert_sorted(array, result)
