Complexity:
----------
Time:   
    O(N) - Constructor
    O(Alpha(N)) - Find/Union/isConnected
Space: O(N).

Alpha is inverse Ackermann function


class QuickUnionByRankPathOptimization:
    def __init__(self, size: int):
        self._root = [i for i in range(size)]
        self._rank = [1] * size
    
    def find(self, x): 
        if x == self._root[x]:
            return x
        return self._root[x] = self.find(root[x])
    
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
    
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)