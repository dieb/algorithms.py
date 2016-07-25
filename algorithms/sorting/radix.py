from math import log, ceil
from six.moves import range

__all__ = ('radix_sort',)


def num_digits(number):
    if number == 0:
        return 1
    return int(ceil(log(number + 1, 10)))

def lsdigit(number, index):
    """ Returns the least significant digit, offset by `index`.
    """
    return int(number % (10**(index + 1)) / (10**index))

def radix_sort(array):
    """ Radix sort - https://en.wikipedia.org/wiki/Radix_sort

    Sorts digit per digit, starting from the least significant digits (LSD).

    Example: [599, 100, 102, 204, 202, 152, 444]
    - Max number size is 3 digits
    - Go through array observing the LSD
        - Creates 10 buckets, for each digit in 0..9
        - e.g. 599, lsd=9, goes into bucket #9
        - e.g. 204, lsd=4, goes into bucket #4
        and so on
    - Buckets are now sorted in respect to the LSD
    - Clear array, merge buckets into the array
    - Repeat same process now for the second LSD
        - Reallocate the 10 empty buckets
        - Place items on each bucket:
            - e.g. 599, lsd_1=9, goes into bucket #9
            - e.g. 204, lsd_1=0, goes into bucket #0
            and so on
    - Repeat same process for the third LSD (last one)
    - Clear array, merge buckets into the array
    - List is sorted
    """
    for digit in range(num_digits(max(array))):
        bins = [[] for i in range(10)]

        for item in array:
            bins[lsdigit(item, digit)].append(item)

        array = []

        for bin in bins:
            array.extend(bin)

    return array
