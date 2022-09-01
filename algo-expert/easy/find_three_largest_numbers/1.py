# easy, searching
# time O(n*log(n)) | space O(n)
def findThreeLargestNumbers(array):
    return sorted(array)[len(array)-3:]
