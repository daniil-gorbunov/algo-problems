# Best: O(nlog(n)) time | O(log(n)) space
# Average: O(nlog(n)) time | O(log(n)) space
# Worst: O(n^2) time | O(log(n)) space
def quickSort(arr, start = 0, end = None):
    if end is None:
        end = len(arr) - 1
    if start >= end:
        return arr
    pivot = start
    left = pivot + 1
    right = end
    while left <= right:
        if arr[left] > arr[pivot] and arr[right] < arr[pivot]:
            arr[left], arr[right] = arr[right], arr[left]
        if arr[left] <= arr[pivot]:
            left += 1
        if arr[right] >= arr[pivot]:
            right -= 1
    arr[pivot], arr[right] = arr[right], arr[pivot]
    quickSort(arr, start, right - 1)
    quickSort(arr, right + 1, end)
    return arr
