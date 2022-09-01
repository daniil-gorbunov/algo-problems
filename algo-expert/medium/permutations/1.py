# medium, recursion
# time O(n^2*n!) | space O(n*n!)
def getPermutations(nums):
    permutations = []
    permutate(nums, [], permutations)
    return permutations

def permutate(nums, currentPermutation, allPermutations):
    if not nums and currentPermutation:
        allPermutations.append(currentPermutation)
    else:
        for i in range(len(nums)):
            nextNums = nums[:i] + nums[i + 1:]
            nextPermutation = [nums[i]] + currentPermutation
            permutate(nextNums, nextPermutation, allPermutations)
