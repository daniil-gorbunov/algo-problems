# hard, recursion
def solveSudoku(board):
    solve(board, 0, 0)
    return board

def solve(board, i, j):
    if j == 9:
        j = 0
        i += 1
    if i == 9:
        return True
    if board[i][j] != 0:
        return solve(board, i, j + 1)
    for d in range(1, 10):
        if isValid(d, board, i, j):
            board[i][j] = d
            if solve(board, i, j + 1):
                return True
    board[i][j] = 0
    return False

def isValid(num, board, i, j):
    if num in board[i] or num in [row[j] for row in board]:
        return False
    for k in range((i // 3) * 3, (i // 3) * 3 + 3):
        for l in range((j // 3) * 3, (j // 3) * 3 + 3):
            if num == board[k][l]:
                return False
    return True
