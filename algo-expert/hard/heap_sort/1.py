# hard, sorting
# time O(nlogn) | space O(1)
def heapSort(arr):
    buildMaxHeap(arr)
    for heapEnd in range(len(arr) - 1, 0, -1):
        swap(0, heapEnd, arr)
        siftDown(0, heapEnd - 1, arr)
    return arr

# time O(logn) | space O(1)
def siftDown(curIdx, heapEnd, arr):
    leftIdx, rightIdx = getChildren(curIdx)
    while leftIdx <= heapEnd:
        maxChildIdx = rightIdx
        if rightIdx > heapEnd or arr[leftIdx] > arr[rightIdx]:
            maxChildIdx = leftIdx
        if arr[curIdx] < arr[maxChildIdx]:
            swap(curIdx, maxChildIdx, arr)
            curIdx = maxChildIdx
            leftIdx, rightIdx = getChildren(curIdx)
        else:
            break

# time O(n) | space O(1)
def buildMaxHeap(arr):
    parent = len(arr) - 2 // 2
    for i in range(parent + 1, -1, -1):
        siftDown(i, len(arr) - 1, arr)

def getChildren(i):
    return i * 2 + 1, i * 2 + 2

def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]
