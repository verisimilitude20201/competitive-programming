"""
Complexity:
----------
Time: O(M * N * 3 ^ L)
Space: O(L)
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n
            
        def backtrack(row, col, i, seen):
            if i == len(word):
                return True
            
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if valid(new_row, new_col) and (new_row, new_col) not in seen:
                    if board[new_row][new_col] == word[i]:
                        seen.add((new_row, new_col))
                        if backtrack(new_row, new_col, i + 1, seen):
                            return True
                        seen.remove((new_row, new_col))
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and backtrack(i, j, 1, {(i, j)}):
                    return True
        
        return False
            
            