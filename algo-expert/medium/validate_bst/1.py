# medium, BST
# time O(n) | space O(d)
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def validateBst(tree, minVal=float('-inf'), maxVal=float('inf')):
    if tree is None:
        return True
    if tree.value < minVal or tree.value >= maxVal:
        return False
    return validateBst(tree.left, minVal, min(maxVal, tree.value)) and validateBst(tree.right, max(minVal, tree.value), maxVal)
