# medium, arrays
# time O(nlogn) | space O(n)
def mergeOverlappingIntervals(intervals):
    intervals.sort(key=lambda int: int[0])
    merged = []
    i = 0
    while i < len(intervals):
        start, end = intervals[i]
        while i < len(intervals) - 1 and intervals[i + 1][0] <= end:
            i += 1
            end = max(intervals[i][1], end)
        merged.append([start, end])
        i += 1
    return merged
