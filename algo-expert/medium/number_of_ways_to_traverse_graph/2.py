# medium, DP
# time O(m*n) | space O(min(m,n))
def numberOfWaysToTraverseGraph(w, h):
    if h < w:
        w, h = h, w
    ways = [1 for col in range(w)]
    for row in range(1, h):
        prev = 1
        for col in range(1, w):
            temp = ways[col]
            ways[col] += prev
            prev = ways[col]
    return ways[-1]
