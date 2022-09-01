# medium, graphs
from collections import deque

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # time O(v+e) | space O(v)
    def breadthFirstSearch(self, array):
        q = deque()
        q.append(self)
        while len(q) > 0:
            node = q.popleft()
            array.append(node.name)
            q.extend(node.children)
        return array
