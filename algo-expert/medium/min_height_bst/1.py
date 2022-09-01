# medium, BST
# time O(nlogn) | space O(n)
def process(tree, array, start, end):
    if start <= end:
        mid = (start + end) // 2
        if tree is None:
            tree = BST(array[mid])
        else:
            tree.insert(array[mid])
        process(tree, array, start, mid - 1)
        process(tree, array, mid + 1, end)
    return tree

def minHeightBst(array):
    return process(None, array, 0, len(array) - 1)

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
