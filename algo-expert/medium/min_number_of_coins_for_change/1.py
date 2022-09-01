# medium, DP
# time O(n*d) | space O(n)
def minNumberOfCoinsForChange(n, denoms):
    ways = [float('inf') for i in range(n + 1)]
    ways[0] = 0
    for d in denoms:
        for amount in range(1, n + 1):
            if d <= amount:
                ways[amount] = min(ways[amount], ways[amount - d] + 1)
    return ways[n] if ways[n] != float('inf') else -1
