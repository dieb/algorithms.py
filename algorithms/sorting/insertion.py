
from six.moves import range


__all__ = ('insertion_sort',)


def insertion_sort(array, method='forloop'):
    """ Sorts `array` similarly as we sort a deck of cards. Start with an empty
    left hand and cards on the table facing down. We pick a card from the table
    and find the appropriate position on the left hand.

    Complexity:
        - Running time (Worst):     O(n^2)
        - Running time (Average):   O(n^2)

    Memory = O(1) (in-place)
    """
    return METHODS[method](array)


def insertion_sort_for_loop(array):
    """ Looks at items from left to right, starting from the second position.
    The algorithm repositions each item the furthest to the left it can, as
    long its left is less or equal than itself.

    For every `item`,
        Find the lowest-index item to the left that's higher than `item`
        If found:
            Remove previous item from its position
            Insert item on lowest_idx

    In summary, we act similarly to the deck of cards by sequentially searching
    what position to insert it.

    Although slightly longer and more verbose, this code is exactly as
    efficient as the while loop version. I think this one is easier for the
    reader in the sense that it's easily relatable to the deck of cards sorting
    procedure most people are familiar with.

    On the downside, this one changes the list allocation size when it pops the
    current item to reposition it somewhere else. Depending on the underlying
    software implementation, this could be negligible. For example, CPython
    implementation over-allocates proportionally to the list size (e.g. you
    create a list with 4 elements, it allocates room for 8). Thus, this will
    rarely result in a realloc() system call, pretty cheap.
    """
    for idx in range(1, len(array)):
        item = array[idx]

        # Item cannot be any place to the left of a larger number
        # Since left is guaranteed to be sorted, this item is already on
        # its final position.
        if item >= array[idx - 1]:
            continue

        # Find lowest to the left that this can be inserted into
        lowest_idx = None

        for j in range(idx - 1, -1, -1):
            # Item cannot be to the left of array[j] (item is larger)
            # Since the left is guaranteed to be sorted, we can stop here
            if item > array[j]:
                break

            # Item could belong to the left of array[j] (item is smaller)
            if item < array[j]:
                lowest_idx = j

        if lowest_idx is not None:
            array.pop(idx)
            array.insert(lowest_idx, item)

    return array


def insertion_sort_while_loop(array):
    """ Looks at items from left to right, starting from the second position.

    For every `item`:
        For every `prev_item` to the left of `item`:
            If larger than item, copy it one place forward
            If smaller than item, stop
        Insert item before last larger item copied to the right

    The end result of copying forward all larger items and then inserting this
    smaller item to the left is that `item` gets inserted on its final position
    since anything to the left is definitely already sorted (and we would
    never add to the left of a smaller item).

    Compared to the for loop, this one benefits from not modifying the original
    array allocation size. Personally, I think this one loses in code
    simplicity, readability and easiness to understand - since the sorting seems to happen implicitly from the copy forward operations.

    Interestingly, both methods are equivalent because the left-search is
    exactly the same.
    """
    for idx in range(1, len(array)):
        item = array[idx]

        i = idx - 1

        while i > -1 and array[i] > item:
            array[i + 1] = array[i]
            i = i - 1

        array[i + 1] = item

    return array


METHODS = {
    'forloop': insertion_sort_for_loop,
    'whileloop': insertion_sort_while_loop
}

