# time O(n) | space O(1)
def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0
    prevSum = 0
    curSum = array[0]
    for i in range(1, len(array)):
        nextSum = max(array[i] + prevSum, curSum)
        prevSum = curSum
        curSum = nextSum
    return curSum
