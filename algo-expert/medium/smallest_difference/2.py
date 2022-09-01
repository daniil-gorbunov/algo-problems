# medium, arrays
# time O(nlogn + mlogm) | space O(1)
def smallestDifference(arr1, arr2):
    arr1.sort()
    arr2.sort()
    p1 = 0
    p2 = 0
    smallest = [arr1[0], arr2[0]]
    dif = abs(arr1[0] - arr2[0])
    while p1 < len(arr1) and p2 < len(arr2):
        num1 = arr1[p1]
        num2 = arr2[p2]
        if abs(num1 - num2) < dif:
            smallest = [num1, num2]
            dif = abs(num1 - num2)
        if num1 < num2:
            p1 += 1
        else:
            p2 += 1
    return smallest
