"""
Complexity:
---------
Time: O(N)
Space: O(N)

"""
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        prefix_sum = 0
        ans = 0
        for num in nums:
            prefix_sum += (num % 2)
            ans += count[prefix_sum - k]
            count[prefix_sum] += 1
        
        return ans