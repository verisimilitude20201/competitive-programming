```
class UnionFind
    def __init__(self, size):
        self._arr = [i for i in range(size)]
    
    def find(self, x):
        return self._arr[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            for i in range(size):
                if arr[i] == root_y:
                    arr[i] = root_x
    
    def is_connected(self, x: int, y:int) -> bool:
        return self.find(x) == self.find(y)

