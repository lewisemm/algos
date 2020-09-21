def kth_largest(array, k):
    """
    Find the k(th) largest element in an array in O(n) complexity.
    """
    largest = array[0]
    empty = [None] * (largest + 1)
    offset = 0
    for digit in array:
        if digit >= largest:
            empty += [None] * (digit - largest)
            largest = digit
        if digit in empty:
            index = empty.index(digit)
            empty.insert(index + 1, digit)
            offset += 1
            continue
        empty[digit + offset] = digit
    empty = [digit for digit in empty if digit != None]
    return empty[len(empty) - k]


array = [6, 7, 4, 3, 1, 2]
k = 3
print(kth_largest(array, k))

array = [2, 3, 4, 5, 6, 2, 8, 3, 4, 5, 7]
k = 5
print(kth_largest(array, k))

array = [2, 12, 7, 3, 18, 1, 13, 5, 16, 6, 15, 8, 17, 9, 4, 0, 10, 14, 11]
k = 7
print(kth_largest(array, k))