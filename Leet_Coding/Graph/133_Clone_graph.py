"""
Explanation:
-----------
cloneGraph1
----------
DFS

cloneGraph2
----------
BFS

Complexity:
----------
cloneGraph1
-----------
Time: O(N + M) viz M Edges N vertices
Space: O(N) N vertices get stored in HashMap


cloneGraph2
-----------
Time: O(M + N)
Space: O(N)

"""
class Solution:
    def __init__(self):
        self.visited_clone_nodes = dict()

    def cloneGraph1(self, node: 'Node') -> 'Node':
        if not node:
            return None
        if node in self.visited_clone_nodes:
            return self.visited_clone_nodes[node]
        clone_node = Node(node.val, [])
        self.visited_clone_nodes[node] = clone_node
        for neighbor in node.neighbors:
            clone_node.neighbors.append(self.cloneGraph(neighbor))

        return clone_node
    
    def cloneGraph2(self, node: 'Node') -> 'Node':
        if not node:
            return None
        Q = deque([node])
        self.visited_nodes[node] = Node(node.val, [])
        while len(Q):
            n = Q.popleft()
            for neighbor in n.neighbors:
                if neighbor not in self.visited_nodes:
                    self.visited_nodes[neighbor] = Node(neighbor.val, [])
                    Q.append(neighbor)
                self.visited_nodes[n].neighbors.append(self.visited_nodes[neighbor])

        return self.visited_nodes[node]