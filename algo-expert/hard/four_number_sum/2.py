# hard, arrays
# time O(n^2) -> O(n^3) | space O(n^2)
def fourNumberSum(arr, targetSum):
    quadruplets = []
    pairs = {}
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            pairSum = arr[i] + arr[j]
            if pairSum not in pairs:
                pairs[pairSum] = []
            pairs[pairSum].append([i, j])
    for i in range(len(arr) - 3):
        for j in range(i + 1, len(arr) - 2):
            dif = targetSum - (arr[i] + arr[j])
            matchedDuplets = pairs.get(dif, [])
            for [k, l] in matchedDuplets:
                if k > j:
                    quadruplets.append([arr[i], arr[j], arr[k], arr[l]])
    return quadruplets
