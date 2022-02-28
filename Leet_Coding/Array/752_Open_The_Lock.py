"""
Complexity:
----------
Time: O(N^2 * A^N + D)
Space: O(A^N + D)

Where, N = number of digits which is 4
       D = length of the dead ends set
       A = numbers which is 10 (viz 0 to 9) here.

There are 10 * 10 * 10 * 10 = 10 ^ 4 combinations viz. A^N
For each combination we loop N times ie 4 times and take substring viz. O(N^2)
O(D) is the time complexity of creating a set of dead-ends.
"""
class Solution:
    def get_neighbors(self, node):
        for i in range(4):
            x = int(node[i])
            for d in (-1, 1):
                y = (x + d) % 10
                yield node[:i] + str(y) + node[i + 1:]

    def openLock(self, deadends: List[str], target: str) -> int:
        Q = deque([("0000", 0)])
        seen = {"0000"}
        dead_ends = set(deadends)
        while Q:
            node, depth = Q.popleft()
            if node == target:
                return depth
            if node in dead_ends:
                continue
            for neighbor in self.get_neighbors(node):
                if neighbor not in seen:
                    seen.add(neighbor)
                    Q.append((neighbor, depth + 1))

        return -1