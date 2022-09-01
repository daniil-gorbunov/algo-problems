# medium, DP
# time O(m+n) | space O(1)
from math import factorial
def numberOfWaysToTraverseGraph(w, h):
    w -= 1
    h -= 1
    return factorial(w + h) // (factorial(w) * factorial(h))
