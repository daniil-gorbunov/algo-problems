# hard, searching
# time O(logn) | space O(1)
def shiftedBinarySearch(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[left] < arr[mid]:
            if target < arr[mid] and target >= arr[left]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target > arr[mid] and target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
