# medium, BST
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# time O(n) | space O(n)
def reconstructBst(values, minVal=float('-inf'), maxVal=float('inf'), treeData=None):
    if treeData is None:
        treeData = TreeData()
    if len(values) <= treeData.rootIdx:
        return None
    nodeVal = values[treeData.rootIdx]
    if nodeVal < minVal or maxVal <= nodeVal:
        return None
    treeData.rootIdx += 1
    leftNode = reconstructBst(values, minVal, nodeVal, treeData)
    rightNode = reconstructBst(values, nodeVal, maxVal, treeData)
    return BST(nodeVal, leftNode, rightNode)

class TreeData:
    def __init__(self, rootIdx=0):
        self.rootIdx = rootIdx
