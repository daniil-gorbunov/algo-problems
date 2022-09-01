# easy, arrays
def sortedSquaredArray(arr):
    if (len(arr) == 1):
        return [arr[0] ** 2]
    result = []
    min = 0
    while min < len(arr) - 1 and abs(arr[min]) > abs(arr[min + 1]):
        min += 1
    left = min
    right = min
    if min == 0:
        right += 1
    else:
        left -= 1
    while left >= 0 or right < len(arr):
        if right >= len(arr) or (left >= 0 and abs(arr[left]) <= abs(arr[right])):
            result.append(arr[left] ** 2)
            left -= 1
        else:
            result.append(arr[right] ** 2)
            right += 1
    return result
