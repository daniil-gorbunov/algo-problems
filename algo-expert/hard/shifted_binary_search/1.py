# hard, searching
# time O(logn) | space O(1)
def shiftedBinarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    mid = right // 2
    if arr[-1] < arr[0]:
        while arr[mid] < arr[mid + 1] and arr[mid] != target:
            if arr[mid] < arr[0]:
                right = mid - 1
            else:
                left = mid + 1
            mid = (left + right) // 2
        if target == arr[mid]:
            return mid
        if target < arr[0]:
            left = mid + 1
            right = len(arr) - 1
        else:
            left = 0
            right = mid - 1
        mid = (left + right) // 2

    while left < right and arr[mid] != target:
        if target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
        mid = (left + right) // 2
    return mid if arr[mid] == target else -1
