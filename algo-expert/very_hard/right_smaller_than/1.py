# time O(nd) | space O(n), n - array size, d - BST depth
def rightSmallerThan(array):
    result = [0] * len(array)
    root = None
    for i in reversed(range(len(array))):
        node = Node(array[i])
        root = insert(root, node)
        result[i] = node.rightSmallerNum
    return result

def insert(root, node):
    if root is None:
        return node
    if node.value > root.value:
        node.rightSmallerNum += root.leftSize + 1
        root.right = insert(root.right, node)
    else:
        root.leftSize += 1
        root.left = insert(root.left, node)
    return root

class Node():
    def __init__(self, value):
        self.value = value
        self.leftSize = 0
        self.rightSmallerNum = 0
        self.left = None
        self.right = None
