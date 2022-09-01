# hard, linked lists
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# time O(n) | space O(1)
def reverseLinkedList(head):
    prev = None
    cur = head
    while cur is not None:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev
