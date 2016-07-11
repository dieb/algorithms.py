# -*- coding: utf-8 -*-

import math

from six.moves import range


__all__ = ('bucket_sort', 'DEFAULT_NUM_BUCKETS')


DEFAULT_NUM_BUCKETS = 5


def num_buckets(value_min, value_max, bucket_size):
    return int(math.floor((value_max - value_min) / bucket_size)) + 1


def bucket_sort(array, num_buckets=DEFAULT_NUM_BUCKETS):
    """ https://en.wikipedia.org/wiki/Bucket_sort

    Interesting when the input array is expected to be uniformily distributed
    over a range.
    """
    value_min, value_max = min(array), max(array)
    bucket_length = (value_max - value_min) / float(num_buckets)
    buckets = [[] for i in range(num_buckets)]

    for element in array:
        buckets_away = math.ceil((element - value_min)/bucket_length)
        bucket_idx = min(int(buckets_away), num_buckets - 1)
        buckets[bucket_idx].append(element)

    for bucket_idx, bucket in enumerate(buckets):
        buckets[bucket_idx] = sorted(bucket)

    return sum(buckets, [])



""" Example: 5 buckets

    min value = 1, max = 15 (y)
    ymax-ymin = 14 (length of the ruler)

    divide 14 into 5 buckets, each of length 2.8

    1st: [1, 3.8]
    2nd: [3.8, 6.6]
    3rd: [6.6, 9.4]
    4th: [9.4, 12.2]
    5th: [12.2, 15]

    Given an input element 5, figure out in which interval to put it.

        max is 15, min is 1, length is 14.
        5 is distance 5-min = 4 from minimum.
        distance / length = 4 / 2.8 = 1.42 buckets away forward.
        ceil is 2.

    Same logic for 9: 2.85 buckets away, thus bucket number 3 (ceil)

    Same logic for 14: 14-min = 13 (dist). distance / length = 4.6428 buckets
    away forward, ceil would be 5 (that'd mean index 6 , wrong).
    This can be fixed if we clamp with min(ceil, num_buckets - 1).

    Same reasoning could be used for a function that calculates the number of
    buckets away from the maximum value.
"""
