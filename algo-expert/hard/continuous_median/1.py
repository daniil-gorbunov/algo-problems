# hard, heaps
from heapq import heappush, heappop

class ContinuousMedianHandler:
    def __init__(self):
        self.median = None
        self.mid = None
        self.maxHeap = []
        self.minHeap = []

    # time O(log(n)) | space O(n)
    def insert(self, val):
        if self.mid is None:
            if len(self.minHeap) == 0:
                self.mid = val
            elif val < -self.maxHeap[0]:
                heappush(self.maxHeap, -val)
                self.mid = -heappop(self.maxHeap)
            elif val > self.minHeap[0]:
                heappush(self.minHeap, val)
                self.mid = heappop(self.minHeap)
            else:
                self.mid = val
            self.median = self.mid
        else:
            if val <= self.mid:
                heappush(self.maxHeap, -val)
                heappush(self.minHeap, self.mid)
            else:
                heappush(self.maxHeap, -self.mid)
                heappush(self.minHeap, val)
            self.mid = None
            self.median = (-self.maxHeap[0] + self.minHeap[0]) / 2

    def getMedian(self):
        return self.median
