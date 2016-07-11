# -*- coding: utf-8 -*-

import math

from six.moves import xrange


def int_size(x):
    """ Returns the number of bits required to represent x in base 2.
    """
    return int(math.floor(math.log(x, 2) + 1))


def msbits(x, num_bits):
    """ Returns the count most significant bits of x.

    E.g. X_(b_10) = 341
    X_(b_2) = 0001 0101 0101
    msbits(X, 1) = 0      = 0 (b_10)
    msbits(X, 5) = 0001 0 = 2 (b_10)
    """
    return int(math.floor(x/(2.0**(int_size(x) - num_bits))))


def bucket_sort(array, num_buckets):
    """ https://en.wikipedia.org/wiki/Bucket_sort

    Interesting when the input array is expected to be uniformily distributed
    over a range.

    """
    buckets = [[] for i in xrange(num_buckets)]
    minimal, maximum = min(array), max(array)
    sorted_array = []

    for item in array:
        bucket_idx = min(int(math.floor(num_buckets * (item/float(maximum)))),
                         num_buckets - 1)
        buckets[bucket_idx].append(item)

    for bucket_idx, bucket in enumerate(buckets):
        sorted_array += sorted(bucket)

    return sorted_array

