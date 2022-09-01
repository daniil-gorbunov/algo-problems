# medium, graphs
# time O(n) | space O(1)
def hasSingleCycle(array):
    current = 0
    currentSum = 0
    checkSum = (len(array) - 1) * len(array) / 2
    for i in range(len(array)):
        current = (current + array[current]) % len(array)
        currentSum += current
    return current == 0 and currentSum == checkSum
