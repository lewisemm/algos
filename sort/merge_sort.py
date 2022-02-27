import random

def merger(left, right):

    sorted_array = []

    while right and left and len(left) and len(right):
        if left[0] <= right[0]:
            sorted_array.append(left.pop(0))
        else:
            sorted_array.append(right.pop(0))

    while left:
        sorted_array.append(left.pop(0))

    while right:
        sorted_array.append(right.pop(0))

    return sorted_array
            

def merge_sort(unsorted):
    length = len(unsorted)

    if length <= 1:
        return unsorted

    middle = length // 2

    left = unsorted[0:middle]
    right = unsorted[middle:length]

    left = merge_sort(left)
    right = merge_sort(right)

    return merger(left, right)
