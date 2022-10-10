# time O(bs + ns) | space O(ns)
def multiStringSearch(bigString, smallStrings):
    trie = Trie(bigString)
    for str in smallStrings:
        trie.insert(str)
    foundStrings = set()
    for i in range(len(bigString)):
        findSubstrings(bigString, i, trie, foundStrings)
    return [str in foundStrings for str in smallStrings]

# time O(n) | space O(1)
def findSubstrings(bigString, i, trie, foundStrings):
    node = trie.root
    for i in range(i, len(bigString)):
        char = bigString[i]
        if char not in node:
            break
        node = node[char]
        if trie.endSymbol in node:
            foundStrings.add(node[trie.endSymbol])

class Trie:
    def __init__(self, str):
        self.root = {}
        self.endSymbol = '*'

    # time O(n) | space O(n)
    def insert(self, str):
        node = self.root
        for i in range(len(str)):
            char = str[i]
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.endSymbol] = str
