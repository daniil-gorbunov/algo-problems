# hard, heaps
# time O(nlolg(n)) | space O(n)
def laptopRentals(times):
    starts = sorted([t[0] for t in times])
    ends = sorted([t[1] for t in times])
    laptopsNum = startIdx = endIdx = 0
    while startIdx < len(starts):
        if starts[startIdx] < ends[endIdx]:
            laptopsNum += 1
        else:
            endIdx += 1
        startIdx += 1
    return laptopsNum
