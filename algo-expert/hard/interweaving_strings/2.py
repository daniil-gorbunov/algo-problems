# hard, recursion
# time O(n*m) | space O(n*m)
def interweavingStrings(s1, s2, s):
    if len(s1) + len(s2) != len(s):
        return False
    return helper(s1, s2, s, 0, 0, {})
def helper(s1, s2, s, p1, p2, memo):
    p = p1 + p2
    key = f'{p1},{p2}'
    if key in memo:
        return memo[key]
    if p == len(s):
        return True
    if p1 < len(s1) and s1[p1] == s[p]:
        memo[key] = helper(s1, s2, s, p1 + 1, p2, memo)
        if memo[key]:
            return True
    if p2 < len(s2) and s2[p2] == s[p]:
        memo[key] = helper(s1, s2, s, p1, p2 + 1, memo)
        return memo[key]
    memo[key] = False
    return False
