# medium, recursion
# time O(n*2^n) | space O(n*2^n)
def powerset(array):
    powerSet = []
    for i in range(2 ** len(array)):
        subSet = []
        for pos in range(len(array)):
            if i & 2 ** pos > 0:
                subSet.append(array[pos])
        powerSet.append(subSet)
    return powerSet
