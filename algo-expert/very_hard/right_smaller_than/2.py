# time O(n^2) | space O(n)
def rightSmallerThan(array):
    result = [0] * len(array)
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[j] < array[i]:
                result[i] += 1
    return result
