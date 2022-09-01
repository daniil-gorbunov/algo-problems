# medium, recursion
# time O(h) | space O(h)
def staircaseTraversal(height, maxSteps):
    stairs = [1]
    numSteps = 0
    for step in range(1, height + 1):
        if step > maxSteps:
            numSteps -= stairs[step - maxSteps - 1]
        numSteps += stairs[step - 1]
        stairs.append(numSteps)
    return stairs[height]
