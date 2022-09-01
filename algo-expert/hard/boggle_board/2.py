# hard, graphs
# O(nm*8^s + ws) time | O(ws) space
def boggleBoard(board, words):
    trie = Trie()
    for word in words:
        trie.add(word)
    foundWords = set()
    visited = set()
    for row in range(len(board)):
        for col in range(len(board[0])):
            traverse(row, col, board, trie.root, visited, foundWords)
    return list(foundWords)

def traverse(row, col, board, trie, visited, foundWords):
    if (row, col) in visited:
        return
    char = board[row][col]
    if char not in trie:
        return
    visited.add((row, col))
    trie = trie[char]
    if '*' in trie:
        foundWords.add(trie['*'])
    neighbors = getNeighbors(row, col, board)
    for nRow, nCol in neighbors:
        traverse(nRow, nCol, board, trie, visited, foundWords)
    visited.remove((row, col))

def getNeighbors(row, col, board):
    shifts = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    neighbors = []
    for dRow, dCol in shifts:
        nRow = row + dRow
        nCol = col + dCol
        if nRow >= 0 and nRow < len(board) and nCol >= 0 and nCol < len(board[0]):
            neighbors.append((nRow, nCol))
    return neighbors

class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = '*'

    def add(self, word):
        current = self.root
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current[self.endSymbol] = word
