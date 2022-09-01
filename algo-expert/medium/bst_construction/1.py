# medium, BST
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Avg: Time: O(log(n)) | Space: O(1)
    # Worst: Time: O(n) | Space: O(1)
    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
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
        parent = None
        currentNode = self
        while value != currentNode.value:
            parent = currentNode
            if currentNode is None:
                return self
            elif value < currentNode.value:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right

        if currentNode.left is None and currentNode.right is None:
            if parent is None:
                return self
            if parent.left is currentNode:
                parent.left = None
            else:
                parent.right = None
        elif currentNode.left is not None and currentNode.right is None:
            leftNode = currentNode.left
            currentNode.value = leftNode.value
            currentNode.left = leftNode.left
            currentNode.right = leftNode.right
        elif currentNode.left is None and currentNode.right is not None:
            rightNode = currentNode.right
            currentNode.value = rightNode.value
            currentNode.left = rightNode.left
            currentNode.right = rightNode.right
        else:
            minParent = currentNode
            minNode = currentNode.right
            while minNode.left is not None:
                minParent = minNode
                minNode = minNode.left
            currentNode.value = minNode.value
            if minParent.left is minNode:
                minParent.left = None
            else:
                minParent.right = None
        return self
