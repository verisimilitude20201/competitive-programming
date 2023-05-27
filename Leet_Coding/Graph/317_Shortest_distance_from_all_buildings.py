"""
Complexity:
----------
Time: O(M^2 * N^2)
Space: O(M * N)
"""
class Solution1:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        building_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    building_count += 1
        min_distance = math.inf
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    min_distance = min(self.bfs(grid, i, j, building_count), min_distance)

        if min_distance == math.inf:
            return -1
        return min_distance

    def bfs(self, grid, row, col, building_count) -> int:
        Q = deque([(row, col)])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        steps = 0
        distance = 0
        seen = set()
        seen.add((row, col))
        m = len(grid)
        n = len(grid[0])
        buildings_reached = 0
        while len(Q) and buildings_reached < building_count:
            for i in range(len(Q)):
                r, c = Q.popleft()
                if grid[r][c] == 1:
                    distance += steps
                    buildings_reached += 1
                    continue
                for direction in directions:
                    new_row = r + direction[0]
                    new_col = c + direction[1]
                    if 0 <= new_row < m and 0 <= new_col < n and (new_row, new_col) not in seen and grid[new_row][
                        new_col] != 2:
                        Q.append((new_row, new_col))
                        seen.add((new_row, new_col))

            steps += 1

        if buildings_reached != building_count:
            for r, c in seen:
                if grid[r][c] == 0:
                    grid[r][c] = 2

            return math.inf

        return distance