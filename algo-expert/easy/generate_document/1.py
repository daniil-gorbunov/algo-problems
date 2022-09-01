# time O(n+m) | space O(c)
# where m - "characters" length, n - "document" length, c - number of unique chars in "characters"
def generateDocument(characters, document):
    charMap = {}
    for ch in characters:
        charMap[ch] = charMap.setdefault(ch, 0) + 1
    for ch in document:
        if ch not in charMap or charMap[ch] <= 0:
            return False
        charMap[ch] -= 1
    return True
