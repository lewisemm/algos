def sorted_sub_array(array, length_sorted):
    
    len_array = len(array)

    for ssorted in range(length_sorted, -1, -1):
        if (ssorted + 1) < len_array and array[ssorted] > array[ssorted + 1]:
            array[ssorted], array[ssorted + 1] = \
                array[ssorted + 1], array[ssorted]        

def insertion_sort(array):

    length = len(array)

    is_sorted = 0

    for index, item in enumerate(array):
        if index > 0 and array[index] < array[index - 1]:
            sorted_sub_array(array, is_sorted)
        is_sorted += 1

    return array
