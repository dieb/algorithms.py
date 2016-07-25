from algorithms.sorting.radix import radix_sort


def test_small(array_ints_small, assert_sorted):
    assert_sorted(array_ints_small, radix_sort)

def test_large(array_ints_large, assert_sorted):
    assert_sorted(array_ints_large, radix_sort)
