# easy, BST
# time O(n) | space O(1)
def findClosestValueInBst(tree, target):
    if tree is None:
        return float("inf")
    return target + min([
        findClosestValueInBst(tree.left, target) - target,
        findClosestValueInBst(tree.right, target) - target,
        tree.value - target,
    ], key=lambda k: abs(k))

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
