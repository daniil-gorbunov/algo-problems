# medium, recursion
# time O(n*2^n) | space O(n*2^n)
def powerset(array):
    powerSet = [[]]
    for num in array:
        for i in range(len(powerSet)):
            subSet = powerSet[i]
            powerSet.append(subSet + [num])
    return powerSet
