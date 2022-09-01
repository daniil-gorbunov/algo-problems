# hard, stacks
# time O(n) | space O(n)
def largestRectangleUnderSkyline(arr):
    maxArea = 0
    stack = []
    for i in range(len(arr) + 1):
        curHeight = arr[i] if i < len(arr) else 0
        while len(stack) > 0 and curHeight <= arr[stack[-1]]:
            height = arr[stack.pop()]
            leftBound = stack[-1] if len(stack) > 0 else -1
            area = height * (i - leftBound - 1)
            maxArea = max(area, maxArea)
        stack.append(i)
    return maxArea
