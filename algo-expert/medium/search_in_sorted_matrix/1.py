# medium, searching
# time O(m+n) | space O(1)
def searchInSortedMatrix(m, target):
    row = len(m) - 1
    for col in range(len(m[0])):
        while m[row][col] > target and row >= 0:
            row -= 1
        if row < 0:
            break
        if m[row][col] == target:
            return [row, col]
    return [-1, -1]
