# easy, strings
# time O(n) | space O(1)
def firstNonRepeatingCharacter(string):
    freq = {}
    for c in string:
        freq[c] = freq.get(c, 0) + 1
    for i, c in enumerate(string):
        if freq[c] == 1:
            return i
    return -1
