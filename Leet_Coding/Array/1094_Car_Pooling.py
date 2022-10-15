"""
Complexity:
----------
Time: O(N + M)
Space: O(N)
"""
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = [0] * (max([trip[2] for trip in trips]) + 1)
        for num_passenger, source, destination in trips:
            arr[source] += num_passenger
            arr[destination] -= num_passenger
        
        current_sum = 0
        for passenger in arr:
            current_sum += passenger
            if current_sum > capacity:
                return False
        
        return True