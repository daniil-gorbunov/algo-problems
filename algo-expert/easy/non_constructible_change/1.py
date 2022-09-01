# easy, arrays
# time O(nlogn) | space O(1)
def nonConstructibleChange(coins):
    coins.sort()
    min = 1
    for coin in coins:
        if coin > min:
            break
        min += coin
    return min
