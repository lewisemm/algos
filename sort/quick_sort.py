sorted_array = []
def quick_sort(array):
    largers, smallers, pivot = [], [], array[0]
    if len(array) > 1:
        array.pop(0)
        for no in array:
            if no > pivot:
                largers.append(no)
            elif no <= pivot:
                smallers.append(no)
        if len(smallers) > 0:
            quick_sort(smallers)
        sorted_array.append(pivot)
        if len(largers) > 0:
            quick_sort(largers)
    elif len(array) == 1:
        sorted_array.append(pivot)
        return pivot

array = [-182, 139, 163, -183, 4, 166, -89, -158, 14, 19, 39, -194, 197, -103, 
76, 165, -147, 74, -76, 70, -13, -81, 9, -14, -140, -189, -13, -128, 190, 152, 
-23, 171, -34, 87, -119, 196, -15, -176, 44, 155]


print("-" * 80)
print("Before: {0}".format(array))
quick_sort(array)
print("After: {0}".format(sorted_array))
print("-" * 80)