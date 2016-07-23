# -*- coding: utf-8 -*-

from algorithms.sorting.insertion import insertion_sort


def insertion_for(array):
    return insertion_sort(array, method='forloop')

def insertion_while(array):
    return insertion_sort(array, method='whileloop')


def test_insertion_small(array_ints_small, assert_sorted):
    assert_sorted(array_ints_small, insertion_for)
    assert_sorted(array_ints_small, insertion_while)

def test_insertion_large(array_ints_large, assert_sorted):
    assert_sorted(array_ints_large, insertion_for)
    assert_sorted(array_ints_large, insertion_while)
