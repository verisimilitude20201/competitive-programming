"""
Explanation:
-----------
Crux of problem is to be able to map each 3 * 3 box on a scale of 0 to 8. 

isValidSudoku1
--------------
    0 1 2   3 4 5   6 7 8
0
1
2

3
4
5

6
7
8

Each box can be identified by the tuple (r // 3, c // 3)
For row and column we can index the values in a HashSet separately s.t all row 0's elements go into hash set 1, all row 1's elements go in hash set 1 and so on.
For each 3 * 3 box, we can turn it into an integer in the range 0 to 8 by the formula (r // 3) * 3  + c // 3

isValidSudoku2
--------------
We maintain a 3 separate 2-darrays for rows, cols and boxes

row = [
        0  1  2  3    4  5   6  7  8
Row 1 [0, 0, 0 , 0 , 0 ,0 , 0 ,0 ,0 ],
    .
    .
    .
Row 9 [0, 0, 0 , 0 , 0 ,0 , 0 ,0 ,0 ]
]

We set 1 to Row 0's 0th position if a 1 is found at board[0][0] and so on 

Complexity:
----------
isValidSudoku1
--------------
Time: O(N^2)
Space: O(N^2)


isValidSudoku2
-------------
Time: O(N^2)
Space: O(N^2)

isValidSudoku3
--------------
Time: O(N^2)
Space: O(N)

"""
class Solution:
    def isValidSudoku1(self, board: List[List[str]]) -> bool:
        N = 9

        # Use hash set to record the status
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                val = board[r][c]
                # Check if the position is filled with number
                if val == ".":
                    continue

                # Check the row
                if val in rows[r]:
                    return False
                rows[r].add(val)

                # Check the column
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # Check the box
                idx = (r // 3) * 3 + c // 3
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)

        return True
    
    def isValidSudoku2(self, board: List[List[str]]) -> bool:
        row = [[0] * 9 for _ in range(9)]
        col = [[0] * 9 for _ in range(9)]
        box = [[0] * 9 for _ in range(9)]
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val  == ".":
                    continue

                pos = int(val) - 1
                if row[r][pos] == 1:
                    return False
                row[r][pos] = 1

                if col[c][pos] == 1:
                    return False
                col[c][pos] = 1

                idx = (r // 3) * 3 + c // 3
                if box[idx][pos] == 1:
                    return False
                box[idx][pos] = 1

        return True
    
    def isValidSudoku3(self, board: List[List[str]]) -> bool:
        row = [0] * 9
        col = [0] * 9
        box = [0] * 9
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val  == ".":
                    continue

                pos = int(val) - 1
                if row[r] & (1 << pos):
                    return False
                row[r] |= (1 << pos)

                if col[c] & (1 << pos):
                    return False
                col[c] |= (1 << pos)

                idx = (r // 3) * 3 + c // 3
                if box[idx] & (1 << pos):
                    return False
                box[idx] |= (1 << pos)

        return True


solution = Solution()
A = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

B = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(solution.isValidSudoku1(A))
print(solution.isValidSudoku1(B))