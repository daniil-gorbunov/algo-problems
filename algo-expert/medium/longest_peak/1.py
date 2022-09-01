# medium, arrays
# time O(n) | space O(1)
def longestPeak(arr):
    longest = 0
    i = 0
    while i < len(arr):
        peakStart = i
        tip = i
        while tip < len(arr) - 1 and arr[tip + 1] > arr[tip]:
            tip += 1
        if tip == i:
            i += 1
            continue
        peakEnd = tip
        while peakEnd < len(arr) - 1 and arr[peakEnd + 1] < arr[peakEnd]:
            peakEnd += 1
        if peakEnd > tip:
            longest = max(longest, peakEnd - peakStart + 1)
        i = peakEnd
    return longest
