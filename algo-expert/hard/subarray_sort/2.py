# hard, arrays
# time O(n) | space O(1)
def subarraySort(arr):
    firstDesc = 1
    while firstDesc < len(arr) and arr[firstDesc - 1] <= arr[firstDesc]:
        firstDesc += 1
    if firstDesc == len(arr):
        return [-1, -1]
    minDisplaced = firstDesc
    for i in range(minDisplaced, len(arr)):
        if arr[i] <= arr[minDisplaced]:
            minDisplaced = i

    firstAsc = len(arr) - 2
    while firstAsc >= 0 and arr[firstAsc] <= arr[firstAsc + 1]:
        firstAsc -= 1
    maxDisplaced = firstAsc
    for i in range(maxDisplaced, -1, -1):
        if arr[maxDisplaced] <= arr[i]:
            maxDisplaced = i

    start = 0
    while start < len(arr) - 1 and arr[start] <= arr[minDisplaced]:
        start += 1
    end = len(arr) - 1
    while end > 0 and arr[maxDisplaced] <= arr[end]:
        end -= 1

    return [start, end]
