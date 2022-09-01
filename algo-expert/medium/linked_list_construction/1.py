# medium, linked lists
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # time O(1) | space O(1)
    def setHead(self, node):
        if self.head is None or self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.insertBefore(self.head, node)

    # time O(1) | space O(1)
    def setTail(self, node):
        if self.head is None or self.tail is None:
            self.setHead(node)
        else:
            self.insertAfter(self.tail, node)

    # time O(1) | space O(1)
    def insertBefore(self, node, nodeToInsert):
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node is self.head:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    # time O(1) | space O(1)
    def insertAfter(self, node, nodeToInsert):
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node is self.tail:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    # time O(p) | space O(1)
    def insertAtPosition(self, position, nodeToInsert):
        if self.head is None or self.tail is None:
            self.setHead(nodeToInsert)
            return
        curNode = self.head
        for i in range(position - 1):
            curNode = curNode.next
        self.insertBefore(curNode, nodeToInsert)

    # time O(n) | space O(1)
    def removeNodesWithValue(self, value):
        current = self.head
        while current is not None:
            next = current.next
            if current.value == value:
                self.remove(current)
            current = next

    # time O(1) | space O(1)
    def remove(self, node):
        if node is self.head:
            self.head = self.head.next
        if node is self.tail:
            self.tail = self.tail.prev
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

    # time O(n) | space O(1)
    def containsNodeWithValue(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False
