from algorithms.sorting.bubblesort import bubble_sort


def test_bubble_sort_small(array_ints_small, assert_sorted):
    assert_sorted(array_ints_small, bubble_sort)

def test_bubble_sort_large(array_ints_large, assert_sorted):
    assert_sorted(array_ints_large[:800], bubble_sort)
