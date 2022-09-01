# hard, BT
# time O(n) | space O(h)
def maxPathSum(tree):
    return calcPaths(tree)[1]

def calcPaths(node):
    if not node:
        return 0, float('-inf')
    leftBranch, leftPath = calcPaths(node.left)
    rightBranch, rightPath = calcPaths(node.right)
    leftBranch = max(leftBranch, 0)
    rightBranch = max(rightBranch, 0)
    bestBranchVal = max(leftBranch, rightBranch, 0)
    maxBranchWithNode = bestBranchVal + node.value
    maxPath = max(leftPath, rightPath, leftBranch + rightBranch + node.value)
    return maxBranchWithNode, maxPath
