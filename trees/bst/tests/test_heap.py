from random import randint
from bst import heap

def test_create_max_heap_from_list():
    """
    [0, 1, 2, 3] ===> [0, 3, 2, 1]
    """
    h = heap.Heap([0, 1, 2, 3])
    assert h.heap == [0, 3, 2, 1]

def test_extract_max():
    """
    Generate ten random integers and store them in an array.

    Create a heap from aforementioned array.

    Confirm that successive calls to `extract_max()` return values in decreasing
    order.
    """
    size = 10
    array = [0]
    for no in range(size):
        array.append(randint(0, 100))
    
    h = heap.Heap(array)
    one = h.extract_max()
    two = h.extract_max()
    assert one >= two
    assert len(h.heap) == 9
    three = h.extract_max()
    assert two >= three
    assert len(h.heap) == 8
    four = h.extract_max()
    assert three >= four
    assert len(h.heap) == 7
    five = h.extract_max()
    assert four >= five
    assert len(h.heap) == 6
    six = h.extract_max()
    assert five >= six
    assert len(h.heap) == 5
    seven = h.extract_max()
    assert six >= seven
    assert len(h.heap) == 4
    eight = h.extract_max()
    assert seven >= eight
    assert len(h.heap) == 3
    nine = h.extract_max()
    assert eight >= nine
    assert len(h.heap) == 2
    ten = h.extract_max()
    assert nine >= ten
    assert len(h.heap) == 1
