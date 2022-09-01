# hard, BST
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# time O(h) | space O(1)
def validateThreeNodes(n1, n2, n3):
    top, bottom = (n1, n3) if hasChild(n1, n3) else (n3, n1)
    current = top
    while current and current is not bottom:
        if current is n2:
            return True
        current = current.left if current.value > bottom.value else current.right
    return False

# time O(h) | space O(1)
def hasChild(root, node):
    while root and root is not node:
        root = root.left if root.value > node.value else root.right
    return root is node
