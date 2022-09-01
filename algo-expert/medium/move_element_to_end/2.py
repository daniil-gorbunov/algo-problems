# medium, arrays
# time O(n) | space O(1)
def moveElementToEnd(arr, toMove):
    left = 0
    right = len(arr) - 1
    while left < right:
        while arr[right] == toMove and left < right:
            right -= 1
        while arr[left] != toMove and left < right:
            left += 1
        while arr[left] == toMove and arr[right] != toMove and left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr
