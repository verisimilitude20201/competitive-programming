"""
Complexity:
----------
Time: O(N log N + N + M log N) ~ O((M + N) * log N)
Space: O(N)
"""
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        
        ans = []
        for query in queries:
            index = bisect.bisect_right(prefix_sum, query)
            ans.append(index)
        return ans