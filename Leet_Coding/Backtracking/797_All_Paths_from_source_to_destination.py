"""
Complexity:
---------
Time: O(2^N * N)
Space: O(N) 
"""
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        def dfs(path, node):
            if node == len(graph) - 1:
                path.append(node)
                paths.append(path[:])
                return
            path.append(node)
            for neighbor in graph[node]:
                if neighbor:
                    dfs(path, neighbor)
                    path.pop()
        
        dfs([], 0)
        return paths
                
        