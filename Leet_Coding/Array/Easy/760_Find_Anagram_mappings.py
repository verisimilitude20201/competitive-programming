"""
Complexity:
----------
Time: O(N)
Space: O(N)

"""
class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        num2_positions = {}
        for i in range(len(nums2)):
            num2_positions[nums2[i]] = i

        mapping = [None] * len(nums1)
        for j in range(len(nums1)):
            mapping[j] =  num2_positions[nums1[j]]


        return mapping 

