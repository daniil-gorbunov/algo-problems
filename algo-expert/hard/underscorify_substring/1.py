# hard, strings
# time O(n*m) | space O(n)
# n - string length, m - substring length
def underscorifySubstring(str, substr):
    stringParts = []
    rangeEnd = -1
    for i in range(len(str) + 1):
        char = str[i] if i < len(str) else ''
        if isStartOfSubstr(i, str, substr):
            if i > rangeEnd:
                stringParts.append('_')
            rangeEnd = i + len(substr)
        elif i == rangeEnd:
            stringParts.append('_')
        stringParts.append(char)
    return ''.join(stringParts)

def isStartOfSubstr(i, str, substr):
    for j in range(len(substr)):
        if i + j >= len(str) or str[i + j] != substr[j]:
            return False
    return True
