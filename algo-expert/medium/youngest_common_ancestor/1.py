# medium, graphs
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

# time O(d^2) | space O(v)
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    current = descendantOne
    visited = []
    while current is not None:
        visited.append(current)
        current = current.ancestor
    current = descendantTwo
    while current not in visited:
        current = current.ancestor
    return current
