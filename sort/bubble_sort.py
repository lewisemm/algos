def bubble_sort(array):

    length = len(array)
    
    for loop in range(length):
        swapped = False

        for index in range(length):
            if index > 0 and array[index - 1] > array[index]:
                array[index], array[index - 1] = array[index - 1], array[index]
                swapped = True

        if not swapped:
            break

    return array
    