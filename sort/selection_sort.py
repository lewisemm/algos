def selection_sort(arr):
    end = len(arr) - 1
    # select index
    si = 0
    # least index
    least, li = float('inf'), float('inf')

    while si <= end:
        index = si
        while index <= end:
            if arr[index] < least:
                least = arr[index]
                li = index
            index += 1
        arr[si], arr[li] = arr[li], arr[si]
        si += 1
        least, li = float('inf'), float('inf')
    return arr
