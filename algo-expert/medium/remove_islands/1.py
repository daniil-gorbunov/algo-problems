# medium, graphs
# time O(w*h) | space O(w*h)
def removeIslands(m):
    borderPath = getBorderPath(m)
    childShifts = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for row, col in borderPath:
        if m[row][col] == 1:
            q = []
            q.append((row, col))
            while len(q) > 0:
                cRow, cCol = q.pop(0)
                m[cRow][cCol] = 2
                for dRow, dCol in childShifts:
                    childRow = cRow + dRow
                    childCol = cCol + dCol
                    if isValidLand(childRow, childCol, m):
                        q.append((childRow, childCol))
    for row in range(len(m)):
        for col in range(len(m[0])):
            if m[row][col] > 0:
                m[row][col] -= 1
    return m

def getBorderPath(matrix):
    height = len(matrix)
    width = len(matrix[0])
    topRow = [(0, col) for col in range(width)]
    bottomRow = [(height - 1, col) for col in range(1, width)]
    leftCol = [(row, 0) for row in range(1, height)]
    rightCol = [(row, width - 1) for row in range(1, height - 1)]
    return topRow + leftCol + bottomRow + rightCol

def isValidLand(row, col, matrix):
    return row >= 0 and row < len(matrix) and col >=0 and col < len(matrix[0]) and matrix[row][col] == 1
