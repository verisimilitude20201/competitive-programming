"""
Complexity:
---------
Time: O(N / K)
Space: O(K + M)
"""
class Bucket:
    def __init__(self):
        self._buckets = []
    
    def put(self, key, value) -> None:
        found = False
        for i, kv in enumerate(self._buckets):
            if kv[0] == key:
                self._buckets[i] = (key, value)
                found = True
                break
        if not found:
           self._buckets.append((key, value))
    
    def get(self, key) -> int:
        for i, kv in enumerate(self._buckets):
            if kv[0] == key:
                return kv[1]
        return -1
    
    def remove(self, key):
        value = None
        for i, kv in enumerate(self._buckets):
            if kv[0] == key:
                value = kv[1]
                del self._buckets[i]
        return value

class MyHashMap:

    def __init__(self):
        self._N = 769
        self._buckets = [Bucket() for _ in range(769)]
    
    def _hash(self, key) -> int:
        return key % self._N

    def put(self, key: int, value: int) -> None:
        hash_value = self._hash(key)
        self._buckets[hash_value].put(key, value)
        

    def get(self, key: int) -> int:
        hash_value = self._hash(key)
        return self._buckets[hash_value].get(key)
        

    def remove(self, key: int) -> int:
        hash_value = self._hash(key)
        return self._buckets[hash_value].remove(key)