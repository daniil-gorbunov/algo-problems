# easy, BST
# time O(log n) if tree is balanced, otherwise O(n)
# space O(1)
def findClosestValueInBst(tree, target):
    current = tree
    closest = tree.value
    while current is not None:
        if target == current.value:
            current.value
        if abs(current.value - target) < abs(closest - target):
            closest = current.value
        current = current.left if target < current.value else current.right
    return closest

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
