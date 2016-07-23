from algorithms.sorting.counting import counting_sort


def test_counting_small(array_ints_small, assert_sorted):
    assert_sorted(array_ints_small, counting_sort)

def test_counting_large(array_ints_large, assert_sorted):
    assert_sorted(array_ints_large, counting_sort)
