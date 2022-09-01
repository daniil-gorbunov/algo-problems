# easy, BT
# time O(n) | space O(n)
from collections import deque

def branchSums(root):
    result_list = []
    if root is None:
        return []
    temp_list = branchSums(root.left) + branchSums(root.right)
    if not temp_list:
        return [root.value]
    return list(map(lambda x: x + root.value, temp_list))

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
