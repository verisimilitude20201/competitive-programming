"""
Complexity:
----------
wallsAndGates1
--------------
Time: O(M^2 *  N^2)
Space: O(M * N)

wallsAndGates2
--------------
Time: O(M*N)
Space: O(M*N)

"""


class Solution:
    EMPTY =  2147483647
    WALL = -1
    GATE = 0
    MAX_VALUE = EMPTY
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    
    def wallsAndGates1(self, rooms: List[List[int]]) -> None:
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == EMPTY:
                    rooms[i][j] = self.find_distance_to_nearest_gate(rooms, i, j)
    
    
    def find_distance_to_nearest_gate(self, rooms: List[List[int]], row, col) -> List[List[int]]:
        m = len(rooms)
        n = len(rooms[0])
        q = deque([])
        distance = [[0] * n for _ in range(m)]
        q.add([row, col])
        while len(q):
            row1, col1 = q.popleft()
            for direction in directions:
                r = row1 + direction[0]
                c = col1 + direction[1]                
                if r < 0 or c < 0 or r >= m or c >= n or rooms[r][c] == WALL or distance[r][c] != 0:
                    continue
                distance[r][c] = distance[row1][col1] + 1
                if rooms[r][c] == GATE:
                    return distance[r][c]
                q.append([r, c])
        
        return MAX_VALUE
    
    def wallsAndGates2(self, rooms: List[List[int]]) -> None:
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == self.GATE:
                    self.q.append([i, j])

        self.find_distance_to_empty_room(rooms)

    def find_distance_to_empty_room(self, rooms: List[List[int]]) -> None:
        m = len(rooms)
        n = len(rooms[0])
        while len(self.q):
            row, col = self.q.popleft()
            for direction in self.directions:
                r = row + direction[0]
                c = col + direction[1]
                if r < 0 or c < 0 or r >= m or c >= n or rooms[r][c] != self.EMPTY:
                    continue

                rooms[r][c] = rooms[row][col] + 1
                self.q.append([r, c])