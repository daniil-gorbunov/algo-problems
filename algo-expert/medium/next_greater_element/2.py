# medium, stacks
# time O(n) | space O(n)
def nextGreaterElement(array):
    result = [-1] * len(array)
    stack = []
    for i in range(2 * len(array)):
        idx = i % len(array)
        while len(stack) > 0 and array[idx] > array[stack[-1]]:
            top = stack.pop()
            result[top] = array[idx]
        stack.append(idx)
    return result
