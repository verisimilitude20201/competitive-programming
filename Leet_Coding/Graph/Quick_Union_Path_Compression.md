class QuickUnionPathOptimization:
    def __init__(self, size):
        self._root = [i for i in range(size)]
    
    def find(self, x):
        if x == self._root[x]:
            return x
        return self._root[x] = self.find(root[x])
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self._root[root_y] = root_x
    
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)