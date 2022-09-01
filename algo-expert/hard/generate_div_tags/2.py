# hard, recursion
def generateDivTags(numberOfTags):
    return generate(numberOfTags, numberOfTags, [])

def generate(openingNum, closingNum, allStrings, currentString = ''):
    if closingNum == 0:
        allStrings.append(currentString)
    if openingNum > 0:
        generate(openingNum - 1, closingNum, allStrings, currentString + '<div>')
    if openingNum < closingNum:
        generate(openingNum, closingNum - 1, allStrings, currentString + '</div>')
    return allStrings
