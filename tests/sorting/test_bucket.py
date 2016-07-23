from algorithms.sorting.bucket import bucket_sort


def test_bucket_sort_small(array_floats_small, assert_sorted):
    bucket_sort5 = lambda l: bucket_sort(l, 5)
    assert_sorted(array_floats_small, bucket_sort5)

def test_bucket_sort_large(array_floats_large, assert_sorted):
    bucket_sort10 = lambda l: bucket_sort(l, 10)
    assert_sorted(array_floats_large, bucket_sort10)
