## Depth-first search
1. This means we search a path until we cannot go any further. 
2. We then return to the previous state possible.
3. We can implement this using a Stack or by recursion


## Uses
It is used to 
1. Traverse all vertices in a Graph: Time complexity is O(V + E), Space complexity is O(V)
2. Traverse all edges between any two vertices in the Graph

## DFS code to traverse all vertices of a Graph 
Time: O(V + E) Because we traverse all vertices and all edges
Space: O(V)

Assume below adjacency list representation

```
{
    A: [B, C, D],
    D: [A, E]
    C: [A, E] 
    B: [A, E, F]
    E: [C, B, F]
    F: [B, E]
}
```
                         

### Iterative using stack assuming

class DFS:
    def __init__(self, graph):
        self._graph = graph
        self._visited_nodes = {}
        self._stack = []
    
    def dfs(start_node):
        self._stack = [start_node]
        self._visited_nodes = {start_node}
        while len(stack):
            node = stack.pop()
            for neighbor in self._graph[node]:
                if neighbor not in self._visited_nodes:
                    self._visited_nodes.add(neighbor)
                    self._stack.append(neighbor)

### Recursive using stack
class DFS:
    def __init__(self, graph):
        self._graph = graph
        self._visited_nodes = {}
    
    def dfs(start_node):
        self._visited_nodes = {start_node}
        self.recursive_dfs(start_node)
    
    def recursive_dfs(node):
        for neighbor in self._graph[node]
            if neighbor not in self._visited_nodes:
                self.recursive_dfs(neighbor)
                self._visited_nodes.add(neighbor)
        


