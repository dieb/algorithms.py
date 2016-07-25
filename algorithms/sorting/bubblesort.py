from six.moves import range

__all__ = ('bubble_sort',)


def bubble_sort(array):
    size = len(array)

    while True:
        swapped = False

        for i in range(size):
            if i == size - 1:
                break

            if array[i + 1] < array[i]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        if not swapped:
            break

    return array
