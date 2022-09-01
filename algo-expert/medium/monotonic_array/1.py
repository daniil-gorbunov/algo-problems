# medium, arrays
# time O(n) | space O(1)
def isMonotonic(a):
    delta = 0
    for i in range(len(a) - 1):
        dif = a[i + 1] - a[i]
        if (dif < 0 and delta > 0) or (dif > 0  and delta < 0):
            return False
        if delta == 0:
            delta = dif
    return True
