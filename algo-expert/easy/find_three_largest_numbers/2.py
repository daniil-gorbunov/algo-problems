# easy, searching
# time O(n) | space O(1)
def findThreeLargestNumbers(array):
    max1 = -float("inf")
    max2 = -float("inf")
    max3 = -float("inf")
    for num in array:
        if num > max3:
            max1 = max2
            max2 = max3
            max3 = num
        elif num > max2:
            max1 = max2
            max2 = num
        elif num > max1:
            max1 = num
    return [max1, max2, max3]
