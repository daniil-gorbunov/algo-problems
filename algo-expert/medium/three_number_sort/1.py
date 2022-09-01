# medium, searching
# time O(n) | space O(1)
def threeNumberSort(array, order):
    left = 0
    right = len(array) - 1
    current = 0
    while current <= right and left < right:
        while left < len(array) and array[left] == order[0]:
            left += 1
            current = left
        while right > 0 and array[right] == order[2]:
            right -= 1
        if array[current] == order[0]:
            swap(current, left, array)
            left += 1
        elif array[current] == order[2]:
            swap(current, right, array)
            right -= 1
        else:
            current += 1
    return array

def swap(a, b, array):
    array[a], array[b] = array[b], array[a]
