# medium, arrays
# time O(n) | space O(1)
def isMonotonic(a):
    hasIncrease = False
    hasDecrease = False
    for i in range(len(a) - 1):
        if a[i] < a[i + 1]:
            hasIncrease = True
        if a[i] > a[i + 1]:
            hasDecrease = True
    return not (hasIncrease or hasDecrease)
