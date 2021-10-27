"""
Complexity:
----------
intersect1
----------
Time: O(n + m)
Space: O(min(n, m))

intersect2
----------
Time: O(n log n + m log m)
Space: O(log n + log m) to O(n + m) depending upon the sorting algorith implementation

"""

class Solution:
    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) < len(nums1):
            return self.intersect(nums2, nums1)
        num_count = {}
        for num in nums1:
            num_count[num] = num_count.get(num, 0) + 1

        k = 0
        for num in nums2:
            if num in num_count and num_count[num] > 0:
                nums1[k] = num
                num_count[num] -= 1
                k += 1

        return nums1[:k]

    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i, j, k = 0, 0, 0
        nums1.sort()
        nums2.sort()
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                nums1[k] = nums1[i]
                i += 1
                j += 1
                k += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return nums1[:k]
