# hard, recursion
def generateDivTags(numberOfTags):
    allStrings = []
    start = (numberOfTags + 1) * numberOfTags / 2
    end = start + numberOfTags
    generate(numberOfTags, start, end, '', allStrings)
    return allStrings

def generate(level, node, end, currentString, allStrings):
    if node == end:
        allStrings.append(currentString)
    if 0 > node or node > end:
        return
    if node != (level + 3) * level / 2:
        generate(level - 1, node - level, end, currentString + '<div>', allStrings)
    generate(level + 1, 2 + node + level, end, currentString + '</div>', allStrings)
