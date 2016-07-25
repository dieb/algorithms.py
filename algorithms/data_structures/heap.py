from six.moves import range

__all__ = ('MaxHeap',)


class AbstractHeap(object):
    """Heap is a tree-based data structure that satisfies the heap property:

    Given A is a parent node of B, then Key(A) is ordered in respect to Key(B)
    with the same ordering applying across the heap.

    Heaps can be further classified into "max heap" or "min heap". In a max
    heap, parent nodes are always greater or equal than those of children, and
    the highest key is the root node.
    """

    @staticmethod
    def parent(idx):
        return max(idx / 2 - 1, 0)

    @staticmethod
    def child_left(idx):
        return 2 * idx + 1

    @staticmethod
    def child_right(idx):
        return 2 * idx + 2


class MaxHeap(AbstractHeap):
    """ MaxHeap is a heap where the root node is the largest key. Parent nodes
    are always greater or equal than children nodes, therefore the smallest
    keys appear on the leaves.

    Heaps are typically implemented making use of arrays. Root is assigned to
    items[0].

    Definition (Height of a node): number of edges on the longest simple
    downward path from the node to a leaf

    Definition (Height of a heap): height of the root node

    """

    def __init__(self, items=[]):
        self.items = items[:]
        self.length = len(self.items)
        self._build_max_heap()

    @property
    def maximum(self):
        return self.items[0]

    def insert(self, key):
        self.length += 1
        self.items.append(float('-inf'))
        self.increase_key(self.length - 1, key)

    def increase_key(self, index, key):
        """ Sets items[index] = key and rebalances the tree efficiently.

        Traverse upwards through parents finding a potential new suitable
        position for this new value. This looks like the new large value
        is bubbling up to its appropriate position.
        """
        assert key >= self.items[index]

        self.items[index] = key

        while index > 0 and self.items[index] > self.items[self.parent(index)]:
            # This consists of a violation: item's value greater than parent
            self._swap(index, self.parent(index))
            index = self.parent(index)

    def _max_heapify(self, idx=0):
        """ Possible violations of the heap property

            - items[idx] is smaller than items[idx_left]
            - items[idx] is smaller than items[idx_right]

        Procedure:

            - Find which side violation is worse. Swap. Descend heapify.
        """
        idx_left = self.child_left(idx)
        idx_right = self.child_right(idx)
        idx_largest = idx

        if idx_left <= self.length - 1 and \
            self.items[idx] < self.items[idx_left]:
            idx_largest = idx_left

        if idx_right <= self.length - 1 and \
            self.items[idx_largest] < self.items[idx_right]:
            idx_largest = idx_right

        if idx_largest != idx:
            self._swap(idx, idx_largest)
            self._max_heapify(idx_largest)

    def _build_max_heap(self):
        if self.length > 0:
            for i in range(int(self.length / 2), -1, -1):
                self._max_heapify(i)

    def _swap(self, a, b):
        self.items[a], self.items[b] = self.items[b], self.items[a]

    def __getitem__(self, index):
        return self.items[index]
