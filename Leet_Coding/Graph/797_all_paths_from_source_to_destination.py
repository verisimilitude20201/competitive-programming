"""
Complexity:
----------
Time: O(V * (2^(V - 1) - 1) ---> For a directed acyclic graph, there can be (2^(V-1)) - 1 possible paths from the starting to the ending vertex. There are V such paths.
Space: O(V)
"""
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node):
            path.append(node)
            if node == len(graph) - 1:
                paths.append(path)
                return
            nodes = graph[node]
            for next_node in nodes:
                dfs(next_node)
                path.pop()

        paths = []
        path = []
        if not graph or len(graph) == 0:
            return paths
        dfs(0)

        return paths