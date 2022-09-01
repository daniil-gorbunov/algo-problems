# easy, strings
# time O(n) | space O(1)
def firstNonRepeatingCharacter(string):
    unique = set()
    duplicates = set()
    for i, c in enumerate(string):
        if c not in duplicates:
            if c in unique:
                unique.remove(c)
                duplicates.add(c)
            else:
                unique.add(c)

    for i, c in enumerate(string):
        if c in unique:
            return i

    return -1
