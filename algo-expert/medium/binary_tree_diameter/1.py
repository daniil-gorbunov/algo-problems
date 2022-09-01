# medium, BT
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# time O(n) | space O(d)
def binaryTreeDiameter(tree):
  return getTreeProps(tree)[0]

def getTreeProps(tree):
  if tree is None:
    return 0, 0
  leftDiameter, leftDepth = getTreeProps(tree.left)
  rightDiameter, rightDepth = getTreeProps(tree.right)
  return max(leftDepth + rightDepth, leftDiameter, rightDiameter), 1 + max(leftDepth, rightDepth)
