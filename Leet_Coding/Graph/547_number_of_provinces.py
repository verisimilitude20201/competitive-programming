"""
Complexity:
----------
Time: O(N^2 * alpha(N))
Space: O(N)

Solution2

Time: O(N^2)
Space: O(N)
"""
class QuickUnion:
    def __init__(self, size):
        self._root = [i for i in range(size)]
        self._rank = [1] * size

    def find(self, x):
        if x == self._root[x]:
            return x
        self._root[x] = self.find(self._root[x])
        return self._root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self._rank[root_x] > self._rank[root_y]:
                self._root[root_y] = root_x
            elif self._rank[root_x] < self._rank[root_y]:
                self._root[root_x] = root_y
            else:
                self._root[root_y] = root_x
                self._rank[root_x] += 1

    def get_disjoint_set(self) -> List[int]:
        return self._root.copy()


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        quick_union = QuickUnion(len(isConnected))

        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if i != j and isConnected[i][j] == 1:
                    quick_union.union(i, j)
        disjoint_set = quick_union.get_disjoint_set()
        count = 0
        for i, value in enumerate(disjoint_set):
            count += (i == value)
        return count

class Solution2:
    def __init__(self):
        self._seen = set()
        self._graph = defaultdict(list)
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = self.construct_graph(isConnected)
        province_count = 0
        for i in range(len(isConnected)):
            if i not in self._seen:
                self._seen.add(i)
                self.dfs(i)
                province_count += 1
        
        return province_count
            
    
    def construct_graph(self, isConnected: List[List[int]]):
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j]:
                    self._graph[i].append(j)
                    self._graph[j].append(i)
    
    def dfs(self, node: int):
        for neighbor in graph[node]:
            if neighbor not in self._seen:
                self._seen.add(neighbor)
                self.dfs(neighbor)