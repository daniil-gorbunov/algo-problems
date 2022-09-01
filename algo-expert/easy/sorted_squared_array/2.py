# easy, arrays
# time O(n) | space O(n)
def sortedSquaredArray(arr):
    result = []
    left = 0
    right = len(arr) - 1
    while left <= right:
        if abs(arr[left]) > abs(arr[right]):
            result.insert(0, arr[left] ** 2)
            left += 1
        else:
            result.insert(0, arr[right] ** 2)
            right -= 1
    return result
