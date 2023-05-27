"""
Complexity:
----------
Time: O(N log N)
Space: O(N) for Timsort in Python for Quicksort it's O(log N)
"""
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for asteriod in asteroids:
            if asteriod > mass:
                return False
            mass += asteriod
        
        return True