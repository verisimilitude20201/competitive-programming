"""
Explanation:
-----------
Solution 1
----------
DFS with marking visited nodes with "0".

Solution 2
----------
BFS with marking visited nodes with "0".

Complexity:
----------
Solution1
---------
Time: O(M * N)
Space: O(M * N)

Solution2
---------
Time: O(M * N)
Space: O(min(M, N))
"""
class Solution1:
    def numIslands(self, grid: List[List[str]]) -> int:
        count_of_islands = 0
        num_rows = len(grid)
        num_cols = len(grid[0])
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == "1":
                    count_of_islands += 1
                    grid[i][j] == "0"
                    self._find_adjancent_lands_dfs(grid, i, j, num_rows, num_cols)

        return count_of_islands

    def _find_adjancent_lands_dfs(self, grid, row, col, num_rows, num_cols):
        if row < 0 or row >= num_rows or col < 0 or col >= num_cols or grid[row][col] == "0":
            return
        grid[row][col] = "0"
        self._find_adjancent_lands_dfs(grid, row + 1, col, num_rows, num_cols)
        self._find_adjancent_lands_dfs(grid, row - 1, col, num_rows, num_cols)
        self._find_adjancent_lands_dfs(grid, row, col + 1, num_rows, num_cols)
        self._find_adjancent_lands_dfs(grid, row, col - 1, num_rows, num_cols)


class Solution2:
    def __init__(self) -> None:
        self.q = deque([])

    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        nc = len(grid[0])
        island_count = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == "1":
                    island_count += 1
                    grid[i][j] = "0"
                    self.q.append([i, j])
                    self.visit_adjancent_lands(grid, nr, nc)

        return island_count

    def visit_adjancent_lands(self, grid, nr, nc) -> None:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while len(self.q):
            row, col = self.q.popleft()
            for direction in directions:
                r = row + direction[0]
                c = col + direction[1]
                if r < 0 or c < 0 or r >= nr or c >= nc or grid[r][c] == "0":
                    continue
                grid[r][c] = "0"
                self.q.append([r, c])