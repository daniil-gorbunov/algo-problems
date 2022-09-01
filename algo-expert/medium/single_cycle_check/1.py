# medium, graphs
# time O(n) | space O(n)
def hasSingleCycle(array):
    visited = set()
    current = 0
    for i in range(len(array)):
        current = (current + array[current]) % len(array)
        if current in visited:
            return False
        visited.add(current)
    return True
