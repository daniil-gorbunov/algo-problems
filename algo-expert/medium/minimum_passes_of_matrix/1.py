# medium, graphs
# time O(h*w) | space O(h*w)
def minimumPassesOfMatrix(matrix):
    positiveNodes = set()
    numNegative = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] < 0:
                numNegative += 1
                continue
            negativeNeighbors = {matrix[nRow][nCol] < 0 for nRow, nCol in getNeighbors(row, col, matrix)}
            if matrix[row][col] > 0 and (len(negativeNeighbors) == 0 or any(negativeNeighbors)):
                positiveNodes.add((row, col))
    minAttempts = 0

    while len(positiveNodes) > 0:
        nextNodes = set()
        for row, col in positiveNodes:
            for nRow, nCol in getNeighbors(row, col, matrix):
                if matrix[nRow][nCol] < 0:
                    nextNodes.add((nRow, nCol))
                    matrix[nRow][nCol] *= -1
                    numNegative -= 1
        positiveNodes = nextNodes
        if len(positiveNodes) > 0:
            minAttempts += 1

    return minAttempts if numNegative == 0 else -1

def getNeighbors(row, col, matrix):
    neighbors = set()
    neighborShifts = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dRow, dCol in neighborShifts:
        nRow = row + dRow
        nCol = col + dCol
        if 0 <= nRow and nRow < len(matrix) and 0 <= nCol and nCol < len(matrix[0]):
            neighbors.add((nRow, nCol))
    return neighbors
