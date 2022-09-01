# hard, arrays
# time O(n) | space O(n)
def largestRange(array):
    largest = [array[0], array[0]]
    nums = set(array)
    while len(nums) > 0:
        for start in nums:
            break
        nums.remove(start)
        end = start
        while start - 1 in nums:
            start -= 1
            nums.remove(start)
        while end + 1 in nums:
            end += 1
            nums.remove(end)
        if end - start > largest[1] - largest[0]:
            largest = [start, end]
    return largest
