import random

def merger(left, right):

    sorted_array = []
    # left index, right index, left_length, right_length
    li, ri, left_length, right_length = 0, 0, len(left), len(right)

    while li < left_length and ri < right_length:
        if left[li] <= right[ri]:
            sorted_array.append(left[li])
            li += 1
        else:
            sorted_array.append(right[ri])
            ri += 1

    while li < left_length:
        sorted_array.append(left[li])
        li += 1

    while ri < right_length:
        sorted_array.append(right[ri])
        ri += 1

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
