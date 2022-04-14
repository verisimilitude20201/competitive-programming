"""
Explanation:
-----------
BFS

Complexity:
----------
Time: O(N + K) Where N is the number of rooms and K is the number of keys per room
Space: O(N) Since we store visited rooms in a set. 
"""
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited_rooms = {0}
        Q = deque([0])
        while len(Q):
            room_key = Q.popleft()
            room_keys = rooms[room_key]
            if not room_keys:
                if room_key not in visited_rooms:
                    visited_rooms.add(room_key)
            for rk in room_keys:
                if rk not in visited_rooms:
                    visited_rooms.add(rk)
                    Q.append(rk)

        return len(rooms) == len(visited_rooms)