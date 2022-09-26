"""
Complexity:
----------
Let M be the number of operations, N be the number of friends.

Time: O(N + M log M + N * Alpha(N))
Space: O(N + log M)
"""
class QuickUnion:
    def __init__(self, n):
        self._groups = [i for i in range(n)]
        self._rank = [1] * n
    
    def find(self, a):
        if a == self._groups[a]:
            return a
        self._groups[a] = self.find(self._groups[a])
        
        return self._groups[a]
    
    def union(self, a, b) -> bool:
        group_a = self.find(a)
        group_b = self.find(b)
        if group_a == group_b:
            return False
        
        if group_a != group_b:
            if self._rank[group_a] > self._rank[group_b]:
                self._groups[group_b] = group_a
            elif self._rank[group_a] < self._rank[group_b]:
                self._groups[group_a] = group_b
            else:
                self._groups[group_b] = group_a
                self._rank[group_a] += 1
        
        return True
    
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        if  len(logs) < n - 1:
            return -1
        logs.sort(key=lambda x: x[0])
        group_cnt = n
        quick_union = QuickUnion(n)
        for timestamp, a, b in logs:
            if quick_union.union(a, b):
                group_cnt -= 1
            
            if group_cnt == 1:
                return timestamp
        
        return -1