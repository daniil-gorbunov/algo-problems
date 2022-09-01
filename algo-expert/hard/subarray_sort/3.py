# hard, arrays
# time O(n) | space O(1)
def subarraySort(arr):
    minDisplaced = float('inf')
    maxDisplaced = float('-inf')
    for i in range(len(arr)):
        if not isOrdered(i, arr):
            minDisplaced = min(minDisplaced, arr[i])
            maxDisplaced = max(maxDisplaced, arr[i])
    if maxDisplaced < minDisplaced:
        return [-1, -1]
    start = 0
    while arr[start] <= minDisplaced:
        start += 1
    end = len(arr) - 1
    while maxDisplaced <= arr[end]:
        end -= 1
    return [start, end]

def isOrdered(i, arr):
    leftOrdered = i == 0 or arr[i - 1] <= arr[i]
    rightOrdered = i == len(arr) - 1 or arr[i] <= arr[i + 1]
    return leftOrdered and rightOrdered
