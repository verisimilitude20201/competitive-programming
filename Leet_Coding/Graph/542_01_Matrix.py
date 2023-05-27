"""
Complexity:
----------
Time: O(M * N)
Space: O(M * N)
"""
class Solution:

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def is_valid(r, c):
            return 0 <= r < m and 0 <= c < n

        seen = set()
        m = len(mat)
        n = len(mat[0])
        Q = deque([])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    seen.add((i, j))
                    Q.append((i, j, 1))
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while len(Q):
            row, col, steps = Q.popleft()
            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy
                if is_valid(new_row, new_col) and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    mat[new_row][new_col] = steps
                    Q.append((new_row, new_col, steps + 1))

        return mat