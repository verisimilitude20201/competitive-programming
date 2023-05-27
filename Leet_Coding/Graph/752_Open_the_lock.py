"""
Complexity:
----------
Time: O(N^2 + A^N + d) where d is the length of deadends, N is number of digits in node and A is the numer of alphabet
Space: O(A^N + d)
"""
class Solution:
    def get_neighbors(self, node: str) -> str:
        for i in range(4):
            num = int(node[i])
            for d in (-1, 1):
                x = (num + d) % 10
                yield node[: i] + str(x) + node[i+1 :]
                

    def openLock(self, deadends: List[str], target: str) -> int:
        seen = {"0000"}
        Q = deque([("0000", 0)])
        deadends = set(deadends)
        while len(Q):
            node, steps = Q.popleft()
            if node == target:
                return steps
            if node in deadends:
                continue
            for neighbor in self.get_neighbors(node):
                if neighbor not in seen:
                    seen.add(neighbor)
                    Q.append((neighbor, steps + 1))
        return -1