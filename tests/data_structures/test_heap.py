from algorithms.data_structures.heap import MaxHeap


def test_max_heap_property():
    array_ints_small = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    heap = MaxHeap(array_ints_small)

    heap.insert(20)
    assert heap[0] == 20
    assert heap.maximum == heap[0] == 20

    heap.insert(999)
    assert heap[0] == 999
    assert heap[1] == 20
    assert heap.maximum == 999
