# hard, BST
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# time O(h) | space O(1)
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    if hasChild(nodeTwo, nodeOne):
        return hasChild(nodeThree, nodeTwo)
    elif hasChild(nodeTwo, nodeThree):
        return hasChild(nodeOne, nodeTwo)
    return False

# time O(h) | space O(1)
def hasChild(root, node):
    while root and root is not node:
        root = root.left if root.value > node.value else root.right
    return root is node
