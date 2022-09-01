# easy, greedy algorithms
# time O(nlogn) | space O(1)
def tandemBicycle(red, blue, fastest):
    result = 0
    red.sort()
    blue.sort(reverse=fastest)
    for i in range(len(red)):
        result += max(red[i], blue[i])
    return result
