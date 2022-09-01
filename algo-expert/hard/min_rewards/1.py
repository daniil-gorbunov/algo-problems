# hard, arrays
# time O(n) | space O(1)
def minRewards(scores):
    lastMaxIdx = 0
    lastMaxReward = 1
    prevReward = 1
    totalRewards = 1
    for i in range(1, len(scores)):
        if scores[i] > scores[i - 1]:
            prevReward += 1
            totalRewards += prevReward
            lastMaxReward = prevReward
            lastMaxIdx = i
        else:
            if prevReward == 1:
                totalRewards += i - lastMaxIdx
                if i - lastMaxIdx >= lastMaxReward:
                    totalRewards += 1
            else:
                totalRewards += 1
            prevReward = 1
    return totalRewards
