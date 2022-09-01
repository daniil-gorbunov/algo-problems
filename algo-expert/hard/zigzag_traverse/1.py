# hard, arrays
# time O(m*n) | space O(m*n)
def zigzagTraverse(array):
    height = len(array) - 1
    width = len(array[0]) - 1
    zigZag = []
    for layer in range(height + width + 2):
        if layer % 2 == 0:
            row = max(0, layer - width)
            col = min(layer, width)
            endRow = min(layer, height)
            endCol = max(0, layer - height)
            dRow = 1
            dCol = -1
        else:
            row = min(layer, height)
            col = max(0, layer - height)
            endRow = max(0, layer - width)
            endCol = min(layer, width)
            dRow = -1
            dCol = 1
        while row != endRow + dRow and col != endCol + dCol:
            zigZag.append(array[row][col])
            row += dRow
            col += dCol
    return zigZag
