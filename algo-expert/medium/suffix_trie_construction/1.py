# medium, tries
class SuffixTrie:
    def __init__(self, str):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(str)

    # time O(n^2) | space O(n^2)
    def populateSuffixTrieFrom(self, str):
        for i in range(len(str)):
            node = self.root
            for j in range(i, len(str)):
                char = str[j]
                if char not in node:
                    node[char] = {}
                node = node[char]
            node[self.endSymbol] = True

    # time O(n) | space O(1)
    def contains(self, str):
        node = self.root
        for c in str:
            if c not in node:
                return False
            node = node[c]
        return self.endSymbol in node
