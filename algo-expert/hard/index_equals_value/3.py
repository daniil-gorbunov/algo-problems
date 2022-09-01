# hard, searching
# time O(logn) | space O(1)
def indexEqualsValue(arr):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == mid and (mid == 0 or arr[mid - 1] < mid - 1):
            return mid
        if arr[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1
    return -1
