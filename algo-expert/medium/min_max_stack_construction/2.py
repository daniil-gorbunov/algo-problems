# medium, stacks
class MinMaxStack:
    def __init__(self):
        self.stack = []

    # time O(1) | space O(1)
    def peek(self):
        return self.stack[-1]['val']

    # time O(1) | space O(1)
    def pop(self):
        return self.stack.pop()['val']

    # time O(1) | space O(1)
    def push(self, number):
        minVal = maxVal = number
        if self.stack:
            topNode = self.stack[-1]
            minVal = min(number, topNode['min'])
            maxVal = max(number, topNode['max'])
        self.stack.append({'val': number, 'min': minVal, 'max': maxVal})

    # time O(1) | space O(1)
    def getMin(self):
        return self.stack[-1]['min']

    # time O(1) | space O(1)
    def getMax(self):
        return self.stack[-1]['max']
