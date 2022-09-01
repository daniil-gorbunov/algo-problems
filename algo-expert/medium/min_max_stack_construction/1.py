# medium, stacks
class Node:
    def __init__(self, val, minVal, maxVal):
        self.val = val
        self.minVal = minVal
        self.maxVal = maxVal

class MinMaxStack:
    def __init__(self):
        self.stack = []

    # time O(1) | space O(1)
    def peek(self):
        return self.stack[-1].val

    # time O(1) | space O(1)
    def pop(self):
        return self.stack.pop().val

    # time O(1) | space O(1)
    def push(self, number):
        if not self.stack:
            minVal = maxVal = number
        else:
            topNode = self.stack[-1]
            minVal = topNode.minVal
            maxVal = topNode.maxVal
        node = Node(number, min(number, minVal), max(number, maxVal))
        self.stack.append(node)

    # time O(1) | space O(1)
    def getMin(self):
        return self.stack[-1].minVal

    # time O(1) | space O(1)
    def getMax(self):
        return self.stack[-1].maxVal
