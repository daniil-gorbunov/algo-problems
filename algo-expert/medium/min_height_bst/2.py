# medium, BST
# time O(n) | space O(n)
def process(array, start, end):
    if start <= end:
        mid = (start + end) // 2
        newNode = BST(array[mid])
        newNode.left = process(array, start, mid - 1)
        newNode.right = process(array, mid + 1, end)
        return newNode

def minHeightBst(array):
    return process(array, 0, len(array) - 1)

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
