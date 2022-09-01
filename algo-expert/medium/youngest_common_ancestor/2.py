# medium, graphs
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

# time O(d) | space O(1)
def getYoungestCommonAncestor(root, desc1, desc2):
    level1 = getLevel(root, desc1)
    level2 = getLevel(root, desc2)
    low, high = (desc1, desc2) if level1 > level2 else (desc2, desc1)
    for i in range(abs(level1 - level2)):
        low = low.ancestor
    while low is not high:
        low = low.ancestor
        high = high.ancestor
    return low

def getLevel(root, node):
    level = 0
    while node is not root:
        node = node.ancestor
        level += 1
    return level
