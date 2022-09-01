# time O(n*d), space O(n)
def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for i in range(n + 1)]
    ways[0] = 1
    for d in denoms:
        for amount in range(1, n + 1):
            if d <= amount:
                ways[amount] += ways[amount - d]
    return ways[n]
