# hard, searching
def quickselect(arr, k):
    return recursiveSelect(arr, 0, len(arr) - 1, k - 1)

def recursiveSelect(arr, start, end, pos):
    while True:
        pivot = start
        left = pivot + 1
        right = end
        while left <= right:
            if arr[left] > arr[pivot] and arr[right] < arr[pivot]:
                arr[left], arr[right] = arr[right], arr[left]
            if arr[left] <= arr[pivot]:
                left += 1
            if arr[right] >= arr[pivot]:
                right -= 1
        arr[pivot], arr[right] = arr[right], arr[pivot]
        if right == pos:
            return arr[right]
        if right < pos:
            start = right + 1
        else:
            end = right - 1
