# hard, BT
# time O(n) | space O(h)
def maxPathSum(tree):
    return calcPaths(tree)[1]

def calcPaths(node):
    if not node:
        return 0, float('-inf')
    leftBranch, leftPath = calcPaths(node.left)
    rightBranch, rightPath = calcPaths(node.right)
    value = node.value
    maxBranchWithNode = max(leftBranch + value, rightBranch + value, value)
    maxPath = max(leftPath, rightPath, leftBranch + rightBranch + value, maxBranchWithNode)
    return maxBranchWithNode, maxPath
