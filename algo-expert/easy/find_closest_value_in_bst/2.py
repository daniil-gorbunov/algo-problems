# easy, BST, recursion
# time O(log n) if tree is balanced, otherwise O(n)
# space O(log n) if tree is balanced, otherwise O(n)
def findClosestValueInBst(tree, target):
    if tree is None:
        return float("inf")
    if target == tree.value:
        return tree.value
    check_node = tree.left if target < tree.value else tree.right
    check_value = findClosestValueInBst(check_node, target)
    return min(tree.value, check_value, key=lambda v: abs(v - target))

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
