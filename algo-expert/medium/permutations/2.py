# medium, recursion
# time O(n*n!) | space O(n*n!)
def getPermutations(nums):
    permutations = []
    permutate(0, nums, permutations)
    return permutations

def permutate(i, nums, allPermutations):
    if i == len(nums) - 1:
        allPermutations.append(nums[:])
    else:
        for j in range(i, len(nums)):
            swap(nums, i, j)
            permutate(i + 1, nums, allPermutations)
            swap(nums, i, j)

def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]
