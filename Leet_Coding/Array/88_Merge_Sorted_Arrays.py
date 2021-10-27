"""
Complexity:
----------
merge1:
------
Time: O(n + m log(n + m))
Space: O(n) 

merge2:
------
Time: O(n + m)
Space: O(m)

merge1:
------
Time: O(n + m)
Space: O(1)
"""

from typing import List


class Solution:
    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1[m + i] = nums2[i]

        nums1.sort()

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1_copy = nums1[:m]

        # Read pointers for nums1Copy and nums2 respectively.
        p1 = 0
        p2 = 0

        # Compare elements from nums1Copy and nums2 and write the smallest to nums1.
        for p in range(n + m):
            # We also need to ensure that p1 and p2 aren't over the boundaries
            # of their respective arrays.
            if p2 >= n or p1 < m and nums1_copy[p1] <= nums2[p2]:
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1

    def merge3(self, nums1: List[int], m: int, nums2: List[int], n: int):
        # Set p1 and p2 to point to the end of their respective arrays.
        p1 = m - 1
        p2 = n - 1

        # And move p backwards through the array, each time writing
        # the smallest value pointed at by p1 or p2.
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1


solution = Solution()
solution.merge3([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)