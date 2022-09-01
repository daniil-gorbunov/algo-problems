# medium, BST
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TraversalInfo:
    def __init__(self, numVisited=None, lastVisited=None):
        self.numVisited = numVisited
        self.lastVisited = lastVisited

# time O(h+k) | space O(h)
def findKthLargestValueInBst(tree, k):
    traversalInfo = TraversalInfo(0, None)
    traverse(tree, traversalInfo, k)
    return traversalInfo.lastVisited

def traverse(node, traversalInfo, k):
    if node is None or traversalInfo.numVisited >= k:
        return
    traverse(node.right, traversalInfo, k)
    if traversalInfo.numVisited < k:
        traversalInfo.lastVisited = node.value
        traversalInfo.numVisited += 1
        traverse(node.left, traversalInfo, k)
