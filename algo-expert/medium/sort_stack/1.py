# medium, stacks
# time O(n^2) | space O(n)
def sortStack(stack):
    for bottomLevel in reversed(range(len(stack))):
        recursiveSort(stack, bottomLevel, 0, float('inf'))
    return stack

def recursiveSort(stack, bottomLevel, currentLevel, minVal):
    curVal = stack.pop()
    nextMinVal = min(curVal, minVal)
    if bottomLevel == currentLevel:
        stack.append(nextMinVal)
        return (None, nextMinVal) if curVal == nextMinVal else (curVal, nextMinVal)
    elevatedVal, totalMin = recursiveSort(stack, bottomLevel, currentLevel + 1, nextMinVal)
    if elevatedVal is None:
        stack.append(curVal)
        return (None, totalMin)
    elif curVal == totalMin:
        stack.append(elevatedVal)
        return (None, totalMin)
    stack.append(elevatedVal)
    return (curVal, totalMin)
