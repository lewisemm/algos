from heap.min_heap import MinHeap


def heap_sort(unsorted):
    heap = MinHeap()
    heap.bulk_insert(unsorted)
    sorted_values = []
    while heap.get_size():
        sorted_values.append(heap.extract_min())
    return sorted_values


def heap_sort_single_insert(unsorted):
    heap = MinHeap()
    for val in unsorted:
        heap.single_insert(val)
    sorted_values = []
    while heap.get_size():
        sorted_values.append(heap.extract_min())
    return sorted_values
