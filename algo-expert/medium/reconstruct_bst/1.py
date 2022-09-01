# medium, BST
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# time O(n^2) | space O(n)
def reconstructBst(values, start=0, end=None):
    end = len(values) - 1 if end is None else end
    if start > end:
        return None
    leftEnd = start
    while leftEnd < end and values[leftEnd + 1] < values[start]:
        leftEnd += 1
    return BST(
        values[start],
        reconstructBst(values, start + 1, leftEnd),
        reconstructBst(values, leftEnd + 1, end)
    )
