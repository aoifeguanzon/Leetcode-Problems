'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache .
An LRU (Least Recently Used) cache is used in situations where you want to efficiently manage limited storage (eg. memory or disk space) 
by automatically discarding the least recently accessed data when new data needs to be stored, and the cache is full.
'''
# Solution 1
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key: int) -> int:
        if key in self.cache:
            self.order.remove(key)
            self.order.insert(0, key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) == self.capacity:
            lru = self.order.pop()
            del self.cache[lru]
        self.cache[key] = value
        self.order.insert(0, key)

'''
Time complexity: O(n) as get(key) and put(key, value) operations involve list manipulations like remove() and insert(0, key), 
which require linear time due to shifting elements in the list.

Space complexity: O(k) (number of items currently in cache)
We store the keys and values in both the dictionary and the list, which together require linear space proportional to the cache size.
'''

# Optimal solution - doubly linked list
class LRUCache:

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = self.Node(0, 0)
        self.tail = self.Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
        elif len(self.cache) == self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
        
        node = self.Node(key, value)
        self.cache[key] = node
        self._insert(node)

'''
Time complexity: O(1)
Hash map for access
Doubly linked list for insertions and deletions

Space complexity: O(k)
Store the key-value pairs in the dictionary a
nd the nodes in the doubly linked list, 
which require linear space proportional to the cache size
'''
