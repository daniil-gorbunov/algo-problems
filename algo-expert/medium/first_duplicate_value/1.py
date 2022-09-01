# medium, arrays
# time O(n) | space O(n)
def firstDuplicateValue(arr):
    visited = set()
    for num in arr:
        if num in visited:
            return num
        visited.add(num)
    return -1
