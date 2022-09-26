This is an optimization on the top of QuickUnion

1. Compute the rank of each node 
2. The new root node will the node of the tree with larger height. 
3. This is balanced during the union operation

       X                Y 
       0                3
       
       1             0      4   
      
      2            1          5


class UnionFindByRank:
    def __init__(size):
        self._root = [for i in range(size)]
        self._rank = [1] * size
    
    def find(x):
        while x != self._root[x]:
            x = self._root[x]
        
        return x
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self._rank[x] > self._rank[y]:
                self._root[root_y] = root_x
            elif self._rank[x] < self._rank[y]:
                self._root[root_x] = root_y
            else:
                self._root[root_x] = root_y
                self._rank[root_x] += 1
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)