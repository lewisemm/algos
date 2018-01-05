def partition(array, first, last):

    pivot = array[last]

    wall = first

    for index in range(first, last):
        if array[index] < pivot:
            array[index], array[wall] = array[wall], array[index]
            wall += 1

    array.insert(wall, array.pop(last))

    return wall


def quick_sort(array, first, last):

    if first < last:
        pivot = partition(array, first, last)
        quick_sort(array, first, pivot - 1)
        quick_sort(array, pivot + 1, last)

    return array
