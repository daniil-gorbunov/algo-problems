# hard, strings
# time O(n^2 + n*m) | space O(n)
# n - string length, m - substring length
def underscorifySubstring(str, substr):
    stringParts = []
    rangeEnd = -1
    for i in range(len(str) + 1):
        char = str[i] if i < len(str) else ''
        if str.find(substr, i) == i:
            if i > rangeEnd:
                stringParts.append('_')
            rangeEnd = i + len(substr)
        elif i == rangeEnd:
            stringParts.append('_')
        stringParts.append(char)
    return ''.join(stringParts)
