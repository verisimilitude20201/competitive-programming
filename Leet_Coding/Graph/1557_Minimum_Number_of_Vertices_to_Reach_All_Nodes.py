"""
Complexity:
---------
Time: O(E + N)
Space: O(N)
"""
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree = [0] * n
        for x, y in edges:
            in_degree[y] += 1

        return [node for node, degree in enumerate(in_degree) if degree == 0]