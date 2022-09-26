"""
Complexity:
------------
Time: O(V + E)
Space: O(V + E)
"""
class Solution:
    def __init__(self):
        self._graph = defaultdict(set)

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        if len(edges) == 0:
            return False;

        for u, v in edges:
            self._graph[u].add(v)
            self._graph[v].add(u)

        return self.check_path_exists(source, destination)

    def check_path_exists(self, source: int, destination: int) -> bool:
        stack = [source]
        visited = {source}
        while len(stack):
            node = stack.pop()
            if node == destination:
                return True

            for neighbor in self._graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)

        return False