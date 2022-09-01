# medium, BT
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, height=0, isBalanced=True):
        self.height = height
        self.isBalanced = isBalanced

# time O(n) | space O(d)
def heightBalancedBinaryTree(tree):
    return getTreeInfo(tree).isBalanced

def getTreeInfo(tree):
    if tree is None:
        return TreeInfo()
    left = getTreeInfo(tree.left)
    right = getTreeInfo(tree.right)
    bothBalanced = left.isBalanced and right.isBalanced
    return TreeInfo(
        1 + max(left.height, right.height),
        bothBalanced and abs(left.height - right.height) < 2,
    )
