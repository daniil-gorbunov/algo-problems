# arrays
# time O(nlogn) | space O(1)
def twoNumberSum(array, targetSum):
    array.sort()
    l = 0
    r = len(array) - 1
    while l < r:
        sum = array[l] + array[r]
        if sum == targetSum:
            return [array[l], array[r]]
        elif sum < targetSum:
            l += 1
        else:
            r -= 1
    return []
