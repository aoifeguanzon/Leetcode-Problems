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
            self.key = key  # store the key of cache item
            self.value = value  # store the value
            self.prev = None  # pointer to previous node in the linked list
            self.next = None  # pointer to next node in the linked list

    def __init__(self, capacity: int):  # initialises the cache with a given capacity
        self.capacity = capacity  # max number of items the cache can hold
        self.cache = {}  # dictionary to map keys to their node
        self.head = self.Node(0, 0)  # create dummy head node
        self.tail = self.Node(0, 0)  # create dummy tail node
        self.head.next = self.tail  # link head to tail
        self.tail.prev = self.head  # link tail back to head

    '''
    When we insert a new node, we always put it right after head, no matter what
    When we evict the least recently used node, it’s always the one right before tail
    This setup guarantees a stable structure where:
    
    head <-> most recent <-> ... <-> least recent <-> tail
    '''

    def _remove(self, node: Node):  # removes a node from the linked list
        # _ means method are meant to be used only inside the class
        node.prev.next = node.next  # bypass current node in forward direction
        node.next.prev = node.prev  # bypass current node in backward direction

    def _insert(self, node: Node):  # inserts a node right after the head (most recently used position)
        node.next = self.head.next  # point new node's next to old first node
        node.prev = self.head  # point new node's prev to head
        self.head.next.prev = node  # point old first node's prev to new node
        self.head.next = node  # head's next becomes new node

    def get(self, key: int) -> int:  # returns value of key if exists and moves it to the front
        if key in self.cache:  # if key exists in cache
            node = self.cache[key]  # get the node
            self._remove(node)  # remove it from current position
            self._insert(node)  # re-insert it at front (most recently used)
            return node.value  # return its value
        return -1  # if key doesn't exist, return -1

    def put(self, key: int, value: int) -> None:  # adds/updates key-value pair and removes the least recently used item from the cache if full
        if key in self.cache:  # if key already exists
            node = self.cache[key]  # get the node
            self._remove(node)  # remove it from current position
        elif len(self.cache) == self.capacity:  # if cache is full
            lru = self.tail.prev  # get least recently used node (just before tail)
            self._remove(lru)  # remove it from the list
            del self.cache[lru.key]  # remove it from the cache dictionary
        node = self.Node(key, value)  # create new node with key and value
        self.cache[key] = node  # add it to the dictionary
        self._insert(node)  # insert it at the front (most recently used)


'''
Time complexity: O(1)
Hash map for access
Doubly linked list for insertions and deletions

Space complexity: O(k)
Store the key-value pairs in the dictionary and the nodes in the doubly linked list, 
which require linear space proportional to the cache size
'''
