# hard, heaps
from heapq import heappush, heappop

# time O(nlog(k)) | space O(k)
def sortKSortedArray(array, k):
    heap = []
    dif = k + 1
    for i in range(len(array) + dif):
        if i < len(array):
            heappush(heap, array[i])
        if i > k:
            array[i - dif] = heappop(heap)
    return array
