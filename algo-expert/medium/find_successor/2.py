# medium, BT
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

# time O(d) | space O(1)
def findSuccessor(tree, node):
    if node.right is not None:
        return findInRight(node.right)
    return findInParent(node)

def findInRight(node):
    while node.left is not None:
        node = node.left
    return node

def findInParent(node):
    while node.parent is not None and node.parent.right is node:
        node = node.parent
    return node.parent
