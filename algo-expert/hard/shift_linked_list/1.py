# hard, linked lists
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# time O(n) | space O(1)
def shiftLinkedList(head, k):
    tail, size = head, 1
    while tail.next:
        tail = tail.next
        size += 1

    offset = k % size
    if offset == 0:
        return head

    newTail = head
    for i in range(1, size - offset):
        newTail = newTail.next
    newHead = newTail.next
    newTail.next = None
    tail.next = head

    return newHead
