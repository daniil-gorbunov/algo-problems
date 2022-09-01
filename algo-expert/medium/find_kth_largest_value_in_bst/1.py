# medium, BST
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# time O(n) | space O(n)
def findKthLargestValueInBst(tree, k):
    array = []
    buildArray(tree, array, k)
    return array[-1]

def buildArray(node, array, k):
    if node is None:
        return
    buildArray(node.right, array, k)
    if len(array) == k:
        return
    array.append(node.value)
    if len(array) == k:
        return
    buildArray(node.left, array, k)
