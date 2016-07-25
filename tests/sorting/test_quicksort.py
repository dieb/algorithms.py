from algorithms.sorting.quicksort import quick_sort


def test_quick_sort_small(array_ints_small, assert_sorted):
    assert_sorted(array_ints_small, quick_sort)

def test_quick_sort_large(array_ints_large, assert_sorted):
    assert_sorted(array_ints_large, quick_sort)
