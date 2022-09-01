# medium, arrays
# time O(n) | space O(1)
def firstDuplicateValue(arr):
    for num in arr:
        idx = abs(num) - 1
        if arr[idx] < 0:
            return abs(num)
        arr[idx] *= -1
    return -1
