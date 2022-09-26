"""
Complexity:
----------
Time: O(E * alpha(N))
Space: O(V)

Where E is the number of edges, V the number of vertices, alpha(N) inverse Ackermann function.
"""
class QuickUnion:
    def __init__(self, n):
        self._connected_components = n
        self._root = [i for i in range(n)]
        self._rank = [1] * n

    def find(self, x):
        if x == self._root[x]:
            return x
        self._root[x] = self.find(self._root[x])

        return self._root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self._rank[x] > self._rank[y]:
                self._root[root_y] = root_x
            elif self._rank[x] < self._rank[y]:
                self._root[root_x] = root_y
            else:
                self._root[root_y] = root_x
                self._rank[root_x] += 1
            self._connected_components -= 1

    def get_count(self):
        return self._connected_components


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        quick_union = QuickUnion(n)
        for x, y in edges:
            quick_union.union(x, y)

        return quick_union.get_count()