# easy, BT
# time O(n) | space O(h)
def nodeDepths(root, depth=0):
    if root is None:
        return 0
    return nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1) + depth

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
