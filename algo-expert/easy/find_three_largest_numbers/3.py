# easy, searching
# time O(n) | space O(1)
def findThreeLargestNumbers(array):
    max = [None] * 3
    for num in array:
        findMax(max, num)
    return max

def findMax(max, num):
    for i in reversed(range(len(max))):
        if max[i] is None or num > max[i]:
            shift(max, i, num)
            break;

def shift(max, idx, num):
    for i in range(idx):
        max[i] = max[i + 1]
    max[idx] = num
