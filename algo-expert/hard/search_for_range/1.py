# hard, searching
# time O(logn) | space O(1)
def searchForRange(arr, target):
    targetIdx = getTargetIdx(arr, target)
    if targetIdx == -1:
        return [-1, -1]
    range = [targetIdx, targetIdx]
    left, right = 0, targetIdx - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] != target and arr[mid + 1] == target:
            range[0] = mid + 1
            break
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    left, right = targetIdx + 1, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target and (mid == len(arr) - 1 or arr[mid + 1] != target):
            range[1] = mid
            break
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return range

def getTargetIdx(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            return mid
        if target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1
