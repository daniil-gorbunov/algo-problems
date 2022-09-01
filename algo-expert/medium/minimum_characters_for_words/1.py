# medium, strings
# time O(n) | space O(c)
# n - total number of chars
# c - number of unique chars
def minimumCharactersForWords(words):
    charSet = []
    allChars = {}
    for word in words:
        wordChars = {}
        for c in word:
            wordChars[c] = wordChars.get(c, 0) + 1
        for c in wordChars:
            if c not in allChars:
                allChars[c] = 0
            allChars[c] = max(allChars[c], wordChars[c])
    for c in allChars:
        charSet.extend([c] * allChars[c])
    return charSet
