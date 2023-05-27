"""
Complexity:
----------
Time: O(M * N)
Space: O(M + N)
"""
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def is_border(x, y) -> bool:
            return [x, y] != entrance and (x == 0 or x == m - 1 or y == 0 or y == n - 1)
        
        def is_valid(new_x, new_y) -> bool:
            return 0 <= new_x < m and 0 <= new_y < n
            
        m = len(maze)
        n = len(maze[0])
        seen = set()
        seen.add((entrance[0], entrance[1]))
        queue = deque([(entrance[0], entrance[1], 0)])
        while len(queue):
            x, y, steps = queue.popleft()
            if is_border(x, y):
                return steps
            
            for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if (new_x, new_y) not in seen and is_valid(new_x, new_y) and maze[new_x][new_y] == ".":
                    queue.append((new_x, new_y, steps + 1))
                    seen.add((new_x, new_y))
            
        return -1