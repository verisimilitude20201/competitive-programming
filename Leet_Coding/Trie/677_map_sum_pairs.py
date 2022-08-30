"""
Complexity:
----------
MapSum1
-------
Time: O(N * S) where S is the length of the prefix.
Space: O(N)

MapSum2:
-------
Time: O(K^2) Where K is length of each string
Space: O(K)

MapSum3:
-------
Time: O(N)
Space: O(N)
"""
class MapSum1:

    def __init__(self):
        self._map = {}

    def insert(self, key: str, val: int) -> None:
        self._map[key] = val

    def sum(self, prefix: str) -> int:
        return sum(value for key, value in self._map.items() if key.startswith(prefix))

class MapSum2:

    def __init__(self):
        self._map = dict()
        self._counter = collections.Counter()
        

    def insert(self, key: str, val: int) -> None:
        delta = val - self._map.get(key, 0)
        self._map[key] = val
        for i in range(len(key) + 1):
            prefix = key[:i]
            self._counter[prefix] += delta
        

    def sum(self, prefix: str) -> int:
        return self._counter[prefix]

class TrieNode(object):
    def __init__(self):
        self._children = dict()
        self._score = 0


class MapSum3:

    def __init__(self):
        self._trie = TrieNode()
        self._map = dict()

    def insert(self, key: str, val: int) -> None:
        delta = val - self._map.get(key, 0)
        self._map[key] = val
        current = self._trie
        for char in key:
            if not current._children.get(char):
                current._children[char] = TrieNode()
            current._children[char]._score += delta
            current = current._children[char]

    def sum(self, prefix: str) -> int:
        current = self._trie
        score = 0
        for char in prefix:
            if char not in current._children:
                return 0
            score = current._children[char]._score
            current = current._children[char]
        return score