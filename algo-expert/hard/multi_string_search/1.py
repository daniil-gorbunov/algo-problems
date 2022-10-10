# time O(b^2 + ns) | space O(b^2 + n)
def multiStringSearch(bigString, smallStrings):
    trie = Trie(bigString)
    return [trie.contains(s) for s in smallStrings]

class Trie:
    def __init__(self, str):
        self.root = {}
        self.populateTrieFrom(str)

    # time O(n^2) | space O(n^2)
    def populateTrieFrom(self, str):
        for i in range(len(str)):
            node = self.root
            for j in range(i, len(str)):
                char = str[j]
                if char not in node:
                    node[char] = {}
                node = node[char]

    # time O(n) | space O(1)
    def contains(self, str):
        node = self.root
        for c in str:
            if c not in node:
                return False
            node = node[c]
        return True
