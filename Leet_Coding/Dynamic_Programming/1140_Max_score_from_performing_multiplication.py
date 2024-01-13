"""
Complexity:
----------
Time: O(2^M + K) Where K is the slicing index
Space: O(M)
"""
class Solution1:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        def max_score_recursive(op, nums):
            if op == m:
                return 0
            return max(multipliers[op] * nums[0] + max_score_recursive(op + 1, nums[1:]), 
            multipliers[op] * nums[-1] + max_score_recursive(op + 1, nums[:-1]))
        return max_score_recursive(0, nums)
    

"""
Complexity:
----------
Time: O(2^M )
Space: O(M)
"""
class Solution2:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        def max_score_recursive(left, right, op):
            if op == m:
                return 0
            
            return max(
            multipliers[op] * nums[left] + max_score_recursive(left + 1, right, op + 1), multipliers[op] * nums[right] + max_score_recursive(left, right - 1, op + 1))
        
        return max_score_recursive(0, len(nums) - 1, 0)

"""
Complexity:
----------
Time: O(2^M )
Space: O(M)
"""
class Solution3:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        cache = dict()
        m = len(multipliers)
        n = len(nums)
        def max_score_recursive(left, op):
            if op == m:
                return 0
            if (left, op) in cache:
                return cache[(left, op)]
            
            l = max_score_recursive(left + 1, op + 1) + nums[left] * multipliers[op]
            r = max_score_recursive(left, op + 1) + nums[n - 1 - (op - left)] * multipliers[op]
            cache[(left, op)] = max(l, r)
            
            return cache[(left, op)]
        return max_score_recursive(0, 0)