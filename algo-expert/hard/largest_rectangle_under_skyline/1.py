# hard, stacks
# time O(n^2) | space O(1)
def largestRectangleUnderSkyline(arr):
    maxArea = 0
    for i in range(len(arr)):
        currentArea = arr[i]
        left = i - 1
        while left > 0 and arr[left] >= arr[i]:
            currentArea += arr[i]
            left -= 1
        right = i + 1
        while right < len(arr) and arr[right] >= arr[i]:
            currentArea += arr[i]
            right += 1
        maxArea = max(maxArea, currentArea)
    return maxArea
