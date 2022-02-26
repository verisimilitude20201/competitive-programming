"""
Explanation:
-----------
Solution1
-----------
Time: O(M * N)
Space: O(M * N)

Solution2
---------
Time: O(M * N)
Space: O(Min(M, N))
"""
class Solution1:
    def numIslands1(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        nc = len(grid[0])
        island_count = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == "1":
                    island_count += 1
                    self.find_adjancent_lands(grid, i, j, nr, nc)
        
        return island_count
    
    def find_adjancent_lands(self, grid, row, col, nr, nc):
        if row < 0 or col < 0 or row >= nr or col >= nc or grid[row][col] == "0":
            return
        grid[row][col] = "0"
        self.find_adjancent_lands(grid, row + 1, col, nr, nc)
        self.find_adjancent_lands(grid, row - 1, col, nr, nc)
        self.find_adjancent_lands(grid, row, col + 1, nr, nc)
        self.find_adjancent_lands(grid, row, col - 1, nr, nc)
    
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