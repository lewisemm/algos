def three_way_quick_sort(array, begin, end):
    """
    Three way quick sort maintains a lower and upper index for the pivot.
    values that are (equal to) pivot will be grouped within `pivot_begin` and
    `pivot_end`.
    This improves algorithm performance by minimizing the number of O(n**2)
    operations when sorting an array with many repetitions.
    """
    length = end - begin
    if length <= 0:
        return
    # pivot begin, pivot end, right index
    pivot_begin, pivot_end, ri = begin, begin, end
    while pivot_end < ri:
        if array[pivot_end] > array[pivot_end + 1]:
            array[pivot_begin], array[pivot_end + 1] = \
                array[pivot_end + 1], array[pivot_begin]
            pivot_begin += 1
            pivot_end += 1
        elif array[pivot_end] == array[pivot_end + 1]:
            pivot_end += 1
        elif array[pivot_end] < array[pivot_end + 1]:
            array[pivot_end + 1], array[ri] = array[ri], array[pivot_end + 1]
            ri -= 1
    three_way_quick_sort(array, begin, pivot_begin - 1)
    three_way_quick_sort(array, pivot_end + 1, end)
