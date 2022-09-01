# medium, DP
# time O(m*n) | space O(min(m,n))
def levenshteinDistance(s1, s2):
    short, long = (s1, s2) if len(s1) < len(s2) else (s2, s1)
    e = [col for col in range(1 + len(short))]
    for row in range(1, 1 + len(long)):
        prevSub = row - 1
        e[0] = row
        for col in range(1, 1 + len(short)):
            tempSub = e[col]
            charsEqual = long[row - 1] == short[col - 1]
            e[col] = prevSub if charsEqual else 1 + min(e[col], e[col - 1], prevSub)
            prevSub = tempSub
    return e[-1]
