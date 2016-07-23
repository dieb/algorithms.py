# -*- coding: utf-8 -*-

from six.moves import range


__all__ = ('counting_sort',)


def counting_sort(array, k=None):
    """ Integer sorting algorithm.

    For each element in array, counts the number of elements that are less
    than itself. E.g. if there are 18 elements less than element, then it
    belongs on position=19 on the final array. This must be slightly modified
    when there are equal values.

    Analysis:
        - Allocating `output`: O(n) - could be passed to the function
        - Allocating `count`: O(k)
        - Histogram: O(n)
        - Indexes: O(k)
        - Creating output: O(n)
        Overall: O(k + n). When k = O(n), O(k + n) = O(n)

    Complexity: O(n)
    Space: O(n + k)
    """
    k = max(array)
    output = [None for i in range(len(array))]
    count = [0 for i in range(k + 1)]

    # Histogram of keys frequencies. `count[i]` contains the number of
    # occurrences of i in array.
    for elem in array:
        count[elem] += 1

    # Transform `count` into an array of indexes where each key goes.
    #
    # Starting from the left (index = 0), checks count[0], sets count[0] to
    # index (=0), then adds to index the number of occurences of 0.
    #
    # When repeated, this procedure iteratively transforms `count` into an
    # array where the position is the key and the position content is where to
    # start adding this key.
    index = 0

    for i in range(k + 1):
        old = count[i]
        count[i] = index
        index += old

    # Now `count[i]` is the index where `i` must be inserted at. For every
    # insertion, we update `count[i]` to be at the previous index + 1.
    for elem in array:
        output[count[elem]] = elem
        count[elem] += 1

    return output

