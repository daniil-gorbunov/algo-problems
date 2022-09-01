# medium, linked lists
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# time O(max(n,m)) | space O(max(n,m))
def sumOfLinkedLists(list1, list2):
    resultHead = None
    prevResult = None
    overflow = 0
    while list1 is not None and list2 is not None:
        result = LinkedList(list1.value + list2.value + overflow)
        overflow = 0
        if result.value > 9:
            result.value %= 10
            overflow = 1
        list1 = list1.next
        list2 = list2.next
        if prevResult is None:
            resultHead = result
        else:
            prevResult.next = result
        prevResult = result

    rest = list1 if list2 is None else list2

    while rest is not None:
        result = LinkedList(rest.value + overflow)
        overflow = 0
        rest = rest.next
        prevResult.next = result
        prevResult = result

    if overflow > 0:
        prevResult.next = LinkedList(overflow)

    return resultHead
