# medium, arrays
# time O(n^2) | space O(n)
def threeNumberSum(arr, targetSum):
    arr.sort()
    triplets = []
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            sum = arr[i] + arr[left] + arr[right]
            if sum == targetSum:
                triplets.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
            elif sum < targetSum:
                left += 1
            else:
                right -= 1
    return triplets
