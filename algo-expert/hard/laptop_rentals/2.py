# hard, heaps
from heapq import heappush, heappop

# time O(nlolg(n)) | space O(n)
def laptopRentals(times):
    heap = []
    for start, end in sorted(times, key=lambda t: t[0]):
        if len(heap) and start >= heap[0]:
            heappop(heap)
        heappush(heap, end)
    return len(heap)
