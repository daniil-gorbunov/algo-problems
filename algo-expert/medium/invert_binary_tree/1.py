# medium, BT
# time O(n) | space O(d)
def invertBinaryTree(tree):
    if tree is None:
        return
    tree.left, tree.right = tree.right, tree.left
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
