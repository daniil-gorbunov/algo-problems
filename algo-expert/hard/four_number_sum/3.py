# hard, arrays
# time O(n^2) -> O(n^3) | space O(n^2)
def fourNumberSum(arr, targetSum):
    quadruplets = []
    pairs = {}
    for i in range(1, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            pair = [arr[i], arr[j]]
            dif = targetSum - sum(pair)
            matchedPairs = pairs.get(dif, [])
            for matchedPair in matchedPairs:
                quadruplets.append(pair + matchedPair)
        for j in range(0, i):
            pair = [arr[i], arr[j]]
            pairSum = sum(pair)
            if pairSum not in pairs:
                pairs[pairSum] = []
            pairs[pairSum].append(pair)
    return quadruplets
