"""
Complexity:
---------
Time: O(N + E)
Space: O(N)
"""
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = {0}
        def dfs(node):
            for neighbor in rooms[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        
        dfs(0)
        return len(rooms) == len(seen)