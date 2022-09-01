# medium, DP
# time O(m*n) | space O(m*n)
def levenshteinDistance(s1, s2):
    a = [[i + j if i == 0 or j == 0 else 0 for j in range(1 + len(s2))] for i in range(1 + len(s1))]
    for i in range(1, 1 + len(s1)):
        for j in range(1, 1 + len(s2)):
            a[i][j] = min(
                1 + a[i - 1][j],
                1 + a[i][j - 1],
                (1 if s1[i - 1] != s2[j - 1] else 0) + a[i - 1][j - 1]
            )
    return a[-1][-1]
