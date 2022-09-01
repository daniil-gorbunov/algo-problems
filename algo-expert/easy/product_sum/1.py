# easy, recursion
# time O(n) | space O(d)
def productSum(array, depth=1):
    if type(array) is int:
        return array
    sum = 0
    for el in array:
        sum += productSum(el, depth + 1)
    return sum * depth
