"""
Complexity:
----------
Time: O(M + N)
Space: O(M + N)
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return [x for x in set1 if x in set2]