"""
Complexity:
----------
MyHashSet1
---------
Time: O(N / K) Where N is the number of items in the map and K is the number of buckets
Space: O(K + M) Where M is the number of unique values in the HashSet and K is the number of buckets
"""
class Bucket:
    class Node:
        def __init__(self, value, new_node=None):
            self._value = value
            self._next = new_node

    def __init__(self):
        self._head = self.Node(0)

    def insert(self, key):
        if not self.exists(key):
            new_node = self.Node(key, self._head._next)
            self._head._next = new_node

    def exists(self, key) -> bool:
        current = self._head
        while current:
            if current._value == key:
                return True
            current = current._next
        return False

    def remove(self, key):
        prev = self._head
        current = prev._next
        while current:
            if current._value == key:
                prev._next = current._next
                return
            prev = current
            current = current._next


class MyHashSet:

    def __init__(self):
        self._N = 769
        self._buckets = [Bucket() for _ in range(self._N)]

    def _hash(self, key):
        return key % self._N

    def add(self, key: int) -> None:
        hash_value = self._hash(key)
        self._buckets[hash_value].insert(key)

    def remove(self, key: int) -> None:
        hash_value = self._hash(key)
        self._buckets[hash_value].remove(key)

    def contains(self, key: int) -> bool:
        hash_value = self._hash(key)
        return self._buckets[hash_value].exists(key)