# hard, graphs
def boggleBoard(board, words):
    charToWord = buildCharsMap(words)
    foundWords = set()
    for row in range(len(board)):
        for col in range(len(board[0])):
            if len(foundWords) == len(words):
                return list(foundWords)
            char = board[row][col]
            for word in charToWord.get(char, []):
                visited = {(row, col)}
                if word not in foundWords and isWordOnBoard(board, word, 1, row, col, visited):
                    foundWords.add(word)
    return list(foundWords)

def buildCharsMap(words):
    charToWord = {}
    for word in words:
        char = word[0]
        if char not in charToWord:
            charToWord[char] = []
        charToWord[char].append(word)
    return charToWord

shifts = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
def isWordOnBoard(board, word, charIdx, row, col, visited):
    if charIdx >= len(word):
        return True
    char = word[charIdx]
    for dRow, dCol in shifts:
        nRow = row + dRow
        nCol = col + dCol
        pair = (nRow, nCol)
        if nRow < 0 or nRow >= len(board) or nCol < 0 or nCol >= len(board[0]) \
        or pair in visited or board[nRow][nCol] != char:
            continue
        visited.add(pair)
        if isWordOnBoard(board, word, charIdx + 1, nRow, nCol, visited):
            return True
        visited.remove(pair)
    return False
