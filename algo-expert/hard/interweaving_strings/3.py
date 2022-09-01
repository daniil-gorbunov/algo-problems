# hard, recursion
# time O(2^(n+m)) | space O(n+m)
def interweavingStrings(s1, s2, s, p1 = 0, p2 = 0):
    if len(s1) + len(s2) != len(s):
        return False
    p = p1 + p2
    if p == len(s):
        return True
    return (p1 < len(s1) and s1[p1] == s[p] and interweavingStrings(s1, s2, s, p1 + 1, p2)) or \
           (p2 < len(s2) and s2[p2] == s[p] and interweavingStrings(s1, s2, s, p1, p2 + 1))
