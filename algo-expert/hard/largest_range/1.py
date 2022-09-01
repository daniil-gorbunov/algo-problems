# hard, arrays
# time O(nlogn) | space O(1)
def largestRange(array):
    array.sort()
    largest = [0, 0]
    start = end = 0
    while end < len(array) - 1:
        if array[end + 1] != array[end] + 1 and array[end + 1] != array[end]:
            largest = getLargestRange(start, end, largest, array)
            start = end + 1
        end += 1
    largest = getLargestRange(start, end, largest, array)
    return [array[largest[0]], array[largest[1]]]

def getLargestRange(start, end, largest, array):
    if array[end] - array[start] > array[largest[1]] - array[largest[0]]:
        return [start, end]
    return largest
