# time O(n^2 + m) | space O(n + m)
def patternMatcher(pattern, string):
    positions = {'x': [], 'y': []}
    singlePos = None
    for i in range(len(pattern)):
        positions[pattern[i]].append(i)
    if not positions['x']:
        singlePos = positions['y']
    elif not positions['y']:
        singlePos = positions['x']
    if singlePos:
        subLen = int(len(string) / len(singlePos))
        substring = string[0:subLen]
        for pos in singlePos:
            start = pos * len(substring)
            end = start + len(substring)
            if string.find(substring, start, end) == -1:
                return []
        return ['', substring] if positions['y'] else [substring, '']

    substrInfo = {
        'x': {'substr': '', 'len': 1},
        'y': {'substr': '', 'len': calcLenY(1, len(positions['x']), len(positions['y']), string)},
    }
    while substrInfo['y']['len'] > 0:
        curPos = 0
        for char in pattern:
            if not substrInfo[char]['substr']:
                substrInfo[char]['substr'] = string[curPos:curPos + substrInfo[char]['len']]
            elif string.find(substrInfo[char]['substr'], curPos, curPos + substrInfo[char]['len']) == -1:
                continue
            curPos += substrInfo[char]['len']
        if curPos == len(string):
            return [substrInfo['x']['substr'], substrInfo['y']['substr']]
        substrInfo['x']['len'] += 1
        substrInfo['y']['len'] = calcLenY(substrInfo['x']['len'], len(positions['x']), len(positions['y']), string)
        substrInfo['x']['substr'] = ''
        substrInfo['y']['substr'] = ''
    return []

def calcLenY(lenX, numX, numY, string):
    return int((len(string) - lenX * numX) / numY)
