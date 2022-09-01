# medium, arrays
# time O(n) | space O(1)
def moveElementToEnd(arr, toMove):
    left = 0
    right = len(arr) - 1
    while left < right:
        while arr[right] == toMove and left < right:
            right -= 1
        if arr[left] == toMove:
            arr[left], arr[right] = arr[right], arr[left]
        left += 1
    return arr
