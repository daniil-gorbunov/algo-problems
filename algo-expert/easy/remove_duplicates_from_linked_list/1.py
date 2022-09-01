# easy, linked lists
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# time O(n) | space O(1)
def removeDuplicatesFromLinkedList(linkedList):
    cur = linkedList
    while cur.next is not None:
        if cur.next.value == cur.value:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return linkedList
