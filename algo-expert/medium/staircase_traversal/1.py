# medium, recursion
# time O(s*h) | space O(h)
def staircaseTraversal(height, maxSteps):
    stairs = [2 ** i for i in range(maxSteps)]
    for step in range(maxSteps, height):
        stairs.append(sum(stairs[step - maxSteps:step]))
    return stairs[-1]
