# medium, arrays
# time O(n^2) | space O(1)
def smallestDifference(arr1, arr2):
    pair = []
    minDif = abs(arr1[0] - arr2[0])
    for num1 in arr1:
        for num2 in arr2:
            dif = abs(num1 - num2)
            if dif < minDif:
                minDif = dif
                pair = [num1, num2]
    return pair
