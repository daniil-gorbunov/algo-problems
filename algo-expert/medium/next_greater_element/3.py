# medium, stacks
# time O(n) | space O(n)
def nextGreaterElement(array):
    result = [-1] * len(array)
    stack = []
    for i in reversed(range(2 * len(array) - 1)):
        idx = i % len(array)
        while len(stack) > 0:
            if array[idx] >= stack[-1]:
                stack.pop()
            else:
                result[idx] = stack[-1]
                break
        stack.append(array[idx])
    return result
