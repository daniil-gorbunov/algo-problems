# easy, recursion
# time O(1) | space O(1)
from math import sqrt
def getNthFib(n):
    sqrt5 = sqrt(5)
    return round(((1 + sqrt5) / 2) ** (n - 1) / sqrt5)
