__all__ = ('quick_sort',)


def quick_sort(array):
    if len(array) == 0: return []

    pivot_idx = len(array) - 1
    pivot = array[pivot_idx]

    left = []
    right = []

    for idx, element in enumerate(array):
        if idx == pivot_idx:
            continue
        if element < pivot:
            left.append(element)
        else:
            right.append(element)

    return quick_sort(left) + [pivot] + quick_sort(right)



