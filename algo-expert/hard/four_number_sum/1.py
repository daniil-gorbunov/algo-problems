# hard, arrays
# time O(n^4) | space O(n)
def fourNumberSum(array, targetSum):
    quadruplets = []
    for a in range(len(array) - 3):
        for b in range(a + 1, len(array) - 2):
            for c in range(b + 1, len(array) - 1):
                for d in range(c + 1, len(array)):
                    if array[a] + array[b] + array[c] + array[d] == targetSum:
                        quadruplets.append([array[a], array[b], array[c], array[d]])
    return quadruplets
