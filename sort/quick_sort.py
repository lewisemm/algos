def quick_sort(arr, start, stop):
    length = stop - start
    if length <= 1:
        if length == 1 and arr[start] > arr[stop]:
            arr[start], arr[stop] = arr[stop], arr[start]
        return
    # pivot index, left index, right index
    pi, li, ri = start, start + 1, stop
    while li <= ri:
        if arr[li] > arr[pi]:
            arr[li], arr[ri] = arr[ri], arr[li]
            ri -= 1
        elif arr[li] <= arr[pi]:
            arr[li], arr[pi] = arr[pi], arr[li]
            pi += 1
            li = pi + 1
    quick_sort(arr, start, pi - 1)
    quick_sort(arr, pi + 1, stop)
