# -*- coding: utf-8 -*-

import random

from algorithms.sorting.bucket import bucket_sort

from six.moves import range


def assert_sorted(array):
    assert sorted(array) == array


def test_bucket_sort_small():
    array = [1, 9, 5, 3, 2, 7, 15]

    result = bucket_sort(array, 5)

    assert_sorted(result)


def test_bucket_sort_large():
    array = [random.random() for _ in range(100000)]

    result = bucket_sort(array, 5)

    assert_sorted(result)
