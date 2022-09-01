# medium, DP
# time O(m*n) | space O(m*n)
def numberOfWaysToTraverseGraph(width, height):
    grid = [[1 for col in range(width)] for row in range(height)]
    for row in range(1, height):
        for col in range(1, width):
            grid[row][col] = grid[row - 1][col] + grid[row][col - 1]
    return grid[-1][-1]
