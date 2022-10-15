"""
Complexity:
----------
Time: O(N)
Space: O(N)

"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = prefix_sum = 0
        for num in nums:
            prefix_sum += num
            ans += counts[prefix_sum - k]
            counts[prefix_sum] += 1
        
        return ans
    