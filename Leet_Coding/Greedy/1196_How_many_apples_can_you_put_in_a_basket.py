"""
Complexity:
----------
Time: O(N log N)
Space: O(1)
"""
class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        total_weight = 0
        count_of_apples = 0
        for w in weight:
            total_weight += w
            if total_weight > 5000:
                break
            count_of_apples += 1
            
        return count_of_apples
        