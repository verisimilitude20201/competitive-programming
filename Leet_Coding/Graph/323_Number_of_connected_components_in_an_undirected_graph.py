"""
Complexity:
----------

Solution 1
-----------
Time: O(E * alpha(N))
Space: O(V)

Where E is the number of edges, V the number of vertices, alpha(N) inverse Ackermann function.

Solution 2: DFS
----------
Time: O(N)
Space: O(N)
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


class Solution1:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        quick_union = QuickUnion(n)
        for x, y in edges:
            quick_union.union(x, y)

        return quick_union.get_count()

class Solution2:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = set()


    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.create_graph(edges)
        count_components = 0
        for i in range(n):
            if i not in self.visited:
                self.visited.add(i)
                self.dfs(i)
                count_components += 1

        return count_components

    def create_graph(self, edges: List[List[int]]):
        for x, y in edges:
            self.graph[x].append(y)
            self.graph[y].append(x)

    def dfs(self, node):
        for neighbor in self.graph[node]:
            if neighbor not in self.visited:
                self.visited.add(neighbor)
                self.dfs(neighbor)