# hard, arrays
# time O(nlogn) | space O(n)
def subarraySort(arr):
    sortedArr = sorted(arr)
    start = 0
    end = len(arr) - 1
    while start < end and arr[start] == sortedArr[start]:
        start += 1
    while start < end and arr[end] == sortedArr[end]:
        end -= 1
    return [start, end] if start < end else [-1, -1]
