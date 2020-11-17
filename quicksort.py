def partition(data, start, end):
    pivot = data[start]
    left = start + 1
    right = end

    while True:
        while left <= right and data[right] >= pivot:
            right = right - 1
        while left <= right and data[left] <= pivot:
            left = left + 1
        if left <= right:
            data[left], data[right] = data[right], data[left]
        else:
            break
    data[start], data[right] = data[right], data[start]
    print(data)
    return right


def quicksort(data, start, end):
    if start >= end:
        return
    p = partition(data, start, end)
    quicksort(data, start, p - 1)
    quicksort(data, p + 1, end)