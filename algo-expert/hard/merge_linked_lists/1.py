# hard, linked lists
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# time O(m + n) | space O(1)
def mergeLinkedLists(h1, h2):
    min, max = (h1, h2) if h1.value < h2.value else (h2, h1)
    head = min
    while min and max:
        while min.next and min.next.value <= max.value:
            min = min.next
        temp = min.next
        min.next = min = max
        max = temp
    return head
