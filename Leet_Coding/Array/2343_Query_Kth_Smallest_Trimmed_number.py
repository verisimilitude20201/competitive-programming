"""
Complexity:
----------
Time: O(Q * (N log N))
Space: O(Q * N)
"""
class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        m = dict()
        ans = []
        for kth_smallest, trim_value in queries:
            m.setdefault(trim_value, sorted([(num[-trim_value: ], i) for i, num in enumerate(nums)]))
            l = m.get(trim_value)
            ans.append(l[kth_smallest - 1][1])
        
        return ans
        
        