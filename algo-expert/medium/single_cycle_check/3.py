# medium, graphs
# time O(n) | space O(1)
def hasSingleCycle(array):
    current = 0
    for visitNum in range(len(array)):
        if visitNum > 0 and current == 0:
            return False
        current = (current + array[current]) % len(array)
    return current == 0
