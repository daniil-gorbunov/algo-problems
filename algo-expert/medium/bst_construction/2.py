# medium, BST
class BST:
    def __init__(self, value, parent = None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    # Avg: Time: O(log(n)) | Space: O(1)
    # Worst: Time: O(n) | Space: O(1)
    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value, currentNode)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value, currentNode)
                    break
                else:
                    currentNode = currentNode.right
        return self

    # Avg: Time: O(log(n)) | Space: O(1)
    # Worst: Time: O(n) | Space: O(1)
    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False

    # Avg: Time: O(log(n)) | Space: O(1)
    # Worst: Time: O(n) | Space: O(1)
    def remove(self, value):
        currentNode = self
        while value != currentNode.value:
            if currentNode is None:
                return self
            elif value < currentNode.value:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right

        if currentNode.left is None and currentNode.right is None:
            if currentNode.parent is None:
                return self
            if currentNode.parent.left is currentNode:
                currentNode.parent.left = None
            else:
                currentNode.parent.right = None
        elif currentNode.left is not None and currentNode.right is None:
            leftNode = currentNode.left
            currentNode.value = leftNode.value
            currentNode.left = leftNode.left
            currentNode.right = leftNode.right
            if leftNode.left is not None:
                leftNode.left.parent = currentNode
            if leftNode.right is not None:
                leftNode.right.parent = currentNode
        elif currentNode.left is None and currentNode.right is not None:
            rightNode = currentNode.right
            currentNode.value = rightNode.value
            currentNode.left = rightNode.left
            currentNode.right = rightNode.right
            if rightNode.left is not None:
                rightNode.left.parent = currentNode
            if rightNode.right is not None:
                rightNode.right.parent = currentNode
        else:
            minNode = currentNode.right
            while minNode.left is not None:
                minNode = minNode.left
            currentNode.value = minNode.value
            if minNode.parent.left is minNode:
                minNode.parent.left = None
            else:
                minNode.parent.right = None
        return self
