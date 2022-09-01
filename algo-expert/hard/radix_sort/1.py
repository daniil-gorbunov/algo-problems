# time O(n*d) | space O(n), n - array length, d - longest number length
def radixSort(arr):
    if (len(arr)) == 0:
        return arr
    maxNumSize = len(str(max(arr)))
    for d in range(maxNumSize):
        counts = [0] * 10
        temp = [0] * len(arr)
        for num in arr:
            digit = getDigit(num, d)
            counts[digit] += 1
        for i in range(1, 10):
            counts[i] += counts[i - 1]
        for num in reversed(arr):
            digit = getDigit(num, d)
            counts[digit] -= 1
            temp[counts[digit]] = num
        arr = temp
    return arr

def getDigit(num, d):
    return num // (10 ** d) % 10
