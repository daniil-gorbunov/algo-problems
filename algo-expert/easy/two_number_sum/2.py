# arrays
# time O(n) | space O(n)
def twoNumberSum(array, targetSum):
    map = {}
    for a in array:
        b = targetSum - a
        if b in map:
            return [a, b]
        else:
            map[a] = True
    return []
