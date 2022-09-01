# medium, famous algorithms
# time O(n) | space O(1)
def kadanesAlgorithm(array):
    sum = array[0]
    maxSum = sum
    for i in range(1, len(array)):
        sum = max(array[i], sum + array[i])
        maxSum = max(maxSum, sum)
    return maxSum
