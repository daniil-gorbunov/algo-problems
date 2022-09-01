# medium, famous algorithms
# time O(n) | space O(1)
def kadanesAlgorithm(array):
    start = 0
    while start < len(array) - 1:
        if array[start] >= 0 or array[start] > array[start + 1]:
            break
        start += 1
    sum = array[start]
    maxSum = sum
    for i in range(start + 1, len(array)):
        sum += array[i]
        maxSum = max(maxSum, sum)
        sum = max(sum, 0)
    return maxSum
