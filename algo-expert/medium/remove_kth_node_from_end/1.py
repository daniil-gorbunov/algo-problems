# medium, linked lists
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# time O(n) | space O(1)
def removeKthNodeFromEnd(head, k):
    size = 0
    curr = head
    while curr is not None:
        size += 1
        curr = curr.next
    if k == size:
        head.value = head.next.value
        head.next = head.next.next
        return
    prev = head
    curr = head.next
    for pos in range(size - k - 1):
        prev = curr
        curr = curr.next
    prev.next = curr.next
