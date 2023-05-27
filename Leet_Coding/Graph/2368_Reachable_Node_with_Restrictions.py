"""
Complexity:
----------
Time: O(N)
Space: O(N)
"""
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        if 0 in restricted:
            return 0
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        visited = {0}
        
        restricted = set(restricted)
        def dfs(node):
            nonlocal visited
            for neighbor in graph[node]:
                if neighbor not in restricted and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        dfs(0)    
        return len(visited)