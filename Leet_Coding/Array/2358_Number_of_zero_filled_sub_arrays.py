"""
Complexity:
----------
Time: O(N)
Space: O(1)

"""
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        sub_array_cnt = 0
        ans = 0
        for num in nums:
            if num == 0:
               sub_array_cnt += 1
            else:
               sub_array_cnt = 0
            
            ans += sub_array_cnt
            
        return ans