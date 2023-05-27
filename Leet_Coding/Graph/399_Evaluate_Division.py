"""
Complexity:
---------
Time: O(Q * (N + E))
Space: O(N + E)
"""

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for i in range(len(equations)):
            numerator, denominator = equations[i]
            graph[numerator][denominator] = values[i]
            graph[denominator][numerator] = 1 / values[i]
        ans = []
        for query in queries:
            ans.append(self.answer_query(graph, query[0], query[1]))
        return ans
    
    def answer_query(graph, start, end):
        if start not in graph:
            return -1
        stack = [(start, 1)]
        seen = set()
        seen.add(start)
        while len(stack):
            node, ratio = stack.pop()
            if node == end:
                return ratio
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append((neighbor, ratio * graph[node][neighbor]))
        return -1