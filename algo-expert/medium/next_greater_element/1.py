# medium, stacks
# time O(n^2) | space O(n)
def nextGreaterElement(array):
    size = len(array)
    result = []
    for i in range(size):
        j = i
        greater = None
        while j < size + i and greater is None:
            j += 1
            idx = j % size
            if array[i] < array[idx]:
                greater = array[idx]
        result.append(-1 if greater is None else greater)
    return result
