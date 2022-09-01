# medium, linked lists
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# time O(max(n,m)) | space O(max(n,m))
def sumOfLinkedLists(list1, list2):
    resultHead = LinkedList(0)
    prevResult = resultHead
    overflow = 0
    while list1 is not None or list2 is not None or overflow > 0:
        val1 = list1.value if list1 is not None else 0
        val2 = list2.value if list2 is not None else 0
        list1 = list1.next if list1 is not None else None
        list2 = list2.next if list2 is not None else None
        sumValue = val1 + val2 + overflow
        overflow = sumValue // 10
        newResult = LinkedList(sumValue % 10)
        prevResult.next = newResult
        prevResult = newResult
    return resultHead.next
