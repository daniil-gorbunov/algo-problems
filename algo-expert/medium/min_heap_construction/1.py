# medium, heaps
class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    # time O(n) | space O(1)
    def buildHeap(self, array):
        parent = self.getParent(len(array) - 1)
        for i in reversed(range(parent + 1)):
            self.siftDown(i, array)
        return array

    # time O(logn) | space O(1)
    def siftDown(self, i, heap):
        leftChild, rightChild = self.getChildren(i)
        while leftChild < len(heap):
            minChild = rightChild
            if rightChild > len(heap) - 1 or heap[leftChild] < heap[rightChild]:
                minChild = leftChild
            if heap[minChild] < heap[i]:
                self.swap(i, minChild, heap)
                i = minChild
                leftChild, rightChild = self.getChildren(minChild)
            else:
                break

    # time O(logn) | space O(1)
    def siftUp(self, i, heap):
        parent = self.getParent(i)
        while i > 0 and heap[i] < heap[parent]:
            self.swap(i, parent, heap)
            i = parent
            parent = self.getParent(i)

    # time O(1) | space O(1)
    def peek(self):
        return self.heap[0]

    # time O(logn) | space O(1)
    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        removedValue = self.heap.pop()
        self.siftDown(0, self.heap)
        return removedValue

    # time O(logn) | space O(1)
    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def getParent(self, i):
        return (i - 1) // 2

    def getChildren(self, i):
        return 2 * i + 1, 2 * i + 2

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
