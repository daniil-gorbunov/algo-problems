# hard, searching
# time O(logn) | space O(1)
def searchForRange(arr, target):
    return [
        calcRangeBorder(arr, target, True),
        calcRangeBorder(arr, target, False),
    ]

def calcRangeBorder(arr, target, searchingLeft):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        foundBorder = (mid == 0 or arr[mid - 1] != target) if searchingLeft else (mid == len(arr) - 1 or arr[mid + 1] != target)
        if arr[mid] == target and foundBorder:
            return mid
        shouldGoright = arr[mid] < target if searchingLeft else arr[mid] <= target
        if shouldGoright:
            left = mid + 1
        else:
            right = mid - 1
    return -1
