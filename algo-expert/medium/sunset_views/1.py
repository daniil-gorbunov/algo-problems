# medium, stacks
# time O(n) | space O(n)
def sunsetViews(buildings, direction):
    maxHeight = 0
    stack = []
    directedRange = range(len(buildings))
    if direction == 'EAST':
        directedRange = reversed(directedRange)
    for i in directedRange:
        if buildings[i] > maxHeight:
            maxHeight = buildings[i]
            if direction == 'EAST':
                stack.insert(0, i)
            else:
                stack.append(i)
    return stack
