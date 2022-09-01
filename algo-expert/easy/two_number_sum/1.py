# arrays
# time O(n^2) | space O(1)
def twoNumberSum(array, targetSum):
    for i, a in enumerate(array):
        for b in array[i+1:]:
            if a + b == targetSum:
                return [a, b]
    return []
