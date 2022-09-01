# medium, arrays
# time O(n) | space O(n)
def arrayOfProducts(arr):
    left = [1 for _ in range(len(arr))]
    right = [1 for _ in range(len(arr))]
    for i in range(1, len(arr)):
        revIdx = len(arr) - i
        left[i] =  left[i - 1] * arr[i - 1]
        right[revIdx - 1] = right[revIdx] * arr[revIdx]
    return [left[i] * right[i] for i in range(len(arr))]
