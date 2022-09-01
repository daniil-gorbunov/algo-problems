# medium, DP
# time O(m*n) | space O(min(m,n))
def levenshteinDistance(s1, s2):
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    a = [j for j in range(1 + len(s2))]
    for i in range(1, 1 + len(s1)):
        curLine = a[:]
        curLine[0] = i
        for j in range(1, 1 + len(s2)):
            curLine[j] = min(
                1 + a[j],
                1 + curLine[j - 1],
                (1 if s1[i - 1] != s2[j - 1] else 0) + a[j - 1]
            )
        a = curLine[:]
    return a[-1]
