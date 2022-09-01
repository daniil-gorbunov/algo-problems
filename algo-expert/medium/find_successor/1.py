# medium, BT
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

# time O(n) | space O(n)
def findSuccessor(tree, node):
    nodeList = inOrderTraverse(tree)
    for i in range(1, len(nodeList)):
        if nodeList[i-1] is node:
            return nodeList[i]
    return None

def inOrderTraverse(tree, nodeList=[]):
    if tree is None:
        return nodeList
    inOrderTraverse(tree.left, nodeList)
    nodeList.append(tree)
    inOrderTraverse(tree.right, nodeList)
    return nodeList
