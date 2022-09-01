# hard, BT
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# time O(n) | space O(n)
def findNodesDistanceK(tree, target, k):
    foundNodes = []
    getDistToTarget(tree, target, 0, k, foundNodes)
    return foundNodes

def getDistToTarget(node, target, passedDist, targetDist, foundNodes):
    if not node:
        return -1
    if node.value == target:
        findDesc(node, targetDist, foundNodes)
        return passedDist
    leftDist = getDistToTarget(node.left, target, passedDist + 1, targetDist, foundNodes)
    rightDist = getDistToTarget(node.right, target, passedDist + 1, targetDist, foundNodes)
    if leftDist - passedDist == targetDist or rightDist - passedDist == targetDist:
        foundNodes.append(node.value)
    if rightDist != -1:
        findDesc(node.left, targetDist - rightDist + passedDist - 1, foundNodes)
        return rightDist
    if leftDist != -1:
        findDesc(node.right, targetDist - leftDist + passedDist - 1, foundNodes)
        return leftDist
    return -1

def findDesc(node, dist, foundNodes):
    if not node or dist < 0:
        return
    elif dist == 0:
        foundNodes.append(node.value)
    else:
        findDesc(node.left, dist - 1, foundNodes)
        findDesc(node.right, dist - 1, foundNodes)
