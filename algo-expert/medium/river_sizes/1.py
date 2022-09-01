# medium, graphs
# time O(w*h) | space O(w*h)
def riverSizes(m):
    q = []
    h = len(m)
    w = len(m[0])
    sizes = []
    childShifts = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for row in range(h):
        for col in range(w):
            if m[row][col] == 1:
                riverSize = 0
                q.append((row, col))
                while len(q) > 0:
                    riverSize += 1
                    riverRow, riverCol = q.pop(0)
                    m[riverRow][riverCol] = -1
                    for dRow, dCol in childShifts:
                        childRow = riverRow + dRow
                        childCol = riverCol + dCol
                        if childRow >= 0 and childRow < h and childCol >= 0 and childCol < w and m[childRow][childCol] == 1:
                            q.append((childRow, childCol))
                            m[childRow][childCol] = -1
                sizes.append(riverSize)
    return sizes
