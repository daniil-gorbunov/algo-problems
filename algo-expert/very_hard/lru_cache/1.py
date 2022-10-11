class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.cache = {}
        self.recentList = RecentList()

    # time O(1) | space O(1)
    def insertKeyValuePair(self, key, value):
        if key in self.cache:
            cached = self.cache[key]
            cached.key = key
            cached.value = value
            self.recentList.updateHead(cached)
            return
        if self.recentList.size >= self.maxSize:
            removedListNode = self.recentList.remove()
            self.cache.pop(removedListNode.key)
        addedListNode = self.recentList.add(key, value)
        self.cache[key] = addedListNode

    # time O(1) | space O(1)
    def getValueFromKey(self, key):
        if key not in self.cache:
            return None
        cached = self.cache[key]
        self.recentList.updateHead(cached)
        return cached.value

    # time O(1) | space O(1)
    def getMostRecentKey(self):
        if self.recentList.head:
            return self.recentList.head.key
        return None

class RecentList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # time O(1) | space O(1)
    def add(self, key, value):
        node = RecentListNode(key, value)
        node.next = self.head
        if self.head:
            self.head.prev = node
        if not self.tail:
            self.tail = node
        self.head = node
        self.size += 1
        return node

    # time O(1) | space O(1)
    def remove(self):
        node = self.tail
        if not node:
            return None
        self.tail = node.prev
        if node.prev:
            node.prev.next = None
        if node is self.head:
            self.head = None
        return node

    # time O(1) | space O(1)
    def updateHead(self, node):
        if node is self.head:
            return
        prev = node.prev
        prev.next = node.next
        node.prev = None
        if node is self.tail:
            self.tail = prev
        else:
            node.next.prev = prev
        node.next = self.head
        self.head.prev = node
        self.head = node

class RecentListNode():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
