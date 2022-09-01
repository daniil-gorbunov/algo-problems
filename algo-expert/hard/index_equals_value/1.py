# hard, searching
# time O(n) | space O(1)
def indexEqualsValue(arr):
    for i in range(len(arr)):
        if arr[i] == i:
            return i
    return -1
