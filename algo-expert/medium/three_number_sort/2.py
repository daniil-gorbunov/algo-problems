# medium, searching
# time O(n) | space O(1)
def threeNumberSort(array, order):
    left, current, right = 0, 0, len(array) - 1
    while current <= right:
        if array[current] == order[0]:
            array[current], array[left] = array[left], array[current]
            left += 1
            current += 1
        elif array[current] == order[2]:
            array[current], array[right] = array[right], array[current]
            right -= 1
        else:
            current += 1
    return array
