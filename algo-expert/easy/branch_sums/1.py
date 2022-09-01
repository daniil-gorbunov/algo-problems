# easy, BT
# time O(n) | space O(n)
def branchSums(root):
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [root.value]
    sums = branchSums(root.left) + branchSums(root.right)
    return list(map(lambda x: x + root.value, sums))

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
