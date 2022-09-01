# medium, recursion
# time O(n*2^n) | space O(n*2^n)
def powerset(array, idx=None):
    if idx is None:
        idx = len(array) - 1
    if idx < 0:
        return [[]]
    num = array[idx]
    powerSet = powerset(array, idx - 1)
    for i in range(len(powerSet)):
        subSet = powerSet[i]
        powerSet.append(subSet + [num])
    return powerSet
